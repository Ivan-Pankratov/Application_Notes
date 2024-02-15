import json
import Note



# Печать мануала
def help_info():
    path = 'manual.json'
    data = open('manual.json', 'r', encoding='utf-8')
    for line in data:
        print(line)
    data.close()

# Добавление заметки
def add_note(f):
    title = input("Введите заголовок: ")
    body = input("Введите текст заметки: ")
    note = Note.Note(title, body)
    str = note.to_string()
    f[note.id] = note
    print("Заметка успешно добавлена.")


#  Экспорт/Сохранение заметок
def save(f):
    if f== {}:
        print("Вы пытаетесь сохранить пустой файл, \n "
              "Попытка перезаписи файла остановлена,\n"
              " т.к. это приведёт к потере данных.")
    else:
        with open("notes.json", "w", encoding="utf-8") as fh:
            fh.write(json.dumps(f, ensure_ascii=False))
        print("Справочник заметок успешно сохранен в файле notes.json")


# Изменение заметки
def change_note(f):
    id = input("Введите id заметки для поиска: ")
    if id in f:
        print(f[id].to_string())
        dt = input("Введите параметр, который хотите поменять: ")
        if (dt== "body")or (dt== "title") :
            dt_value = input("Введите новое значение : ")
            Note.Note.change_note(f[id], dt, dt_value)
        else:print("Ввод параметра не удался ")
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
def load(f):
    with open("note.json", "r", encoding="utf-8") as fh:
        f = json.load(fh)
    print("Заметки успешно загружены")
    return f


# Печать
def print_info(f):
    if (f == {}):
        print("Текущий список заметок пуст \n"
              "добавьте запись или загрузите список из хранилища")
    else:
        for k, w in f.items():
            print(w.to_string())
