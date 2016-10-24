class InvalidHovercraftContents(Exception):
    """Your hovercraft has the wrong contents and you should feel bad."""


class Hovercraft:
    """
    Note:
        The contents of a :class:`Hovercraft` can only be eels.

    Args:
        contents (str): The contents of the :class:`Hovercraft`. By default this
            is empty string.

    Attributes:
        contents (str): The contents of the :class:`Hovercraft`.

    Example:
        >>> h = Hovercraft()
        >>> h.contents = 'eels'
        My hovercraft is full of eels.
    """

    def __init__(self, contents: str = '') -> None:
        self._contents = contents

    @property
    def contents(self) -> str:
        """
        The contents of the :class:`Hovercraft`.

        Note:
            This property reports the contents of the :class:`Hovercraft` before
            returning them. Additionally, attempts to set the
            :class:`Hovercraft` contents to anything other than eels will result
            in an error.

        Raises:
            InvalidHovercraftContents: If the contents are not eels.
        """
        if self._contents:
            print("My hovercraft is full of {}.".format(self._contents))
        else:
            print('My hovercraft is empty.')

        return self._contents

    @contents.setter
    def contents(self, item: str) -> None:
        if item.lower() == 'eels':
            self._contents = item
            print('My hovercraft is full of eels.')
        else:
            raise InvalidHovercraftContents(
                "No, no, no ...tobacco...er, cigarettes?"
            )


def uppercase(s: str) -> str:
    """
    Convert a string to uppercase.

    Args:
        s (str): The string to be converted.

    Returns:
        str: The converted uppercase string.

    Example:
        >>> uppercase('completely different') == 'COMPLETELY DIFFERENT'
        True
    """
    return s.upper()
