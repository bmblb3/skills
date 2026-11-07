from dataclasses import asdict, dataclass, field
from datetime import datetime


@dataclass
class Task:
    id: int
    title: str
    done: bool = False
    created_at: str = field(
        default_factory=lambda: datetime.now().isoformat(timespec="seconds")
    )

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict) -> "Task":
        return cls(**d)
