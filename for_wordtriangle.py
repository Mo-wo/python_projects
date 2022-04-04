def wordinput():
    word = input("Enter your word here: ")
    return word

def asc_triangle():
    word = wordinput()
    length = len(word)
    for letters in range(length):
        print(word[:letters + 1])

def desc_triangle():
    word = wordinput()
    length = len(word)
    for letters in range(length):
        print(word[:length - letters])

def word_triangle():
    angleType = input("Do you want an ascending or descending word triangle?\n")
    if angleType == "ascending":
        asc_triangle()
    elif angleType == "descending":
        desc_triangle()
    else:
        print("Invalid input! Select either 'ascending' or 'descending'\n")
        word_triangle()

word_triangle()
