def minimumSwaps(brackets):
    open_count = 0  # Count of open parentheses
    swap_count = 0  # Count of swaps needed to balance parentheses
    stack = []
    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)
            open_count += 1
        elif bracket == ")":
            if open_count > 0:
                stack.pop()
                open_count -= 1
            else:
                stack.append(bracket)
                open_count -= 1
                swap_count += 1
    if open_count == 0:
        return (swap_count + 1) // 2
    else:
        return -1


if __name__ == "__main__":
    # Example usage:
    expression1 = "(()())"
    expression2 = "())("
    expression3 = "()()("
    expression4 = "((()))"
    expression5 = ")))((("
    swap_count1 = minimumSwaps(expression1)
    swap_count2 = minimumSwaps(expression2)
    swap_count3 = minimumSwaps(expression3)
    swap_count4 = minimumSwaps(expression4)
    swap_count5 = minimumSwaps(expression5)

    print(f"Minimum swaps for '{expression1}': {swap_count1}")
    print(f"Minimum swaps for '{expression2}': {swap_count2}")
    print(f"Minimum swaps for '{expression3}': {swap_count3}")
    print(f"Minimum swaps for '{expression4}': {swap_count4}")
    print(f"Minimum swaps for '{expression5}': {swap_count5}")
