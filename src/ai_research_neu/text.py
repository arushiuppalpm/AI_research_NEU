import re
from collections import Counter

_SPACE_RE = re.compile(r"\s+")


def normalize(value: str) -> str:
    return _SPACE_RE.sub(" ", value.strip().lower())


def tokenize(value: str) -> list[str]:
    return normalize(value).split()
def text_step_02(value: str) -> list[str]:
    """Tokenize normalized text for feature step 2."""
    return tokenize(value)

