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
            'deck1Completion': IntVar(value = 0),
            'deck2Completion': IntVar(value = 0),
            'deck3Completion': IntVar(value = 0),
            'deck4Completion': IntVar(value = 0),
            'deck5Completion': IntVar(value = 0),
            'deck6Completion': IntVar(value = 0), #Don't delete!
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
            'translationCorrectAnswer': StringVar(value = ''),
            'roundNumber': IntVar (value = 6),
            'check': IntVar (value = 0),
            'donetext': StringVar (value = '')
        }
        self._studyStatsDict = {
            'round1pinyin': StringVar(value = f"{self._valueDict['pDeckCorrect1'].get()}/{self._valueDict['deck1Completion'].get()}"),
            'round2pinyin': StringVar(value = f"{self._valueDict['pDeckCorrect2'].get()}/{self._valueDict['deck2Completion'].get()}"),
            'round3pinyin': StringVar(value = f"{self._valueDict['pDeckCorrect3'].get()}/{self._valueDict['deck3Completion'].get()}"),
            'round4pinyin': StringVar(value = f"{self._valueDict['pDeckCorrect4'].get()}/{self._valueDict['deck4Completion'].get()}"),
            'round1translation': StringVar(value = f"{self._valueDict['tDeckCorrect1'].get()}/{self._valueDict['deck1Completion'].get()}"),
            'round2translation': StringVar(value = f"{self._valueDict['tDeckCorrect2'].get()}/{self._valueDict['deck2Completion'].get()}"),
            'round3translation': StringVar(value = f"{self._valueDict['tDeckCorrect3'].get()}/{self._valueDict['deck3Completion'].get()}"),
            'round4translation': StringVar(value = f"{self._valueDict['tDeckCorrect4'].get()}/{self._valueDict['deck4Completion'].get()}"),
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
        学习的框架.place(x = 200, y = 120)
        self._笔记本.add(学习的框架, text = '学习')

    def _createUISFPracticeTitle(self, 练习的框架) -> None:
        练习的题目 = Frame(练习的框架,
            height = 50,
            width = 600,
            bg = 'aquamarine2'
        )

        练习的题目.place(x = 0, y = 0)
        Label(
            练习的题目,
            text = "咱们练习中文吧! ",
            width = 20, 
            font = 15,
            bg = 'aquamarine2'
        ).place(x = 10, y = 10)

    def _createUISFStudyRefiner(self, 练习的框架) -> None:
        study_refiner = Frame(
            练习的框架,
            height = 350,
            width = 155,
            bg = 'pink',
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
            bg = "pink"
        )
        pinyin_label = Label(
            study_refiner,
            text = "Pin1Yin1: ",
            bg = "pink"
        )
        posl_label = Label(
            study_refiner,
            text = "POS or Lesson: ",
            bg = "pink"
        )
        eng_label = Label(
            study_refiner,
            text = "English: ",
            bg = "pink"
        )
        choose_lang_label = Label(
            study_refiner,
            text = "Question Language: ",
            bg = "pink"

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
            text = 'Zh',
            bg = 'pink'
        )
        英文字 = Label(
            study_refiner,
            text = 'En', 
            bg = 'pink',
        )
        英文的设定 = Radiobutton(
            study_refiner,
            bg = 'pink',
            variable = self._valueDict['langChoice'],
            value = 'En',
            command = self._switchLangtoEn
        )
        中文的设定 = Radiobutton(
            study_refiner,
            bg = 'pink',
            variable = self._valueDict['langChoice'],
            value = 'Zh',
            command = self._switchLangtoZh
        )

        char_账目.place(x = 3, y = 50)
        pinyin_账目.place(x = 3, y = 100)
        posl_账目.place(x = 3, y = 150)
        eng_账目.place(x = 3, y = 200)
        中文字.place(x = 15, y = 250)
        英文字.place(x = 65, y = 250)
        中文的设定.place(x = 40, y = 250)
        英文的设定.place(x = 90, y = 250)

        #Add Study Button
        练习的按键 = Button(
            study_refiner,
            text = "练习", 
            bg = 'white'
        )
        练习的按键.place(x = 50, y = 275)
        练习的按键.bind('<Button-1>', self._runQuiz)

    def _createUISFStudyStats(self, study_frame) -> None:
        round1pinyin = Label(
            study_frame,
            textvariable = self._studyStatsDict['round1pinyin'],
            bg = 'white'
        )
        round1pinyin.place(x = 180, y = 120)
        round2pinyin = Label(
            study_frame,
            textvariable = self._studyStatsDict['round2pinyin'],
            bg = 'white'
        )
        round2pinyin.place(x = 230, y = 120)

        round3pinyin = Label(
            study_frame,
            textvariable = self._studyStatsDict['round3pinyin'],
            bg = 'white'
        )
        round3pinyin.place(x = 280, y = 120)

        round4pinyin = Label(
            study_frame,
            textvariable = self._studyStatsDict['round4pinyin'],
            bg = 'white'
        )
        round4pinyin.place(x = 330, y = 120)

        round1translation = Label(
            study_frame,
            textvariable = self._studyStatsDict['round1translation'],
            bg = 'white'
        )
        round1translation.place(x = 180, y = 215)

        round2translation = Label(
            study_frame,
            textvariable = self._studyStatsDict['round2translation'],
            bg = 'white'
        )
        round2translation.place(x = 230, y = 215)

        round3translation = Label(
            study_frame,
            textvariable = self._studyStatsDict['round3translation'],
            bg = 'white'
        )
        round3translation.place(x = 280, y = 215)
        
        round4translation = Label(
            study_frame,
            textvariable = self._studyStatsDict['round4translation'],
            bg = 'white'
        )
        round4translation.place(x = 330, y = 215)

    def _createUISFStudyFrame(self, 练习的框架) -> None:
        study_frame = Frame(
            练习的框架, height = 350,
            width = 465,
            padx = 2,
            bg = 'white'
        )
        study_frame.place(x = 136,y = 50)

        question_label = Label(
            study_frame,
            textvariable = self._valueDict['currentQuestion'],
            bg = 'white'
        )
        question_label.place(x = 35, y= 35)

        pinyin_entry_label = Label(
            study_frame,
            text = 'Pin1yin1:  ',
            bg = 'white'
        )
        pinyin_entry_label.place(x = 80, y = 80)

        pinyin_correct_answer_label = Label(
            study_frame,
            textvariable = self._valueDict['pin1yin1CorrectAnswer'],
            bg = 'white',
            font = 15
        )
        pinyin_correct_answer_label.place(x = 180, y = 143)

        translation_entry_label = Label(
            study_frame,
            text = 'Translation:  ',
            bg = 'white'
        )
        translation_entry_label.place(x = 80, y = 180)

        translation_correct_answer_label_en = Label(
            study_frame,
            textvariable = self._valueDict['translationCorrectAnswer'],
            bg = 'white',
            font = 48
        )
        translation_correct_answer_label_en.place(x = 180, y = 237)

        pinyin_answer_entry = Entry(study_frame, textvariable = self._valueDict['pin1yin1Response'], state = 'normal')
        pinyin_answer_entry.place(x = 180, y = 90)

        translation_answer_entry = Entry(study_frame, textvariable = self._valueDict['translationResponse'], state = self._valueDict['responseState'].get())
        translation_answer_entry.place(x = 180, y = 180)

        done_text = Label(
            study_frame,
            textvariable = self._valueDict['donetext'],
            bg = 'white',
            font = 16
        )
        done_text.place(x = 180, y = 260)

        self._createUISFStudyStats(study_frame)

        correct_check = Checkbutton(
            study_frame,
            command = self._updateCompletion,
            bg = 'white',
            variable = self._valueDict['check']
        )
        correct_check.place(x = 350, y = 180)

        percent_complete = Label(
            study_frame,
            textvariable = self._studyStatsDict['percentComplete'],
            bg = 'white'
        )
        percent_complete.place(x = 280, y = 35)

    def _createUIStudyFrame(self) -> None:
        练习的框架 = ttk.Frame(self._笔记本, width = 600, height = 380)
        练习的框架.place(x = 0, y = 0)
        self._笔记本.add(练习的框架, text = '练习')

        self._createUISFPracticeTitle(练习的框架)
        self._createUISFStudyRefiner(练习的框架)
        self._createUISFStudyFrame(练习的框架)

    def _createUiWindow(self) -> None:
        self._master.title('汉字数据库')
        self._master.maxsize(600, 400)
        self._master.minsize(600, 400)

        # Create Tabs
        self._笔记本.place(x = 0, y = 0)

        self._createUIDictFrame()
        self._createUIStudyFrame()

        self._master.bind('<Return>', self._enterBind)
        self._master.bind('x', self._checkTheBox)

    def runMainLoop(self) -> None:
        self._master.mainloop()

    def _checkTheBox(self, event) -> None:
        if self._answered == False:
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

    def _showAnswersEn(self) -> None:
        print('showAnswersEn')
        self._valueDict['pin1yin1CorrectAnswer'].set(self._shuffledDeck[self._valueDict[f"deck{self._valueDict['roundNumber'].get()}Completion"].get()-1].get('pin1yin1'))
        self._valueDict['translationCorrectAnswer'].set(self._shuffledDeck[self._valueDict[f"deck{self._valueDict['roundNumber'].get()}Completion"].get()-1].get('character'))

    def _showAnswersZh(self) -> None:
        print('showAnswersZh')
        self._valueDict['pin1yin1CorrectAnswer'].set(self._shuffledDeck[self._valueDict[f"deck{self._valueDict['roundNumber'].get()}Completion"].get()-1].get('pin1yin1'))
        self._valueDict['translationCorrectAnswer'].set(self._shuffledDeck[self._valueDict[f"deck{self._valueDict['roundNumber'].get()}Completion"].get()-1].get('definition'))

    def _checkTransResponses(self) -> None:
        print('checkTransResponses')
        if self._valueDict['check'].get() == 1:
            tDeckCorrectNum = 'tDeckCorrect' + str(self._valueDict['roundNumber'].get())
            self._valueDict[tDeckCorrectNum].set(self._valueDict[tDeckCorrectNum].get()+1)
            self._valueDict['check'].set(0)
        self._answered = False
        self._valueDict['currentQuestion'].set('')

    def _runQuiz(self, event):
        print('runQuiz')
        self._valueDict['deck1Completion'].set(0)
        self._valueDict['deck2Completion'].set(0)
        self._valueDict['deck3Completion'].set(0)
        self._valueDict['deck4Completion'].set(0)
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
        self._valueDict['pin1yin1Response'].set('')
        self._valueDict['translationResponse'].set('')
        self._valueDict['pin1yin1CorrectAnswer'].set('')
        self._valueDict['translationCorrectAnswer'].set('')
        self._valueDict['donetext'].set('')
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
        self._valueDict['entryCharacter'].set('')
        self._valueDict['entryPin1yin1'].set([])
        self._valueDict['entryPOSL'].set('')
        self._valueDict['entryEnglish'].set('')
        if self._valueDict['langChoice'].get() == 'En':
            self._runQuizEn()
        else:
            self._runQuizZh()

    def _runQuizEn(self):
        if self._valueDict['langChoice'].get() == 'En':
            newQuestionSlice = self._valueDict[f"deck{self._valueDict['roundNumber'].get()}Completion"].get() - 1 #Type int
            newQuestion = self._shuffledDeck[newQuestionSlice] #Type dict
            newQuestionDef = newQuestion.get('definition')
            self._valueDict['currentQuestion'].set(newQuestionDef)
            if self._answered == False:
                self._master.after(100, self._runQuizEn)  # Schedule the function in the Tkinter main loop
            else:
                self._master.after(100, self._runQuizEn)  # Don't delete this!  It does something!

    def _runQuizZh(self):
        if self._valueDict['langChoice'].get() == 'Zh':
            newQuestionSlice = self._valueDict[f"deck{self._valueDict['roundNumber'].get()}Completion"].get() - 1 #Type int
            newQuestion = self._shuffledDeck[newQuestionSlice] #Type dict
            newQuestionDef = newQuestion.get('character')
            print(str(newQuestionSlice) + ': ' + str(newQuestionDef))
            self._valueDict['currentQuestion'].set(newQuestionDef)
            if self._answered == False:
                self._master.after(100, self._runQuizZh)  # Schedule the function in the Tkinter main loop
            else:
                self._master.after(100, self._runQuizZh)  # Don't delete this! It does something!

    def _done(self):    
        self._studyStatsDict['round1pinyin'].set('0/0'),
        self._studyStatsDict['round2pinyin'].set('0/0'),
        self._studyStatsDict['round3pinyin'].set('0/0'),
        self._studyStatsDict['round4pinyin'].set('0/0'),
        self._studyStatsDict['round1translation'].set('0/0'),
        self._studyStatsDict['round2translation'].set('0/0'),
        self._studyStatsDict['round3translation'].set('0/0'),
        self._studyStatsDict['round4translation'].set('0/0'),
        self._studyStatsDict['percentComplete'].set('--'),
        self._valueDict['translationCorrectAnswer'].set('')
        self._valueDict['donetext'].set('做得好！')    
        print('done')    

    def _newRound(self):
        print('newRound')
        self._valueDict['roundNumber'].set(self._valueDict['roundNumber'].get() + 1)
        missedCardsShuffled: list[dict] = []
        missedCardsShuffled = missedCardsShuffled + self._missedCards
        random.shuffle(missedCardsShuffled)
        print(missedCardsShuffled)
        self._shuffledDeck.clear()
        self._shuffledDeck: list[dict] = self._shuffledDeck + missedCardsShuffled
        print(self._shuffledDeck)
        print(len(self._shuffledDeck))
        self._valueDict['deckLength'].set(len(self._shuffledDeck))
        self._answered = False  
        self._missedCards.clear()
        if self._shuffledDeck == []:
            self._done()
    
    def _lastCard(self) -> None:
        pass

    def _updateStats(self) -> None:
        print('updateStats')
        deckCompletion = self._valueDict[f"deck{self._valueDict['roundNumber'].get()}Completion"].get()
        pDeckNum = 'pDeckCorrect' + str(self._valueDict['roundNumber'].get())
        tDeckNum = 'tDeckCorrect' + str(self._valueDict['roundNumber'].get())
        if self._valueDict['pin1yin1Response'].get() == self._valueDict['pin1yin1CorrectAnswer'].get():
            self._valueDict[pDeckNum].set(self._valueDict[pDeckNum].get()+1)
        else:
            self._missedCards.append(self._shuffledDeck[deckCompletion-1])

        self._valueDict['pin1yin1CorrectAnswer'].set('')
        self._valueDict['translationCorrectAnswer'].set('')
        self._valueDict['pin1yin1Response'].set('')
        self._valueDict['translationResponse'].set('')
        self._valueDict[f"deck{self._valueDict['roundNumber'].get()}Completion"].set(deckCompletion+1)
        roundNumPinyin = f"round{self._valueDict['roundNumber'].get()}pinyin"
        self._studyStatsDict[roundNumPinyin].set(f"{self._valueDict[pDeckNum].get()}/{deckCompletion+1}")
        self._studyStatsDict[roundNumPinyin].get()
        roundNumTrans = f"round{self._valueDict['roundNumber'].get()}translation"
        self._studyStatsDict[roundNumTrans].set(f"{self._valueDict[tDeckNum].get()}/{deckCompletion+1}")

    def _updateCompletion(self) -> None:
        print('updateCompletion')
        deckCompletion = self._valueDict[f"deck{self._valueDict['roundNumber'].get()}Completion"].get()
        if (
            deckCompletion != ''
            and self._valueDict['deckLength'].get() != ''
        ):
            self._studyStatsDict['percentComplete'].set(f"{deckCompletion}/{self._valueDict['deckLength'].get()} Complete")
        else:
            self._studyStatsDict['percentComplete'].set('--')
        self._answered = True
        print(self._valueDict['responseState'].get())
        self._valueDict['responseState'].set('disabled')
        print(self._valueDict['responseState'].get())


    def _switchLangtoEn(self) -> None:
        self._valueDict['currentQuestion'].set('')
        self._runQuizEn()
    
    def _switchLangtoZh(self) -> None:
        self._valueDict['currentQuestion'].set('')
        self._runQuizZh()

    def _enterBind(self, event) -> None:
        deckCompletion = self._valueDict[f"deck{self._valueDict['roundNumber'].get()}Completion"].get()
        print(deckCompletion)
        if self._valueDict['roundNumber'].get() == 5:
            self._done()
        elif self._valueDict['roundNumber'].get() == 6:
            self._runQuiz(event)
        elif deckCompletion >= self._valueDict['deckLength'].get() and self._valueDict['langChoice'].get() == 'En':
            print("New round subroutine")
            self._showAnswersEn()
            self._checkTransResponses()
            if self._answered == False:
                self._master.after(100, self._lastCard)
            else:
                self._master.after(100, self._lastCard)
            self._valueDict['check'].set(0)
            self._newRound()
            self._runQuizEn()
        elif deckCompletion >= self._valueDict['deckLength'].get():
            self._showAnswersZh()
            self._checkTransResponses()
            if self._answered == False:
                self._master.after(100, self._lastCard)
            else:
                self._master.after(100, self._lastCard)
            self._valueDict['check'].set(0)
            self._newRound()
            self._runQuizZh()
        elif self._answered == False:
            self._updateStats()
            self._updateCompletion()
            self._answered = True
        elif self._valueDict['langChoice'].get() == 'En':
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
        frame instead of master (or make a tab varible and add it to enter bind?)

        !TODO: Last Card (extra card?, delayed update, disabled text boxes)

        !TODO: Input 202 Vocab (2.12, 2.13, 2.16)

        !TODO: Input BAND 1 & the rest of HSK 2
        azure & lightblue2
'''''
