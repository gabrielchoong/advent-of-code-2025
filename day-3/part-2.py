from rich import print

with open("input.txt", "r") as f:
    data = [line.rstrip("\n") for line in f]


def g(x: list[int], k_digit: int) -> list[int]:
    stack: list[int] = []
    removals = len(x) - k_digit

    for num in x:
        while stack and removals > 0 and stack[-1] < num:
            stack.pop()
            removals -= 1
        stack.append(num)

    return stack[:k_digit]


def largest_k_digit_integer(x: str, k_digit: int) -> int:
    """
    1. Find the largest digit
    2. Find the largest digit after removing the largest digit
    """

    x_string: list[str] = [i for i in x]
    x_int_list: list[int] = [int(i) for i in x_string]

    x_int_list = g(x_int_list, k_digit)

    s = "".join(map(str, x_int_list))
    return int(s)


def algo(data: list[str]):
    total = 0
    for banks in data:
        total += largest_k_digit_integer(banks, 12)
    return total


if __name__ == "__main__":
    print(f"Answer: {algo(data)}")
