# The Double split pattern

fhand = open('mbox-short.txt')
for line in fhand :
    line.rstrip()
    if not line.startswith('From ') :
        continue
    words = line.split()
    email = words[1]
    pieces = email.split('@')
    print(pieces[1])