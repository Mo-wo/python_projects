from asyncore import write
import string

test_words = ["crap", "darn!", "Heck!!!", "jerk...", "idiot?", "butt", "devil"]


def bleeper(rudeword):
    pos = 0
    for char in rudeword:
        if char not in string.punctuation:
            char = "*"
        else:
            char = char
        rudeword = rudeword.replace(rudeword[pos], char)
        pos += 1
    return rudeword

for rudeword in test_words:
    with open("bleeped_word.py", "w") as file:
        print(bleeper(rudeword))
        file.write(bleeper(f"{rudeword}\n"))



print(bleeper("crap"))
bleeper("darn!")
bleeper("Heck!!!")
bleeper("jerk...")
bleeper("idiot?")
bleeper("butt")
bleeper("devil")