import make_notes
import operation


def run():
    notes = {}
    while True:
        command = input("Введите команду \n(для справки: /help) ")
        if command == "/all":  # Печать справочника в консоль
            operation.print_info(notes)
        elif command == "/stop":  # Прерывание программы с записью
            operation.save(notes)
            print("Бот остановил свою работу. Заходите ещё, будем рады!")
            break
        elif command == "/help":  # Вывод мануала
            operation.help_info()
        elif command == "/add":  # Добавление заметки
            make_notes.add_note(notes)
        elif command == "/change":  # Изменение заметки
            make_notes.change_note(notes)
        elif command == "/find":    # Поиск заметки
            make_notes.find_note(notes)
        elif command == "/data":    # Вывод по временному промежутку
            operation.date_selection(notes)
        elif command == "/save":  # Экспорт/Сохранение списка заметок
            operation.save(notes)
        elif command == "/load":  # Импорт/Загрузка списка заметок из хранилища
            operation.load(notes)
        elif command == "/del":  # Удаление заметки из списка
            make_notes.delete_note(notes)
        else:
            print("Неопознанная команда. Просьба изучить мануал через /help")
