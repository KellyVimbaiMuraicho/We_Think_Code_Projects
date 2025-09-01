# The program will continuously prompt the user for a fraction until a valid one is entered.
while True:
    try:
        # Prompt the user for input. The input will be read as a string.
        fuel_fraction = input("Fraction: ")
        
        # Split the string at the '/' character.
        numerator_str, denominator_str = fuel_fraction.split('/')
        
        # Convert the string parts to integers.
        # This will raise a ValueError if the parts are not valid integers.
        numerator = int(numerator_str)
        denominator = int(denominator_str)
        
        # Check for invalid conditions: denominator is 0 or numerator is greater than denominator.
        if denominator == 0:
            # If the denominator is 0, this will cause a ZeroDivisionError,
            # but we can handle it here explicitly for clarity.
            continue
        elif numerator > denominator:
            # If the numerator is greater than the denominator, the fraction is invalid.
            continue
            
    # Catch specific exceptions that might occur from the user's input.
    except ValueError:
        # This exception is raised if the user's input cannot be converted to an integer.
        # The loop will continue, prompting the user again.
        continue
    except ZeroDivisionError:
        # This exception is raised if the denominator is 0.
        # The loop will continue, prompting the user again.
        continue
    
    # If the input is valid and no exceptions were raised, proceed with the calculation.
    else:
        # Calculate the percentage of fuel.
        # The result is rounded to the nearest integer.
        fuel_percentage = round((numerator / denominator) * 100)
        
        # Check the percentage to determine the output.
        if fuel_percentage <= 1:
            print("E")
        elif fuel_percentage >= 99:
            print("F")
        else:
            print(f"{fuel_percentage}%")
            
        # Break the loop once a valid output has been printed.
        break
