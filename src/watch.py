# TODO: Claude와 함께 완성합니다 (6회차)
# docs/ 폴더를 감시해서 변경 시 자동으로 재인덱싱합니다.
#
# Claude에게 요청:
#   "watch.py 만들어줘.
#    docs/ 폴더를 감시해서 .md 파일이 추가·변경·삭제되면
#    자동으로 재인덱싱하는 스크립트야."
#
# 기대 동작:
#   python src/watch.py
#   → Watching docs/ for changes...
#   → [10:32:15] decision-chunking.md 변경 감지 → 재인덱싱 시작
#   → ✓ 13개 문서, 52개 청크 인덱싱 완료
#
# 필요 패키지: pip install watchdog
#
# 실행: python src/watch.py
