def balance_check(given_string):
    # Check is even number of brackets
    if len(given_string) % 2 != 0:
        return False

    # Set of opening brackets
    opening_paren = set('([{')

    # Matching Pairs
    matches = set([('(', ')'), ('[', ']'), ('{', '}')])

    # Use a list as a "Stack"
    stack = []

    # Check every parenthesis in string
    for items in given_string:

        # If its an opening, append it to list
        if items in opening_paren:
            stack.append(items)

        else:

            # Check that there are parentheses in Stack
            if len(stack) == 0:
                return False

            # Check the last open parenthesis
            last_open = stack.pop()

            # Check if it has a closing match
            if (last_open, items) not in matches:
                return False

    return len(stack) == 0

print(balance_check('[]'))
print(balance_check('()'))
print(balance_check(''))