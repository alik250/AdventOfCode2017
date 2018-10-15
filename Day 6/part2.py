from part1 import *


def _main():
    bank = None
    with open("input.txt") as f:
        bank = MemoryBank(parse_list(f.readline()))

    bank.redistribute()
    print((len(bank.all_data) - 1) - bank.all_data.index(bank.all_data[-1]))


if __name__ == "__main__":
    _main()
