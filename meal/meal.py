def main():
    """
    Prompts the user for a time and outputs if it's breakfast, lunch, or dinner time.
    """
    time_str = input("What time is it? ")
    hours = convert(time_str)

    # Check if the time is within the meal ranges
    if 7.0 <= hours <= 8.0:
        print("breakfast time")
    elif 12.0 <= hours <= 13.0:
        print("lunch time")
    elif 18.0 <= hours <= 19.0:
        print("dinner time")


def convert(time):
    """
    Converts a time string in 24-hour format (e.g., "7:30" or "12:00")
    to the corresponding number of hours as a float.
    """
    # Split the string into hours and minutes
    hours_str, minutes_str = time.split(":")

    # Convert the strings to integers
    hours = int(hours_str)
    minutes = int(minutes_str)

    # Calculate the total time as a float
    return hours + (minutes / 60)


if __name__ == "__main__":
    main()