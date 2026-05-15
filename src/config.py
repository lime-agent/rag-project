from pathlib import Path
import os

ROOT = Path(__file__).parent.parent

_vault = os.environ.get("OBSIDIAN_VAULT", "")
DOCS_DIR = Path(_vault) / "Projects/rag-project" if _vault else ROOT / "docs"

CHROMA_DIR = ROOT / ".chroma"

EMBED_MODEL = "nomic-embed-text"
COLLECTION_NAME = "wiki"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
TOP_K = 3

OLLAMA_MODEL = "qwen2.5:3b"
OLLAMA_URL = "http://localhost:11434"
