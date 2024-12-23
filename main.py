def is_alphabet(char):
    """
    Checks if the given character is an alphabet.

    Args:
        char: The character to check.

    Returns:
        True if the character is an alphabet, False otherwise.
    """

    if (ord('a') <= ord(char) <= ord('z')) or (ord('A') <= ord(char) <= ord('Z')):
        return True
    else:
        return False

# Get input from the user
char = input("Enter a character: ")

# Check if the character is an alphabet
if is_alphabet(char):
    print(char, "is an alphabet.")
else:
    print(char, "is not an alphabet.")