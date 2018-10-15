import math


def TODO(message):
    raise NotImplementedError(message)


class Logger:
    '''
    Object. Logs if {Logger.debug}==True. Send only strings, use string formatting when necessary.
    '''
    debug = False

    @staticmethod
    def log(*messages):
        '''Send only strings. Use string formatting when necessary.'''
        if Logger.debug:
            output = ""
            for i in messages:
                output += i
            print(output)


class SpiralSquare:
    '''Base spiral square class.'''

    def __init__(self, end_value: int):
        self.end_value = end_value
        self.data = self._construct(self.get_next_odd_square(end_value))
        self.cardinal_values = self._get_cardinal_values()

    def _construct(self, end: int):    # return tuple of tuples
        '''Main logic. Takes the {end_value} and returns a list of lists, representing a list of rings around the starting value, of {1}. '''

        data = []
        ring = []

        for i in range(1, end + 1):
            ring.append(i)

            if (math.sqrt(i)) % 2 == 1:
                data.append(tuple(ring))
                ring.clear()

        return tuple(data)

    def _get_cardinal_values(self):    # return tuple of tuples
        '''
        Using {self.data}, find the values at the middle of the edges, where the distance is closest to the center. 
        '''
        cardinal_values = []
        ring_index = 0

        for i in self.data:  # done
            # i is now a ring of the spiral, containing ascending integers starting with the beginning of the ring

            # Skip the first ring (innermost "ring", containing only 1 in a tuple)
            if i[0] == 1:
                cardinal_values += tuple([i])
                ring_index += 1
                continue

            # Append a tuple of the cardinal values we just found to the main cardinal values list
            cardinal_values += [tuple(range(i[ring_index - 1],
                                            i[len(i) - 1],
                                            ring_index * 2))]

            ring_index += 1

        return tuple(cardinal_values)

    def get_manhattan_value(self, value: int=None):    # return int
        '''
        Return: int. Return the manhattan distance from the value given to the center of the square. If no value is given, default to {self.end_value}. 
        '''

        # If no value is manually entered, use the {self.end_value} variable used to create the square in the first place.
        if value is None:
            value = self.end_value

        # If the value is 1, it is already at the center of the square. No need to calculate anything.
        if value == 1:
            return 0

        return_value = 0

        # Getting the index of the ring that [value] resides in
        def get_correct_index(_value):
            for index, item in enumerate(self.data):
                if _value in self.data[index]:
                    Logger.log("Value found in ring {}".format(index),
                               "\n", "cardinal_values[index]: {}".format(self.cardinal_values[index]))
                    return index

        ring_index = get_correct_index(value)
        Logger.log("get_manhattan_value.ring_index: {}".format(ring_index))

        # Checking distance from each cardinal value. Returning the lowest distance.
        def lowest_distance():

            def distance_from_zero(item):
                if item < 0:
                    return 0 - item
                else:
                    return item

            potential_distances = []
            for i in self.cardinal_values[ring_index]:
                potential_distances += [distance_from_zero(value - i)]

            Logger.log("get_manhattan_value.lowest_distance.potential_distances: {}".format(
                potential_distances))

            # Using [value], because the potential cardinal distances will always be less than the value we're looking for
            # the manhattan distance for (and because there's no [MAX_INT] variable)
            actual_lowest_distance = value
            for i in potential_distances:
                if i < actual_lowest_distance:
                    actual_lowest_distance = i

            return actual_lowest_distance

        distance = lowest_distance()
        Logger.log("get_manhattan_value.distances: {}".format(distance))

        return distance + ring_index

    @staticmethod
    def get_next_odd_square(value):    # return int
        if value <= 1:
            return 1

        # (start (with 1 so they will all be odd), stop, step)
        for i in range(1, value, 2):
            if i * i < value:
                continue
            else:
                return i * i

    @classmethod
    def from_number_of_rings(cls, num_of_rings: int):  # Not Implemented
        TODO("Object creator with number of rings instead of goal value")


def _main():
    # Logger.debug = True
    with open("input.txt") as f:
        puzzle_input = int(f.read())
        print(SpiralSquare(puzzle_input).get_manhattan_value())


if __name__ == "__main__":
    _main()
