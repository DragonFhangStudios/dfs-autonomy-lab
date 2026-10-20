"""Small text helpers. A deliberately tiny codebase for testing the DFS autonomous workflow."""

import re


def word_count(text: str) -> int:
    """Number of whitespace-separated words in text."""
    return len(text.split())


def truncate(text: str, max_length: int, suffix: str = "...") -> str:
    """Shortens text to at most max_length characters, ending with suffix when cut."""
    if max_length < len(suffix):
        raise ValueError("max_length must be at least the suffix length")
    if len(text) <= max_length:
        return text
    return text[: max_length - len(suffix)] + suffix


def slugify(text: str) -> str:
    """URL-friendly slug: lowercase, runs of non-alphanumerics become one "-", no leading/trailing "-"."""
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
