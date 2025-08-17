<<<<<<< HEAD
# prompt the user for a greeting.
greeting = input("May you please greet us today !")

#Converts user's answer to lowercase and removes any leading/trailing whitespace.
=======
# prompt user greeting 
greeting = input("May you please greet us today !")

#Convert the user's answer to lowercase and remove any leading/trailing whitespace.
>>>>>>> ded301c5e5a09321370a090b2b35c7eaf7e59558
given_greeting = greeting.lower().strip()

if given_greeting == "hello":
    print("$0")
<<<<<<< HEAD
    
elif given_greeting[0] == "h":
    print("$20")
    
else:
    print("$100")
    
=======

elif given_greeting[0] == "h":
    print("$20")

else:
    print("$100")
>>>>>>> ded301c5e5a09321370a090b2b35c7eaf7e59558
