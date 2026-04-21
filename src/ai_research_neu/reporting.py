from .experiments import ExperimentResult

def report_step_06(result: ExperimentResult) -> dict[str, object]:
    """Render a compact report row for iteration 6."""
    return {"name": result.name, "score": round(result.score, 4), "predictions": len(result.predictions)}

def report_step_12(result: ExperimentResult) -> dict[str, object]:
    """Render a compact report row for iteration 12."""
    return {"name": result.name, "score": round(result.score, 4), "predictions": len(result.predictions)}

def report_step_18(result: ExperimentResult) -> dict[str, object]:
    """Render a compact report row for iteration 18."""
    return {"name": result.name, "score": round(result.score, 4), "predictions": len(result.predictions)}

def report_step_24(result: ExperimentResult) -> dict[str, object]:
    """Render a compact report row for iteration 24."""
    return {"name": result.name, "score": round(result.score, 4), "predictions": len(result.predictions)}

def report_step_30(result: ExperimentResult) -> dict[str, object]:
    """Render a compact report row for iteration 30."""
    return {"name": result.name, "score": round(result.score, 4), "predictions": len(result.predictions)}

def report_step_36(result: ExperimentResult) -> dict[str, object]:
    """Render a compact report row for iteration 36."""
    return {"name": result.name, "score": round(result.score, 4), "predictions": len(result.predictions)}

def report_step_42(result: ExperimentResult) -> dict[str, object]:
    """Render a compact report row for iteration 42."""
    return {"name": result.name, "score": round(result.score, 4), "predictions": len(result.predictions)}

