def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.
    """
    # Use a list as a stack for opening brackets
    stack = []

    # Map closing brackets to their corresponding opening brackets
    matching = {
        ')': '(',
        '}': '{',
        ']': '[',
    }

    for char in s:
        # If it's an opening bracket, push onto the stack
        if char in matching.values():
            stack.append(char)
        # If it's a closing bracket, check for a valid match
        elif char in matching:
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()
        # Ignore any other characters

    # Valid if no unmatched opening brackets remain
    return not stack