user_answer = input("What is the Answer to the Great Question of Life, the Universe and Everything?")

# Convert the user's answer to lowercase and remove any leading/trailing whitespace
given_answer = user_answer.lower().strip()

if given_answer == "42" or given_answer == "forty-two" or given_answer == "forty two":
    print("Yes")
else:
    print("No")