from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Example:
    id: str
    text: str
    label: str
    metadata: dict[str, Any] | None = None
