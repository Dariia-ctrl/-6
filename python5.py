#import math #підключає бібліотеку
#from math import *
#import statistics as stat #даємо псевдонім стат
#import random
#from datetime import date
#import demo

def text():
    lbl_text['text'] = 'hello world'

def clear(event):
    lbl_text['text'] = ''

from tkinter import *

#print(math.sqrt(81))    #Знаходить корінь

#a = [10, 15, 3, 5, 8, 9]
#print(f"Середній бал: {stat.mean(a)}") #знаходить середнє
#r = int(input('r = '))
#circle_area = round(pi * pow(r, 2) , 2) #два знаки після коми (округлює де перше значення а друге кількість знаків після коми)
#print(circle_area)

#balls = 25
#n = 6
#print(f'Повністю заповнених коробок: {floor(balls / n)}') #округлює до цілого меншого
#print(f'Всього коробок: {ceil(balls / n)}') #округлює до цілого більшого числа

#numbers = []
#for i in range(10):
#    numbers.append(random.randint(1, 100))  #рандомні значення в діапазоні від 1 до 100
#print(f'Випадкові 10 чисел: {numbers}')

#selected = random.choice(numbers)
#print(f'Випадкове число із послідовності: {selected}')
#print(f'Сьогодні: {date.today()}')

#print(demo.square(5))
#print(demo.square(7))
#grades = [12, 5, 7, 9]
#print(demo.average(grades))


#def square(number):
#    return number ** 2

#def is_even(number):
#    return number % 2 == 0

#def average(numbers):
 #   return sum(numbers) / len(numbers)

window = Tk()
window.title('My not first window')
window.geometry('500x300')
window.resizable(width=False, height=False)
window["bg"] = "#00FA9A"
label = Label(window, text="Супер-пупер бебебе", font=('Arial', 18), bg ='#00FA9A', pady = 20)
label.pack()
frame = Frame(window, bg = '#00FA9A')
frame.pack()
bt1 = Button(frame, text = 'OK', width = 7, activebackground = 'Lightgreen', command = text)
bt1.grid(row = 0, column = 1)
bt2 = Button(frame, text = 'Cancel', width = 7, activebackground = 'Lightgreen', command = text)
bt2.grid(row = 0, column = 2, padx = 10)
bt2.bind("<Button-1>", clear)
lbl_text = Label(frame, text= '', font=('Arial', 18), bg='#00FA9A', pady=20)
lbl_text.grid(row=1, column=0, columnspan=3)
#label.place (x = 0 , y = 0)


window.mainloop() #Шоб не закривалось