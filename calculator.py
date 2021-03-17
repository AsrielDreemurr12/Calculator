from tkinter import*
from tkinter.messagebox import*


def about():
    showinfo("О программе", "Было трудно. Но мы это сделали. Март, 2021")


def change_theme(t):
    global btns, a, entry
    if t == 1:
        for i in btns:
            i['bg'] = 'white'
            i['fg'] = 'black'
        a['bg'] = 'silver'
        entry['bg'] = 'white'
        entry['fg'] = 'black'
    elif t == 2:
        for i in btns:
            i['bg'] = 'black'
            i['fg'] = 'white'
        a['bg'] = 'darkgray'
        entry['bg'] = 'gray'
        entry['fg'] = 'white'
    else:
        for i in btns:
            i['bg'] = 'cornsilk'
            i['fg'] = 'chocolate'
        a['bg'] = 'sienna'
        entry['fg']='cornsilk'
        entry['bg'] = '#9966cc'


def setting():    
    b=Tk()
    b.title('Темы')
    b.geometry('220x80+600+100')
    b.resizable(width=False, height=False)
        
    theme=IntVar()    
    b1 = Radiobutton(b, text='Светлая', variable=theme, value=1,
                   width=11, command=lambda t=1: change_theme(t))
    b1.grid(row=0, column=0, sticky=W)
    b1.select()
    
    b2 = Radiobutton(b, text='Тёмная', variable=theme, value=2,
                   width=11, command=lambda t=2: change_theme(t))
    b2.grid(row=1, column=0, sticky=W)
    
    b3 = Radiobutton(b, text='Цветная', variable=theme, value=3,
                   width=11, command=lambda t=3: change_theme(t))
    b3.grid(row=2, column=0, sticky=W)
    b.mainloop()


def main(btn_text):
    global entry
    if btn_text in '0123456789+-*/.()':        
        entry.insert(END, btn_text)
    elif btn_text == '^':
        entry.insert(END, '**')
    elif btn_text == '√':
        entry.insert(END, '**(0.5)')
    elif btn_text == 'x²':
        entry.insert(END, '**2')
    elif btn_text == 'x³':
        entry.insert(END, '**3')
    elif btn_text == 'C':
        entry.delete(0, END)
    elif btn_text == '←':
        entry.delete(len(entry.get())-1)
    elif btn_text == '=':
        try:
            entry.insert(END, '='+str(eval(entry.get())))
        except ZeroDivisionError:
            entry.delete(0, END)
            entry.insert(END, 'На 0 делить нельзя!')
            
        except ValueError:
            showerror("Ошибка", "Недопустимая операция")

        except SyntaxError:
            showerror("Ошибка", "Ошибка в синтаксисе")

        except NameError:
            showerror("Ошибка", "Недопустимые символы!")


a = Tk()
a.title('Калькулятор')
a.iconbitmap('images/icon.ico')
a.resizable(width=False, height=False)

mainmenu = Menu(a)
a.config(menu=mainmenu)

menu1 = mainmenu.add_command(label='О программе', command=about)
menu2 = mainmenu.add_command(label='Настройки', command=setting)

entry = Entry(width='60', bd=3, relief=SUNKEN)
entry.grid(row=0, columnspan=8)

btns_list = list('0123456789()+-*/√.←C=^')
btns_list.append('x²')
btns_list.append('x³') 
btns = []

row = 1
col = 0

for i in range(len(btns_list)):    
    btn = Button(text=btns_list[i], bd=4, width=10)
    btn['command'] = lambda x=btn['text']: main(x)
    btn.grid(row=row, column=col, padx=1, pady=1)
    btns.append(btn)
    col += 1
    if col > 7:
        col = 0
        row += 1
a.mainloop()