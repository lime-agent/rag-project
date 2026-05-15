# RAG Project — Claude 지시서

이 프로젝트는 Obsidian wiki 노트를 지식 베이스로 사용하는 RAG 시스템을 만든다.
Claude는 이 파일을 읽고 아래 설계 원칙과 구조를 따라 코드를 작성한다.

## 프로젝트 목표

```
$OBSIDIAN_VAULT/Projects/rag-project/   ← 인덱싱할 마크다운 문서 (wiki 노트)
  → ingest   → 청크 분할 + 임베딩 + ChromaDB 저장
  → query    → 질문 입력 → 관련 청크 검색 → Ollama 답변 생성
```

## 기술 스택

- **임베딩**: Ollama (`requests`로 localhost:11434/api/embed 호출, 모델: nomic-embed-text, 응답: `embeddings[0]`)
- **벡터 DB**: `chromadb` (로컬 파일 기반)
- **LLM**: Ollama (`requests`로 localhost:11434/api/generate 호출, 모델: qwen2.5:3b)
- **언어**: Python 3.10+

외부 유료 API 없이 동작한다. 임베딩과 답변 생성 모두 로컬에서 처리한다.

## 파일 구조

```
rag-project/
├── CLAUDE.md
├── README.md
├── requirements.txt
├── setup.sh
├── docs/               ← fallback 문서 디렉토리 ($OBSIDIAN_VAULT 미설정 시)
├── src/
│   ├── config.py       ← 경로·모델명 등 설정
│   ├── ingest.py       ← 문서 로드 + 청크 + 임베딩 + 저장
│   ├── ingest_v2.py    ← 청크 전략 개선 버전
│   ├── query.py        ← 검색 + 답변 생성 CLI
│   └── watch.py        ← docs/ 감시 + 자동 재인덱싱
└── .chroma/            ← ChromaDB 저장소 (gitignore)
```

## 설계 원칙

1. **단순하게**: 수업용 토이 프로젝트다. 과도한 추상화 금지.
2. **CLI 우선**: 웹 UI 없이 터미널에서 동작.
3. **한국어 지원**: 문서와 질문 모두 한국어 처리 가능.
4. **출처 표시**: 답변에 반드시 참조한 파일명 포함.
5. **점진적 구현**: ingest → query 순서로 단계별 완성.

## ingest.py 동작 명세

```
입력: $OBSIDIAN_VAULT/Projects/rag-project 아래 모든 .md 파일
      ($OBSIDIAN_VAULT 미설정 시 fallback: ./docs/)
처리:
  1. 파일 읽기
  2. 청크 분할 (chunk_size=500, overlap=50)
  3. 임베딩 생성 (Ollama nomic-embed-text, POST localhost:11434/api/embed, 응답에서 embeddings[0] 추출)
  4. ChromaDB에 저장 (메타데이터: 파일명, 청크 번호)
출력: "✓ N개 문서, M개 청크 인덱싱 완료"
```

## query.py 동작 명세

```
입력: 사용자 질문 (CLI 인수: python src/query.py "질문")
처리:
  1. 질문 임베딩
  2. ChromaDB에서 유사 청크 top-3 검색
  3. Ollama로 답변 생성 (localhost:11434)
     - 프롬프트: "아래 문서를 참고해서 답변하라. 근거가 없으면 모른다고 해라."
     - 검색된 청크를 컨텍스트로 주입
출력:
  [답변]
  참조: 파일명1, 파일명2
```

## 환경변수

없음. Ollama는 로컬에서 동작하므로 API 키 불필요.

## 작업 순서 (Claude에게)

사용자가 "ingest 만들어줘" 또는 "query 만들어줘"라고 하면 해당 파일을 위 명세에 맞게 구현한다.
구현 전 "이렇게 만들겠습니다" 2~3줄 계획 먼저 말하고 진행한다.
