value = ''

while True:
    first_value = input("enter first value or value q to exit: ")
    if first_value == 'q':
        break

    second_value = input("enter second value or value q to exit: ")
    if second_value == 'q':
        break

    try:
        result = int(first_value) / int(second_value)
    except:
        print(f"impossibile by division {first_value} and {second_value}")
    else:
        print(result)

