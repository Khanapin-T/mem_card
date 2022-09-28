from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QLabel, QPushButton, QButtonGroup
from random import shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('Государственный язык США', 'Американский', 'Английский(United Kingdom)', 'Немецкий', 'Французский'))
questions_list.append(Question('Скольки равен корень из 144', '12', '41', '71', '21'))
questions_list.append(Question('Какого цвета нет на флаге России', 'Зелёный', 'Белый', 'Красный', 'Синий'))
questions_list.append(Question('Сколько дней нужно, чтобы Земля совершила оборот вокруг Солнца', '365', '24', '7', '720'))
questions_list.append(Question('Какой элемент обозначается химическим символом (Fe) в периодической таблице', 'Железо', 'Медь', 'Дубний', 'Феридий'))
questions_list.append(Question('В каком году случился распад Советского Союзa', '1991', '1945', '1816', '2002'))
questions_list.append(Question('Какая самая большая страна в мире', 'Россия', 'США', 'Китай', 'Италия'))
questions_list.append(Question('Сколько игроков в бейсбольной команде', '9', '4', '11', '7'))

app = QApplication([])

window = QWidget()
window.setWindowTitle('Приложение - тест')

btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Самый сложный вопрос в мире!')

RadioGroupBox = QGroupBox('Варианты ответов:')
rbtn1 = QRadioButton('Вариант 1')
rbtn2 = QRadioButton('Вариант 2')
rbtn3 = QRadioButton('Вариант 3')
rbtn4 = QRadioButton('Вариант 4')


RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)


layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnswerGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('Правильно/Неправильно')
lb_Correct = QLabel('True/False')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result)
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)

AnswerGroupBox.setLayout(layout_res)

ResultGroupBox = QGroupBox('Результат теста')
lb_Result1 = QLabel('Правильно/Неправильно')
lb_Correct1 = QLabel('True/False')

layout_res1 = QVBoxLayout()
layout_res1.addWidget(lb_Result1)
layout_res1.addWidget(lb_Correct1, alignment=Qt.AlignHCenter, stretch=2)

ResultGroupBox.setLayout(layout_res1)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(lb_Question, alignment=Qt.AlignCenter)
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnswerGroupBox)
layout_line2.addWidget(ResultGroupBox)

AnswerGroupBox.hide
ResultGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch = 2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

AnswerGroupBox.hide()

def show_result():
    RadioGroupBox.hide()
    AnswerGroupBox.show()
    ResultGroupBox.hide()
    btn_OK.setText('Следующий вопрос')



def show_question():
    RadioGroupBox.show()
    AnswerGroupBox.hide()
    ResultGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)

def show_test_result():
    RadioGroupBox.hide()
    AnswerGroupBox.hide()
    ResultGroupBox.show()
    btn_OK.setText('Начать заново')
    lb_Result1.setText('Завершено')
    lb_Correct1.setText('Результат теста: ' + str(window.points) + ' из ' + str(window.questions))
    lb_Question.hide()
    window.points = 0
    window.questions = 0

answers = [rbtn1, rbtn2, rbtn3, rbtn4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()
    
def check_answer():
    window.cur_question = window.cur_question + 1
    if answers[0].isChecked():
        window.points += 1
        window.questions += 1
        show_correct('Правильно!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            window.questions += 1
            show_correct('Неверно! это:')

def next_question():
    window.cur_question = window.cur_question + 1
    if window.cur_question >= len(questions_list):
        lb_Correct.setText('Вопросы закончились')
        btn_OK.setText('Завершить тест')
        window.cur_question = -1
    else:
        lb_Question.show()
        q = questions_list[window.cur_question]
        ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    elif  btn_OK.text() == 'Завершить тест':
        show_test_result()
    else:
        next_question()

window.points = 0
window.questions = 0
window.setLayout(layout_card)
btn_OK.clicked.connect(click_OK)
window.cur_question = -1
window.resize(400, 200)
next_question()
window.show()
app.exec()