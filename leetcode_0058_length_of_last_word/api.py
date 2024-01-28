"""API for solving problem Length of Last Word"""


def _is_upper_letter(c: str) -> bool:
    return 65 <= ord(c) <= 90


def _is_lower_letter(c: str) -> bool:
    return 97 <= ord(c) <= 122


def _is_letter(c: str) -> bool:
    return _is_upper_letter(c) or _is_lower_letter(c)


def _is_space(c: str) -> bool:
    return ord(c) == 32


def _is_letter_or_space(c: str) -> bool:
    return _is_letter(c) or _is_space(c)


def _check_preconditions(s: str) -> bool:
    if not 1 <= len(s) <= 10**4:
        return False

    if not all(_is_letter_or_space(c) for c in s):
        return False

    if not any(_is_letter(c) for c in s):
        return False

    return True


def length_of_last_word(s: str) -> int:
    """Solves problem Length of Last Word"""

    assert _check_preconditions(s)

    pass
