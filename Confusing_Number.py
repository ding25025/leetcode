"""

"""


def find_confusable_numbers():
    flip_map = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}

    def isConfusable(num):
        flipped = ""
        for digit in str(num):
            if digit not in flip_map:
                return False
            flipped += flip_map[digit]

        # Check if the flipped number is different from the original number
        if num != int(flipped):
            # Check if the flipped number ends in zero, which would make it invalid
            if flipped[-1] == "0":
                return False
            # Check if the first digit is 6 and the last digit is 9, or vice versa
            if (flipped[0] == "6" and flipped[-1] == "9") or (
                flipped[0] == "9" and flipped[-1] == "6"
            ):
                return False
            # Check if the number is a three-digit number and satisfies the specific conditions
            if len(str(num)) == 3 and (num % 10 == 0 or num % 10 == 8 or num % 10 == 6):
                return False
            return True

        return False

    confusables = []
    for num in range(1, 650):
        if isConfusable(num):
            confusables.append(num)

    return confusables


confusables = find_confusable_numbers()
print(confusables)
