from pathlib import Path

ROOT = Path(__file__).parent.parent
DOCS_DIR = ROOT / "docs"
CHROMA_DIR = ROOT / ".chroma"

EMBED_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
COLLECTION_NAME = "wiki"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
TOP_K = 3

OLLAMA_MODEL = "qwen2.5:3b"
OLLAMA_URL = "http://localhost:11434"
