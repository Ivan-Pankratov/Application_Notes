from datetime import datetime
import uuid


class Note:

    # конструктор заметки
    def __init__(self, i=str(uuid.uuid1())[0:3], title="text", body="text",
                 date=str(datetime.now().strftime("%d.%m.%Y %H:%M"))):
        self.id = i
        self.title = title
        self.body = body
        self.date = date

    # преобразование заметки в строку для вывода в консоль
    def to_string(self):
        if isinstance(self, Note):
            str_note = ("id: " + self.id + ';' + " title: " + self.title + ';'
                        + " body: " + self.body + ';' + " date of change: " + self.date)
            return str_note
        print("Попытка преобразовать в строку объект отличный от Заметки")
        return

    # Преобразование заметки в строку для записи в файл
    def to_write(self):
        str_note = self.id + ';' + self.title + ';' + self.body + ';' + self.date
        return str_note

    # изменение поля заметки
    def change_note(self, item, item_value):
        if item == "body":
            self.body = item_value
        elif item == "title":
            self.title = item_value
        self.date = str(datetime.now().strftime("%d.%m.%Y %H:%M"))
        print("Заметка id: " + self.id + " изменена")

    def set_id(self):
        self.id = str(uuid.uuid1())[0:3]

    def get_id(self):
        return self.id

    def get_date(self):
        return self.date

#    def __del__(self):
#        print("Удалена заметка ", self.name)
