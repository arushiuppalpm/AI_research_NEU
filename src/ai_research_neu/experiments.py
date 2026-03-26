from dataclasses import dataclass
from .records import Example


@dataclass(frozen=True)
class ExperimentResult:
    name: str
    score: float
    predictions: list[str]
def experiment_step_05(name: str, predictions: list[str]) -> ExperimentResult:
    """Create a scored experiment result for iteration 5."""
    score = len([item for item in predictions if item]) / len(predictions) if predictions else 0.0
    return ExperimentResult(name=name, score=score, predictions=predictions)

def experiment_step_11(name: str, predictions: list[str]) -> ExperimentResult:
    """Create a scored experiment result for iteration 11."""
    score = len([item for item in predictions if item]) / len(predictions) if predictions else 0.0
    return ExperimentResult(name=name, score=score, predictions=predictions)

def experiment_step_17(name: str, predictions: list[str]) -> ExperimentResult:
    """Create a scored experiment result for iteration 17."""
    score = len([item for item in predictions if item]) / len(predictions) if predictions else 0.0
    return ExperimentResult(name=name, score=score, predictions=predictions)

def experiment_step_23(name: str, predictions: list[str]) -> ExperimentResult:
    """Create a scored experiment result for iteration 23."""
    score = len([item for item in predictions if item]) / len(predictions) if predictions else 0.0
    return ExperimentResult(name=name, score=score, predictions=predictions)

def experiment_step_29(name: str, predictions: list[str]) -> ExperimentResult:
    """Create a scored experiment result for iteration 29."""
    score = len([item for item in predictions if item]) / len(predictions) if predictions else 0.0
    return ExperimentResult(name=name, score=score, predictions=predictions)

