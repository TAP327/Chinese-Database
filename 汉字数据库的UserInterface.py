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
        self._searchTerms = {
            'character': StringVar(value = ''),
            'pin1yin1': StringVar(value = ''),
            'POSL': StringVar(value = ''),
            'english': StringVar(value = ''),
            'langChoice': StringVar(value = 'En'),
        }
        self._questionInfo = {
            'currentQuestion': StringVar(value = ''),
            'pResponse': StringVar(value = ''),
            'tResponse': StringVar (value = ''),
            'pCorrectAnswer': StringVar(value = ''),
            'tCorrectAnswer': StringVar(value = ''),
            'check': IntVar (value = 0),
        }
        self._roundInfo = {
            'deckLength': IntVar(value = 1),
            'roundNumber': IntVar (value = 5),
            'donetext': StringVar (value = ''),
            'pDeckNum': IntVar(value = 0),
            'tDeckNum': IntVar(value = 0)
        }
        self._deckCompletion = [
            IntVar(value = 1),
            IntVar(value = 1),
            IntVar(value = 1),
            IntVar(value = 1),
            IntVar(value = 1),
            IntVar(value = 1), #Don't delete!
        ]
        self._pDeckCorrect = [
            IntVar(value = 0),
            IntVar(value = 0),
            IntVar(value = 0),
            IntVar(value = 0),
        ]
        self._tDeckCorrect = [
            IntVar(value = 0),
            IntVar(value = 0),
            IntVar(value = 0),
            IntVar(value = 0),
        ]
        self._studyStats = {
            'p0': StringVar(value = str(self._pDeckCorrect[0].get()) + '/' + str(self._deckCompletion[0].get())),
            'p1': StringVar(value = str(self._pDeckCorrect[1].get()) + '/' + str(self._deckCompletion[1].get())),
            'p2': StringVar(value = str(self._pDeckCorrect[2].get()) + '/' + str(self._deckCompletion[2].get())),
            'p3': StringVar(value = str(self._pDeckCorrect[3].get()) + '/' + str(self._deckCompletion[3].get())),
            't0': StringVar(value = str(self._tDeckCorrect[0].get()) + '/' + str(self._deckCompletion[0].get())),
            't1': StringVar(value = str(self._tDeckCorrect[1].get()) + '/' + str(self._deckCompletion[1].get())),
            't2': StringVar(value = str(self._tDeckCorrect[2].get()) + '/' + str(self._deckCompletion[2].get())),
            't3': StringVar(value = str(self._tDeckCorrect[3].get()) + '/' + str(self._deckCompletion[3].get())),
            'percent': StringVar(value = "--")
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
        char_账目 = Entry(study_refiner, textvariable = self._searchTerms['character'])
        pinyin_账目 = Entry(study_refiner, textvariable = self._searchTerms['pin1yin1'])
        posl_账目 = Entry(study_refiner, textvariable = self._searchTerms['POSL'])
        eng_账目 = Entry(study_refiner, textvariable = self._searchTerms['english'])
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
            variable = self._searchTerms['langChoice'],
            value = 'En',
            command = self._switchLangtoEn
        )
        中文的设定 = Radiobutton(
            study_refiner,
            bg = 'pink',
            variable = self._searchTerms['langChoice'],
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
        round0pinyin = Label(
            study_frame,
            textvariable = self._studyStats['p0'],
            bg = 'white'
        )
        round0pinyin.place(x = 180, y = 120)
        round1pinyin = Label(
            study_frame,
            textvariable = self._studyStats['p1'],
            bg = 'white'
        )
        round1pinyin.place(x = 230, y = 120)

        round2pinyin = Label(
            study_frame,
            textvariable = self._studyStats['p2'],
            bg = 'white'
        )
        round2pinyin.place(x = 280, y = 120)

        round3pinyin = Label(
            study_frame,
            textvariable = self._studyStats['p3'],
            bg = 'white'
        )
        round3pinyin.place(x = 330, y = 120)

        round0translation = Label(
            study_frame,
            textvariable = self._studyStats['t0'],
            bg = 'white'
        )
        round0translation.place(x = 180, y = 215)

        round1translation = Label(
            study_frame,
            textvariable = self._studyStats['t1'],
            bg = 'white'
        )
        round1translation.place(x = 230, y = 215)

        round2translation = Label(
            study_frame,
            textvariable = self._studyStats['t2'],
            bg = 'white'
        )
        round2translation.place(x = 280, y = 215)
        
        round3translation = Label(
            study_frame,
            textvariable = self._studyStats['t3'],
            bg = 'white'
        )
        round3translation.place(x = 330, y = 215)

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
            textvariable = self._questionInfo['currentQuestion'],
            bg = 'white',
            font = 14,
            wraplength = 250,
            justify = 'left'
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
            textvariable = self._questionInfo['pCorrectAnswer'],
            bg = 'white',
            font = 15,
            wraplength = 250,
            justify = 'left'
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
            textvariable = self._questionInfo['tCorrectAnswer'],
            bg = 'white',
            font = 15,
            wraplength = 250,
            justify = 'left'
        )
        translation_correct_answer_label_en.place(x = 180, y = 237)

        self.pinyin_answer_entry = Entry(study_frame, textvariable = self._questionInfo['pResponse'], state = 'normal')
        self.pinyin_answer_entry.place(x = 180, y = 90)

        self.translation_answer_entry = Entry(study_frame, textvariable = self._questionInfo['tResponse'], state = 'normal')
        self.translation_answer_entry.place(x = 180, y = 180)

        done_text = Label(
            study_frame,
            textvariable = self._roundInfo['donetext'],
            bg = 'white',
            font = 16
        )
        done_text.place(x = 180, y = 260)

        self._createUISFStudyStats(study_frame)

        correct_check = Checkbutton(
            study_frame,
            command = self._updateCompletion,
            bg = 'white',
            variable = self._questionInfo['check']
        )
        correct_check.place(x = 350, y = 180)

        percent_complete = Label(
            study_frame,
            textvariable = self._studyStats['percent'],
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
            if self._questionInfo['check'].get() == 0:
                self._questionInfo['check'].set(1)
            else:
                self._questionInfo['check'].set(0)

    def _searchDatabaseUI(self) -> None:
        '''
            for key, value in self._searchTerms.items():
                if key in [
                    'character',
                    'pin1yin1',
                    'POSL',
                    'english'
                ] and value.get() != '':
                    search_values.update({key: value.get()})
        '''
        search_values = {
            key: value.get()
            for key, value in self._searchTerms.items() if
            key in ['character', 'pin1yin1', 'POSL', 'english']
            and value.get() != ''
        }
        self._search_results = self._ZH_DB.search_database_DB(search_values)

    def _showAnswersEn(self) -> None:
        roundNumber = self._roundInfo['roundNumber'].get()
        roundCompletion = self._deckCompletion[roundNumber].get() - 1
        pin1yin1 = self._shuffledDeck[roundCompletion].get('pin1yin1')
        self._questionInfo['pCorrectAnswer'].set(pin1yin1)

        character = self._shuffledDeck[roundCompletion].get('character')
        self._questionInfo['tCorrectAnswer'].set(character)

    def _showAnswersZh(self) -> None:
        roundNumber = self._roundInfo['roundNumber'].get()
        roundCompletion = self._deckCompletion[roundNumber].get() - 1
        pin1yin1 = self._shuffledDeck[roundCompletion].get('pin1yin1')
        self._questionInfo['pCorrectAnswer'].set(pin1yin1)

        definition = self._shuffledDeck[roundCompletion].get('definition')
        self._questionInfo['tCorrectAnswer'].set(definition)

    def _checkTransResponses(self) -> None:
        if self._questionInfo['check'].get() == 1:
            roundNumber = self._roundInfo['roundNumber'].get()
            self._tDeckCorrect[roundNumber].set(self._tDeckCorrect[roundNumber].get() + 1)
            self._questionInfo['check'].set(0)
        self._answered = False
        self._questionInfo['currentQuestion'].set('')

    def _runQuiz(self, event):
        self._questionInfo['currentQuestion'].set('')
        self._questionInfo['pResponse'].set('')
        self._questionInfo['tResponse'].set('')
        self._questionInfo['pCorrectAnswer'].set('')
        self._questionInfo['tCorrectAnswer'].set('')
        self._roundInfo['roundNumber'].set(0)
        self._roundInfo['donetext'].set('')
        self._deckCompletion[0].set(1)
        self._deckCompletion[1].set(1)
        self._deckCompletion[2].set(1)
        self._deckCompletion[3].set(1)
        self._pDeckCorrect[0].set(0)
        self._pDeckCorrect[1].set(0)
        self._pDeckCorrect[2].set(0)
        self._pDeckCorrect[3].set(0)
        self._tDeckCorrect[0].set(0)
        self._tDeckCorrect[1].set(0)
        self._tDeckCorrect[2].set(0)
        self._tDeckCorrect[3].set(0)
        self._answered = False

        self._searchDatabaseUI()
        '''
        tmp_list = []
        for result in self._search_results.values():
            tmp_list.append(result)
        '''
        self._shuffledDeck = [result for result in self._search_results.values()]
        random.shuffle(self._shuffledDeck)
        self._roundInfo['deckLength'].set(len(self._search_results))
        self._updateCompletion()
        self._searchTerms['character'].set('')
        self._searchTerms['pin1yin1'].set([])
        self._searchTerms['POSL'].set('')
        self._searchTerms['english'].set('')
        if self._searchTerms['langChoice'].get() == 'En':
            self._runQuizEn()
        else:
            self._runQuizZh()
        
       

    def _runQuizEn(self):
        if self._searchTerms['langChoice'].get() == 'En':
            roundNumber = self._roundInfo['roundNumber'].get()
            newQuestionSlice = self._deckCompletion[roundNumber].get() - 1
            newQuestion = self._shuffledDeck[newQuestionSlice] #Type dict
            newQuestionDef = newQuestion.get('definition')
            self._questionInfo['currentQuestion'].set(newQuestionDef)
            if self._answered == False:
                self._master.after(100, self._runQuizEn)  # Schedule the function in the Tkinter main loop
            else:
                self._master.after(100, self._runQuizEn)  # Don't delete this!  It does something!

    def _runQuizZh(self):
        if self._searchTerms['langChoice'].get() == 'Zh':
            roundNumber = self._roundInfo['roundNumber'].get()
            newQuestionSlice = self._deckCompletion[roundNumber].get() - 1
            newQuestion = self._shuffledDeck[newQuestionSlice] #Type dict
            newQuestionDef = newQuestion.get('character')
            self._questionInfo['currentQuestion'].set(newQuestionDef)
            if self._answered == False:
                self._master.after(100, self._runQuizZh)  # Schedule the function in the Tkinter main loop
            else:
                self._master.after(100, self._runQuizZh)  # Don't delete this! It does something!

    def _done(self):
        self._roundInfo['roundNumber'].set(6)
        self._questionInfo['tCorrectAnswer'].set('')
        self._roundInfo['donetext'].set('做得好！')

    def _newRound(self):
        self._roundInfo['roundNumber'].set(self._roundInfo['roundNumber'].get() + 1)
        missedCardsShuffled: list[dict] = []
        missedCardsShuffled = missedCardsShuffled + self._missedCards
        random.shuffle(missedCardsShuffled)
        self._shuffledDeck.clear()
        self._shuffledDeck: list[dict] = self._shuffledDeck + missedCardsShuffled
        self._roundInfo['deckLength'].set(len(self._shuffledDeck))
        self._answered = False  
        self._missedCards.clear()
        if self._shuffledDeck == []:
            self._done()
    
    def _lastCard(self) -> None:
        pass

    def _updateStats(self) -> None:
        roundNumber = self._roundInfo['roundNumber'].get()
        deckCompletion = self._deckCompletion[roundNumber].get()
        if self._questionInfo['pResponse'].get() == self._questionInfo['pCorrectAnswer'].get():
            self._pDeckCorrect[roundNumber].set(self._pDeckCorrect[roundNumber].get() + 1)
        else:
            self._missedCards.append(self._shuffledDeck[deckCompletion-1])

        self._questionInfo['pCorrectAnswer'].set('')
        self._questionInfo['tCorrectAnswer'].set('')
        self._questionInfo['pResponse'].set('')
        self._questionInfo['tResponse'].set('')
        self._deckCompletion[roundNumber].set(deckCompletion + 1)
    
        roundNumPinyin = 'p' + str(roundNumber)
        self._studyStats[roundNumPinyin].set(str(self._pDeckCorrect[roundNumber].get()) + '/' + str(deckCompletion))
        roundNumTrans = 't' + str(roundNumber)
        self._studyStats[roundNumTrans].set(str(self._tDeckCorrect[roundNumber].get()) + '/' + str(deckCompletion))

    def _updateCompletion(self) -> None:
        roundNumber = self._roundInfo['roundNumber'].get()
        deckCompletion = self._deckCompletion[roundNumber].get()
        if (
            deckCompletion != ''
            and self._roundInfo['deckLength'].get() != ''
        ):
            self._studyStats['percent'].set(f"{deckCompletion-1}/{self._roundInfo['deckLength'].get()} Complete")
        else:
            self._studyStats['percent'].set('--')
        self._answered = True
        self.pinyin_answer_entry['state'] = 'normal'
        self.translation_answer_entry['state'] = 'normal'

    def _switchLangtoEn(self) -> None:
        self._questionInfo['currentQuestion'].set('')
        self._runQuizEn()
    
    def _switchLangtoZh(self) -> None:
        self._questionInfo['currentQuestion'].set('')
        self._runQuizZh()

    def _enterBind(self, event) -> None:
        roundNumber = self._roundInfo['roundNumber'].get()
        deckCompletion = self._deckCompletion[roundNumber].get()
        if roundNumber == 4:
            self._done()
        elif roundNumber == 5:
            self._runQuiz(event)
        elif deckCompletion == self._roundInfo['deckLength'].get() and self._searchTerms['langChoice'].get() == 'En':
            self._showAnswersEn()
            self._checkTransResponses()
            if self._answered == False:
                self._master.after(100, self._lastCard)
            else:
                self._master.after(100, self._lastCard)
            self._questionInfo['check'].set(0)
            self.pinyin_answer_entry['state'] = 'disabled'
            self.translation_answer_entry['state'] = 'disabled'
            self._newRound()
            self._runQuizEn()
        elif deckCompletion == self._roundInfo['deckLength'].get():
            self._showAnswersZh()
            self._checkTransResponses()
            self._updateStats()
            self._updateCompletion()
            if self._answered == False:
                self._master.after(100, self._lastCard)
            else:
                self._master.after(100, self._lastCard)
            self._questionInfo['check'].set(0)
            self.pinyin_answer_entry['state'] = 'disabled'
            self.translation_answer_entry['state'] = 'disabled'
            self._newRound()
            self._runQuizZh()
        elif self._answered == False:
            self._updateStats()
            self._updateCompletion()
            self._answered = True
        elif self._searchTerms['langChoice'].get() == 'En':
            self._showAnswersEn()
            self._checkTransResponses()
            self._questionInfo['check'].set(0)
            self.pinyin_answer_entry['state'] = 'disabled'
            self.translation_answer_entry['state'] = 'disabled'
        else:
            self._showAnswersZh()
            self._checkTransResponses()
            self._questionInfo['check'].set(0)
            self.pinyin_answer_entry['state'] = 'disabled'
            self.translation_answer_entry['state'] = 'disabled'
    




'''''
        !TODO: Fix line 340 (bind syntax) find a way to bind enter to
        frame instead of master (or make a tab varible and add it to enter bind?)

        !TODO: Last Card

        !TODO: Refactor Study Tab

        azure & lightblue2
'''''
