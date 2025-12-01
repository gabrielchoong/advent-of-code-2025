def read_input(input_file: str, debug: bool = False) -> list[str]:
    try:
        with open(input_file, "r") as f:
            if debug:
                print("The file exists on your path!")
            # https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list
            return [line.rstrip("\n") for line in f]
    except FileNotFoundError:
        raise FileNotFoundError(f"Oops, the file does not exist on the path.")


def dial(instruction: list[str], debug: bool) -> int:
    """Sums a list of numbers"""
    dial_position = 50
    zero_hits = 0
    for ins in instruction:
        if ins[:1] == "R":
            dial_position += int(ins[1:])
        elif ins[:1] == "L":
            dial_position -= int(ins[1:])

        dial_position %= 100

        if dial_position == 0:
            zero_hits += 1

    return zero_hits


def algo(file: str) -> int:
    """
    Algorithm:

    1. convert each line into an element in a list
    2. assign 'R' as positive and 'L' as negative
    3. starting from 50, add R or subtract L from it
    4. if the counter points at 0, increment counter by 1
    5. return the counter
    """
    instructions = read_input(file)

    return dial(instructions, debug=True)


def main():
    """
    The dial starts by pointing at 50.

    You could follow the instructions, but your recent required official North Pole secret entrance security training seminar taught you that the safe is actually a decoy. The actual password is the number of times the dial is left pointing at 0 after any rotation in the sequence.

    For example, suppose the attached document contained the following rotations:

    L68
    L30
    R48
    L5
    R60
    L55
    L1
    L99
    R14
    L82
    Following these rotations would cause the dial to move as follows:

    The dial starts by pointing at 50.
    The dial is rotated L68 to point at 82.
    The dial is rotated L30 to point at 52.
    The dial is rotated R48 to point at 0.
    The dial is rotated L5 to point at 95.
    The dial is rotated R60 to point at 55.
    The dial is rotated L55 to point at 0.
    The dial is rotated L1 to point at 99.
    The dial is rotated L99 to point at 0.
    The dial is rotated R14 to point at 14.
    The dial is rotated L82 to point at 32.

    Because the dial **points at 0 a total of three times** during this process, the password in this example is 3.
    """
    print(f"Answer: {algo('input.txt')}")


if __name__ == "__main__":
    main()
