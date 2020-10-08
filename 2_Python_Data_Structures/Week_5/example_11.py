name = input('Enter a file name: ')
handle = open(name)

counts = dict()
for line in handle :
    words = line.split()
    for word in words :
        counts[word] = counts.get(word,0) + 1

bigkey = None
bigvalue = None
for key,value in counts.items() :
    if bigvalue is None or value > bigvalue :
        bigkey = key
        bigvalue = value

print(bigkey, bigvalue)