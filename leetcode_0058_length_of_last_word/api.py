"""API for solving problem Length of Last Word"""

UPPER_MAX = 90
UPPER_MIN = 65


def _is_upper_letter(c: str) -> bool:
    return UPPER_MIN <= ord(c) <= UPPER_MAX


LOWER_MAX = 122
LOWER_MIN = 97


def _is_lower_letter(c: str) -> bool:
    return LOWER_MIN <= ord(c) <= LOWER_MAX


def _is_letter(c: str) -> bool:
    return _is_upper_letter(c) or _is_lower_letter(c)


SPACE = 32


def _is_space(c: str) -> bool:
    return ord(c) == SPACE


def _is_letter_or_space(c: str) -> bool:
    return _is_letter(c) or _is_space(c)


S_MAX = 10**4
S_MIN = 1


def _check_preconditions(s: str) -> bool:
    if not S_MIN <= len(s) <= S_MAX:
        return False

    if not all(_is_letter_or_space(c) for c in s):
        return False

    if not any(_is_letter(c) for c in s):
        return False

    return True


def length_of_last_word(s: str) -> int:
    """Solves problem Length of Last Word"""

    assert _check_preconditions(s)

    s = s.rstrip()
    i = s.rfind(" ")

    return len(s) - (i + 1)
