import tkinter as Tk
from tkinter import *
import 汉字数据库的事理 as database

class Ui():
    def __init__(self) -> None:
        self._master = Tk()

    def _close(self):
        self._master.destroy()
           
    def _createUiWindow(self) -> None:    
        self._master.geometry('600x400')
        self._master.tite('汉字数据库')
        self._createUiWindow()

    def runMainLoop(self) -> None:
        self._master.mainloop()
    
Ui()

'''''
studyrefiner = Frame(root, height = 400, width = 200, bg = 'Light Gray')
studyrefiner.pack(side = LEFT)
studyrefinerheader = Label(root, text = 'Study by:  ', font = '50')
studyrefinerheader.pack(fill = 'both', expand =  1)
study = Frame(root, height = 400, width = 400)
study.pack(side = RIGHT)


root.mainloop()

'''''











'''''
#tabfont = font.Font(family = "Helvetica", size = 74, weight = 'bold')
#Tabs
tab = ttk.Notebook(root, height = 400, width = 600)
tab.pack(expand=1, fill='both')
学习 = ttk.Frame(tab, width = 600, height = 380)
练习 = ttk.Frame(tab, width = 600, height = 380)
学习.pack(fill='both', expand = 1)
练习.pack(fill='both', expand = 1)
tab.add(学习, text='学习')
tab.add(练习, text='练习')
Learninglabel = Label(学习, text = "Let's learn!").grid(column=0, row=0, padx=30, pady=30)

style = Style()
style.theme_use('default')
style.configure('TNotebook.Tab', background = 'gray')
style.map("TNotebook", background = [("selected",  "gray")])

refinestudyframe = Label(练习, text = 'Sort by:  \n ', bg = 'blue', height= 5, width = 10)
refinestudyframe.grid(columnspan =  30)
'''''

'''
refinestudyframe = Frame(root)
tab.add(refinestudyframe, text = 'study!')
refinestudyframe.pack(side = LEFT)
lesson = Button(refinestudyframe, text = 'Lesson')
lesson.pack(side = TOP)
'''