# TODO: Claude와 함께 완성합니다 (5회차)
# 아래 명세를 참고해서 Claude한테 "eval.py 만들어줘" 라고 요청하세요.
#
# 동작:
#   DOCS_DIR 아래 .md 파일 각각에 대해 두 가지를 측정한다.
#   (config.py 의 DOCS_DIR, CHROMA_DIR, COLLECTION_NAME, EMBED_MODEL,
#    OLLAMA_MODEL, OLLAMA_URL, TOP_K 사용. ingest.py 의 strip_frontmatter() 패턴 재사용)
#
#   [1] Retrievability
#     - LLM으로 "이 문서 내용으로만 답할 수 있는 핵심 질문 1개" 생성
#       프롬프트: "아래 문서를 읽고, 이 문서의 내용으로만 답할 수 있는 핵심 질문 1개를 만들어라.
#                 질문만 출력하라. 설명 없이."
#     - 생성된 질문을 임베딩 → ChromaDB top-k 검색
#     - 해당 파일이 검색 결과에 있으면 ✓ 찾힘, 없으면 ✗ 못 찾힘 출력
#     - 못 찾혔을 때는 실제 top-k 파일명도 출력
#
#   [2] Quality (LLM-as-judge)
#     LLM 프롬프트로 아래 JSON만 응답하도록 요청:
#       {"specificity": 0.0, "focus": 0.0, "vocabulary": 0.0, "suggestion": "개선 제안 한 줄"}
#     평가 기준 (각 0~1):
#       - specificity: 구체적 이유·비교·결론이 있는가 (0=했다/됐다 수준, 1=상세한 근거)
#       - focus:       한 주제에 집중되는가 (0=여러 내용 혼재, 1=단일 주제)
#       - vocabulary:  도메인 개념어가 풍부한가 (0=모호한 표현, 1=구체적 개념어 다수)
#     LLM이 JSON 앞뒤에 텍스트를 붙일 수 있으니 regex로 {} 블록만 추출해서 파싱할 것
#
# 출력 형식:
#   파일별:
#     Q: {생성된 질문}
#     검색 결과: ✓ 찾힘 / ✗ 못 찾힘 (못 찾혔으면 실제 top-k 파일명 출력)
#     구체성  ██████░░░░ 0.6  △ 보통      ← 10칸 바 그래프(█░), 점수, 레이블
#     집중도  ██████████ 1.0  ✓ 양호
#     개념어  ████░░░░░░ 0.4  △ 보통
#     평균 < 0.6 이면: 💡 {suggestion}
#   점수 레이블: 0.7 이상 → ✓ 양호 / 0.4~0.7 → △ 보통 / 0.4 미만 → ✗ 개선 필요
#
#   종합 요약:
#     문서 수 / Retrievability 비율(N/M, %) / 평균 품질 점수
#     품질 0.5 미만이거나 검색 실패한 파일을 "개선 우선순위"로 나열
#
# 실행: python src/eval.py
