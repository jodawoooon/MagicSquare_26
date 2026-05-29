"""Control-layer exceptions for solve orchestration."""


class NoValidAssignmentError(Exception):
    """Raised when the domain solver finds no valid two-cell assignment."""
