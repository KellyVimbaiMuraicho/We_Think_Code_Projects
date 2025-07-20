s = "This        is      CS50"
s_split = s.split()# this is going to help as a seperator any white space will be treated as one white space even if there is more.
new_str = " ".join(s_split)
new_str = new_str.replace(" ", "...")
print(new_str)
