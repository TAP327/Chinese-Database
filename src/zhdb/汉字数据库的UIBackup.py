import tkinter as Tk
from tkinter import ttk
from tkinter import *
import zhdb.汉字数据库的事理 as database

class Ui():
    def __init__(self) -> None:
        self._master = Tk()
        self._createUiWindow()

    def _close(self):
        self._master.destroy()
           
    def _createUiWindow(self) -> None:    
        self._master.geometry('600x400')
        self._master.title('汉字数据库')

        #Create Tabs
        笔记本 = ttk.Notebook()
        笔记本.pack(fill = 'both', expand = 1)
        
        学习的框架 = ttk.Frame(笔记本, width = 600, height = 380)
        练习的框架 = ttk.Frame(笔记本, width = 600, height = 380)

        学习的框架.pack(fill = 'both', expand = 1)
        练习的框架.pack(fill = 'both', expand = 1)

        笔记本.add(学习的框架, text = '学习')
        笔记本.add(练习的框架, text = '练习')

        #Create Practice Title
        练习的题目 = Frame(
            练习的框架,
            height = 50,
            width = 600,
            bg = 'pale turquoise'
        )
        练习的题目.place(x = 0, y = 0)
        Label(
            练习的题目,
            text = "咱们练习中文吧! ",
            width = 20, 
            font = 15,
            bg = 'pale turquoise'
        ).place(x = 10, y = 10)

        #Create Study Refiner
        study_refiner = Frame(
            练习的框架,
            height = 350,
            width = 135,
            bg = 'light cyan',
            padx = 2
        )
        study_refiner.place(
            x = 0,
            y = 50
        )

        #Add Study Refining Labels
        char_label = Label(
            study_refiner,
            text = "Character: ",
            bg = "light cyan"
        )
        pinyin_label = Label(
            study_refiner,
            text = "Pin1Yin1: ",
            bg = "light cyan"
        )
        pos_label = Label(
            study_refiner,
            text = "Part of Speech: ",
            bg = "light cyan"
        )
        eng_label = Label(
            study_refiner,
            text = "English: ",
            bg = "light cyan"
        )
        choose_lang_label = Label(
            study_refiner,
            text = "设定: ",
            bg = "light cyan"

        )

        char_label.place(x = 7, y = 25)
        pinyin_label.place(x = 7, y = 75)
        pos_label.place(x = 7, y = 125)
        eng_label.place(x = 7, y = 175)
        choose_lang_label.place(x = 7, y = 225)
        
        #Add Study Refiner Entries
        char_账目 = Entry(study_refiner)
        pinyin_账目 = Entry(study_refiner)
        pos_账目 = Entry(study_refiner)
        eng_账目 = Entry(study_refiner)
        中文字 = Label(
            study_refiner,
            text = 'En',
            bg = 'light cyan'
        )
        英文字 = Label(
            study_refiner,
            text = 'Zh', 
            bg = 'light cyan',
            #activeforeground = 'dark cyan',
            #selectcolor = 'teal'
        )
        中文的设定 = Radiobutton(
            study_refiner,
            bg = 'light cyan',
            #activeforeground = 'dark cyan',
            #selectcolor = 'teal', 
            #IntVar = 0,
            #value = 1
        )
        英文的设定 = Radiobutton(
            study_refiner,
            bg = 'light cyan'
        )

        char_账目.place(x = 3, y = 50)
        pinyin_账目.place(x = 3, y = 100)
        pos_账目.place(x = 3, y = 150)
        eng_账目.place(x = 3, y = 200)
        中文字.place(x = 15, y = 250)
        英文字.place(x = 65, y = 250)
        中文的设定.place(x = 30, y = 250)
        英文的设定.place(x = 90, y = 250)
        
        #Add Study Button
        练习的按键 = Button(
            study_refiner, 
            text = "练习", 
            bg = 'azure'
        )
        练习的按键.place(x = 50, y = 275)

        #Create Study Frame
        study_frame = Frame(
            练习的框架,
            height = 350,
            width = 450,
            padx = 2,
            bg = 'azure'
        )
        study_frame.place(x = 136,y = 50)

        #Add Study Elements
        question_label = Label(
            study_frame,
            text = 'Sample',
            bg = 'azure',
        )
        question_label.place(x = 35, y= 35)

        pinyin_answer_label = Label(
            study_frame,
            text = 'Pin1yin1:  ',
            bg = 'azure'
        )
        pinyin_answer_label.place(x = 80, y = 80)

        translation_answer_label = Label(
            study_frame,
            text = 'Translation:  ',
            bg = 'azure'
        )
        translation_answer_label.place(x = 80, y = 200)

        pinyin_answer_entry = Entry(study_frame)
        pinyin_answer_entry.place(x = 180, y = 90)

        translation_answer_entry = Entry(study_frame)
        translation_answer_entry.place(x = 180, y = 200)

        pinyin_answer = Label(
            study_frame,
            text = 'pinyin sample answer',
            bg = 'azure'
        )
        pinyin_answer.place(x = 180, y = 113)
        translation_answer = Label(
            study_frame,
            text = 'translation sample answer',
            bg = 'azure'
        )
        translation_answer.place(x =  180, y = 233)

        round1pinyin = Label(
            study_frame,
            text = '#/#',
            bg = 'azure'
        )
        round1pinyin.place(x = 180, y = 146)
        round2pinyin = Label(
            study_frame,
            text = '#/#',
            bg = 'azure'
        )
        round2pinyin.place(x = 230, y = 146)

        round3pinyin = Label(
            study_frame,
            text = '#/#',
            bg = 'azure'
        )
        round3pinyin.place(x = 280, y = 146)
        
        round4pinyin = Label(
            study_frame,
            text = '#/#',
            bg = 'azure'
        )
        round4pinyin.place(x = 330, y = 146)

        round1translation = Label(
            study_frame,
            text = '#/#',
            bg = 'azure'
        )
        round1translation.place(x = 180, y = 266)

        round2translation = Label(
            study_frame,
            text = '#/#',
            bg = 'azure'
        )
        round2translation.place(x = 230, y = 266)

        round3translation = Label(
            study_frame,
            text = '#/#',
            bg = 'azure'
        )
        round3translation.place(x = 280, y = 266)
        
        round4translation = Label(
            study_frame,
            text = '#/#',
            bg = 'azure'
        )
        round4translation.place(x = 330, y = 266)

        correct_check = Checkbutton(
            study_frame,
            bg = 'azure'
        )
        correct_check.place(x = 350, y = 200)
        #if self._valueDict['deckCompletion'].get() != '' and self._valueDict['deckLength'].get() != '':
        #    percent = str(int(self._valueDict['deckCompletion'].get())/int(self._valueDict['deckLength'].get()))
        #else:
        #    percent = '--'
        percent_complete = Label(
            study_frame,
            text = '#% Complete',
            bg = 'azure'
        )
        percent_complete.place(x = 280, y = 35)
        

    def runMainLoop(self) -> None:
        self._master.mainloop()

        

    #def searchDatabase(self, event) -> None:
    
