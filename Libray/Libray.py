from tkinter import *



class Book():
    def __init__(self, title, author, year, is_available):
        self.title = title
        self.author = author
        self.year = year
        self.is_avaibilable = is_available

    def __str__(self):
        return f'{self.title}, {self.author}, {self.year}, {self.is_avaibilable}'

    def borrow_book(self):
        if self.is_avaibilable == 'Доступна':
            self.is_avaibilable = 'Выдана'

    def return_book(self):
        if self.is_avaibilable == 'Выдана':
            self.is_avaibilable = 'Доступна'


class Libray():
    def __init__(self):
        self.books_list = list()

    def __str__(self):
        result = ''
        i = 1
        for book in self.books_list:
            result += f'{str(i)}) {str(book)}\n'
            i+=1
        return  result.strip()

    def add_book(self, book):
        self.books_list.append(book)

    def show_books(self):
        i = 1
        for book in self.books_list:
            if book.is_avaibilable == True:
                print(f'{i}){book.title}, {book.author}, {book.year}')
            i+=1




root = Tk()

lb_text_1 = Label(root, text='Список книг')
lb_text_1.grid(row=0, column=0, columnspan=3)
book_text = Text(root)
book_text.grid(row=1, column=0, columnspan=3)
root.title('Библиотека')

libray = Libray()



lb_title = Label(root, text='Название')
lb_title.grid(row=2, column=0)
ent_title = Entry(root, width=35)
ent_title.grid(row=3, column=0)

with open("Libray.txt", 'r', encoding='utf-8') as file_book:
    listik = list(file_book.readlines())
    for book in listik:
        book = book.rstrip().split(',')
        book_class = Book(book[0],book[1],book[2],book[3])
        libray.add_book(book_class)

lb_author = Label(root, text='Автор')
lb_author.grid(row=2, column=1)
ent_author = Entry(root, width=35)
ent_author.grid(row=3, column=1, pady = 5)
lb_year = Label(root, text='Год')
lb_year.grid(row=2, column=2)
ent_year = Entry(root, width=35)
ent_year.grid(row=3, column=2, pady = 5)

def append_libray():
    book_text.config(state='normal')
    title_book = ent_title.get()
    author_book = ent_author.get()
    year_book = ent_year.get()
    new_book = Book(title_book, author_book, year_book, is_available='Доступна')
    libray.add_book(new_book)
    book_text.delete(1.0, END)
    book_text.insert(END, str(libray))
    book_text.config(state='disabled')
    with open('Libray.txt', 'a', encoding='utf-8') as file:
        s = f'{title_book},{author_book},{year_book},Доступна\n'
        file.write(s)

btn = Button(root, text='Добавить книгу', command=append_libray, width=30)
btn.grid(row=4, column=0, pady = 5)
book_text.insert(END, str(libray))
book_text.config(state='disabled')

ent_brown = Entry(root, width=35)
lb_title2 = Label(root, text='Название')
lb_title2.grid(row=5, column=0)
ent_brown.grid(row=6, column=0, pady = 5)
def book_brown():
    book_text.config(state='normal')
    title_book_brown = ent_brown.get()
    listik = libray.books_list
    for book in listik:
        if book.title == title_book_brown:
            book.borrow_book()
    book_text.delete(1.0, END)
    book_text.insert(END, str(libray))
    book_text.config(state='disabled')

btn_brown = Button(root, text='Взять книгу', command=book_brown, width=30)
btn_brown.grid(row=7, column=0, pady = 5)
lb_title3 = Label(root, text='Название')
lb_title3.grid(row=8, column=0)
ent_return = Entry(root, width=35)
ent_return.grid(row=9, column=0, pady = 5)

def return_book():
    book_text.config(state='normal')
    title_book_return = ent_return.get()
    listik = libray.books_list
    for book in listik:
        if book.title == title_book_return:
            book.return_book()
    book_text.delete(1.0, END)
    book_text.insert(END, str(libray))
    book_text.config(state='disabled')

btn_return = Button(root, text='Вернуть книгу', command=return_book, width=30)
btn_return.grid(row=10, column=0, pady = 5)
lb_text_2 = Label(root, text='Фильтрация')
lb_text_2.grid(row=0, column=3, columnspan=3, pady = 5)
book_filter = Text(root, state='disabled')
book_filter.grid(row=1, column=3, columnspan=3, pady = 5)
var = IntVar(value=0)
lb_filter1 = Label(root, text='Выбор фильтра')
lb_filter1.grid(row=2,column=3, pady = 5)
radiobut1= Radiobutton(root, text='Фильтрация по названию', variable=var, value=1)
radiobut2= Radiobutton(root, text='Фильтрация по автору', variable=var, value=2)
radiobut3= Radiobutton(root, text='Фильтрация по году', variable=var, value=3)
radiobut1.grid(row=3, column=3, pady = 5, padx = 5, sticky="w")
radiobut2.grid(row=4, column=3, pady = 5, padx = 5, sticky="w")
radiobut3.grid(row=5, column=3, pady = 5, padx = 5, sticky="w")
lb_filter_2 = Label(root, text='Введите фильтр')
lb_filter_2.grid(row=3, column=4, pady = 5)
ent_filter = Entry(root, width=35)
ent_filter.grid(row=4, column=4, pady = 5)

def filter_book():
    book_filter.config(state="normal")
    value = var.get()
    listik = libray.books_list
    libray_filter = Libray()
    filter_v = ent_filter.get()
    if value == 1:
        for book in listik:
            if book.title == filter_v:
                libray_filter.add_book(book)
    elif value == 2:
        for book in listik:
            if book.author == filter_v:
                libray_filter.add_book(book)
    elif value == 3:
        for book in listik:
            if book.year == filter_v:
                libray_filter.add_book(book)
    book_filter.delete(1.0, END)
    book_filter.insert(END, str(libray_filter))
    book_filter.config(state="disabled")

btn_filter = Button(root, text='Фильтровать', command=filter_book, width=30)
btn_filter.grid(row=5, column=4, pady = 5)



root.mainloop()