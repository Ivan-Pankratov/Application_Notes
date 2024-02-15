from datetime import datetime
import uuid

class Note:
    # конструктор заметки
    def __init__(self, title, body):
        self.id = str(uuid.uuid1())[0:3]
        self.title = title
        self.body = body
        self.date = str(datetime.now().strftime("%d.%m.%Y %H:%M"))
        print("Создана заметка. id: ", self.id)

# преобразование заметки в строку
    def to_string(note):
        str = ("id: " + note.id + ';'+ " title: " + note.title + ';'
               + " body: " + note.body + ';' + " Date of change: " + note.date)
        return str

# изменение поля заметки
    def change_note(note, item, item_value):
        if (item == "body"):
            note.body = item_value
        elif (item == "title"):
            note.title = item_value
        note.date = str(datetime.now().strftime("%d.%m.%Y %H:%M"))
        print("Заметка id: " + note.id + " изменена")


#    def __del__(self):
#        print("Удалена заметка ", self.name)
