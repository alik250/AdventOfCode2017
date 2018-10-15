class SpreadSheet:
    def __init__(self, string: str):
        self.string = string
        self._sheet = self._parseString()
        del self.string

    def _parseString(self):
        VALID_CHARACTERS = ("1", "2", "3", "4", "5",
                            "6", "7", "8", "9", "0")
        DIVIDERS = (" ", "\t")
        NEWLINES = ("\n")
        tempElement = ""
        tempSheetElement = []
        sheet = []

        for i in self.string:
            if i in VALID_CHARACTERS:
                tempElement += i

            if i in DIVIDERS or i in NEWLINES:
                if len(tempElement) != 0:
                    tempSheetElement.append(int(tempElement))
                    tempElement = ""

            if i in NEWLINES:
                sheet.append(tuple(tempSheetElement))
                tempSheetElement = []

        if len(tempElement) != 0:
            tempSheetElement.append(int(tempElement))
            sheet.append(tuple(tempSheetElement))

        return tuple(sheet)

    @property
    def checksum(self):
        lowestVal = 1000000
        highestVal = -1
        toBeSummed = []

        for i in self._sheet:
            for j in i:
                #print("{} --- {}".format(j, int(j)))
                if int(j) > highestVal:
                    highestVal = int(j)

                if int(j) < lowestVal:
                    lowestVal = int(j)

            toBeSummed.append(highestVal - lowestVal)

            lowestVal = 1000000
            highestVal = -1

        checksum = 0
        for i in toBeSummed:
            checksum += i

        return checksum

    @property
    def secondChecksum(self):
        compatibleValues = []
        lumpSum = 0

        for i in self._sheet:
            for j in i:
                for k in i:
                    if k == j:
                        continue

                    if k % j == 0:
                        #print("Match found! {}---{}".format(k, j))
                        compatibleValues.append((k, j))
                        break
                else:
                    continue
                break
            else:
                raise Exception(
                    "No match found in this row. Invalid input. {0}Row: {1} ".format("\n", i))

        for i in compatibleValues:
            lumpSum += i[0] / i[1]

        return lumpSum

    @property
    def sheetX(self):  # Just for fun
        highestCount = 0
        tempCount = 0

        for i in range(len(self._sheet)):
            for j in self._sheet[i]:
                tempCount += 1

            if tempCount > highestCount:
                highestCount = tempCount

            tempCount = 0

        return highestCount

    @property
    def sheetY(self):  # Just for fun
        return len(self._sheet)


def _main():
    try:
        inputFile = open("input.txt")
        spreadSheet = SpreadSheet(inputFile.read())

        print(spreadSheet._sheet)

        print("-{}-".format(spreadSheet.checksum))

        print("~{}~".format(spreadSheet.secondChecksum))

        print(spreadSheet.sheetX, spreadSheet.sheetY)

    finally:
        inputFile.close()


if __name__ == "__main__":
    _main()
