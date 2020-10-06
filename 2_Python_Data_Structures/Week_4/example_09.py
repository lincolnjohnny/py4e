# Find the average from the elements of a numeric list

numlist = list()
while True :
    inp = input('Enter a number: ')
    if inp == 'done' :
        break
    try:
        value = float(inp)
    except:
        print('Invalid number')
        continue
    numlist.append(value)

average = sum(numlist)/len(numlist)
print('Average is', average)