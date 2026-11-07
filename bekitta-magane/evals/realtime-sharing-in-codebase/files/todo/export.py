"""Export tasks to Markdown or JSON, and import tasks from a JSON export."""
import json
from pathlib import Path

from todo.models import Task


def to_markdown(tasks: list[Task]) -> str:
    lines = [f"- [{'x' if t.done else ' '}] {t.title}" for t in tasks]
    return "\n".join(lines) + "\n"


def to_json(tasks: list[Task]) -> str:
    return json.dumps([t.to_dict() for t in tasks], indent=2)


def import_json(path: Path, existing: list[Task]) -> list[Task]:
    """Merge tasks from an exported JSON file. Titles already present are skipped."""
    incoming = [Task.from_dict(d) for d in json.loads(path.read_text())]
    titles = {t.title for t in existing}
    next_id = max((t.id for t in existing), default=0) + 1
    merged = list(existing)
    for t in incoming:
        if t.title in titles:
            continue
        merged.append(Task(id=next_id, title=t.title, done=t.done, created_at=t.created_at))
        next_id += 1
    return merged
