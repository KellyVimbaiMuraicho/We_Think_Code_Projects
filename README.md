Problem Set 0

playback.py implements a program in Python that prompts the user for input and then outputs that same input, replacing each space with ...

indoor.py program prompts a user for input and then outputs the same in lowercase.

faces.py implements a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face). All other text should will returned unchanged.

einsten.py implements a program in python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

tip.py implements two functions:

dollars_to_float, will accept a str as input and return the amount as a float. For instance, given $50.00 as input, it should return 50.0.

percent_to_float, will accept a str as input remove the trailing %, and return the percentage as a float. For instance, given 15% as input, it should return 0.15.

Problem Set 1 

deep.py will implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

bank.py implements a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

extensions.py implements a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes.

interpretor.py implements a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

x is an integer
y is +, -, *, or /
z is an integer

meal.py implements a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, it does not  output anything at all. It assumes that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

Problem set 2 

camel.py, implements a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. It assumes that the user’s input will indeed be in camel case.

coke.py, implements a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
