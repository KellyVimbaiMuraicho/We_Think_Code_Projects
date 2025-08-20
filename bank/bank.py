# Get the user's greeting
greeting = input("May you please greet us today! ")

# Convert the greeting to lowercase and remove extra whitespace
given_greeting = greeting.lower().strip()

# Check the conditions in the correct order
if given_greeting == "hello":
    print("$0")
elif given_greeting.startswith("h"):
    print("$20")
else:
    print("$100")

