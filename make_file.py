import json
import Note
import os


def write_file(f):
    with open("notes.json", "w", encoding="utf-8") as fw:
        for k, w in f.items():
            w = Note.Note.to_write(w)
            fw.writelines(json.dumps(w, ensure_ascii=False))
        print("Список заметок успешно сохранен в файле notes.json")


def read_file():
    with open("notes.json", "r", encoding="utf-8") as fw:
        if os.stat("notes.json").st_size == 0:
            print("Сохранённых заметок нет")
            return
        else:
            f = fw.read()[1:-1]
    print("Заметки успешно загружены")
    return f

