from rich import print

with open("input.txt", "r") as f:
    data = [line.rstrip("\n") for line in f]


def largest_two_digit_integer(x: str) -> int:
    """
    1. Find the largest digit
    2. Find the largest digit after removing the largest digit
    """

    x_string: list[str] = [i for i in x]
    x_int_list: list[int] = [int(i) for i in x_string]

    largest = max(x_int_list)
    # https://stackoverflow.com/a/176921/14841168
    largest_index = x_int_list.index(largest)

    if largest_index != len(x_int_list) - 1:
        return largest * 10 + max(x_int_list[largest_index + 1 :])
    else:
        return max(x_int_list[:largest_index]) * 10 + largest


def algo(data: list[str]):
    total = 0
    for banks in data:
        total += largest_two_digit_integer(banks)
    return total


if __name__ == "__main__":
    print(f"Answer: {algo(data)}")
