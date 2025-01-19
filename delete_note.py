# Список заметок с данными
notes = [
    {
        'id': 1,
        'username': 'Виталий',
        'title': 'Список дел',
        'specification': 'Помыть посуду'
    },
    {
        'id': 2,
        'username': 'Андрей',
        'title': 'Работа',
        'specification': 'Выполнить план до конца месяца'
    },
    {
        'id': 3,
        'username': 'Иван',
        'title': 'Устроиться на работу',
        'specification': 'Сходить сегодня на собеседование'
    }
]

# Вывод списка заметок
print("Текущие заметки:")
for note in notes:
    print(f"{note['id']}. Имя: {note['username']}")
    print(f"   Заголовок: {note['title']}")
    print(f"   Описание: {note['specification']}\n")

# Запрос информации для удаления
search_term = input("Введите имя пользователя или заголовок для удаления заметки: ")

# Проверка на пустоту ввода
if not search_term:
    print("Ошибка: критерий для поиска не может быть пустым")
else:
    # Список для хранения заметок, которые нужно оставить
    notes_to_keep = []
    notes_to_delete = []

    # Поиск заметок для удаления
    for note in notes:
        if note['username'] == search_term or note['title'] == search_term:
            notes_to_delete.append(note)
        else:
            notes_to_keep.append(note)

    # Проверка на наличие заметок для удаления
    if not notes_to_delete:
        print("Заметок с таким именем пользователя или заголовком не найдено")
    else:
        # Заметки, которые будут удалены
        print("\nЭти заметки будут удалены:")
        for note in notes_to_delete:
            print(f"{note['id']}, Имя: {note['username']}")
            print(f"   Заголовок: {note['title']}")
            print(f"   Описание: {note['specification']}\n")

        # Подтверждение удаления
        confirm = input("Вы уверены, что хотите удалить эти заметки? (да/нет): ")

        if confirm == 'да':
            # Обновление списка
            notes = notes_to_keep

            # Обновление ID заметок
            for a, note in enumerate(notes, 1):
                note['id'] = a

            # Результат
            print("\nЗаметки успешно удалены")
            if notes:
                print("\n Остались следующие заметки:")
                for note in notes:
                    print(f"{note['id']}, Имя: {note['username']}")
                    print(f"   Заголовок: {note['title']}")
                    print(f"   Описание: {note['specification']}\n")
            else:
                print("Список заметок пуст")
        else:
            print("\nУдаление отменено")






