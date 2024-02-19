import json
import Note
from make_file import *


# Печать мануала
def help_info():
    data = open('manual.md', 'r', encoding='utf-8')
    for line in data:
        print(line)
    data.close()


# Добавление заметки
def add_note(f):
    title = input("Введите заголовок: ")
    body = input("Введите текст заметки: ")
    note = Note.Note(title, body)
    f[note.id] = note
    print("Заметка успешно добавлена.")


#  Экспорт/Сохранение заметок
def save(f):
    if (f == {}):
        print("Вы пытаетесь сохранить пустой файл, \n "
              "Попытка перезаписи файла остановлена,\n"
              " т.к. это может привести к потере данных.")
    else:
        write_file(f)


# Изменение заметки
def change_note(f):
    id = input("Введите id заметки для поиска: ")
    if (id in f):
        print(f[id].to_string())
        dt = input("Введите параметр, который хотите поменять: ")
        if ((dt == "body") or (dt == "title")):
            dt_value = input("Введите новое значение : ")
            Note.Note.change_note(f[id], dt, dt_value)
        else:
            print("Ввод параметра не удался ")
    else:
        print("Нет заметки с таким id ")


# Удаление заметки
def delete_note(f):
    id = input("Введите id заметки, которую надо удалить: ")
    try:
        f.pop(id)
        print("Заметка удалена")
    except:
        print("Такой заметки не найдено ")


# Загрузка из файла
def load(f, note=Note):
    fr = read_file()

    print(type(fr))
    to_note(fr, note)
    if (note.Note.get_id() in f):
        print("Заметка из файла уже есть в активном списке")
    else:
        f[note.Note.get_id()]= note
        print("Заметка из хранилища загружена")



# Печать
def print_info(f):
    if (f == {}):
        print("Текущий список заметок пуст \n"
              "добавьте запись или загрузите список из хранилища")
    else:
        for k, w in f.items():
            print(Note.Note.to_string(w))

# Преобразование строки из айла в заметку
def to_note(string_file, note=Note):
    try:
        print(string_file)
        sf = string_file.split(";")
        note.id = sf[0]
        note.title = sf[1]
        note.body = sf[2]
        return note
    except:
        print("Из файла прочитали что-то не то(")
    return
