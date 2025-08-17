def remove_vowels(word):
    vowels = "aeiouAEIOU"
    new_word = ""
    for char in word:
        if char not in vowels:
            new_word += char
    return new_word

user_input = input("Enter a word: ")
result = remove_vowels(user_input)
print("The word without vowels is:", result)
                