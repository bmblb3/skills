# todo

A tiny command-line todo list. Tasks live in a JSON file in your home directory.

## Usage

```bash
todo add "Buy milk"
todo list
todo done 1
todo rm 1
todo export --format md > list.md
todo export --format json > list.json
todo import list.json
```

Set `TODO_FILE` to keep your list somewhere other than `~/.todo.json`.
