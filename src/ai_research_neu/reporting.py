from .experiments import ExperimentResult

def report_step_06(result: ExperimentResult) -> dict[str, object]:
    """Render a compact report row for iteration 6."""
    return {"name": result.name, "score": round(result.score, 4), "predictions": len(result.predictions)}

def report_step_12(result: ExperimentResult) -> dict[str, object]:
    """Render a compact report row for iteration 12."""
    return {"name": result.name, "score": round(result.score, 4), "predictions": len(result.predictions)}

