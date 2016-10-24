import pytest
from demo.utils import InvalidHovercraftContents, Hovercraft, uppercase


@pytest.fixture
def hovercraft() -> Hovercraft:
    return Hovercraft()


def test_hovercrafts_can_be_full_of_nothing(hovercraft) -> None:
    """Test that :class:`Hovercraft` can be full of nothing."""
    assert hovercraft.contents == ''


def test_hovercrafts_can_be_full_of_eels(hovercraft) -> None:
    """Test that :class:`Hovercraft` can be full of eels."""
    hovercraft.contents = 'eels'
    assert hovercraft.contents == 'eels'


def test_hovercrafts_cannot_be_full_of_anything_else(hovercraft) -> None:
    """Test that :class:`Hovercraft` cannot be full of anything else."""
    with pytest.raises(InvalidHovercraftContents) as exc_info:
        hovercraft.contents = 'dogs'
    assert "No, no, no ...tobacco...er, cigarettes?" in str(exc_info.value)


def test_uppercase_leaves_empty_string_unmodified() -> None:
    """The empty string shouldn't be modified by ``uppercase()``."""
    assert uppercase('') == ''


def test_uppercase_converts_lowercase_ASCII_characters() -> None:
    """
    Lowercase ASCII characters should be converted to uppercase by
    the ``uppercase()`` function.
    """
    assert uppercase('pining for the fjords') == 'PINING FOR THE FJORDS'


def test_uppercase_does_not_modify_punctuation() -> None:
    """Punctuation should be unmodified by ``uppercase()``."""
    given = "Well it's hardly a bloody replacement, is it?!!???!!?"
    expected = "WELL IT'S HARDLY A BLOODY REPLACEMENT, IS IT?!!???!!?"
    assert uppercase(given) == expected


def test_uppercase_does_not_convert_emoji() -> None:
    """Snek is always snek. A.K.A UTF-8 emoji work."""
    assert uppercase('🐍') == '🐍'


def test_uppercase_raises_attribute_error_on_invalid_input() -> None:
    """An ``AttributeError`` should be raised on invalid input."""
    with pytest.raises(AttributeError) as exc_info:
        uppercase(1)
    assert "'int' object has no attribute 'upper'" in str(exc_info.value)
