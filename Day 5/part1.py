
def raise_by_one(x, y=1):
    '''Add y to the absolute value of x, keeping negatives'''
    if x < 0:
        return 0 - ((0 - x) + y)
    else:
        return x + y


def logic(instruction_list: list, day=1, debug=False):

    total_instructions = 0
    current_index = 0

    try:
        # Primary logic loop. Read and evaluate instructions.
        while True:

            # Save the index we are about to use. We need to increment the instruction before throwing it away.
            new_index = instruction_list[current_index] + current_index

            if debug:
                print("total: {} -- index: {} -- instruction: {}".format(
                    total_instructions,
                    current_index,
                    instruction_list[current_index]))

            # Update variables
            if day == 1:
                instruction_list[current_index] += 1
            elif day == 2:
                if instruction_list[current_index] > 2:
                    instruction_list[current_index] -= 1
                else:
                    instruction_list[current_index] += 1
            current_index = new_index
            total_instructions += 1

    except IndexError:
        return (total_instructions)


def _main():
    # Get the data from the file and put it into a list, so we can alter the data without altering the source file just in case.
    instruction_list = []
    with open("input.txt") as f:
        for item in f.readlines():
            instruction_list.append(int(item))

    print(logic(instruction_list))


if __name__ == "__main__":
    _main()
