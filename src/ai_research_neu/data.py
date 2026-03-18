import json
import random
from pathlib import Path
from .records import Example

def data_step_01(rows: list[Example]) -> list[Example]:
    """Return a stable copy of examples for research step 1."""
    return sorted(list(rows), key=lambda row: row.id)

def data_step_07(rows: list[Example]) -> list[Example]:
    """Return a stable copy of examples for research step 7."""
    return sorted(list(rows), key=lambda row: row.id)

def data_step_13(rows: list[Example]) -> list[Example]:
    """Return a stable copy of examples for research step 13."""
    return sorted(list(rows), key=lambda row: row.id)

def data_step_19(rows: list[Example]) -> list[Example]:
    """Return a stable copy of examples for research step 19."""
    return sorted(list(rows), key=lambda row: row.id)

def data_step_25(rows: list[Example]) -> list[Example]:
    """Return a stable copy of examples for research step 25."""
    return sorted(list(rows), key=lambda row: row.id)

