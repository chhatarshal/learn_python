print('Type input values: \n')
iv = input()

worlds = [wd for wd in iv.split(' ') if wd]
print(len(worlds))
words_n_counts = {}

for word in worlds:
    if word in words_n_counts:
        words_n_counts[word] =  words_n_counts[word] + 1
    else:
        words_n_counts[word] = 1

[words_n_counts[w] =  words_n_counts[w] + 1 for w in worlds if word in words_n_counts]

print(words_n_counts)
