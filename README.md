# RAG Project

Claude와 함께 만드는 토이 RAG 시스템. 마크다운 문서를 지식 베이스로 인덱싱하고, 질문에 답하는 CLI 도구를 직접 구현한다.

## 실습 흐름

```
3회차: ingest.py 구현 — 문서 인덱싱 파이프라인
4회차: query.py 구현 + ingest_v2.py 청크 전략 개선
5회차: wiki 노트 → docs/ 연결 — 내 기록이 검색된다
6회차: watch.py 구현 — 파일 변경 감지 + 자동 재인덱싱
```

---

## 시작하기

### 1. 환경 설치

```bash
bash setup.sh
source .venv/bin/activate
```

### 2. docs/ 에 문서 추가

`docs/` 폴더에 인덱싱할 마크다운 파일을 넣는다. 샘플 파일 2개가 이미 들어 있다.

자신의 wiki 노트, 업무 문서, 강의 정리 노트 등 무엇이든 가능하다.

### 3. Claude로 ingest.py 구현 (3회차)

Claude Code 세션에서:

```
ingest.py 만들어줘
```

CLAUDE.md에 명세가 있어서 한 줄이면 된다.

구현 완료 후 실행:

```bash
python src/ingest.py
```

성공 메시지:
```
✓ 3개 문서, 12개 청크 인덱싱 완료
```

### 4. Claude로 query.py 구현 (4회차)

```
query.py 만들어줘
```

구현 완료 후 실행:

```bash
python src/query.py "ChromaDB를 선택한 이유가 뭐야?"
```

### 5. 청크 전략 개선 (4회차)

검색 결과가 어색하면 청크 전략을 개선한다.

```
ingest.py 청크 전략 개선해줘. RecursiveCharacterTextSplitter 방식으로.
```

### 6. wiki 노트 → docs/ 연결 (5회차)

자신의 wiki 노트를 `docs/`에 복사하고 재인덱싱한다.

```bash
cp ~/path/to/wiki/semantic/*.md docs/
cp ~/path/to/wiki/episodic/*.md docs/
python src/ingest.py
python src/query.py "ChromaDB를 선택한 이유가 뭐야?"
```

### 7. 자동 재인덱싱 (6회차)

```
watch.py 만들어줘.
docs/ 폴더를 감시해서 .md 파일이 추가·변경·삭제되면
자동으로 재인덱싱하는 스크립트야.
```

```bash
pip install watchdog
python src/watch.py
```

---

## Claude 요청문 — 기록 템플릿 (4회차)

아래 요청문을 복사해서 `{}` 부분만 채워 Claude에게 붙여넣는다.

**오류가 났을 때**

```
오늘 query.py 실행하다가 이 오류 났어:
{오류 메시지}

{해결 방법}으로 해결했어.
이거 episodic에 기록해줘.
```

**결정을 내렸을 때**

```
청크 전략을 바꿨어.
기존: 500자 단순 분할
변경: RecursiveCharacterTextSplitter, 구분자 ["\n\n", "\n", ". "]
이유: {이유}
decision 노트로 저장해줘.
```

**비교 결과를 기록할 때**

```
청크 전략 바꾸기 전후 검색 결과 비교했어.
질문: {질문}
before: {결과 요약}
after: {결과 요약}
episodic에 기록해줘.
```

---

## 예상 오류

| 오류 | 해결 |
|------|------|
| `ModuleNotFoundError: No module named 'chromadb'` | `pip install -r requirements.txt` |
| `ModuleNotFoundError: No module named 'sentence_transformers'` | `pip install -r requirements.txt` |
| `FileNotFoundError: docs/ not found` | `rag-project/` 디렉토리에서 실행 |
| 첫 실행 시 수십 초 대기 | 임베딩 모델 다운로드 중 (정상) |
| `✓ 0개 문서` | `docs/`에 `.md` 파일 추가 |
| Ollama connection error | `ollama serve` 실행 후 재시도 |

---

## 오류·결정 기록하기

개발 중 오류가 나면 그 자리에서 wiki에 기록한다.

```
오늘 ingest.py 실행하다가 이 오류 났어:
ModuleNotFoundError: No module named 'chromadb'

pip install chromadb 로 해결했어.
이거 episodic에 기록해줘.
```

결정이 생기면:

```
ChromaDB로 결정했어. FAISS는 설치가 복잡해서.
이거 decision 노트로 저장해줘.
```
