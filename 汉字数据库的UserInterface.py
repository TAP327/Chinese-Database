from tkinter import ttk
from tkinter import *
from 汉字数据库的事理 import Database
from random import *
from time import *

class Ui():
    def __init__(self) -> None:
        self._master = Tk()
        self._valueDict = {
            'entryCharacter': StringVar(value = ''),
            'entryPin1yin1': StringVar(value = ''),
            'entryPOSL': StringVar(value = ''),
            'entryEnglish': StringVar(value = ''),
            'langChoice': StringVar(value = 'En'),
            'deckCompletion': IntVar(value = 0),
            'deckLength': IntVar(value = 1),
            'pDeckCorrect1': IntVar(value = 0),
            'pDeckCorrect2': IntVar(value = 0),
            'pDeckCorrect3': IntVar(value = 0),
            'pDeckCorrect4': IntVar(value = 0),
            'tDeckCorrect1': IntVar(value = 0),
            'tDeckCorrect2': IntVar(value = 0),
            'tDeckCorrect3': IntVar(value = 0),
            'tDeckCorrect4': IntVar(value = 0),
            'currentQuestion': StringVar(value = ''),
            'pin1yin1Response': StringVar(value = ''),
            'translationResponse': StringVar (value = ''),
            'pin1yin1Answer': StringVar(value = ''),
            'translationAnswer': StringVar(value = ''),
            'answered': IntVar (value = 0),
            'roundNumber': IntVar (value = 1),
            'check': IntVar (value = 0)
        }
        self.ZH_DB = Database()
        self._createUiWindow()
        self._search_results = {}
        self._shuffledDeck = {}
        self._missedCards = {}

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
        练习的题目 = Frame(练习的框架,
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
        posl_label = Label(
            study_refiner,
            text = "POS or Lesson: ",
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
        posl_label.place(x = 7, y = 125)
        eng_label.place(x = 7, y = 175)
        choose_lang_label.place(x = 7, y = 225)
        
        #Add Study Refiner Entries
        char_账目 = Entry(study_refiner, textvariable = self._valueDict['entryCharacter'])
        pinyin_账目 = Entry(study_refiner, textvariable = self._valueDict['entryPin1yin1'])
        posl_账目 = Entry(study_refiner, textvariable = self._valueDict['entryPOSL'])
        eng_账目 = Entry(study_refiner, textvariable = self._valueDict['entryEnglish'])
        中文字 = Label(
            study_refiner,
            text = 'En',
            bg = 'light cyan'
        )
        英文字 = Label(
            study_refiner,
            text = 'Zh', 
            bg = 'light cyan',
        )
        中文的设定 = Radiobutton(
            study_refiner,
            bg = 'light cyan',
        )
        英文的设定 = Radiobutton(
            study_refiner,
            bg = 'light cyan'
        )

        char_账目.place(x = 3, y = 50)
        pinyin_账目.place(x = 3, y = 100)
        posl_账目.place(x = 3, y = 150)
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
        练习的按键.bind('<Button-1>', self._runQuiz)

        #Create Study Frame
        study_frame = Frame(
            练习的框架, height = 350,
            width = 450,
            padx = 2,
            bg = 'azure'
        )
        study_frame.place(x = 136,y = 50)

        #Add Study Elements
        question_label = Label(
            study_frame,
            textvariable = self._valueDict['currentQuestion'].get(),
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

        pinyin_answer_entry = Entry(study_frame, textvariable = self._valueDict['pin1yin1Response'])
        pinyin_answer_entry.place(x = 180, y = 90)

        translation_answer_entry = Entry(study_frame, textvariable = self._valueDict['translationResponse'])
        translation_answer_entry.place(x = 180, y = 200)

        pinyin_answer = Label(
            study_frame,
            textvariable = self._valueDict['pin1yin1Answer'].get(),
            bg = 'azure'
        )
        pinyin_answer.place(x = 180, y = 113)
        translation_answer = Label(
            study_frame,
            textvariable = self._valueDict['translationAnswer'].get(),
            bg = 'azure'
        )
        translation_answer.place(x =  180, y = 233)

        round1pinyin = Label(
            study_frame,
            textvariable = (
                str(self._valueDict['pDeckCorrect1'].get())
                + '/'
                + str(self._valueDict['deckCompletion'].get())
            ),
            bg = 'azure'
        )
        round1pinyin.place(x = 180, y = 146)
        round2pinyin = Label(
            study_frame,
            textvariable = (
                str(self._valueDict['pDeckCorrect2'].get())
                + '/' 
                + str(self._valueDict['deckCompletion'].get())
            ),
            bg = 'azure'
        )
        round2pinyin.place(x = 230, y = 146)

        round3pinyin = Label(
            study_frame,
            textvariable = (
                str(self._valueDict['pDeckCorrect3'].get())
                + '/' 
                + str(self._valueDict['deckCompletion'].get())
            ),
            bg = 'azure'
        )
        round3pinyin.place(x = 280, y = 146)
        
        round4pinyin = Label(
            study_frame,
            textvariable = (
                str(self._valueDict['pDeckCorrect4'].get())
                + '/' 
                + str(self._valueDict['deckCompletion'].get())
            ),
            bg = 'azure'
        )
        round4pinyin.place(x = 330, y = 146)

        round1translation = Label(
            study_frame,
            textvariable = (
                str(self._valueDict['tDeckCorrect1'].get())
                + '/' 
                + str(self._valueDict['deckCompletion'].get())
            ),
            bg = 'azure'
        )
        round1translation.place(x = 180, y = 266)

        round2translation = Label(
            study_frame,
            textvariable = (
                str(self._valueDict['tDeckCorrect2'].get())
                + '/' 
                + str(self._valueDict['deckCompletion'].get())
            ),
            bg = 'azure'
        )
        round2translation.place(x = 230, y = 266)

        round3translation = Label(
            study_frame,
            textvariable = (
                str(self._valueDict['tDeckCorrect3'].get())
                + '/' 
                + str(self._valueDict['deckCompletion'].get())
            ),
            bg = 'azure'
        )
        round3translation.place(x = 280, y = 266)
        
        round4translation = Label(
            study_frame,
            textvariable = (
                str(self._valueDict['tDeckCorrect4'].get())
                + '/'
                + str(self._valueDict['deckCompletion'].get())
            ),
            bg = 'azure'
        )
        round4translation.place(x = 330, y = 266)

        correct_check = Checkbutton(
            study_frame,
            bg = 'azure',
            variable = self._valueDict['check']
        )
        correct_check.place(x = 350, y = 200)
        if (
            self._valueDict['deckCompletion'] != ''
            and self._valueDict['deckLength'] != ''
        ):
            percent = str(
                self._valueDict['deckCompletion'].get()
                /self._valueDict['deckLength'].get()
            )
        else:
            percent = '--'
        percent_complete = Label(
            study_frame,
            textvariable = [percent + '% Complete'],
            bg = 'azure'
        )
        percent_complete.place(x = 280, y = 35)

        练习的框架.bind('<Return>', self._enterBind())
        练习的框架.bind('x', self._checkTheBox())

    def _runMainLoop(self) -> None:
        self._master.mainloop() 

    def _checkTheBox(self, event) -> None:
        self._valueDict['check'].set(1)
        
    def _enterBind(self) -> None:
        if self._valueDict['deckCompletion'].get() == self._valueDict['deckLength'].get():
            self._searchDatabaseUI()
        elif self._valueDict['answered'].get() == 0 and self._valueDict['langChoice'].get() == 'En':
            self._showAnswersEn()
        elif self._valueDict['answered'].get() == 0:
            self._showAnswersZh()
        else: 
            self._checkResponses()       

    def _searchDatabaseUI(self, event) -> None:
        search_values = {
            key: value.get() 
            for key, value in self._valueDict.items() if 
            key in ['entryCharacter', 'entryPin1yin1', 'entryPOSL', 'entryEnglish']
            and value.get() != ''
        }
        self._search_results = Database.search_database(search_values)
    
    def _showAnswersEn(self): #not finished
        if self._valueDict['pin1yin1Response'].get() == self._valueDict[self._shuffledDeck[self._valueDict['deckCompletion'].get()]]:
            self._valueDict['pDeckCorrect' + str(self._valueDict['roundNumber'])].set(self._valueDict['pDeckCorrect' + str(self._valueDict['roundNumber'])] + 1)
        else: 
            self._missedCards = self._missedCards + self._shuffledDeck[self._valueDict['deckCompletion']].get()
        self._valueDict['pin1yin1Answer'].set(self._shuffledDeck[self._valueDict['deckCompletion']].get('pin1yin1'))
        self._valueDict['translationAnswer'].set(self._shuffledDeck[self._valueDict['deckCompletion']].get('character'))

    def _showAnswersZh(self): #not finished
        if self._valueDict['pin1yin1Response'].get() == self._valueDict[self._shuffledDeck[self._valueDict['deckCompletion'].get()]]:
            self._valueDict['pDeckCorrect' + str(self._valueDict['roundNumber'])].set(self._valueDict['pDeckCorrect' + str(self._valueDict['roundNumber'])] + 1)
        else: 
            self._missedCards = self._missedCards + self._shuffledDeck[self._valueDict['deckCompletion']].get()
        self._valueDict['pin1yin1Answer'].set(self._shuffledDeck[self._valueDict['deckCompletion']].get('pin1yin1'))
        self._valueDict['translationAnswer'].set(self._shuffledDeck[self._valueDict['deckCompletion']].get('definition'))

    def _checkResponses(self) -> None: #maybe finished
        if self._valueDict['checked'].get() == 1:
            self._valueDict['tDeckCorrect' + str(self._valueDict['roundNumber'])].set(self._valueDict['tDeckCorrect' + str(self._valueDict['roundNumber'])] + 1)
        self._valueDict['answered'].set(0)
        self._valueDict['checked'].set(0)
    
    def _runQuiz(self, event): #not finished

        #reset values after previous quiz
        if self._valueDict['deckCompletion'].get() != 0:
            self._valueDict['deckCompletion'].set(0)
            self._valueDict['pDeckCorrect1'].set(0)
            self._valueDict['pDeckCorrect2'].set(0)
            self._valueDict['pDeckCorrect3'].set(0)
            self._valueDict['pDeckCorrect4'].set(0)
            self._valueDict['tDeckCorrect1'].set(0)
            self._valueDict['tDeckCorrect2'].set(0)
            self._valueDict['tDeckCorrect3'].set(0)
            self._valueDict['tDeckCorrect4'].set(0)
            self._valueDict['answered'].set(0)
            self._valueDict['roundNumber'].set(1)
        
        self._shuffledDeck = self._searchDatabaseUI().shuffle()
        self._valueDict['deckLength'].set(len(self._search_results()))
        if self._valueDict['langChoice'].get() == 'En':
            while self._valueDict['roundNumber'].get() < 5:
                while self._valueDict['deckCompletion'].get() <= self._valueDict['deckLength'].get():
                    self._valueDict['currectQuestion'].set(self._shuffledDeck[self._valueDict['deckCompletion'].get('definition')])
                    self._valueDict['answered'].set(1)
                    while self._valueDict['answered'].set(0):
                        time.sleep()
                    self._valueDict['deckCompletion'].set(self._valueDict['deckCompletion'].get() + 1)
                self._valueDict['roundNumber'].set(self._valueDict['roundNumber'].get() + 1)
        else:
            while self._valueDict['roundNumber'].get() < 5:
                while self._valueDict['deckCompletion'].get() <= self._valueDict['deckLength'].get():
                    self._valueDict['currectQuestion'].set(self._shuffledDeck[self._valueDict['deckCompletion'].get('character')])
                    self._valueDict['answered'].set(1)
                    while self._valueDict['answered'].set(0):
                        time.sleep()
                    self._valueDict['deckCompletion'].set(self._valueDict['deckCompletion'].get() + 1)
                self._valueDict['roundNumber'].set(self._valueDict['roundNumber'].get() + 1)
                  

'''''
self._valueDict = {
            'entryCharacter': StringVar(value = ''),
            'entryPin1yin1': StringVar(value = ''),
            'entryPOSL': StringVar(value = ''),
            'entryEnglish': StringVar(value = ''),
            'langChoice': StringVar(value = 'En'),
            'deckCompletion': IntVar(value = 0),
            'deckLength': IntVar(value = 1),
            'pDeckCorrect1': IntVar(value = 0),
            'pDeckCorrect2': IntVar(value = 0),
            'pDeckCorrect3': IntVar(value = 0),
            'pDeckCorrect4': IntVar(value = 0),
            'tDeckCorrect1': IntVar(value = 0),
            'tDeckCorrect2': IntVar(value = 0),
            'tDeckCorrect3': IntVar(value = 0),
            'tDeckCorrect4': IntVar(value = 0),
            'currentQuestion': StringVar(value = ''),
            'pin1yin1Response': StringVar(value = ''),
            'translationResponse': StringVar (value = ''),
            'answered': IntVar (value = 0),
            'roundNumber': IntVar (value = 1)
        }
'''''