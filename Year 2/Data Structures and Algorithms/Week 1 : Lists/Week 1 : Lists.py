def is_pal(word):
    if word[::1] == word[::-1]:
        return True

print(is_pal("happah"))