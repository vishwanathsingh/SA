#test.py
try:
    import tkinter as tk  # for python 3
except:
    import Tkinter as tk  # for python 2
import pygubu



class Row:
    def __init__(self, master):

        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        builder.add_from_file('order.ui')
       
        #3: Create the widget using a master as parent
        self.mainwindow = builder.get_object('OrderDetails', master)

        self.truck_num = self.get_object_from_mainwindow('truck_num')
        self.date = self.get_object_from_mainwindow('date')
        self.gc_num = self.get_object_from_mainwindow('gc_num')
        self.loading = self.get_object_from_mainwindow('e_loading')
        self.received = self.get_object_from_mainwindow('e_received')
        self.client = self.get_object_from_mainwindow('e_client')
        self.rate = self.get_object_from_mainwindow('e_rate')
        self.advance = self.get_object_from_mainwindow('e_advance')
        self.amount = self.get_object_from_mainwindow('e_amount')

        populate_defaults()
        builder.connect_callbacks(self)

    def get_object_from_mainwindow(self, object_id):
        return self.builder.get_object(object_id, self.mainwindow)

    def set_text(entry, text):
        entry.delete(0, tk.END)
        entry.insert(0, text)

    def on_submit_button_click(self):
        print ("submit button was clicked")

    def populate_defaults():
        pass
        
        

class Application:
    def __init__(self, master):
        self.builder = builder = pygubu.Builder()

        builder.add_from_file('example.ui')

        self.mainwindow = builder.get_object('mainwindow', master)
        builder.connect_callbacks(self)


    def on_add_order(self):
        print("hello")
        Row(self.mainwindow)


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()