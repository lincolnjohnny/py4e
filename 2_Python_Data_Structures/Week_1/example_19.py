# Parsing and Extracting

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

# identify the position of '@' in the string
atpos = data.find('@')
print(atpos)

# identify the fist ' ' after '@'
posat = data.find(' ', atpos)
print(posat)

host = data[atpos+1 : posat]
print(host)