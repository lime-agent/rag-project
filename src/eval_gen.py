# TODO: Claude와 함께 완성합니다 (5회차)
# 아래 명세를 참고해서 Claude한테 "eval_gen.py 만들어줘" 라고 요청하세요.
#
# 동작:
#   1. DOCS_DIR 아래 .md 파일 모두 읽기 (frontmatter 제거 후)
#   2. 파일마다 Ollama로 질문 2개 자동 생성
#      프롬프트: "이 문서를 읽고 답할 수 있는 질문 2개를 만들어라.
#                JSON 배열로만 응답: [\"질문1\", \"질문2\"]"
#   3. {question, source_file} 형태로 수집
#   4. eval_dataset.json 으로 저장
#
# 출력 예시 (eval_dataset.json):
#   [
#     {"question": "ChromaDB를 선택한 이유는?", "source_file": "ADR-002-tech-stack.md"},
#     {"question": "nomic-embed-text 벡터 차원은?", "source_file": "ADR-002-tech-stack.md"}
#   ]
#
# 실행: python src/eval_gen.py
