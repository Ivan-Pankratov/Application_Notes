from make_file import *


# Добавление заметки
def add_note(f):
    title = input("Введите заголовок (без ';'): ")
    body = input("Введите текст заметки (без ';'): ")
    if good_text(title) < 0:
        if good_text(body) < 0:
            note = Note.Note(title=title, body=body)
            while Note.Note.get_id(note) in f:
                Note.Note.set_id(note)
            f[note.id] = note
            print("Заметка успешно добавлена.")
    else:
        print("Проверьте корректность введенных данных, пожалуйста, где-то ошибка ")


# Изменение заметки
def change_note(f):
    i = input("Введите id заметки для поиска: ")
    if i in f:
        print(f[i].to_string())
        dt = input("Введите параметр, который хотите поменять: ")
        if (dt == "body") or (dt == "title"):
            dt_value = input("Введите новое значение (без \";) : ")
            if good_text(dt_value) < 0:
                Note.Note.change_note(f[i], dt, dt_value)
            else:
                print("Ввод значения не удался ")
        else:
            print("Ввод параметра не удался ")
    else:
        print("Нет заметки с таким id ")


# Поиск заметки
def find_note(f):
    i = input("Введите id заметки, которая интересует: ")
    print(f[i].to_string())


# Удаление заметки
def delete_note(f):
    i = input("Введите id заметки, которую надо удалить: ")
    try:
        f.pop(i)
        print("Заметка удалена")
    except:
        print("Такой заметки не найдено ")


# Преобразование строки из файла в заметкb
def to_note(string_file):
    try:
        sf = string_file.split(";")
        note = Note.Note(sf[0], sf[1], sf[2], sf[3])
        return note
    except:
        print("Из файла прочитали что-то не то(")
    return


def good_text(f):
    return f.find(";")
