# Finding the smallest value

smallest = None
for value in [9, 41, 12, 3, 74, 15]:
    if smallest == None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('Smallest is', smallest)