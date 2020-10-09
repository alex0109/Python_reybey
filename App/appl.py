from tkinter import *
from tkinter import messagebox as mb

window = Tk()

def btn_click():
    login = loginInput.get()
    password = passField.get()

    info_str = f'Данные: {str(login)}, {str(password)}'
    mb.showinfo(title='Название', message=info_str)

    #окно с ошибкой
    #mb.showerror(title='', message='Error always!!!')

window['bg'] = '#fafafa'
window.title("Reybey's application")
window.geometry('500x500')
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

canvas = Canvas(window, height=500, width=500)
canvas.grid()

frame = Frame(window, bg='red')
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

title = Label(frame, text='Текст подсказка', bg='gray', font='40')
title.grid()
btn = Button(frame, text='Кнопка', bg='yellow', command=btn_click)
btn.grid()

loginInput = Entry(frame, bg='green')
loginInput.grid()

passField = Entry(frame, bg='white', show='*')
passField.grid()

window.mainloop()