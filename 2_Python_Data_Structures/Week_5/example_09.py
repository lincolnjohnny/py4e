# Retrieving lists of Keys and Values

jjj = {'chuck': 1, 'fred': 42, 'jan': 100}

print(jjj) # keys and values
print(list(jjj)) # only keys

# keys, values, items methods
print(jjj.keys())       # dict_keys
print(jjj.values())     # dict_values
print(jjj.items())      # dict_items