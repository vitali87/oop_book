from typing import Optional


class Formatter:
    def format(self, string: str) -> str:
        pass


def format_string(string: str, formatter: Optional[Formatter] = None) -> str:
    """
    Format a string using the Formatter object which 
    is expected to have a format() method that accepts 
    a tring.
    """

    class DefaultFormatter(Formatter):
        """Format a string in title case."""

        def format(self, string: str) -> str:
            return str(string).title()
    
    if not formatter:
        formatter = DefaultFormatter()

    return formatter.format(string)
