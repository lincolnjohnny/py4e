# Definite Loops and Dictionaries

# the loop goes through the KEYS of the dictionary (chuck, fred, jan), not the values (1, 42, 100)
counts = {'chuck': 1, 'fred': 42, 'jan': 100}
for key in counts :
    print(key, counts[key])