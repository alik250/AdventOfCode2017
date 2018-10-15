class Captcha:
    def __init__(self):
        self.DIGITS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

    def returnPart1(self, userInput):
        lastDigit = ""
        lumpSum = 0

        for element in userInput:
            if element not in self.DIGITS:
                raise TypeError(
                    "Only numbers are permitted in this operation. ")

            if element == lastDigit:
                lumpSum += int(element)

            lastDigit = element

        if userInput[len(userInput) - 1] == userInput[0]:
            lumpSum += int(userInput[0])

        return lumpSum

    def returnPart2(self, userInput):
        indexMod = int(len(userInput) / 2)
        lumpSum = 0
        currentIndex = 0

        for element in userInput:
            try:
                if element == userInput[currentIndex + indexMod]:
                    lumpSum += int(element) * 2
                currentIndex += 1
            except IndexError:
                return lumpSum

        return lumpSum


def _main(*args):
    try:
        f = open("puzzleInput.txt")
        getInput = f.read()
        thisCaptcha = Captcha()

        if "1" in args:
            print(thisCaptcha.returnPart1(getInput))

        if "2" in args:
            print(thisCaptcha.returnPart2(getInput))

    finally:
        f.close()


if __name__ == "__main__":
    _main("1", "2")
