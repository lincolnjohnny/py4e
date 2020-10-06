str1 = "Hello "
str2 = 'there'
bob = str1 + str2
print(bob)

str3 = '123'
# cannot concatenate 'str' and 'int' objects
# str3 = str3 + 1

# we have to convert to int before
x = int(str3) + 1
print(x)