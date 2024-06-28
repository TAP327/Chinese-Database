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
from zhdb.汉字数据库的事理 import Database
import random

class Ui():
    def __init__(self) -> None:
        self._master = Tk()
        self._笔记本 = ttk.Notebook(self._master)
        self._DsearchTerms = {
            'character': StringVar(value = ''),
            'pin1yin1': StringVar(value = ''),
            'POS': StringVar(value = ''),
            'HSK': StringVar(value = ''),
            'definition': StringVar(value = ''),
            'langChoice': StringVar(value = 'En'),
        }
        self._SsearchTerms = {
            'character': StringVar(value = ''),
            'pin1yin1': StringVar(value = ''),
            'POS': StringVar(value = ''),
            'HSK': StringVar(value = ''),
            'definition': StringVar(value = ''),
            'langChoice': StringVar(value = 'En'),
        }
        self._searchInfo = {
            'pageCounter': StringVar(value = 'Search Results: '),
            'ZH1': StringVar(value = '汉字'),
            'PY1': StringVar(value = 'pin1yin1'),
            'EN1': StringVar(value = 'English example'),
            'ZH2': StringVar(value = '汉字汉字'),
            'PY2': StringVar(value = 'pin1yin1'),
            'EN2': StringVar(value = 'English'),
            'ZH3': StringVar(value = '汉字'),
            'PY3': StringVar(value = 'pin1yin1'),
            'EN3': StringVar(value = 'English'),
            'ZH4': StringVar(value = '汉字'),
            'PY4': StringVar(value = 'pin1yin1'),
            'EN4': StringVar(value = 'English sample that is kind of obnoxiously long')
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
        self._Dsearch_results = {}
        self._Ssearch_results = {}
        self._shuffledDeck = []
        self._missedCards = []
        self._answered = False
        self._createUiWindow()

    def _close(self):
        self._master.destroy()

    def _createFrameTitle(self, 框架, 课文) -> None:
        学习的题目 = Frame(框架,
            height = 50,
            width = 600, 
            bg = 'aquamarine2'
        )
        学习的题目.place(x = 0, y = 0)
        Label(
            学习的题目, 
            text = 课文,
            width = 19, 
            font = 15,
            bg = 'aquamarine2'
        ).place(x = 0, y = 10)

    def _createRefinerLabels(self, frame_refiner) -> None:
        char_label = Label(
            frame_refiner,
            text = "Character: ",
            bg = "pink"
        )
        pinyin_label = Label(
            frame_refiner,
            text = "Pin1Yin1: ",
            bg = "pink"
        )
        pos_label = Label(
            frame_refiner,
            text = "Part of Speech: ",
            bg = "pink"
        )
        hsk_label = Label(
            frame_refiner,
            text = "HSK Level: ",
            bg = "pink"
        )
        def_label = Label(
            frame_refiner,
            text = "Definition: ",
            bg = "pink"
        )
        choose_lang_label = Label(
            frame_refiner,
            text = "Question Language: ",
            bg = "pink"
        )

        char_label.place(x = 7, y = 25)
        pinyin_label.place(x = 7, y = 75)
        pos_label.place(x = 7, y = 125)
        hsk_label.place(x = 7, y = 175)
        def_label.place(x = 7, y = 225)
        choose_lang_label.place(x = 7, y = 275)      

    def _createRefinerVars(self, study_refiner, XsearchTerms: dict, buttFunc) -> None:
        char_账目 = Entry(study_refiner, textvariable = XsearchTerms['character'])
        pinyin_账目 = Entry(study_refiner, textvariable = XsearchTerms['pin1yin1'])
        pos_账目 = Entry(study_refiner, textvariable = XsearchTerms['POS'])
        hsk_账目 = Entry(study_refiner, textvariable = XsearchTerms['HSK'])
        def_账目 = Entry(study_refiner, textvariable = XsearchTerms['definition'])
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
            variable = XsearchTerms['langChoice'],
            value = 'En',
            command = self._switchLangtoEn
        )
        中文的设定 = Radiobutton(
            study_refiner,
            bg = 'pink',
            variable = XsearchTerms['langChoice'],
            value = 'Zh',
            command = self._switchLangtoZh
        )

        char_账目.place(x = 3, y = 50)
        pinyin_账目.place(x = 3, y = 100)
        pos_账目.place(x = 3, y = 150)
        hsk_账目.place(x = 3, y = 200)
        def_账目.place(x = 3, y = 250)
        中文字.place(x = 15, y = 300)
        英文字.place(x = 65, y = 300)
        中文的设定.place(x = 40, y = 300)
        英文的设定.place(x = 90, y = 300)

        #Add Study Button
        按键 = Button(
            study_refiner,
            text = "练习", 
            bg = 'white'
        )
        按键.place(x = 50, y = 330)
        按键.bind('<Button-1>', buttFunc)

    def _createDictRefiner(self, 学习的框架) -> None:
        dict_refiner = Frame(
            学习的框架,
            height = 400,
            width = 155,
            bg = 'pink',
            padx = 2
        )
        dict_refiner.place(
            x = 0,
            y = 50
        )
        self._createRefinerLabels(dict_refiner)
        self._createRefinerVars(dict_refiner, self._DsearchTerms, self._runQuery)

    def _createStudyRefiner(self, 练习的框架) -> None:
        study_refiner = Frame(
            练习的框架,
            height = 400,
            width = 155,
            bg = 'pink',
            padx = 2
        )
        study_refiner.place(
            x = 0,
            y = 50
        )
        self._createRefinerLabels(study_refiner)
        self._createRefinerVars(study_refiner, self._SsearchTerms, self._runQuiz)

    def _createStudyStats(self, study_frame) -> None:
        round0pinyin = Label(
            study_frame,
            textvariable = self._studyStats['p0'],
            bg = 'white'
        )
        round0pinyin.place(x = 190, y = 160)
        round1pinyin = Label(
            study_frame,
            textvariable = self._studyStats['p1'],
            bg = 'white'
        )
        round1pinyin.place(x = 240, y = 160)

        round2pinyin = Label(
            study_frame,
            textvariable = self._studyStats['p2'],
            bg = 'white'
        )
        round2pinyin.place(x = 290, y = 160)

        round3pinyin = Label(
            study_frame,
            textvariable = self._studyStats['p3'],
            bg = 'white'
        )
        round3pinyin.place(x = 340, y = 160)

        round0translation = Label(
            study_frame,
            textvariable = self._studyStats['t0'],
            bg = 'white'
        )
        round0translation.place(x = 190, y = 265)

        round1translation = Label(
            study_frame,
            textvariable = self._studyStats['t1'],
            bg = 'white'
        )
        round1translation.place(x = 240, y = 265)

        round2translation = Label(
            study_frame,
            textvariable = self._studyStats['t2'],
            bg = 'white'
        )
        round2translation.place(x = 290, y = 265)
        
        round3translation = Label(
            study_frame,
            textvariable = self._studyStats['t3'],
            bg = 'white'
        )
        round3translation.place(x = 340, y = 265)

    def _createQuizFrame(self, 练习的框架) -> None:
        study_frame = Frame(
            练习的框架, 
            height = 450,
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
        question_label.place(x = 70, y= 75)

        pinyin_entry_label = Label(
            study_frame,
            text = 'Pin1yin1:  ',
            bg = 'white'
        )
        pinyin_entry_label.place(x = 95, y = 125)

        pinyin_correct_answer_label = Label(
            study_frame,
            textvariable = self._questionInfo['pCorrectAnswer'],
            bg = 'white',
            font = 15,
            wraplength = 250,
            justify = 'left'
        )
        pinyin_correct_answer_label.place(x = 190, y = 183)

        translation_entry_label = Label(
            study_frame,
            text = 'Translation:  ',
            bg = 'white'
        )
        translation_entry_label.place(x = 95, y = 230)

        translation_correct_answer_label = Label(
            study_frame,
            textvariable = self._questionInfo['tCorrectAnswer'],
            bg = 'white',
            font = 15,
            wraplength = 250,
            justify = 'left'
        )
        translation_correct_answer_label.place(x = 191, y = 287)

        self.pinyin_answer_entry = Entry(study_frame, textvariable = self._questionInfo['pResponse'], state = 'normal')
        self.pinyin_answer_entry.place(x = 190, y = 125)

        self.translation_answer_entry = Entry(study_frame, textvariable = self._questionInfo['tResponse'], state = 'normal')
        self.translation_answer_entry.place(x = 190, y = 230)

        done_text = Label(
            study_frame,
            textvariable = self._roundInfo['donetext'],
            bg = 'white',
            font = 16
        )
        done_text.place(x = 190, y = 316)

        self._createStudyStats(study_frame)

        correct_check = Checkbutton(
            study_frame,
            command = self._updateCompletion,
            bg = 'white',
            variable = self._questionInfo['check']
        )
        correct_check.place(x = 350, y = 219)

        percent_complete = Label(
            study_frame,
            textvariable = self._studyStats['percent'],
            bg = 'white'
        )
        percent_complete.place(x = 45, y = 40)

    def _createSearchResultsFrame(self, 学习的框架) -> None:
        SR_frame = Frame(
            学习的框架, 
            height = 450,
            width = 465,
            padx = 2,
            bg = 'white'
        )
        SR_frame.place(x = 136,y = 50)
        SR_page_count = Label(
            SR_frame,
            textvariable = self._searchInfo['pageCounter'],
            bg = 'white'
        )
        SR_page_count.place(x = 45, y = 40)

        #Entry No. 1
        self._ZH1 = Button(
            SR_frame,
            textvariable = self._searchInfo['ZH1'],
            bg = 'white',
            font = 'Helvetica 16',
            activebackground = 'white',
            activeforeground = 'cyan3',
            bd = 0,
            fg = 'cyan4',
            relief = 'flat'
        )
        self._ZH1.place(x = 70, y = 75)
        self._ZH1.bind("<Enter>", self.enterChar)
        self._ZH1.bind("<Leave>", self.leaveChar)
        PY1 = Label(
            SR_frame,
            textvariable = self._searchInfo['PY1'],
            bg = 'white'
        )
        PY1.place(x= 165, y = 75)
        EN1 = Label(
            SR_frame,
            textvariable = self._searchInfo['EN1'],
            bg = 'white'
        )
        EN1.place(x = 165, y = 100)
        
    
        #Entry No. 2
        ZH2 = Button(
            SR_frame,
            textvariable = self._searchInfo['ZH2'],
            bg = 'white',
            font = 'Helvetica 16',
            activebackground = 'white',
            activeforeground = 'cyan3',
            bd = 0,
            fg = 'cyan4',
            highlightcolor = 'white',
            relief = 'flat'
        )
        ZH2.place(x = 70, y = 140)
        PY2 = Label(
            SR_frame,
            textvariable = self._searchInfo['PY2'],
            bg = 'white'
        )
        PY2.place(x= 165, y = 140)
        EN2 = Label(
            SR_frame,
            textvariable = self._searchInfo['EN2'],
            bg = 'white'
        )
        EN2.place(x = 165, y = 165)

        #Entry No. 3       
        ZH3 = Button(
            SR_frame,
            textvariable = self._searchInfo['ZH3'],
            bg = 'white',
            font = 'Helvetica 16',
            activebackground = 'white',
            activeforeground = 'cyan3',
            bd = 0,
            fg = 'cyan4',
            highlightcolor = 'white',
            relief = 'flat'
        )
        ZH3.place(x = 70, y = 205)
        PY3 = Label(
            SR_frame,
            textvariable = self._searchInfo['PY3'],
            bg = 'white'
        )
        PY3.place(x= 165, y = 205)
        EN3 = Label(
            SR_frame,
            textvariable = self._searchInfo['EN3'],
            bg = 'white'
        )
        EN3.place(x = 165, y = 230)

        #Entry No. 4
        ZH4 = Button(
            SR_frame,
            textvariable = self._searchInfo['ZH4'],
            bg = 'white',
            font = 'Helvetica 16',
            activebackground = 'white',
            activeforeground = 'cyan3',
            bd = 0,
            fg = 'cyan4',
            highlightcolor = 'white',
            relief = 'flat'
        )
        ZH4.place(x = 70, y = 270)
        PY4 = Label(
            SR_frame,
            textvariable = self._searchInfo['PY4'],
            bg = 'white'
        )
        PY4.place(x= 165, y = 270)
        EN4 = Label(
            SR_frame,
            textvariable = self._searchInfo['EN4'],
            bg = 'white'
        )
        EN4.place(x = 165, y = 295)

        firstButt = Button(
            SR_frame,
            text = '   First   ',
            bg = 'white'
        )
        firstButt.place(x = 101, y = 330)
        previousButt = Button(
            SR_frame,
            text = '< Previous',
            bg = 'white'
        )
        previousButt.place(x = 164, y = 330)
        nextButt = Button(
            SR_frame,
            text = '  Next >  ',
            bg = 'white'
        )
        nextButt.place(x = 241, y = 330)
        lastButt = Button(
            SR_frame,
            text = '   Last   ',
            bg = 'white'
        )
        lastButt.place(x = 312, y = 330)

    def _createUIDictFrame(self) -> None:
        学习的框架 = ttk.Frame(self._笔记本, width = 600, height = 450)
        学习的框架.place(x = 0, y = 0)
        self._笔记本.add(学习的框架, text = '学习')

        self._createFrameTitle(学习的框架, '汉英词典')
        self._createDictRefiner(学习的框架)
        self._createSearchResultsFrame(学习的框架)
    
    def _createUIStudyFrame(self) -> None:
        练习的框架 = ttk.Frame(self._笔记本, width = 600, height = 450)
        练习的框架.place(x = 0, y = 0)
        self._笔记本.add(练习的框架, text = '练习')

        self._createFrameTitle(练习的框架, '            咱们练习中文吧! ')
        self._createStudyRefiner(练习的框架)
        self._createQuizFrame(练习的框架)

    def _createUiWindow(self) -> None:
        self._master.title('汉字数据库')
        self._master.maxsize(600, 450)
        self._master.minsize(600, 450)

        # Create Tabs
        self._笔记本.place(x = 0, y = 0)

        self._createUIDictFrame()
        self._createUIStudyFrame()

        self._master.bind('<Return>', self._enterBind)
        self._master.bind('x', self._checkTheBox)

    def runMainLoop(self) -> None:
        self._master.mainloop()

    def enterChar(self, event) -> None:
        self._ZH1['background'] = 'azure'

    def leaveChar(self, event) -> None:
        self._ZH1['background'] = 'white'

    def _checkTheBox(self, event) -> None:
        if self._answered == False:
            if self._questionInfo['check'].get() == 0:
                self._questionInfo['check'].set(1)
            else:
                self._questionInfo['check'].set(0)

    def _XsearchDatabaseUI(self, XsearchTerms: dict[str, StringVar]) -> None:
        '''
            for key, value in XsearchTerms.items():
                if key in [
                    'character',
                    'pin1yin1',
                    'POS',
                    'HSK',
                    'definition'
                ] and value.get() != '':
                    search_values.update({key: value.get()})
        '''
        search_values = {
            key: value.get()
            for key, value in XsearchTerms.items() if
            key in ['character', 'pin1yin1', 'POS', 'HSK', 'definition']
            and value.get() != ''
        }
        if XsearchTerms == self._Dsearch_results:
            self._Dsearch_results = self._ZH_DB.search_database_DB(search_values)
        else:
            self._Ssearch_results = self._ZH_DB.search_database_DB(search_values)      

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

    def _runQuery(self, event):
        print('BUTT FUNK IS A SUCCESS')

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

        self._XsearchDatabaseUI(self._SsearchTerms)

        '''
        tmp_list = []
        for result in self._Ssearch_results.values():
            tmp_list.append(result)
        '''
        self._shuffledDeck = [result for result in self._Ssearch_results.values()]
        random.shuffle(self._shuffledDeck)
        self._roundInfo['deckLength'].set(len(self._Ssearch_results))
        self._updateCompletion()
        self._SsearchTerms['character'].set('')
        self._SsearchTerms['pin1yin1'].set([])
        self._SsearchTerms['POS'].set('')
        self._SsearchTerms['HSK'].set('')
        self._SsearchTerms['definition'].set('')
        if self._SsearchTerms['langChoice'].get() == 'En':
            self._runQuizEn()
        else:
            self._runQuizZh()
        
       

    def _runQuizEn(self):
        if self._SsearchTerms['langChoice'].get() == 'En':      #TODO Does this if statement do anything? Same in _runQuizZh(self)
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
        if self._SsearchTerms['langChoice'].get() == 'Zh':
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
        elif deckCompletion == self._roundInfo['deckLength'].get() and self._SsearchTerms['langChoice'].get() == 'En':
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
        elif self._SsearchTerms['langChoice'].get() == 'En':
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
