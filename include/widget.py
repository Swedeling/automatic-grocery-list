from tkinter import *
import threading


class GroceryWidget:

    def __init__(self, menu_list):
        self.menu_list = menu_list
        self.window = Tk()

    def run(self):
        self.window.title('Grocery list app')
        
        # for scrolling vertically
        yscrollbar = Scrollbar(self.window)
        yscrollbar.pack(side = RIGHT, fill = Y)
        
        label = Label(self.window,
                    text = "Select the dishes :  ",
                    font = ("Calibri", 10), 
                    padx = 10, pady = 10)
        label.pack()
        self.list = Listbox(self.window, selectmode = "multiple", 
                    yscrollcommand = yscrollbar.set)
        
        # Widget expands horizontally and 
        # vertically by assigning both to
        # fill option
        self.list.pack(padx = 10, pady = 10,
                expand = YES, fill = "both")

        i = 0
        
        for each_item in self.menu_list:
            
            self.list.insert(END, self.menu_list[each_item].name)
            self.list.itemconfig(i, bg = "white")
            i += 1
        
        # Attach listbox to vertical scrollbar
        yscrollbar.config(command = self.list.yview)

        button = Button(self.window,text='Ready!',command=self._but_callback)
        button.pack(pady=20)

        self.window.mainloop()


    def _but_callback(self):
        self.next_week_menu = [self.list.get(idx) for idx in self.list.curselection()]
        print('[_but_callback] You choose: \n\t- ' + '\n\t- '.join(self.next_week_menu) + "\n")

        self.window.destroy()