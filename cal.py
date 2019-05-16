# main program
import ui
import common
import storage


def choose(menu_number, menu):
    pass


def main():
    menu = ["Quit", "Schedule a new meeting", "Cancel a meeting"]
    while True:
        ui.print_items()
        try:
            choose(int(ui.get_input("","Menu number:")), menu)
        except ValueError:
            ui.print_error("Invalid input, try again!")
            continue
                   

if __name__="__main__":
    main()