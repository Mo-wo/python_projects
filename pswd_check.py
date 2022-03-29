def good_length(password):
    return len(password) > 8 and len(password) < 64

print(good_length("Onyemowo23455!@+_\""))
print(good_length("Mowo"))
