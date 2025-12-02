from rich import print


def read_file(input_file: str):
    with open(input_file, "r") as f:
        return f.read().strip().split(",")


def check(id_string: str):
    """
    For exact duplicates of 2 an even length string is required.
    """
    start, end = id_string.split("-")
    total = 0

    for ids in range(int(start), int(end) + 1, 1):
        # https://stackoverflow.com/questions/1906717/how-to-split-an-integer-into-a-list-of-digits
        id_list = [int(i) for i in str(ids)]
        midpoint = len(id_list) // 2
        if id_list[:midpoint] == id_list[midpoint:]:
            total += ids

    return total


def algo() -> int:
    """
    Algorithm:

    1. get file input and split each id into individual list elements
    2. loop over each id to check the range for invalid ids
    3. use an algorithm to check the id for sequence of digits that repeats twice
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
    The ranges are separated by commas (,); each range gives its first ID and last ID separated by a dash (-).

    Since the young Elf was just doing silly patterns, you can find the invalid IDs by looking for any ID which is made only of some sequence of digits repeated twice. So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.

    None of the numbers have leading zeroes; 0101 isn't an ID at all. (101 is a valid ID that you would ignore.)

    Your job is to find all of the invalid IDs that appear in the given ranges. In the above example:

        11-22 has two invalid IDs, 11 and 22.
        95-115 has one invalid ID, 99.
        998-1012 has one invalid ID, 1010.
        1188511880-1188511890 has one invalid ID, 1188511885.
        222220-222224 has one invalid ID, 222222.
        1698522-1698528 contains no invalid IDs.
        446443-446449 has one invalid ID, 446446.
        38593856-38593862 has one invalid ID, 38593859.
        The rest of the ranges contain no invalid IDs.

    Adding up all the invalid IDs in this example produces 1227775554.

    What do you get if you add up all of the invalid IDs?
    """
    print(f"Answer: {algo()}")
    # print(check("62371645-62509655"))


if __name__ == "__main__":
    main()
