history = ''
current = ''

while True:
    inp = input("Enter text:")
    if inp != 'quit':
        if history != '':
            current = inp
            print(history)
            print(current)
            history = current
        else:
            history = inp
            print(history)
            print(current)
    else:
        break