"""Shared fixtures for Boundary Track A tests."""

import pytest


@pytest.fixture
def boundary_validator():
    """BoundaryValidator instance for matrix size validation tests."""
    from boundary.validator import BoundaryValidator

    return BoundaryValidator()
