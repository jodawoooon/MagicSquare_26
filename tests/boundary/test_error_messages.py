"""Boundary error message SSOT (envelope fallback)."""

from boundary.error_messages import message_for_code


def test_message_for_code_returns_known_invalid_size_message() -> None:
    """Known code returns canonical PRD message."""
    assert message_for_code("INVALID_SIZE") == "Grid must be 4x4."


def test_message_for_code_returns_unknown_code_as_message() -> None:
    """Unknown code falls back to the code string itself."""
    assert message_for_code("VALUE_OUT_OF_RANGE") == "VALUE_OUT_OF_RANGE"
