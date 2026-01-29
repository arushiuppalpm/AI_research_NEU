import re
from collections import Counter

_SPACE_RE = re.compile(r"\s+")


def normalize(value: str) -> str:
    return _SPACE_RE.sub(" ", value.strip().lower())


def tokenize(value: str) -> list[str]:
    return normalize(value).split()
