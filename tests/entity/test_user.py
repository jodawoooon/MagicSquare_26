"""Tests for the User entity."""

import pytest

from entity.user import User


def test_create_user_sets_initial_values() -> None:
    """User 생성 시 초기 속성이 올바르게 설정되어야 한다."""
    # Arrange
    user_id = "user-001"
    name = "Alice"

    # Act
    user = User(user_id=user_id, name=name)

    # Assert
    assert user.user_id == user_id
    assert user.name == name
    assert user.is_active is True


def test_deactivate_user_changes_is_active_to_false() -> None:
    """deactivate 호출 시 활성 상태가 False로 변경되어야 한다."""
    # Arrange
    user = User(user_id="user-001", name="Alice")

    # Act
    user.deactivate()

    # Assert
    assert user.is_active is False


def test_rename_user_updates_name() -> None:
    """rename 호출 시 이름이 새 값으로 변경되어야 한다."""
    # Arrange
    user = User(user_id="user-001", name="Alice")
    new_name = "Bob"

    # Act
    user.rename(new_name)

    # Assert
    assert user.name == new_name


@pytest.mark.parametrize("invalid_user_id", ["", "   "])
def test_create_user_raises_value_error_for_invalid_user_id(
    invalid_user_id: str,
) -> None:
    """비어 있거나 공백 user_id로 생성하면 ValueError가 발생해야 한다."""
    # Arrange
    name = "Alice"

    # Act / Assert
    with pytest.raises(ValueError):
        User(user_id=invalid_user_id, name=name)


@pytest.mark.parametrize("invalid_name", ["", "   "])
def test_create_user_raises_value_error_for_invalid_name(invalid_name: str) -> None:
    """비어 있거나 공백 name으로 생성하면 ValueError가 발생해야 한다."""
    # Arrange
    user_id = "user-001"

    # Act / Assert
    with pytest.raises(ValueError):
        User(user_id=user_id, name=invalid_name)
