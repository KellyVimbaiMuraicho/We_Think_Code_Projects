

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Rule 1: Check length
    if len(s) < 2 or len(s) > 6:
        return False

    # Rule 2: Check first two characters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Rule 3: Check for numbers in the middle and starting with '0'
    found_number = False
    for i, char in enumerate(s):
        if char.isdigit():
            found_number = True
            if i > 0 and char == '0': # Ensures '0' is not the first number
                if not s[i-1].isdigit():
                    return False
        elif found_number:
            # Rule: letter appears after a number
            return False

    # Rule 4: Check for punctuation
    for char in s:
        if not char.isalnum():
            return False

    # If all checks pass
    return True
main()