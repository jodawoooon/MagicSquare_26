"""Generate Golden Master baseline from current solver output."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from tests.golden_master.approve import DEFAULT_GOLDEN_PATH, write_expected
from tests.golden_master.capture import capture_all


def main() -> int:
    """Write the Golden Master baseline file."""
    parser = argparse.ArgumentParser(
        description="Generate Golden Master baseline from current solver output.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_GOLDEN_PATH,
        help=f"Output path (default: {DEFAULT_GOLDEN_PATH})",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an existing baseline file.",
    )
    args = parser.parse_args()

    if args.output.is_file() and not args.force:
        print(f"Baseline already exists: {args.output}")  # noqa: T201
        print("Use --force to overwrite.")  # noqa: T201
        return 1

    content = capture_all()
    write_expected(content, args.output)
    print(f"Wrote Golden Master baseline to {args.output}")  # noqa: T201
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
