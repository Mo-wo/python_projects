
def start_with(str1, str2):
    return str1[0] == str2[0]

print(start_with("apple", "sauce"))
print(start_with("banana", "biscuits"))
print(start_with("hi", "hello"))
print(start_with("myname", "yourname"))

def start_K(string):
    if string[0] == "K":
        return True
    else:
        return False

print(start_K("Kelly"))
print(start_K("Abe"))
