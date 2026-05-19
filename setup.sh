#!/bin/bash
set -e

echo "=== RAG Project 환경 세팅 ==="

python3 --version || { echo "Python 3가 필요합니다."; exit 1; }

# Ollama 설치 여부 확인 및 설치
if ! command -v ollama &> /dev/null; then
  echo "Ollama 설치 중..."
  curl -fsSL https://ollama.com/install.sh | sh
  sudo systemctl enable ollama
  echo "✓ Ollama 설치 완료"
fi

# Ollama 서비스 시작
if ! curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
  echo "Ollama 서비스 시작 중..."
  sudo systemctl start ollama
  sleep 5
fi
echo "✓ Ollama 실행 확인"

# 모델 다운로드 (없는 경우만)
if ! ollama list 2>/dev/null | grep -q "qwen2.5:3b"; then
  echo "qwen2.5:3b 모델 다운로드 중... (시간이 걸립니다)"
  ollama pull qwen2.5:3b
fi
echo "✓ qwen2.5:3b 확인"

if ! ollama list 2>/dev/null | grep -q "nomic-embed-text"; then
  echo "nomic-embed-text 모델 다운로드 중..."
  ollama pull nomic-embed-text
fi
echo "✓ nomic-embed-text 확인"

# Python 가상환경 및 패키지
if ! python3 -c "import ensurepip" &> /dev/null 2>&1; then
  echo "python3-venv 설치 중..."
  sudo apt-get update && sudo apt-get install -y python3-venv
fi

if [ ! -f ".venv/bin/activate" ]; then
  rm -rf .venv
  python3 -m venv .venv
  echo "✓ 가상환경 생성"
fi

source .venv/bin/activate
pip install -q -r requirements.txt
echo "✓ 패키지 설치 완료"

if [ -z "$OBSIDIAN_VAULT" ]; then
  echo ""
  echo "ℹ OBSIDIAN_VAULT 환경변수가 설정되지 않았습니다."
  echo "  docs/ 폴더를 소스로 사용합니다."
  if [ -z "$(ls -A docs/ 2>/dev/null)" ]; then
    echo "⚠ docs/ 폴더가 비어 있습니다. 인덱싱할 마크다운 파일을 넣으세요."
  fi
else
  echo "✓ OBSIDIAN_VAULT: $OBSIDIAN_VAULT"
fi

echo ""
echo "=== 세팅 완료 ==="
echo "다음 단계:"
echo "  1. Claude 실행 후 'ingest.py 만들어줘' 요청 (4회차)"
echo "  2. python src/ingest.py"
