text = "hi hello hi"
w = text.split()
word_count = {}
for word in w:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)
