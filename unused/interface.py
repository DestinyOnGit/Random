import tkinter as tk
from tkinter import ttk
import ai
from ai import run
from ai import train
from ai import model
from ai import characters
from ai import combined_path
import unused.commandrun as commandrun
import os as filesys
print(combined_path)
version_number = 'V-3.2.7-[cpufire]' #change this for every update. goes like:
#Major update, previous API incompatible | Moderate | Patch/Hotfix
print("App running")
print("App version:", version_number)
print("Initializing")
#all code goes below here
combined_ver_num = ('BR AGENT', version_number)
bg = 'white'
class App():
    def __init__(self):
        print('Initialization complete! Have fun. :)')
        self.root = tk.Tk()
        self.root.geometry('660x360+330+190')
        self.root.title('Brick-Rigs AI Agent')
        self.mainframe = tk.Frame(self.root, background=bg)
        self.mainframe.pack(fill='both', expand='true')

        #Variables that may be used later
        self.selected = 'data'
        self.stext = ''
        self.stext1 = ''
        self.stext2 = ''

        #Main title label
        self.maintitle = ttk.Label(self.mainframe, text=combined_ver_num , font='Brass', background=bg)
        self.maintitle.grid(row=0, column=0, padx=130)

        #Enter prompt
        self.entpromtext = ttk.Label(self.mainframe, text='Enter prompt:', background=bg, font='Brass')
        self.entpromtext.grid(row=1, column=0, padx=0)

        self.entprom = ttk.Entry(self.mainframe, background=bg)
        self.entprom.grid(row=2, column=0, padx=0)
        self.entprom.insert(0, 'hi')

        self.prombutton = ttk.Button(self.mainframe, text='Submit', command=self.gpromp)
        self.prombutton.grid(row=3, column=0, padx=0)

        self.promconf = ttk.Label(self.mainframe, text='You entered:', font='Brass', background=bg)
        self.promconf.grid(row=4, column=0, padx=0)
        self.promconf2 = ttk.Label(self.mainframe, text='', font='Brass', background=bg)
        self.promconf2.grid(row=5, column=0, padx=0)

        #Submit prompt
        self.lengthof = ttk.Entry(self.mainframe, background=bg)
        self.lengthof.grid(row=6, column=0, padx=0)
        self.lengthof.insert(0, '1')
        self.rusure = ttk.Button(self.mainframe, text='Prompt', command=self.dothething)
        self.rusure.grid(row=7, column=0, padx=0)

        self.intonly = ttk.Label(self.mainframe, text='Integers only ^^^', background=bg, font='Brass')
        self.intonly.grid(row=8, column=0, padx=0)

        #Result. :D
        self.promresulttext = ttk.Label(self.mainframe, text='Prediction:', background=bg, font='Brass')
        self.promresulttext.grid(row=12, column=0, padx=0)
        self.promresult = ttk.Label(self.mainframe, text='', background=bg, font='Brass')
        self.promresult.grid(row=13, column=0, padx=0)

        #Model saving functionality
        self.savemodel = ttk.Button(self.mainframe, text='Save model', command=self.save)
        self.savemodel.grid(row=10, column=0, padx=0)
        
        self.clearmodel = ttk.Button(self.mainframe, text='Clear model', command=self.clear)
        self.clearmodel.grid(row=11, column=0, padx=0)

        
        #Training
        self.enttraintext = ttk.Label(self.mainframe, text='Training data:', font='Brass', background=bg)
        self.enttraintext.grid(row=0, column=1, padx=0)

        self.enttrain = ttk.Entry(self.mainframe, background=bg)
        self.enttrain.grid(row=1, column=1, padx=0)

        self.trainsub = ttk.Button(self.mainframe, text='Submit', command=self.subpt)
        self.trainsub.grid(row=2, column=1, padx=0)

        self.enteredt = ttk.Label(self.mainframe, text='You entered:', font='Brass', background=bg)
        self.enteredt.grid(row=3, column=1, padx=0)
        self.enteredt2 = ttk.Label(self.mainframe, text='', font='Brass', background=bg)
        self.enteredt2.grid(row=4, column=1, padx=0)

        self.traintext = ttk.Label(self.mainframe, text='Select vvv', font='Brass', background=bg)
        self.traintext.grid(row=5, column=1, padx=0)
        self.traintext2 = ttk.Label(self.mainframe, text='Act vvv', font='Brass', background=bg)
        self.traintext2.grid(row=9, column=1, padx=0)
        self.epochs = ttk.Entry(self.mainframe, background=bg)
        self.epochs.grid(row=10, column=1, padx=0)
        self.epochs.insert(0, '10')

        self.train1 = ttk.Button(self.mainframe, text='Train with training data', command=self.train1c)
        self.train2 = ttk.Button(self.mainframe, text='Train with prompt', command=self.train2c)
        self.train3 = ttk.Button(self.mainframe, text='Train with both', command=self.train3c)
        self.train4 = ttk.Button(self.mainframe, text='Train', command=self.strain1)
        self.train5 = ttk.Button(self.mainframe, text='Train and prompt', command=self.strain2)
        self.train1.grid(row=6, column=1, padx=0)
        self.train2.grid(row=7, column=1, padx=0)
        self.train3.grid(row=8, column=1, padx=0)
        self.train4.grid(row=11, column=1, padx=0)
        self.train5.grid(row=12, column=1, padx=0)

        self.root.mainloop()
        return
    
    def gpromp(self):
        prom = self.entprom.get()
        self.promconf2.config(text=prom)
        print('Entered:', prom)

    def dothething(self):
        print("Doing the thing...")
        length_inchar = self.lengthof.get()
        length_inchar = int(length_inchar)
        result_string = ''
        promfr = self.entprom.get()
        counter = length_inchar
        eras = self.epochs.get()
        eras = int(eras)
        print(eras)
        print('Entered:', promfr)
        while counter > 0:
            train(promfr, characters, eras)
            counter -= 1
            result = run(promfr, characters)
            result_string = result_string + result
            print(result_string)
            self.promresult.config(text=result_string)
    
    def save(self):
        model.save(combined_path, True)
    
    def clear(self):
        print('WARNING: YOU ARE ABOUT TO CLEAR THE MODEL. ARE YOU SURE?')
        print('ENTER Y OR N, FOR YES OR NO.')
        while True:
            inp = input()
            inpup = inp.upper()
            if inpup == 'Y':
                try:
                    filesys.remove(combined_path)
                    print('MODEL REMOVED.')
                    break
                except FileNotFoundError:
                    print("You silly goof! You don't have a model!")
                    break
            elif inpup == 'N':
                print('Model deletion cancelled. You may now rest easy.')
                break
            else:
                print('INVALID.')
    

    def subpt(self):
        info = self.enttrain.get()
        print('Entered:', info)
        self.enteredt2.config(text=info)

    def train1c(self):
        self.selected = 'data'
        print('Selected', self.selected)

    def train2c(self):
        self.selected = 'prompt'
        print('Selected', self.selected)

    def train3c(self):
        self.selected = 'both'
        print('Selected', self.selected)

    def strain1(self):
        eras = self.epochs.get()
        eras = int(eras)
        print(eras)
        if self.selected == 'data':
            print('Selected: Training Data')
            self.stext = self.enttrain.get()
            print(self.stext)
            train(self.stext, characters, eras)
        elif self.selected == 'prompt':
            print('Selected: Prompt')
            self.stext = self.entprom.get()
            train(self.stext, characters, eras)
        elif self.selected == 'both':
            print('Selected: Both')
            self.stext1 = self.entprom.get()
            self.stext2 = self.enttrain.get()
            self.stext = self.stext1 + self.stext2
            train(self.stext, characters, eras)
        else:
            print("Whoops! Unexpected error. We're sorry.")

    def strain2(self):
        eras = self.epochs.get()
        eras = int(eras)
        print(eras)
        if self.selected == 'data':
            print('Selected: Training Data')
            self.stext = self.enttrain.get()
            print(self.stext)
            train(self.stext, characters, eras)
            self.dothething()
        elif self.selected == 'prompt':
            print('Selected: Prompt')
            self.stext = self.entprom.get()
            train(self.stext, characters, eras)
            self.dothething()
        elif self.selected == 'both':
            print('Selected: Both')
            self.stext1 = self.entprom.get()
            self.stext2 = self.enttrain.get()
            self.stext = self.stext1 + self.stext2
            train(self.stext, characters, eras)
            self.dothething()
        else:
            print("Whoops! Unexpected error. We're sorry.")

    def reward(self):
        print('Agent has been rewarded! 🎉✨')

    def punish(self):
        print('Agent has been punished.. 😥')

if __name__ == '__main__':
    App()
