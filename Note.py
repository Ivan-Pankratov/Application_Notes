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

    # преобразование заметки в строку для вывода в консоль
    def to_string(self):
        if isinstance(self, Note):
            str_note = ("id: " + self.id + ';' + " title: " + self.title + ';'
                        + " body: " + self.body + ';' + " Date of change: " + self.date)
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

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_title(self, title):
        self.title = title

    def set_body(self, body):
        self.body= body

    def set_date(self, date):
        self.date= date


#    def __del__(self):
#        print("Удалена заметка ", self.name)
