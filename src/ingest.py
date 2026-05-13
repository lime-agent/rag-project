# TODO: Claude와 함께 완성합니다 (3회차)
# 아래 명세를 참고해서 Claude한테 "ingest.py 만들어줘" 라고 요청하세요.
#
# 동작:
#   1. docs/ 아래 .md 파일 모두 읽기
#   2. CHUNK_SIZE 단위로 분할 (overlap 포함)
#   3. EMBED_MODEL로 임베딩 생성
#   4. ChromaDB COLLECTION_NAME에 저장
#      메타데이터: {"source": 파일명, "chunk": 청크번호}
#   5. 완료 메시지 출력: "✓ N개 문서, M개 청크 인덱싱 완료"
#
# 실행: python src/ingest.py
