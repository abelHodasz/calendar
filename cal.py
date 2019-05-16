# main program
import ui
import common
import storage


def choose(menu_number, menu):
    menu_item = {item: number for number, item in enumerate(menu)}
    while True:
        ui.print_menu("Menu:", menu)
        try:
            choice = int(ui.get_input("", "Your choice: "))
            if choice == menu_item["Quit"]:
                pass
            elif choice == menu_item["Schedule a new meeting"]:
                pass
            elif choice == menu_item["Cancel a meeting"]:
                pass
            else:
                raise ValueError
        except ValueError:
            ui.print_error()


def main():
    menu = ["Quit", "Schedule a new meeting", "Cancel a meeting"]
    while True:
        ui.print_items()
        try:
            choose(int(ui.get_input("", "Menu number:")), menu)
        except ValueError:
            ui.print_error()
            continue
                   

if __name__ == "__main__":
    main()