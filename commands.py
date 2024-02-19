import make_notes


def run():
    notes = {}
    while True:
        command = input("Введите команду \n(для справки: /help) ")
        if command == "/all":  # Печать справочника в консоль
            make_notes.print_info(notes)
        elif command == "/stop":  # Прерывание программы с записью
            make_notes.save(notes)
            print("Бот остановил свою работу. Заходите ещё, будем рады!")
            break
        elif command == "/help":  # Вывод мануала
            make_notes.help_info()
        elif command == "/add":  # Добавление заметки
            make_notes.add_note(notes)
        elif command == "/change":  # Изменение заметки
            make_notes.change_note(notes)
        elif command == "/save":  # Экспорт/Сохранение списка заметок
            make_notes.save(notes)
        elif command == "/load":  # Импорт/Загрузка списка заметок из хранилища
            make_notes.load(notes)
        elif command == "/delete":  # Удаление заметки из списка
            make_notes.delete_note(notes)
        else:
            print("Неопознанная команда. Просьба изучить мануал через /help")
