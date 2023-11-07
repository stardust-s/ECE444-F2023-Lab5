from project.app import init_db
from pathlib import Path


def setup():
    if not Path("flaskr.db").is_file():
        init_db()
