def desc_triangle(string):
    length = len(string)
    for n in range(length):
        print(n, string[:length-n])

def asc_triangle(string):
    length = len(string)
    for n in range(length):
        print(n, string[:n+1])

#def word_input(word) :
 #   print(input("Enter any", word, "\n"))

def triangle_pick():
    message = input("Do you want an ascending or descending word triangle?\n")
    if message == "ascending":
        #word_input(word)
        word = input("Enter any word\n")
        asc_triangle(word)
    elif message == "descending":
        #word_input(word)
        word = input("Enter any word\n")
        desc_triangle(word)

triangle_pick()
