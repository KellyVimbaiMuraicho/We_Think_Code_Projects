def replace_camel_case():
    #this will initialise new string before the loop.
    new_user_camel_case = ""
    
    user_camel_case = input("What is your variable in camel case? ")

    for char in user_camel_case:
        if char.isupper():
            # Adds an underscore and the lowercase version of the character
            new_user_camel_case += "_" + char.lower()
        else:
            # Adds the character as is, ensuring it's lowercase
            new_user_camel_case += char.lower()
    
    # Returns the new string after the loop has finished
    return new_user_camel_case

#  calls the function to run it and print the result
print(replace_camel_case())