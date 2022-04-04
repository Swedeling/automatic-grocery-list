import pandas as pd

class Dish:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients


class MenuList:
    def __init__(self):
        self.menu = {}
        self.n = 0
        self.generate_menu_list()


    def generate_menu_list(self):        
        cookbook_df = pd.read_csv ('csv_files\cookbook.csv', sep =';', header = None, encoding = 'iso-8859-2')
        header = next(cookbook_df.iterrows())[1]

        for dishname in header:
            if dishname == dishname:
                ingredients = {}

                for i in range(2, len(cookbook_df[self.n])):
                    cell = cookbook_df[self.n][i] 
                    if cell == cell:
                        ingredients[cell] = [cookbook_df[self.n+1][i], cookbook_df[self.n+2][i]]
            

                dish = Dish(dishname, ingredients)

                self.menu[dishname] = dish

                self.n += 3


