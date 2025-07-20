ef main():
  sentence  = input ("sentence:")
  converted_sentence = convert(sentence)
 
  print(converted_sentence)

def convert(user_sentence):
  user_sentence = user_sentence.replace(":)", "🙂")
  user_sentence = user_sentence.replace(":(", "🙁")
  return user_sentence
 

main()
