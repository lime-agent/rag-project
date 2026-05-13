# TODO: Claude와 함께 완성합니다 (4회차)
# 아래 명세를 참고해서 Claude한테 "query.py 만들어줘" 라고 요청하세요.
#
# 동작:
#   1. 사용자 질문 입력 (CLI 인수: python src/query.py "질문")
#   2. 질문 임베딩 → ChromaDB에서 TOP_K 청크 검색
#   3. Ollama 호출 (검색된 청크를 컨텍스트로)
#      시스템: "아래 문서를 참고해서 답변하라. 근거가 없으면 모른다고 해라."
#   4. 답변 출력
#      [답변 내용]
#      참조: 파일명1, 파일명2
#
# 실행: python src/query.py "ChromaDB를 선택한 이유가 뭐야?"
