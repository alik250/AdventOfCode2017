from day3 import Logger, SpiralSquare
import math

log = True


class IndexObject:
    def __init__(self, value: int=None, coords: list=[0, 0]):
        self.value = value
        self.coords = [coords[0], coords[1]]

    def __sub__(self, other):
        return [abs(self.coords[0] - other.coords[0]), abs(self.coords[1] - other.coords[1])]

    def __repr__(self):
        return f"IndexObject({self.value}, {self.coords})"

    def __str__(self):
        return f"{self.coords} {self.value}"

    # Use the modulo operator to return if an object is adjacent to another.
    def __mod__(self, other):  # return bool
        '''Pass only IndexObjects. Return bool.'''
        test = self - other
        return test[0] <= 1 and test[1] <= 1

    @property
    def is_instantiated(self):
        return False if self.value is None else True


class CumulativeSpiralSquare:
    def __init__(self, target_value):
        self.target_value = target_value

        # self.data is a list containing lists of IndexObjects. These objects are organized by which ring of the spiral they are in.
        self.data = []
        for i in self._construct_data():
            self.data.append(i)
            if log:
                print(i)

    def _construct_data(self):
        '''
        Generates IndexObjects
        '''
        yield [IndexObject(1, [0, 0])]

        ring_data = []
        coord_pairs = generate_coords(self.target_value)
        index = 1

        while True:
            if log:
                print("logged")
            coords = next(coord_pairs)
            current_obj = IndexObject(0, coords)

            # search for adjacent squares
            # self.data[-1] and ring_data will be the only places we need to search
            for item in self.data[-1]:
                # if current_obj is adjacent to item:
                if current_obj % item:
                    # add the adjacent square's values
                    current_obj.value += item.value
            for item in ring_data:
                if current_obj % item:
                    current_obj.value += item.value

            if log:
                print(current_obj.value)

            # current_obj is now at the correct state. Append to ring_data
            ring_data.append(current_obj)

            # if the coordinates are equal to [+x, -x], the ring is concluded. Yield the ring and continue
            if coords[0] == abs(coords[0]) and coords[1] == (coords[0] - (coords[0] * 2)):
                yield ring_data
                ring_data = []

            # the first value larger than self.target_value is what we want
            if current_obj.value > self.target_value:
                self._goal_reached(current_obj.value)

            index += 1

    def _goal_reached(self, value):
        print(f"Value found! Value: {value}")
        input("Press any key to continue...")
        exit()


def generate_coords(times: int):
    '''
    Yields every coordinate pair in the spiral square (besides [0, 0]) in order they appear
    '''
    x = 0
    y = 0
    # Iterate more times as we need; unused iterations will be ignored
    for i in range(1, times):

        # If i is odd, we want to add to x and y.
        if i % 2 == 1:

            # We want to add 1 to x, (i) times, and then yield the updated coordinates.
            for plus_x in range(i):
                x = x + 1
                yield [x, y]

            # And then to y.
            for plus_y in range(i):
                y = y + 1
                yield [x, y]

        # If i is even, we want to subtract instead.
        else:
            for minus_x in range(i):
                x = x - 1
                yield [x, y]
            for minus_y in range(i):
                y = y - 1
                yield [x, y]


def _main():
    with open("input.txt") as f:
        square = CumulativeSpiralSquare(int(f.readline()))

        s = IndexObject(coords=(3, 2))
        print(s)


if __name__ == "__main__":
    _main()
