def read_input(input_file: str, debug: bool = False) -> list[str]:
    try:
        with open(input_file, "r") as f:
            if debug:
                print("The file exists on your path!")
            # https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list
            return [line.rstrip("\n") for line in f]
    except FileNotFoundError:
        raise FileNotFoundError(f"Oops, the file does not exist on the path.")


def dial(instruction: list[str]) -> int:
    """Sums a list of numbers"""
    dial_position = 50
    zero_hits = 0

    for ins in instruction:
        val = int(ins[1:])
        current_position = dial_position

        if ins[:1] == "R":
            dial_position += val

            distance_to_zero = 100 - current_position

            if val >= distance_to_zero:
                zero_hits += 1

                remaining = val - distance_to_zero
                zero_hits += remaining // 100

        elif ins[:1] == "L":
            dial_position -= val

            if current_position == 0:
                distance_to_zero = 100
            else:
                distance_to_zero = current_position - 0

            if val >= distance_to_zero:
                zero_hits += 1

                remaining = val - distance_to_zero
                zero_hits += remaining // 100

        dial_position %= 100

    return zero_hits


def algo(file: str) -> int:
    """
    Algorithm:

    1. convert each line into an element in a list
    2. assign 'R' as positive and 'L' as negative
    3. starting from 50, add R or subtract L from it
    4. if the dial passes through or points at 0, increment counter by 1
    6. return the counter
    """
    instructions = read_input(file)

    return dial(instructions)


def main():
    """
    Following the same rotations as in the above example, the dial points at zero a few extra times during its rotations:

    The dial starts by pointing at 50.
    The dial is rotated L68 to point at 82; during this rotation, it points at 0 once.
    The dial is rotated L30 to point at 52.
    The dial is rotated R48 to point at 0.
    The dial is rotated L5 to point at 95.
    The dial is rotated R60 to point at 55; during this rotation, it points at 0 once.
    The dial is rotated L55 to point at 0.
    The dial is rotated L1 to point at 99.
    The dial is rotated L99 to point at 0.
    The dial is rotated R14 to point at 14.
    The dial is rotated L82 to point at 32; during this rotation, it points at 0 once.
    In this example, the dial points at 0 three times at the end of a rotation, plus three more times during a rotation. So, in this example, the new password would be 6.

    Be careful: if the dial were pointing at 50, a single rotation like R1000 would cause the dial to point at 0 ten times before returning back to 50!
    """
    print(f"Answer: {algo('input.txt')}")


if __name__ == "__main__":
    main()
