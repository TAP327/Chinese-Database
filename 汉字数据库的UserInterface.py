from tkinter import ttk
from tkinter import (
    Tk,
    Frame,
    StringVar,
    IntVar,
    Label,
    Entry,
    Radiobutton,
    Button,
    Checkbutton,
)
from 汉字数据库的事理 import Database
import random
import time

class Ui():
    def __init__(self) -> None:
        self._master = Tk()
        self._笔记本 = ttk.Notebook(self._master)
        self._valueDict = {
            'entryCharacter': StringVar(value = ''),
            'entryPin1yin1': StringVar(value = ''),
            'entryPOSL': StringVar(value = ''),
            'entryEnglish': StringVar(value = ''),
            'langChoice': StringVar(value = 'En'),
            'deckCompletion': IntVar(value = 1),
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
            'responseState': StringVar(value = 'normal'),
            'pin1yin1CorrectAnswer': StringVar(value = ''),
            'translationCorrectAnswerEn': StringVar(value = ''),
            'translationCorrectAnswerZh': StringVar(value = ''),
            'roundNumber': IntVar (value = 6),
            'check': IntVar (value = 0)
        }
        self._studyStatsDict = {
            'round1pinyin': StringVar(value = f"{self._valueDict['pDeckCorrect1'].get()}/{self._valueDict['deckCompletion'].get()}"),
            'round2pinyin': StringVar(value = f"{self._valueDict['pDeckCorrect2'].get()}/{self._valueDict['deckCompletion'].get()}"),
            'round3pinyin': StringVar(value = f"{self._valueDict['pDeckCorrect3'].get()}/{self._valueDict['deckCompletion'].get()}"),
            'round4pinyin': StringVar(value = f"{self._valueDict['pDeckCorrect4'].get()}/{self._valueDict['deckCompletion'].get()}"),
            'round1translation': StringVar(value = f"{self._valueDict['tDeckCorrect1'].get()}/{self._valueDict['deckCompletion'].get()}"),
            'round2translation': StringVar(value = f"{self._valueDict['tDeckCorrect2'].get()}/{self._valueDict['deckCompletion'].get()}"),
            'round3translation': StringVar(value = f"{self._valueDict['tDeckCorrect3'].get()}/{self._valueDict['deckCompletion'].get()}"),
            'round4translation': StringVar(value = f"{self._valueDict['tDeckCorrect4'].get()}/{self._valueDict['deckCompletion'].get()}"),
            'percentComplete': StringVar(value = f"--")
        }
        self._ZH_DB = Database()
        self._search_results = {}
        self._shuffledDeck = []
        self._missedCards = []
        self._answered = False

        self._createUiWindow()

    def _close(self):
        self._master.destroy()

    def _createUIDictFrame(self) -> None:
        学习的框架 = ttk.Frame(self._笔记本, width = 600, height = 380)
        学习的框架.pack(fill = 'both', expand = 1)
        self._笔记本.add(学习的框架, text = '学习')

    def _createUISFPracticeTitle(self, 练习的框架) -> None:
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

    def _createUISFStudyRefiner(self, 练习的框架) -> None:
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

    def _createUISFStudyStats(self, study_frame) -> None:
        round1pinyin = Label(
            study_frame,
            textvariable = self._studyStatsDict['round1pinyin'],
            bg = 'azure'
        )
        round1pinyin.place(x = 180, y = 120)
        round2pinyin = Label(
            study_frame,
            textvariable = self._studyStatsDict['round2pinyin'],
            bg = 'azure'
        )
        round2pinyin.place(x = 230, y = 120)

        round3pinyin = Label(
            study_frame,
            textvariable = self._studyStatsDict['round3pinyin'],
            bg = 'azure'
        )
        round3pinyin.place(x = 280, y = 120)

        round4pinyin = Label(
            study_frame,
            textvariable = self._studyStatsDict['round4pinyin'],
            bg = 'azure'
        )
        round4pinyin.place(x = 330, y = 120)

        round1translation = Label(
            study_frame,
            textvariable = self._studyStatsDict['round1translation'],
            bg = 'azure'
        )
        round1translation.place(x = 180, y = 235)

        round2translation = Label(
            study_frame,
            textvariable = self._studyStatsDict['round2translation'],
            bg = 'azure'
        )
        round2translation.place(x = 230, y = 235)

        round3translation = Label(
            study_frame,
            textvariable = self._studyStatsDict['round3translation'],
            bg = 'azure'
        )
        round3translation.place(x = 280, y = 235)
        
        round4translation = Label(
            study_frame,
            textvariable = self._studyStatsDict['round4translation'],
            bg = 'azure'
        )
        round4translation.place(x = 330, y = 235)

    def _createUISFStudyFrame(self, 练习的框架) -> None:
        study_frame = Frame(
            练习的框架, height = 350,
            width = 450,
            padx = 2,
            bg = 'azure'
        )
        study_frame.place(x = 136,y = 50)

        question_label = Label(
            study_frame,
            textvariable = self._valueDict['currentQuestion'],
            bg = 'azure',
        )
        question_label.place(x = 35, y= 35)

        pinyin_entry_label = Label(
            study_frame,
            text = 'Pin1yin1:  ',
            bg = 'azure'
        )
        pinyin_entry_label.place(x = 80, y = 80)

        pinyin_correct_answer_label = Label(
            study_frame,
            textvariable = self._valueDict['pin1yin1CorrectAnswer'],
            bg = 'azure'
        )
        pinyin_correct_answer_label.place(x = 180, y = 143)

        translation_entry_label = Label(
            study_frame,
            text = 'Translation:  ',
            bg = 'azure'
        )
        translation_entry_label.place(x = 80, y = 200)

        translation_correct_answer_label_en = Label(
            study_frame,
            textvariable = self._valueDict['translationCorrectAnswerEn'],
            bg = 'azure',
            font = 16
        )
        translation_correct_answer_label_en.place(x = 180, y = 257)

        translation_correct_answer_label_zh = Label(
            study_frame,
            textvariable = self._valueDict['translationCorrectAnswerZh'],
            bg = 'azure'
        )
        translation_correct_answer_label_zh.place(x = 180, y = 257)


        pinyin_answer_entry = Entry(study_frame, textvariable = self._valueDict['pin1yin1Response'], state = 'normal')
        pinyin_answer_entry.place(x = 180, y = 90)

        translation_answer_entry = Entry(study_frame, textvariable = self._valueDict['translationResponse'], state = self._valueDict['responseState'].get())
        translation_answer_entry.place(x = 180, y = 200)

        self._createUISFStudyStats(study_frame)

        correct_check = Checkbutton(
            study_frame,
            command = self._updateCompletion,
            bg = 'azure',
            variable = self._valueDict['check']
        )
        correct_check.place(x = 350, y = 200)

        percent_complete = Label(
            study_frame,
            textvariable = self._studyStatsDict['percentComplete'],
            bg = 'azure'
        )
        percent_complete.place(x = 280, y = 35)

    def _createUIStudyFrame(self) -> None:
        练习的框架 = ttk.Frame(self._笔记本, width = 600, height = 380)
        练习的框架.pack(fill = 'both', expand = 1)
        self._笔记本.add(练习的框架, text = '练习')

        self._createUISFPracticeTitle(练习的框架)
        self._createUISFStudyRefiner(练习的框架)
        self._createUISFStudyFrame(练习的框架)

    def _createUiWindow(self) -> None:
        self._master.geometry('600x400')
        self._master.title('汉字数据库')
        self._master.maxsize(600, 400)
        self._master.minsize(600, 400)

        # Create Tabs
        self._笔记本.pack(fill = 'both', expand = 1)

        self._createUIDictFrame()
        self._createUIStudyFrame()

        self._master.bind('<Return>', self._enterBind)
        self._master.bind('x', self._checkTheBox)

    def runMainLoop(self) -> None:
        self._master.mainloop()

    def _checkTheBox(self, event) -> None:
        if self._answered == True:
            if self._valueDict['check'].get() == 0:
                self._valueDict['check'].set(1)
            else:
                self._valueDict['check'].set(0)

    def _searchDatabaseUI(self) -> None:
        '''
            for key, value in self._valueDict.items():
                if key in [
                    'entryCharacter',
                    'entryPin1yin1',
                    'entryPOSL',
                    'entryEnglish'
                ] and value.get() != '':
                    search_values.update({key: value.get()})
        '''
        search_values = {
            key: value.get()
            for key, value in self._valueDict.items() if
            key in ['entryCharacter', 'entryPin1yin1', 'entryPOSL', 'entryEnglish']
            and value.get() != ''
        }
        self._search_results = self._ZH_DB.search_database_DB(search_values)

    def _showAnswersEn(self) -> None:  # not finished
        self._valueDict['pin1yin1CorrectAnswer'].set(self._shuffledDeck[self._valueDict['deckCompletion'].get()-1].get('pin1yin1'))
        self._valueDict['translationCorrectAnswerZh'].set('')
        self._valueDict['translationCorrectAnswerEn'].set(self._shuffledDeck[self._valueDict['deckCompletion'].get()-1].get('character'))

    def _showAnswersZh(self) -> None:  # not finished
        self._valueDict['pin1yin1CorrectAnswer'].set(self._shuffledDeck[self._valueDict['deckCompletion'].get()-1].get('pin1yin1'))
        self._valueDict['translationCorrectAnswerEn'].set('')
        self._valueDict['translationCorrectAnswerZh'].set(self._shuffledDeck[self._valueDict['deckCompletion'].get()-1].get('definition'))

    def _checkTransResponses(self) -> None:  # maybe finished
        if self._valueDict['check'].get() == 1:
            tDeckCorrectNum = 'tDeckCorrect' + str(self._valueDict['roundNumber'].get())
            self._valueDict[tDeckCorrectNum].set(self._valueDict[tDeckCorrectNum].get()+1)
            self._valueDict['check'].set(0)
        self._answered = False

    def _runQuiz(self, event):  # not finished
        # reset values after previous quiz
        self._valueDict['deckLength'].set(1)
        self._valueDict['deckCompletion'].set(1)
        self._valueDict['pDeckCorrect1'].set(0)
        self._valueDict['pDeckCorrect2'].set(0)
        self._valueDict['pDeckCorrect3'].set(0)
        self._valueDict['pDeckCorrect4'].set(0)
        self._valueDict['tDeckCorrect1'].set(0)
        self._valueDict['tDeckCorrect2'].set(0)
        self._valueDict['tDeckCorrect3'].set(0)
        self._valueDict['tDeckCorrect4'].set(0)
        self._valueDict['roundNumber'].set(1)
        self._valueDict['currentQuestion'].set('')
        self._answered = False

        self._searchDatabaseUI()
        '''
        tmp_list = []
        for result in self._search_results.values():
            tmp_list.append(result)
        '''
        self._shuffledDeck = [result for result in self._search_results.values()]
        random.shuffle(self._shuffledDeck)
        self._valueDict['deckLength'].set(len(self._search_results))
        self._updateCompletion()
        if self._valueDict['langChoice'].get() == 'En':
            self._runQuizEn()
        else:
            self._runQuizZh()

    def _runQuizEn(self):
        newQuestionSlice = self._valueDict['deckCompletion'].get() - 1 #Type int
        newQuestion = self._shuffledDeck[newQuestionSlice] #Type dict
        newQuestionDef = newQuestion.get('definition')
        self._valueDict['currentQuestion'].set(newQuestionDef)
        self._answered == False
        if self._answered == False:
            self._master.after(100, self._runQuizEn)  # Schedule the function in the Tkinter main loop
        else:
            self._master.after(100, self._runQuizEn)  # Schedule the function in the Tkinter main loop

    def _runQuizZh(self):
        if self._valueDict['roundNumber'].get() < 5:
            if self._valueDict['deckCompletion'].get() < self._valueDict['deckLength'].get():
                self._valueDict['currentQuestion'].set(self._shuffledDeck[self._valueDict['deckCompletion'].get() - 1].get('character'))
                if self._answered == False:
                    self._master.after(100, self._runQuizZh)  # Schedule the function in the Tkinter main loop
                else:
                    self._master.after(100, self._runQuizZh)  # Schedule the function in the Tkinter main loop'                
            else:
                self._valueDict['roundNumber'].set(self._valueDict['roundNumber'].get() + 1)
                missedcards = []
                missedcards.append(random.shuffle(self._missedCards))
                self._shuffledDeck = missedcards
                self._valueDict['deckLength'].set(len(self._shuffledDeck))
                self._answered = False
        
    def _newRound(self):
        self._valueDict['roundNumber'].set(self._valueDict['roundNumber'].get() + 1)
        self._missedCards = []
        self._missedCards.append(random.shuffle(self._missedCards))
        self._shuffledDeck = self._missedCards
        self._valueDict['deckLength'].set(len(self._shuffledDeck))
        self._valueDict['deckCompletion'].set(1)
        self._answered = False  

    def _updateStats(self) -> None:
        pDeckNum = 'pDeckCorrect' + str(self._valueDict['roundNumber'].get())
        tDeckNum = 'tDeckCorrect' + str(self._valueDict['roundNumber'].get())
        if self._valueDict['pin1yin1Response'].get() == self._valueDict['pin1yin1CorrectAnswer'].get():
            self._valueDict[pDeckNum].set(self._valueDict[pDeckNum].get()+1)
            print('correct')
        else:
            self._missedCards.append(self._shuffledDeck[self._valueDict['deckCompletion'].get()-1])

        self._valueDict['pin1yin1CorrectAnswer'].set('')
        self._valueDict['translationCorrectAnswerEn'].set('')
        self._valueDict['pin1yin1Response'].set('')
        self._valueDict['translationResponse'].set('')
        self._valueDict['deckCompletion'].set(self._valueDict['deckCompletion'].get()+1)
        roundNumPinyin = f"round{self._valueDict['roundNumber'].get()}pinyin"
        print(roundNumPinyin)
        self._studyStatsDict[roundNumPinyin].set(f"{self._valueDict[pDeckNum].get()}/{self._valueDict['deckCompletion'].get()-1}")
        self._studyStatsDict[roundNumPinyin].get()
        roundNumTrans = f"round{self._valueDict['roundNumber'].get()}translation"
        self._studyStatsDict[roundNumTrans].set(f"{self._valueDict[tDeckNum].get()}/{self._valueDict['deckCompletion'].get()-1}")

    def _updateCompletion(self) -> None:
        if (
            self._valueDict['deckCompletion'] != ''
            and self._valueDict['deckLength'] != ''
        ):
            self._studyStatsDict['percentComplete'].set(f"{self._valueDict['deckCompletion'].get()-1}/{self._valueDict['deckLength'].get()} Complete")
        else:
            self._studyStatsDict['percentComplete'].set('--')
        self._answered = True
        self._valueDict['responseState'].set('disabled')


    def _enterBind(self, event) -> None:
        print(self._studyStatsDict['round1pinyin'].get())
        if self._valueDict['roundNumber'].get() == 5:
            print('Done!')
            self._valueDict['roundNumber'].set(6)
        elif self._valueDict['roundNumber'].get() == 6:
            print('enter: new game')
            self._runQuiz(event)
        elif self._valueDict['deckCompletion'].get() == self._valueDict['deckLength'].get() and self._valueDict['langChoice'].get() == 'En':
            print('enter: new round')
            self._newRound()
            self._runQuizEn()
        elif self._valueDict['deckCompletion'].get() == self._valueDict['deckLength'].get():
            self._newRound()
            self._runQuizZh()
        elif self._answered == False and self._valueDict['langChoice'].get() == 'En':
            print('updateCompletion & updateStats')
            self._updateStats()
            self._updateCompletion()
            self._answered = True
        elif self._answered == False:
            print()
            self._updateStats()
            self._updateCompletion()
            self._answered = True
        elif self._valueDict['langChoice'].get() == 'En':
            print('Saen & checkTransResponses')
            self._showAnswersEn()
            self._checkTransResponses()
            self._valueDict['check'].set(0)
            self._valueDict['responseState'].set('normal')
        else:
            self._showAnswersZh()
            self._checkTransResponses()
            self._valueDict['check'].set(0)
            self._valueDict['responseState'].set('normal')


'''''
        !TODO: Fix line 340 (bind syntax) find a way to bind enter to
        frame instead of master

        !TODO: Look into error handling for certain functions

        !TODO: Bind radio buttons

        !TODO: Done

        !TODO: allow for specific searches (hao3 shouldn't include chao3 and and zhao3)

        !TODO: search has one or two entries

        !TODO: Check the box
'''''