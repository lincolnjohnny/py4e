# Tuples are comparable

print((0, 1, 2) < (5, 1, 2))
# True

print((0, 1, 200000000) < (0, 3, 4))
# True

print(('Jones', 'Sally') < ('Jones', 'Sam'))
# True

print(('Jones', 'Sally') > ('Adams', 'Sam'))
# True