import tkinter
import codecs
from tkinter import *
from settings import * #Импортируем настройки



app.title(APP_NAME) # Указываем название нашего приложениния
app.minsize(width=WIDTH,  height=HEIGHT)
app.maxsize(width=WIDTH,  height=HEIGHT)

text = tkinter.Text(app, width=WIDTH - 100,  height=HEIGHT, wrap='word') #Создали поле с текстом
scroll = Scrollbar(app, orient=VERTICAL, command=text.yview) #Создали скролл
scroll.pack(side='right', fill='y') #Разместили наш скролл
text.configure(yscrollcommand=scroll.set) #Связь текста с скроллом
text.pack() #Разместили посе с текстом

menuBar = tkinter.Menu(app) #Создание  меню

editor = Text_editor()

app_menu = tkinter.Menu(menuBar) #Выподающие меню у 'файл'
app_menu.add_command(label='Новый Файл', command=editor.new_file)
app_menu.add_command(label='Открыть', command=editor.open_file)
app_menu.add_command(label='Сохранить', command=editor.save_file)
app_menu.add_command(label='Сохранить как', command=editor.save_as_file)

app_menus = tkinter.Menu(menuBar)
app_menus.add_command(label='Приветствие')
app_menus.add_command(label='Документация')
app_menus.add_command(label='О программе')

menuBar.add_cascade(label='Файл', menu=app_menu)
menuBar.add_cascade(label='Справка', menu=app_menus, command=editor.get_info)
menuBar.add_cascade(label='Вид')
menuBar.add_cascade(label='Выход', command=app.quit)


app.config(menu=menuBar) #Публикуем меню


app.mainloop() # Бесконечный цикл нашего приложения

