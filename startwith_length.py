def startwith_short_str(str1, str2):
    length = len(str2)
    return str1[0:length] == str2

print(startwith_short_str("manage", "man"))
print(startwith_short_str("imagery", "image"))
print(startwith_short_str("mummy", "mommy"))
print(startwith_short_str("honey", "honey"))
print(startwith_short_str("witchcraft", "witchy"))
print(startwith_short_str("tin", "tinkerbell"))

def starts_with_str2(str1, str2):
    for position in range(len(str2)):
        if str1[position] != str2[position]:
            return False
    return True

print(starts_with_str2("manage", "man"))
print(starts_with_str2("imagery", "image"))
print(starts_with_str2("mummy", "mommy"))
print(starts_with_str2("honey", "honey"))
print(starts_with_str2("witchcraft", "witchy"))
print(starts_with_str2("tin", "tinkerbell"))

