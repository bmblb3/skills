"""todo: a tiny command-line todo list."""
import argparse
import sys
from pathlib import Path

from todo import export, storage
from todo.models import Task


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="todo")
    sub = parser.add_subparsers(dest="cmd", required=True)

    add = sub.add_parser("add")
    add.add_argument("title")
    sub.add_parser("list")
    done = sub.add_parser("done")
    done.add_argument("id", type=int)
    rm = sub.add_parser("rm")
    rm.add_argument("id", type=int)
    exp = sub.add_parser("export")
    exp.add_argument("--format", choices=["md", "json"], default="md")
    imp = sub.add_parser("import")
    imp.add_argument("path", type=Path)

    args = parser.parse_args(argv)
    tasks = storage.load()

    if args.cmd == "add":
        next_id = max((t.id for t in tasks), default=0) + 1
        tasks.append(Task(id=next_id, title=args.title))
        storage.save(tasks)
    elif args.cmd == "list":
        for t in tasks:
            print(f"{t.id:>3} [{'x' if t.done else ' '}] {t.title}")
    elif args.cmd == "done":
        for t in tasks:
            if t.id == args.id:
                t.done = True
        storage.save(tasks)
    elif args.cmd == "rm":
        storage.save([t for t in tasks if t.id != args.id])
    elif args.cmd == "export":
        out = export.to_json(tasks) if args.format == "json" else export.to_markdown(tasks)
        sys.stdout.write(out)
    elif args.cmd == "import":
        storage.save(export.import_json(args.path, tasks))
    return 0


if __name__ == "__main__":
    sys.exit(main())
