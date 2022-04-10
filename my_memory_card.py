# -*- mode: python ; coding: utf-8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton, QButtonGroup,
        QPushButton, QLabel)
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2 #ВОПРОСЫ ЖДУТ ТЕБЯ В НАШЕЙ НОВОЙ РАЗРАБОТКЕ!!!!!!!!
        self.wrong3 = wrong3
 
question_list = list()
question_list.append(Question('Когда Путин стал призедентом?', 'в 2000 году', 'в 0000 году', '40 млн. лет до нашей эры', 'в 2020 году'))
question_list.append(Question('Какого цвета нет на флаге России?', 'Зеленого', 'Красного', 'Синего', 'Белого'))
question_list.append(Question('Повар спрашивает ......', 'Повара', 'Милиционера', 'Пожaрного', 'Еду'))
question_list.append(Question('Кирпич', 'Нет блин Путин', 'Камень', 'Ложка', 'Рыжий'))
question_list.append(Question('Что делать если за тобой следят?', 'Смириться', 'Бежать', 'Избить', 'Позвать на помощь'))
question_list.append(Question('6 + 6 = ?', '12', '6', '0', '- 0,000000000000000000001'))
question_list.append(Question('Призидент Америки', 'Путин', 'Трамп', 'Жириновский', 'ЪуЪ'))
question_list.append(Question('Кто сделал ВК?', 'Павел Дуров', 'Марк Цукенберг', 'Стив Джобс', 'Билл Гейтс'))
question_list.append(Question('Русские приложение', 'ВК', 'Инстаграм', 'Фейсбук', 'Ютуб'))
question_list.append(Question('Самый сложный вопрос', 'КОМП', 'КОМП', 'КОМП', 'КОМП'))

app = QApplication([])
 
# Создаем панель вопроса
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Самый сложный вопрос в мире')
 
RadioGroupBox = QGroupBox("Варианты ответов")
 
rbtn_1 = QRadioButton('Вариант1')
rbtn_2 = QRadioButton('0000 году')
rbtn_3 = QRadioButton('2000 году')
rbtn_4 = QRadioButton('2020 году')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
 
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
 
RadioGroupBox.setLayout(layout_ans1)
 
# Создаем панель результата
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') # здесь размещается надпись "правильно" или "неправильно"
lb_Correct = QLabel('ответ будет тут!') # здесь будет написан текст правильного ответа
 
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
 
# Размещаем все виджеты в окне:
layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
# Размещаем в одной строке обе панели, одна из них будет скрываться, другая показываться:
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() # эту панель мы уже видели, скроем, посмотрим, как получилась панель с ответом
 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)
 
# Теперь созданные строки разместим друг под другой:
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым
 
# ----------------------------------------------------------
# Виджеты и макеты созданы, далее - функции:
# ----------------------------------------------------------
def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    ''' показать панель вопросов '''
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)# сняли ограничения, чтобы можно было сбросить выбор радиокнопки
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)# вернули ограничения, теперь только одна радиокнопка может быть выбрана

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

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
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n-Всего вопросов: ', window.total, '/n-Правильных ответов: ', window.score)
        print('Рейтинг', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно!')
            print('Рейтинг', (window.score/window.total*100), '%')

def next_question():
    window.total += 1
    print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)

def click_ok():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')

window.score = 0
window.total = 0
btn_OK.clicked.connect(click_ok)
next_question()
window.resize(400, 300)

window.show()
app.exec()