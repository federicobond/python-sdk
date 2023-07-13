try:
    from enum import StrEnum
except ImportError:
    from enum import Enum

    class StrEnum(str, Enum):  # type: ignore
        """
        Backport StrEnum for Python <3.11
        """

        pass
