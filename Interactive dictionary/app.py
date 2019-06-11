import json
from difflib import get_close_matches


def dictionary_final(words):
    data = json.load(open("data.json"))
    w = words
    return data[get_close_matches(w, data.keys())[0]]


def dictionary(words):
    data = json.load(open("data.json"))
    word = words

    def translate(w):
        w = w.lower()
        if w in data:
            return data[w]
        elif len(get_close_matches(w, data.keys())) > 0:
            return {f"Did you mean {get_close_matches(w, data.keys())[0]} instead? click below button to confirm."}
            if yn == "Y":
                return data[get_close_matches(w, data.keys())[0]]
            elif yn == "N":
                return "The word doesn't exist. Please double check it."
            else:
                return "We didn't understand your entry."
        else:
            invalid = ["Impossible word!!! you are trying to fool me."]
            return invalid

    # word = input("Enter word: ")
    output = translate(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
    return output
