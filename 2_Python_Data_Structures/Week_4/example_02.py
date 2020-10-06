# Tale of two Loops

friends = ['Joseph', 'Gleen', 'Sally']

# when we increment inside the elements of the variable friends
for friend in friends :
    print('Happy New Year', friend)

print()
# when we increment based of an index created from the range of the "friends" length :-)
for i in range(len(friends)) :
    friend = friends[i]
    print('Happy New Year', friend)