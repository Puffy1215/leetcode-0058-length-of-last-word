"""API for solving problem Length of Last Word"""

def _is_letter(c) -> bool:
    pass

def _is_space(c) -> bool:
    pass

def _is_letter_or_space(c) -> bool:
    return _is_letter(c) or _is_space(c)

def _check_preconditions(s) -> bool:
    if not 1 <= len(s) <= 10**4:
        return False
    
    if not all(_is_letter_or_space(c for c in s)):
        return False
    
    if not any(_is_letter(c for c in s)):
        return False
    
    return True


def length_of_last_word(...) -> ...:
    """Solves problem Length of Last Word"""

    assert _check_preconditions(...)

    pass