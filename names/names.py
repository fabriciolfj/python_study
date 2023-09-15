from name_function import get_formatted_name

print("enter first name e last name, or q to exit")
while True:
    first = input("enter first name: ")

    if first == "q":
        break

    last = input("enter last name: ")

    if last == "q":
        break

    result = get_formatted_name(first, last)
    print(f"name completed {result}")