word_freq = {"this": 4, "is": 2, "a": 3, "list": 1}
print(sorted(word_freq.values( ))[2])


print(sorted(word_freq.items( ))[2][1]+1)


print(word_freq["a"] - word_freq["list"])


print(word_freq.get("is"))