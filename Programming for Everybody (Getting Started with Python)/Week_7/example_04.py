# Looping through a set

print('Looping through a set:\n')
print('Before')
for i in [9, 41, 12, 3, 74, 15] :
    print(i)
print('After')

# Finding the largest value

print('Finding the largest value:\n')
n = -1
for i in [9, 41, 12, 3, 74, 15, 115] :
    if i > n:
        n = i
    print(i)
print('The largest value is: ', n)