# Delimiters

# it cuts out the spaces and split the string
line = 'A lot                    of spaces'
etc = line.split()
print(etc)
print(len(etc))

# it doesn't split the string
line = 'first;second;third'
thing = line.split()
print(thing)
print(len(thing))

# it splits the string
line = 'first;second;third'
thing = line.split(';')
print(thing)
print(len(thing))