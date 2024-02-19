import json
import Note


def write_file(f):
    with open("notes.json", "w", encoding="utf-8") as fh:
        for k, w in f.items():
            print(type(w))
            print(w)
            str = Note.Note.to_write(w)
            print(str)
            fh.write(json.dumps(str, ensure_ascii=False))
            #print(str)
            print("Справочник телефонов успешно сохранен в файле phonebook.json")

    

