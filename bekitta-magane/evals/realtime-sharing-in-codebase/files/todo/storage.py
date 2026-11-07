"""Load and save tasks to a local JSON file."""
import json
import os
from pathlib import Path

from todo.models import Task

DEFAULT_PATH = Path.home() / ".todo.json"


def db_path() -> Path:
    # TODO_FILE lets users keep their list somewhere other than the home directory.
    return Path(os.environ.get("TODO_FILE", DEFAULT_PATH))


def load() -> list[Task]:
    path = db_path()
    if not path.exists():
        return []
    with path.open() as f:
        return [Task.from_dict(d) for d in json.load(f)]


def save(tasks: list[Task]) -> None:
    # Whole-file rewrite: the last writer wins.
    path = db_path()
    tmp = path.with_suffix(".tmp")
    with tmp.open("w") as f:
        json.dump([t.to_dict() for t in tasks], f, indent=2)
    tmp.replace(path)
