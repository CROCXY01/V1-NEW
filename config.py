import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

BOT_TOKEN = os.getenv("LANDING_BOT_TOKEN", "").strip()
ADMIN_ID = int(os.getenv("LANDING_ADMIN_ID", "0") or 0)

# Railway Volume should be mounted at /data.
DATA_ROOT = Path(os.getenv("DATA_ROOT", "/data"))
DB_PATH = Path(os.getenv("LANDING_DB_PATH", str(DATA_ROOT / "landing_bot.db")))
INSTANCE_ROOT = Path(os.getenv("INSTANCE_ROOT", str(DATA_ROOT / "instances")))

_template_value = Path(os.getenv("TEMPLATE_ROOT", "px9v_template"))
TEMPLATE_ROOT = _template_value if _template_value.is_absolute() else BASE_DIR / _template_value

MASTER_INSTANCE_KEY = os.getenv("MASTER_INSTANCE_KEY", "").strip()
REVOKE_DELETE_FILES = os.getenv("REVOKE_DELETE_FILES", "true").lower() in ("1", "true", "yes")

# Create writable directories before SQLite or provisioning tries to use them.
DB_PATH.parent.mkdir(parents=True, exist_ok=True)
INSTANCE_ROOT.mkdir(parents=True, exist_ok=True)

if not TEMPLATE_ROOT.exists():
    raise RuntimeError(f"PX9V template folder not found: {TEMPLATE_ROOT}")
  
