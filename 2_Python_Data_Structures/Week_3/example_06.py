# Searching Through a file

#version 1 with additional \n
fhand = open('mbox-short.txt')
for line in fhand :
    if line.startswith('From:') :
        print(line)

#version 2 without additional \n
fhand = open('mbox-short.txt')
for line in fhand :
    line = line.rstrip()
    if line.startswith('From:') :
        print(line)

#version 3
fhand = open('mbox-short.txt')
for line in fhand :
    line = line.rstrip()
    if not line.startswith('From:') :
        continue
    print(line)