# TODO: Claude와 함께 완성합니다 (4회차)
# 아래 명세를 참고해서 Claude한테 "ingest.py 만들어줘" 라고 요청하세요.
#
# 동작:
#   1. DOCS_DIR ($OBSIDIAN_VAULT/Projects/rag-project) 아래 .md 파일 모두 읽기
#      ($OBSIDIAN_VAULT 미설정 시 fallback: ./docs/)
#   2. CHUNK_SIZE 단위로 분할 (overlap 포함)
#   3. EMBED_MODEL(nomic-embed-text)로 임베딩 생성 (Ollama API)
#      POST localhost:11434/api/embed, 응답에서 embeddings[0] 추출
#   4. ChromaDB COLLECTION_NAME에 저장
#      메타데이터: {"source": 파일명, "chunk": 청크번호}
#   5. 완료 메시지 출력: "✓ N개 문서, M개 청크 인덱싱 완료"
#
# 실행: python src/ingest.py
