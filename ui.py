# printing data, asking for user input


def print_menu(label, items):
    print(label)
    for number, item in enumerate(items):
        print(f"\t({number}) {item} ")


def print_items(label, items="empty"):
    print(label)
    if type(items) == list:
        for item in items:
            print(f"({item})")
    elif type(items) == str:
        print(f"({items})")


def get_input(label, items):
    print(label)
    if type(items) == list:
        user_inputs = []
        for item in items:
            user_inputs.append(input(f"{input}: "))
        return user_inputs
    elif type(items) == str:
        return input(f"{items}: ")
    else:
        raise ValueError("Invalid input call!")
