# Reading and converting

name = input('Enter name: ')
print(name)

apple = input('Enter 100: ')
print(apple)

# unsupported operand type(s) for -: 'str' and 'int'
# x = apple - 10

# we must to convert before
x = int(apple) - 10
print(x)