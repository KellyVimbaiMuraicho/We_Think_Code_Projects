def main():
    # Prompt the user and convert input to lowercase for consistent matching
    fruit_choice = input("What type of fruit would you like to have? ").casefold()
    
    # Dictionary of fruits and their calories
    my_fruits = {
        "apple": "130", "avocado": "50", "banana": "110", "cantaloupe": "50",
        "grapefruits": "60", "grapes": "90", "honeybrew melon": "50", "kiwifruit": "90",
        "lemon": "15", "lime": "20", "nectarine": "60", "orange": "80",
        "peach": "60", "pear": "100", "pineapple": "50", "plums": "70",
        "strawberries": "50", "sweet cherries": "100", "tangerine": "50", "watermelon": "80"
    }
    
    # Gets the value for the chosen fruit, or None if it's not in the dictionary
    chosen_fruit = my_fruits.get(fruit_choice)
    
    # Check if a fruit was found (i.e., chosen_fruit is not None)
    if chosen_fruit:
        print(f"The fruit has {chosen_fruit} calories")
    # If chosen_fruit is None, the `if` condition is false, and the program will simply end
    # without printing anything, which achieves the "ignore" behavior.


main()