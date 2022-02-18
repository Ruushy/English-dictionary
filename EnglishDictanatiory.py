import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translating(w):
    w= w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        sure = input("did you mean %s instead (enter Y for yes OR N for no: " %get_close_matches(w,data.keys())[0])
        if sure == "y":
            return data[get_close_matches(w,data.keys())[0]]
        else :
            return "the word doesn't exist"

    else :
        return "the word doesn't exist"




word = input("enter a word: ")
output = translating(word)
if type(output) == list:
    for i in output:
        print(i)
else :
    print(output)











