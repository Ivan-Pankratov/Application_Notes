from make_notes import *
from datetime import datetime


# Печать
def print_info(f):
    if f == {}:
        print("Текущий список заметок пуст \n"
              "добавьте запись или загрузите список из хранилища")
    else:
        for k, w in f.items():
            print(Note.Note.to_string(w))


# Загрузка из файла
def load(f):
    fr = read_file()
    arr = fr.split("\"\"")
    for elem in arr:
        note = to_note(elem)
        if f == {}:
            f[note.id] = note
        elif note.id in f:
            print("Заметка из файла уже есть в активном списке")
        else:
            f[note.id] = note


#  Экспорт/Сохранение заметок
def save(f):
    if f == {}:
        print("Вы пытаетесь сохранить пустой файл, \n "
              "Попытка перезаписи файла остановлена,\n"
              " т.к. это может привести к потере данных.")
    else:
        write_file(f)


# Печать мануала
def help_info():
    data = open('manual.md', 'r', encoding='utf-8')
    for line in data:
        print(line)
    data.close()


# Выбор заметок по дате
def date_selection(f):
    global data1, data2
    print("Формат даты: ДД.ММ.ГГГГ ЧЧ:ММ")
    try:
        data1 = datetime.strptime(input("Ведите первую дату "), "%d.%m.%Y %H:%M")
        data2 = datetime.strptime(input("Ведите вторую дату "), "%d.%m.%Y %H:%M")
        for k, w in f.items():
            data_x = datetime.strptime(Note.Note.get_date(w), "%d.%m.%Y %H:%M")
            if (data_x >= data1) and (data_x <= data2):
                print(Note.Note.to_string(w))
    except:
        print("Что-то не вышло, проверьте корректность дат ")
