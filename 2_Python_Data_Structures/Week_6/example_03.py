# Things not to do with Tuples

x = (3, 2, 1)
x.sort()
# AttributeError: 'tuple' object has no attribute 'sort'

x.append(5)
# AttributeError: 'tuple' object has no attribute 'append'

x.reverse()
# AttributeError: 'tuple' object has no attribute 'reverse'