def get_formatted_name(first, last, middle = ''):

    if middle:
        return f"{first} {middle} {last}".title()

    return f"{first} {last}".title()