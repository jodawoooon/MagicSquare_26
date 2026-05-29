"""Approval / Golden Master comparison utilities."""

from __future__ import annotations

import difflib
from pathlib import Path

from tests.golden_master.capture import capture_all, capture_scenario
from tests.golden_master.scenarios import GoldenMasterScenario, SCENARIOS

DEFAULT_GOLDEN_PATH = Path(__file__).resolve().parents[1] / "golden_master_expected.txt"
SECTION_SEPARATOR = "________________________________________"
DIFF_FOOTER = f"\n{SECTION_SEPARATOR}\n"


def load_expected(path: Path = DEFAULT_GOLDEN_PATH) -> str | None:
    """Load the Golden Master baseline when it exists."""
    if not path.is_file():
        return None
    return path.read_text(encoding="utf-8")


def write_expected(content: str, path: Path = DEFAULT_GOLDEN_PATH) -> None:
    """Persist the Golden Master baseline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    normalized = content if content.endswith("\n") else f"{content}\n"
    path.write_text(normalized, encoding="utf-8")


def extract_section(content: str, section_name: str) -> str | None:
    """Return one scenario block from a Golden Master document."""
    marker = f"[{section_name}]"
    start = content.find(marker)
    if start == -1:
        return None

    end = content.find(SECTION_SEPARATOR, start)
    section = content[start:end] if end != -1 else content[start:]
    return section.rstrip("\n")


def unified_diff(expected: str, actual: str, path: Path = DEFAULT_GOLDEN_PATH) -> str:
    """Return a unified diff between expected and actual Golden Master text."""
    diff_lines = difflib.unified_diff(
        expected.splitlines(keepends=True),
        actual.splitlines(keepends=True),
        fromfile="expected",
        tofile="actual",
    )
    body = "".join(diff_lines)
    if not body:
        return body
    return body + DIFF_FOOTER


def compare_text(expected: str, actual: str, path: Path = DEFAULT_GOLDEN_PATH) -> tuple[bool, str]:
    """Compare two Golden Master text blobs using open().read() semantics."""
    if expected == actual:
        return True, ""
    return False, unified_diff(expected, actual, path=path)


def approve(
    *,
    path: Path = DEFAULT_GOLDEN_PATH,
    auto_create: bool = True,
) -> tuple[bool, str]:
    """Compare full capture with the Golden Master baseline file.

    Approve pattern:
    - baseline missing + auto_create → write full capture and pass
    - baseline present → open(path).read() vs actual
    """
    actual = capture_all()
    expected = load_expected(path)

    if expected is None:
        if not auto_create:
            return False, f"Golden Master baseline not found: {path}"
        write_expected(actual, path)
        return True, f"Created Golden Master baseline at {path}"

    return compare_text(expected, actual, path=path)


def approve_scenario(
    scenario: GoldenMasterScenario,
    *,
    path: Path = DEFAULT_GOLDEN_PATH,
    auto_create: bool = False,
) -> tuple[bool, str]:
    """Compare one scenario section against the baseline file.

    When the baseline file is missing and ``auto_create`` is True, the full
    document is generated from all scenarios.
    """
    actual_section = capture_scenario(scenario)
    expected_document = load_expected(path)

    if expected_document is None:
        if not auto_create:
            return False, f"Golden Master baseline not found: {path}"
        write_expected(capture_all(), path)
        return True, f"Created Golden Master baseline at {path}"

    expected_section = extract_section(expected_document, scenario.name)
    if expected_section is None:
        return False, (
            f"Section [{scenario.name}] not found in {path}. "
            f"Known sections: {[item.name for item in SCENARIOS]}"
        )

    return compare_text(expected_section, actual_section, path=path)
