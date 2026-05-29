"""SSOT error messages keyed by boundary error codes."""

from typing import Final

_ERROR_MESSAGES: Final[dict[str, str]] = {
    "INVALID_SIZE": "Grid must be 4x4.",
    "INVALID_BLANK_COUNT": "빈칸(0)은 정확히 2개여야 한다.",
    "DUPLICATE_NON_ZERO_VALUE": "0을 제외한 숫자는 중복될 수 없다.",
    "NO_VALID_ASSIGNMENT": "NO_VALID_ASSIGNMENT",
}


def message_for_code(code: str) -> str:
    """Return the canonical message for a boundary or pipeline error code."""
    return _ERROR_MESSAGES.get(code, code)
