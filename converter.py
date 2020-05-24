#converter_3.py
#barebone example of a converter

from tkinter import Tk, Entry, Label, Button, StringVar
from tkinter.ttk import Combobox
from tkinter.font import Font
from itertools import permutations

class App():
    """ GUI """
    def __init__(self, root):
        self.master = root
        self.master.configure(bg="grey80")
        self.font1 = Font(family="Helvetica",size=20,weight="bold")
        self.font2 = Font(family="Helvetica",size=24,weight="bold")
        self.ls_from = ["Hexadecimal", "Binary", "Decimal"]
        self.str_var = StringVar()
        self.init_widg()
        
    def init_widg(self):
        self.lab_from = Label(self.master, text="from", font=self.font1)
        self.lab_from.grid(row=0, column=0, sticky="W")
        
        self.lab_to = Label(self.master, text="to", font=self.font1)
        self.lab_to.grid(row=0, column=1, sticky="W")
        
        self.com_from = Combobox(self.master, values=self.ls_from, 
                                font=self.font1, state="readonly")
        self.com_from.grid(row=1, column=0, sticky="W")
        self.com_from.current(0)
        self.com_from.bind("<<ComboboxSelected>>", self.callback)
        
        self.com_to = Combobox(self.master, values=self.ls_from, 
                                font=self.font1,  state="readonly")
        self.com_to.grid(row=1, column=1, sticky="W")
        self.com_to.current(2)
        
        self.lab_from_to = Label(self.master, text="Enter {} number:".format(self.com_from.get()), 
                                font=self.font1)
        self.lab_from_to.grid(row=2, column=0, sticky="W", pady=5)
        
        self.ent_val  = Entry(self.master, font=self.font2)
        self.ent_val.grid(row=3, column=0, sticky="W")
        
        self.but_convert = Button(self.master, text="Convert", 
                                font=self.font1, bg="blue", fg="white",
                                command=self.convert_value)
        self.but_convert.grid(row=4, column=0, sticky="W")
        self.lab_output = Label(self.master, text="Output:", font=self.font1)
        self.lab_output.grid(row=5, column=0, sticky="W", pady=5)
        
        self.ent_output = Entry(self.master, font=self.font1, textvariable=self.str_var)
        self.ent_output.grid(row=6, column=0, sticky="W")
#-------------------------------------------------------------------------------        
    def callback(self, event):
        """ callback set choice in Label <<lab_from_to>> """
        x = self.com_from.get() #which type ex. Hexadecimal - x is a tmp var
        self.lab_from_to.configure(text="Enter {} number:".format(x))
    
    def convert_value(self):
        in_v = self.ent_val.get()
        from_type = self.com_from.get()  #which type ex. Hexadecimal 
        to_type = self.com_to.get()      #which type ex. Decimal 
        print("Choice--\t From: {}\t To: {}".format(from_type, to_type))
       
        #call Converter method
        result = Converter.convert_value(in_v, from_type, to_type)
        # self.ent_output.insert(END, result)   #if you do this instead of useing StringVar then you have to delete before insert new values
        self.str_var.set(result)    #don't have to track variable by yourself set() will do that for you
        
        
class Converter():
    """ The logic behind application """
        
    input_value = None
    mapping = dict(zip(permutations(('Hexadecimal', 'Decimal', 'Binary'), r=2), (1, 2, 4, 6, 3, 5)))
    print(mapping)
    
    def convert_value(input_value, from_which_type, to_which_type):
        Converter.input_value = input_value
        ret_choice = Converter.convert_what(from_which_type, to_which_type)
        print("ret_choice = ", ret_choice)
        func_to_call = Converter.choices(ret_choice)    #which function to call
        print("func_to_call = ", func_to_call)
        return func_to_call()
        
    def convert_what(numeral_sys_1, numeral_sys_2):
    
        return Converter.mapping.get((numeral_sys_1, numeral_sys_2), 0)
                
    #-------------------------------------------------------------------------  
    #converting functions
    def nothing():
        print("nothing") 
        return None
    def hex_to_dec():
        print("hex_to_dec")
        # tmp_dec = eval(Converter.input_value)
        tmp_dec = int(Converter.input_value, 16)
        return tmp_dec
    def hex_to_bin():
        print("hex_to_bin")
        # tmp_dec = eval(Converter.input_value)   #eval() converts also str to int
        tmp_dec = int(Converter.input_value, 16)
        tmp_bin = bin(tmp_dec)
        return tmp_bin[2:]
    def bin_to_dec():
        print("bin_to_dec")
        tmp_dec = int(Converter.input_value, 2)
        return tmp_dec        
    def dec_to_hex():
        print("dec_to_hex")
        tmp_hex = hex(int(Converter.input_value))
        return tmp_hex
    def bin_to_hex():
        print("bin_to_hex")
        tmp_dec = int(Converter.input_value, 2)
        tmp_hex = hex(tmp_dec)
        return tmp_hex
    def dec_to_bin():
        print("dec_to_bin")
        tmp_bin = bin(int(Converter.input_value))
        return tmp_bin[2:]
    #------------------------------------------------------------------------- 
    
    def choices(argument):
        switcher = {
            0: Converter.nothing,
            1: Converter.hex_to_dec,
            2: Converter.hex_to_bin,
            3: Converter.bin_to_hex,
            4: Converter.dec_to_hex,
            5: Converter.bin_to_dec,
            6: Converter.dec_to_bin
        }
        # Get the function from switcher dictionary
        func = switcher.get(argument, lambda: "Invalid values")
        # return the function
        return func

if __name__ == "__main__":
    root = Tk()
    root.title("Converter")
    app = App(root)
    root.mainloop()
    
    
    
    