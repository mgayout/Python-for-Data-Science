from ft_filter import ft_filter
import sys


def specialChar(string):
    return all(char.isalnum() or char.isspace() for char in string)


def main():

    """
    """

    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        words = sys.argv[1].split()
        events = ft_filter(specialChar, words)
        if len(list(events)) != len(words):
            raise AssertionError("strings is invalid")
        try:
            value = int(sys.argv[2])
        except ValueError:
            raise AssertionError("second argument has to be an integer")
        events = ft_filter(lambda word: len(word) >= value, words)
        print(list(events))

    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()
