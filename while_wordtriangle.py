def wordinput():
    word = input("Enter a word here: ")
    return word

def asc_triangle():
    word = wordinput()
    length = len(word)
    n = 0
    while n < length:
        # alternatively increment can be placed here instead
        print(word[:n + 1])
        n += 1

def desc_triangle():
    word = wordinput()
    n = len(word)
    while n >= 1:
        print(word[:n])
        n -= 1
        
def wordtriangle():
    angleType = input("Do you want an ascending or descending triangle?\n")
    if angleType == "ascending":
        asc_triangle()
    elif angleType == "descending":
        desc_triangle()
    else:
        print("Invalid input! Select either 'ascending' or 'descending'")
        wordtriangle()

wordtriangle()
