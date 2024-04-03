def learn(word,char_to_find):
    return "here is your word in lowercase letters " + str(word.lower()) +" here is your word in uppercase letters " + str(word.upper()) + " here is your word with first char uppercase letter " + str(word.capitalize()) + " Your chosen char is in positon " + str(word.find(char_to_find))
print(learn("gamarjoba", "a"))