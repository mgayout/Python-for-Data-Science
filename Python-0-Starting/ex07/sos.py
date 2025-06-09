import sys


def convertMorse(string):
    NESTED_MORSE = {" ": "/ ", "A": ".- ", "B": "-... ", "C": "-.-. ",
                    "D": "-.. ", "E": ". ", "F": "..-. ", "G": "--. ",
                    "H": ".... ", "I": ".. ", "J": ".--- ", "K": "-.- ",
                    "L": ".-.. ", "M": "-- ", "N": "-. ", "O": "--- ",
                    "P": ".--. ", "Q": "--.- ", "R": ".-. ", "S": "... ",
                    "T": "- ", "U": "..- ", "V": "...- ", "W": ".-- ",
                    "X": "-..- ", "Y": "-.-- ", "Z": "--.. ", "1": ".---- ",
                    "2": "..--- ", "3": "...-- ", "4": "....- ",
                    "5": "..... ", "6": "-.... ", "7": "--... ",
                    "8": "---.. ", "9": "----. ", "0": "----- "}

    morse = ""

    for char in string.upper():
        morse += NESTED_MORSE[char]

    return morse


def specialChar(string):
    return all(char.isalnum() or char.isspace() for char in string)


def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        chars = list(sys.argv[1])
        events = list(filter(specialChar, chars))
        if len(events) != len(chars):
            raise AssertionError("the arguments are bad")
        print(convertMorse(sys.argv[1]))
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()
