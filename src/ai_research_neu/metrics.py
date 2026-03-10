from math import sqrt


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0
def metric_step_03(expected: list[str], predicted: list[str]) -> float:
    """Compute exact-match accuracy for metric step 3."""
    if len(expected) != len(predicted):
        raise ValueError("expected and predicted must have matching lengths")
    return sum(a == b for a, b in zip(expected, predicted)) / len(expected) if expected else 0.0

def metric_step_09(expected: list[str], predicted: list[str]) -> float:
    """Compute exact-match accuracy for metric step 9."""
    if len(expected) != len(predicted):
        raise ValueError("expected and predicted must have matching lengths")
    return sum(a == b for a, b in zip(expected, predicted)) / len(expected) if expected else 0.0

def metric_step_15(expected: list[str], predicted: list[str]) -> float:
    """Compute exact-match accuracy for metric step 15."""
    if len(expected) != len(predicted):
        raise ValueError("expected and predicted must have matching lengths")
    return sum(a == b for a, b in zip(expected, predicted)) / len(expected) if expected else 0.0

def metric_step_21(expected: list[str], predicted: list[str]) -> float:
    """Compute exact-match accuracy for metric step 21."""
    if len(expected) != len(predicted):
        raise ValueError("expected and predicted must have matching lengths")
    return sum(a == b for a, b in zip(expected, predicted)) / len(expected) if expected else 0.0

