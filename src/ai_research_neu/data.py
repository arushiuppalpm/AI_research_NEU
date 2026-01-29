import json
import random
from pathlib import Path
from .records import Example

def data_step_01(rows: list[Example]) -> list[Example]:
    """Return a stable copy of examples for research step 1."""
    return sorted(list(rows), key=lambda row: row.id)

