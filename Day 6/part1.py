class MemoryBank:
    def __init__(self, init_value: list):
        self.all_data = [init_value, ]
        self.redistribute_cycles = 0


    def redistribute(self):
        '''MemoryBank.redistribute() -> int. Redistributes all_data[-1] according to the rules, and appends to all_data. '''
        while True:
            data = list(self.all_data[-1])
            temp = self.largest()
            highest_value, highest_index = temp[1], temp[0]
            del temp

            new_list = self.assign_and_wrap(data, highest_index, highest_value)
            self.redistribute_cycles += 1

            if new_list in self.all_data:  # Conditions met!!!
                self.all_data.append(new_list)
                return len(self.all_data)
                
            self.all_data.append(new_list)


    def largest(self, index=-1):
        '''self.largest() -> tuple(index: int, item: int). Highest value stored in the bank's most recent entry. '''
        highest = 0
        highest_index = 0
        for ind, item in enumerate(self.all_data[index]):
            if item > highest:
                highest = item
                highest_index = ind
        return (highest_index, highest)
        

    @staticmethod
    def assign_and_wrap(list_to_assign_to: list, starting_index: int, times_to_assign: int, value_to_assign=1):
        '''Starting at {starting_index}, loops around the given list adding the given value to the current value the given amount of times. If end of list is reached, wrap around to first item.'''
        list_to_assign_to[starting_index] = 0
        starting_index += 1
        while times_to_assign > 0:
            try:
                list_to_assign_to[starting_index] += value_to_assign
                times_to_assign -= 1
                starting_index += 1
            except IndexError:
                starting_index = 0
        return list_to_assign_to


def parse_list(string, separators=(' ', '\t', '\n')):
    '''parse_list(string) -> list<int>. Parses a string into a list of integers, divided by the given separators. '''
    output = []
    temp_word = ""
    for i in string:
        if i in separators and len(temp_word) > 0:
            output.append(int(temp_word))
            temp_word = ""
        elif i not in separators:
            temp_word += i
    if len(temp_word) > 0:
        output.append(int(temp_word))
    return output


def _main():
    bank = None
    with open("input.txt") as f:
        bank = MemoryBank(parse_list(f.readline()))

    print(bank.redistribute())


if __name__ == "__main__":
    _main()
