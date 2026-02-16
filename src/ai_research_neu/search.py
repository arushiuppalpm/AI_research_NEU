from collections import Counter
from .records import Example
from .text import tokenize

def search_step_04(query: str, row: Example) -> float:
    """Score a query against one example for retrieval step 4."""
    q = Counter(tokenize(query))
    r = Counter(tokenize(row.text))
    numerator = sum(q[token] * r.get(token, 0) for token in q)
    q_norm = sum(value * value for value in q.values()) ** 0.5
    r_norm = sum(value * value for value in r.values()) ** 0.5
    return numerator / (q_norm * r_norm) if q_norm and r_norm else 0.0

def search_step_10(query: str, row: Example) -> float:
    """Score a query against one example for retrieval step 10."""
    q = Counter(tokenize(query))
    r = Counter(tokenize(row.text))
    numerator = sum(q[token] * r.get(token, 0) for token in q)
    q_norm = sum(value * value for value in q.values()) ** 0.5
    r_norm = sum(value * value for value in r.values()) ** 0.5
    return numerator / (q_norm * r_norm) if q_norm and r_norm else 0.0

