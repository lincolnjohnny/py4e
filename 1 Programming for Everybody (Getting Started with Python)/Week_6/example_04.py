# Return values

def greet(lang):
    if lang == 'es':
       print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')

print(greet('en'), 'Glenn')
print(greet('es'), 'Sally')
print(greet('fr'), 'Michael')

input("Press <ENTER> to continue")