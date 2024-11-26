def vowel_count(x):
    count = 0
    for i in x:
        if i in "aeiou":
            count += 1
    return count


def sort_vowel(x):
    return sorted(x, key= vowel_count)


print(sort_vowel(["octopus", "to", "teepee", "doe"]), "should be", ["to", "doe", "octopus", "teepee"])
