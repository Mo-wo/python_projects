def total_length(list):
    total = 0
    if len(list) > 0:
        for item in list:
            print(len(item))
            total = total + len(item)
        return total
    else:
        return 0

print(total_length(["main", "man", "is", "porridge"]))

def total_length(list):
    total = 0
    for item in list:
        print(len(item))
        total = total + len(item)
    return total
    
print(total_length(["main", "man", "is", "porridge"]))

