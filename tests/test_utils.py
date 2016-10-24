import pytest
from demo.utils import InvalidHovercraftContents, Hovercraft, uppercase


@pytest.fixture
def hovercraft():
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


def test_can_uppercase_strings() -> None:
    """
    Test that that ``demo.utils.uppercase`` can uppercase strings.

    Note:
        UTF-8 strings are pretty dope, yo.

    Args:
        None

    Returns:
        None
    """

    # The empty string should be unmodified.
    assert uppercase('') == ''

    # Lowercase should become uppercase.
    assert uppercase('pining for the fjords') == 'PINING FOR THE FJORDS'

    # Punctuation shouldn't be modified.
    given = "Well it's hardly a bloody replacement, is it?!!???!!?"
    expected = "WELL IT'S HARDLY A BLOODY REPLACEMENT, IS IT?!!???!!?"
    assert uppercase(given) == expected

    # Snek is always snek. A.K.A UTF-8 emoji work.
    assert uppercase('🐍') == '🐍'

    # Raises ``AttributeError`` on invalid input and has the correct message.
    with pytest.raises(AttributeError) as exc_info:
        uppercase(1)
    assert "'int' object has no attribute 'upper'" in str(exc_info.value)
