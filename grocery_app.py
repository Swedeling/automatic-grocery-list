#!/usr/bin/env python3

from include.widget import GroceryWidget
from include.csv_to_menu import MenuList


def main():
    menu_generator = MenuList() 
    widget = GroceryWidget(menu_generator.menu)

    widget.run()

    print(f"[main] In this week: \n\t {widget.next_week_menu}")

    for each_item in menu_generator.menu:
        print(f"\nFor {menu_generator.menu[each_item].name} you need: \n")
        print(menu_generator.menu[each_item].ingerdients)


if __name__ == '__main__':
    main()
