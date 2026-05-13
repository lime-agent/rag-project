#!/bin/bash
set -e

echo "=== RAG Project 환경 세팅 ==="

python3 --version || { echo "Python 3가 필요합니다."; exit 1; }

if [ ! -d ".venv" ]; then
  python3 -m venv .venv
  echo "✓ 가상환경 생성"
fi

source .venv/bin/activate
pip install -q -r requirements.txt
echo "✓ 패키지 설치 완료"

if [ -z "$(ls -A docs/ 2>/dev/null)" ]; then
  echo "⚠ docs/ 폴더가 비어 있습니다. 인덱싱할 마크다운 파일을 넣으세요."
fi

echo ""
echo "=== 세팅 완료 ==="
echo "다음 단계:"
echo "  1. docs/ 폴더에 마크다운 파일 추가"
echo "  2. claude 실행 후 'ingest.py 만들어줘' 요청"
