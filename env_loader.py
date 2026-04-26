from pathlib import Path
from dotenv import load_dotenv
import os


def load_env():
    # Prefer .env inside the virtualenv Scripts folder if it exists
    venv_env = Path('.venv') / 'Scripts' / '.env'
    project_env = Path('.') / '.env'

    if venv_env.exists():
        load_dotenv(dotenv_path=venv_env)
    elif project_env.exists():
        load_dotenv(dotenv_path=project_env)


def get(key, default=None):
    return os.getenv(key, default)


# Load on import for convenience
load_env()
