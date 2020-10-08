# Even Shorter Version of The top 10 most common words in a file

fhand = open('romeo.txt')
counts = dict()
for line in fhand :
    words = line.split()
    for word in words :
        counts[word] = counts.get(word,0) + 1

print(sorted([(value,key) for key,value in counts.items()], reverse=True))