#1. Ask user for variable name in camel case.

#2.from user output where there is uppercase replace with underscore and convert to lowercase.

#3.Print new name in snake case.

def replace_camel_case():
    # 1. Initialize the new string before the loop
    new_user_camel_case = ""
    
    user_camel_case = input("What is your variable in camel case? ")

    for char in user_camel_case:
        if char.isupper():
            # Add an underscore and the lowercase version of the character
            new_user_camel_case += "_" + char.lower()
        else:
            # Add the character as is, ensuring it's lowercase
            new_user_camel_case += char.lower()
    
    # 2. Return the new string after the loop has finished
    return new_user_camel_case

# You need to call the function to run it and print the result
print(replace_camel_case())