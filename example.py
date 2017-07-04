#test.py
try:
    import tkinter as tk  # for python 3
except:
    import Tkinter as tk  # for python 2
import pygubu
from tkinter import messagebox

from Order import Order

class Row:
    def __init__(self, master):

        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        builder.add_from_file('order.ui')
       
        #3: Create the widget using a master as parent
        self.mainwindow = builder.get_object('OrderDetails', master)

        self.entries = {'truck_num': None, 'date': None, 'gc_num': None, 'e_loading': None, 'e_received': None, 'e_client': None, 'e_rate': None, 'e_advance': None, 'e_amount': None}
        self.get_objects_from_mainwindow()
        self.populate_defaults()

        builder.connect_callbacks(self)

    def get_objects_from_mainwindow(self):
        for item in self.entries.keys():
            self.entries[item] = self.builder.get_object(item, self.mainwindow)

    def set_text(entry, text):
        entry.delete(0, tk.END)
        entry.insert(0, text)

    def get_values(self):
        value_dict = {}
        for item, entry in self.entries.items():
            print (item, entry)
            value_dict[item] = entry.get()
        return value_dict

    def on_submit_button_click(self):
        print ("submit button was clicked")
        value_dict = self.get_values()
        Order.save(value_dict)

    def populate_defaults(self):
        Row.set_text(self.entries['truck_num'], "qwejwj88") #"Enter truck num"
        Row.set_text(self.entries['date'], "2/7/2017")#"Enter date")
        Row.set_text(self.entries['gc_num'], "gc89")#"Loading quantity in Tonnes")
        Row.set_text(self.entries['e_loading'], "12")#"Quanity Received")
        Row.set_text(self.entries['e_received'], "32")#"Client Id")
        Row.set_text(self.entries['e_client'], "11")#"Rate")
        Row.set_text(self.entries['e_rate'], "1")#"Advance Paid")
        Row.set_text(self.entries['e_advance'], "12")#"Total amount")
        Row.set_text(self.entries['e_amount'], "12")#"Total amount")
        

class Application():

    def __init__(self, master):

        #1: Create builder
        self.builder = builder = pygubu.Builder()

        #2: Load UI file
        builder.add_from_file('menu.ui')

        #3: Create the widget using self.master as parent
        self.mainwindow = builder.get_object('mainwindow', master)
  
        # Set main menu
        self.mainmenu = menu = builder.get_object('mainmenu', master)
        self.set_menu(menu)

        builder.connect_callbacks(self)


    def on_add_order(self):
        print("hello")
        Row(self.mainwindow)

    

class MyApplication(pygubu.TkApplication):

    def _create_ui(self):
        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        builder.add_from_file('menu.ui')

        #3: Create the widget using self.master as parent
        self.mainwindow = builder.get_object('mainwindow', self.master)

        # Set main menu
        self.mainmenu = menu = builder.get_object('mainmenu', self.master)
        self.set_menu(menu)

        # Configure callbacks
        builder.connect_callbacks(self)


    def on_mfile_item_clicked(self, itemid):
        if itemid == 'mfile_open':
            messagebox.showinfo('File', 'You clicked Open menuitem')
            Row(self.mainwindow)

        if itemid == 'mfile_quit':
            messagebox.showinfo('File', 'You clicked Quit menuitem. Byby')
            self.quit();


    def on_about_clicked(self):
        messagebox.showinfo('About', 'You clicked About menuitem')

    def on_add_order(self):
        print("hello")
        Row(self.mainwindow)


if __name__ == '__main__':
    root = tk.Tk()
    app = MyApplication(root)
    app.run()