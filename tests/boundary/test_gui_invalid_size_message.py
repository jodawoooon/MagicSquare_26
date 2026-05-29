"""GUI SSOT — INVALID_SIZE status line (Report/12 §7).

Tests the exact string shown in MainWindow._on_validate for null grid.
PyQt is not required; presenter is the message source.
"""

from boundary.schemas import ErrorResponse
from boundary.screen.presenter import ScreenPresenter
from tests.boundary.constants import INVALID_SIZE_CODE, INVALID_SIZE_MESSAGE

_EXPECTED_STATUS_LINE = f"[{INVALID_SIZE_CODE}] {INVALID_SIZE_MESSAGE}"


def test_gui_invalid_size_status_line_matches_prd_ssot() -> None:
    """null validate → `[INVALID_SIZE] Grid must be 4x4.` status format."""
    presenter = ScreenPresenter()

    result = presenter.validate(None)

    assert isinstance(result, ErrorResponse)
    status_line = f"[{result.code}] {result.message}"
    assert status_line == _EXPECTED_STATUS_LINE
    assert status_line == "[INVALID_SIZE] Grid must be 4x4."
