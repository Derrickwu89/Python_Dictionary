import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys()))>0:
        guess = input("Do you mean {}? Please answer Yes or No? ".format(get_close_matches(word, data.keys())[0]))
        if guess.lower() == "yes":
            return data[get_close_matches(word, data.keys())[0]]
        elif guess.lower() == "no":
            return "Please enter the correct word that you want to define"
        else:
            return "I don't understand your answer, please try again later."
    else:
        return "The {} cannot be found in the dictionary".format(word)

word = input("Please define: ")

print(translate(word))
