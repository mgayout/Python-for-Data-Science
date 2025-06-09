import sys


def textBuilding(text):

    """
    Analyzes the given text and prints counts of different character types.

    Parameters:
        text (str): The text to analyze.

    Displays:
    - Total number of characters
    - Number of uppercase and lowercase letters
    - Number of punctuation marks
    - Number of spaces
    - Number of digits
    """

    character = len(text)
    print(f"The text contains {character} characters:")

    upper = sum(1 for char in text if char.isupper())
    print(f"{upper} upper letters")

    lower = sum(1 for char in text if char.islower())
    print(f"{lower} lower letters")

    punctuationList = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    punctuation = sum(1 for char in text if char in punctuationList)
    print(f"{punctuation} punctuation marks")

    space = sum(1 for char in text if char.isspace())
    print(f"{space} spaces")

    digit = sum(1 for char in text if char.isdigit())
    print(f"{digit} digits")


def main():

    """
    Handles user input and controls the program flow.

    Reads input from:
    - Command line argument, if provided
    - Standard input, otherwise (prompting the user)

    Calls:
        textBuilding(text)

    Catches:
    - AssertionError: if more than one argument is given
    - KeyboardInterrupt: if the user interrupts input (Ctrl+C)
    """

    try:
        size = len(sys.argv)
        if size == 1:
            print("What is the text to count?")
            text = sys.stdin.read()
            print("")
        elif size > 2:
            raise AssertionError("more than one argument is provided")
        else:
            text = sys.argv[1]
        textBuilding(text)
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt")


if __name__ == "__main__":
    main()
