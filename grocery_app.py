#!/usr/bin/env python3

from include.widget import GroceryWidget
from include.csv_to_menu import MenuList


def main():
    menu_generator = MenuList() 
    widget = GroceryWidget(menu_generator.menu)
    grocery_list = {}
    items = list()

    widget.run()

    for each_item in widget.next_week_menu:
        for key in menu_generator.menu[each_item].ingredients.keys():
            if key in grocery_list.keys():
                if menu_generator.menu[each_item].ingredients[key][1] in grocery_list[key][1]:
                    menu_generator.menu[each_item].ingredients[key] = [str(int(grocery_list[key][0]) + int(menu_generator.menu[each_item].ingredients[key][0])), grocery_list[key][1]]
                else:
                    temp = [grocery_list[key]]
                    temp.append(menu_generator.menu[each_item].ingredients[key])
                    menu_generator.menu[each_item].ingredients[key] = temp
        grocery_list.update(menu_generator.menu[each_item].ingredients)


    with open('grocery-list.txt', 'w', encoding = 'utf-8') as f:
        for ingredient in grocery_list.keys():
            items.append(ingredient + ' ' + ' '.join(grocery_list[ingredient]))
        
        f.write('\n'.join(items))
        f.close()

    print(grocery_list)

if __name__ == '__main__':
    main()
