from rich import print


def read_file(input_file: str):
    with open(input_file, "r") as f:
        return f.read().strip().split(",")


def check(id_string: str):
    """ """
    start, end = id_string.split("-")
    total = 0

    for ids in range(int(start), int(end) + 1, 1):
        # https://stackoverflow.com/questions/1906717/how-to-split-an-integer-into-a-list-of-digits
        id_list = [int(i) for i in str(ids)]

        for i in range(1, len(id_list) // 2 + 1):
            if len(id_list) % i != 0:
                continue

            multiplier = len(id_list) // i
            if id_list[:i] * multiplier == id_list:
                total += ids
                break

    return total


def algo() -> int:
    """
    Algorithm:

    1. get file input and split each id into individual list elements
    2. loop over each id to check the range for invalid ids
    3. use an algorithm to check the id for sequence of digits that repeats at least twice
    4. compute the running sum of all the invalid ids
    5. return the running sum
    """
    data = read_file("input.txt")
    sum = 0

    for ids in data:
        sum += check(ids)

    return sum


def main():
    """
    The clerk quickly discovers that there are still invalid IDs in the ranges in your list. Maybe the young Elf was doing other silly patterns as well?

    Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice. So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), and 1111111 (1 seven times) are all invalid IDs.

    From the same example as before:

        11-22 still has two invalid IDs, 11 and 22.
        95-115 now has two invalid IDs, 99 and 111.
        998-1012 now has two invalid IDs, 999 and 1010.
        1188511880-1188511890 still has one invalid ID, 1188511885.
        222220-222224 still has one invalid ID, 222222.
        1698522-1698528 still contains no invalid IDs.
        446443-446449 still has one invalid ID, 446446.
        38593856-38593862 still has one invalid ID, 38593859.
        565653-565659 now has one invalid ID, 565656.
        824824821-824824827 now has one invalid ID, 824824824.
        2121212118-2121212124 now has one invalid ID, 2121212121.

    Adding up all the invalid IDs in this example produces 4174379265.

    What do you get if you add up all of the invalid IDs using these new rules?
    """
    print(f"Answer: {algo()}")
    # print(check("62371645-62509655"))


if __name__ == "__main__":
    main()
