# prompt the user for a greeting.
greeting = input("May you please greet us today !")

#Converts user's answer to lowercase and removes any leading/trailing whitespace.
given_greeting = greeting.lower().strip()

if given_greeting == "hello":
    print("$0")
    
elif given_greeting[0] == "h":
    print("$20")
    
else:
    print("$100")
    
