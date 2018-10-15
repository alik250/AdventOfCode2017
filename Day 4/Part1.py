class Passphrase:
    def __init__(self, is_legit=True):
        self.contents = []
        self.is_legit = is_legit

    def __str__(self):
        return str(self.contents)

    def pack(self, string):
        '''packs string into phrase. '''
        if string in self.contents:
            self.is_legit = False
        self.contents.append(string)


def parse_line(text: str, spacers=(' ', '\n')):
    '''Generator. Yields strings to be put into passphrase objects, as divided by spacers'''
    temp_string = ""
    for char in text:
        if char in spacers and len(temp_string) > 0:
            yield temp_string
            temp_string = ""
        else:
            temp_string += char

    if len(temp_string) > 0:
        yield temp_string


def _main():
    with open("input.txt") as f:
        phrases = []
        legit_count = 0

        for i in f.readlines():
            temp_phrase = Passphrase()

            for j in parse_line(i):
                temp_phrase.pack(j)
                print(j)

            print(temp_phrase)

            if temp_phrase.is_legit:
                print("Legit phrase! ")
                legit_count += 1
            else:
                print("Not legit! ")
            # print("------------------")
        print(legit_count)


if __name__ == "__main__":
    _main()
