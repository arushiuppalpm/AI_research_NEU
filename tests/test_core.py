from ai_research_neu.records import Example
from ai_research_neu.text import normalize


def test_core_types_and_text_normalization():
    assert Example("1", "Text", "label").label == "label"
    assert normalize("  Neural   Search ") == "neural search"
