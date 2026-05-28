"""User domain entity for MagicSquare project."""

from dataclasses import dataclass


@dataclass
class User:
    """Represents a user in the domain layer.

    Attributes:
        user_id: Unique identifier for the user.
        name: Display name of the user.
        is_active: Whether the user is active.
    """

    user_id: str
    name: str
    is_active: bool = True

    def __post_init__(self) -> None:
        """Validate entity invariants after initialization.

        Raises:
            ValueError: If `user_id` or `name` is empty or whitespace only.
        """
        self._validate_non_empty("user_id", self.user_id)
        self._validate_non_empty("name", self.name)

    def activate(self) -> None:
        """Mark the user as active."""
        self.is_active = True

    def deactivate(self) -> None:
        """Mark the user as inactive."""
        self.is_active = False

    def rename(self, new_name: str) -> None:
        """Update user name after validation.

        Args:
            new_name: New display name to set.

        Raises:
            ValueError: If `new_name` is empty or whitespace only.
        """
        self._validate_non_empty("new_name", new_name)
        self.name = new_name

    @staticmethod
    def _validate_non_empty(field_name: str, value: str) -> None:
        """Validate that a string field is not empty or whitespace only.

        Args:
            field_name: Name of the field for error messages.
            value: String value to validate.

        Raises:
            ValueError: If the value is empty or whitespace only.
        """
        if not value or value.isspace():
            raise ValueError(f"{field_name} must not be empty.")
