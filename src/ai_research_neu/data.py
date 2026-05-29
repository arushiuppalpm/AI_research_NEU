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

def data_step_31(rows: list[Example]) -> list[Example]:
    """Return a stable copy of examples for research step 31."""
    return sorted(list(rows), key=lambda row: row.id)

def data_step_37(rows: list[Example]) -> list[Example]:
    """Return a stable copy of examples for research step 37."""
    return sorted(list(rows), key=lambda row: row.id)

def data_step_43(rows: list[Example]) -> list[Example]:
    """Return a stable copy of examples for research step 43."""
    return sorted(list(rows), key=lambda row: row.id)

def data_step_49(rows: list[Example]) -> list[Example]:
    """Return a stable copy of examples for research step 49."""
    return sorted(list(rows), key=lambda row: row.id)

def data_step_55(rows: list[Example]) -> list[Example]:
    """Return a stable copy of examples for research step 55."""
    return sorted(list(rows), key=lambda row: row.id)

def data_step_61(rows: list[Example]) -> list[Example]:
    """Return a stable copy of examples for research step 61."""
    return sorted(list(rows), key=lambda row: row.id)

