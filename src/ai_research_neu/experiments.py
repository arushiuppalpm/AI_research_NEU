from dataclasses import dataclass
from .records import Example


@dataclass(frozen=True)
class ExperimentResult:
    name: str
    score: float
    predictions: list[str]
