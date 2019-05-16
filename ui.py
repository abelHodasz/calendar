# printing data, asking for user input


def print_menu(items, label):
    print(label)
    for number, item in enumerate(items):
        print(f"\t({number}) {item} ")


def get_input(items, label):
    print(label)
    if type(items) == list:
        user_inputs = []
        for item in items:
            user_inputs.append(input(f"{input}: "))
    elif type(items) == str:
        return input(f"{items}: ")
    else:
        raise ValueError("Invalid input call!")



