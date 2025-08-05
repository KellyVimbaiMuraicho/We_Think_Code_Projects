# prompt user greeting 
greeting = input("May you please greet us today !")

#Convert the user's answer to lowercase and remove any leading/trailing whitespace.
given_greeting = greeting.lower().strip()

if given_greeting == "hello":
    print("$0")

elif given_greeting[0] == "h":
    print("$20")

else:
    print("$100")
