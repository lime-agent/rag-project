# TODO: Claude와 함께 완성합니다 (4회차)
# ingest.py의 청크 전략을 개선합니다.
#
# Claude에게 요청:
#   "ingest.py 청크 전략 개선해줘. RecursiveCharacterTextSplitter 방식으로."
#
# 개선 포인트:
#   - 단순 글자수 분할 → 구분자 기반 분할
#   - 구분자 우선순위: ["\n\n", "\n", ". ", " ", ""]
#   - 단락 → 문장 → 어절 순서로 자연스러운 경계에서 분할
#
# 비교 방법:
#   1. python src/ingest.py    (기존)
#   2. python src/ingest_v2.py (개선)
#   3. 동일 질문으로 python src/query.py "질문" 실행 후 비교
#
# 실행: python src/ingest_v2.py
