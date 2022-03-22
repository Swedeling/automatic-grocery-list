class Dish:
    def __init__(self, name, ingrediens):
        self.name = name
        self.ingerdients = ingrediens


class MenuList:
    def __init__(self):
        self.menu = {}
        self.generate_menu_list()


    def generate_menu_list(self):

        # TODO Import this variables from csv file
        
        first_dish_name = 'salatka cezar'
        ingrediens = [['kurczak', 500, 'g'],['salata', 1, 'szt']]

        dish = Dish(first_dish_name, ingrediens)

        self.menu[first_dish_name] = dish



        first_dish_name = 'barszcz'
        ingrediens = [['kielbasa', 500, 'g'],['cebula', 1, 'szt']]

        dish = Dish(first_dish_name, ingrediens)

        self.menu[first_dish_name] = dish