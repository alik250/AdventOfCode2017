from part1 import logic


def _main():
    # Get the data from the file and put it into a list, so we can alter the data without altering the source file just in case.
    instruction_list = []
    with open("input.txt") as f:
        for item in f.readlines():
            instruction_list.append(int(item))

    print(logic(instruction_list, day=2))


if __name__ == "__main__":
    _main()
