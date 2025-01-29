# Функция для поиска заметок

# Создаем функцию для поиска заметок
def search_notes(notes, keyword=None, status=None):
    # Список ключей из словаря заметки
    fields_for_search = ["username", "specification", "title"]
    # Пустой список для найденных заметок
    found_notes = []

    # Цикл проверки введенного значения в существующих заметках
    for note in notes:
        keyword_criteria = True
        status_criteria = True

        if keyword is not None:
            for field in fields_for_search:
                if note[field] == keyword:
                    keyword_criteria = True
                else:
                    keyword_criteria = False
        if status is not None:
            if note["status"] == status:
                status_criteria = True
            else:
                status_criteria = False
        # Если значения обнаружены в существующих заметках, то перемещаем их в список найденных заметок
        if keyword_criteria == True and status_criteria == True:
            found_notes.append(note)

    # Список найденных заметок
    return found_notes

if __name__ == '__main__':
    notes = [
        {'username': 'Алексей', 'title': 'Список покупок', 'specification': 'Купить продукты на неделю', 'status': 'новая',
         'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
        {'username': 'Мария', 'title': 'Учеба', 'specification': 'Подготовиться к экзамену', 'status': 'в процессе',
         'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
        {'username': 'Иван', 'title': 'План работы', 'specification': 'Завершить проект', 'status': 'выполнена',
         'created_date': '20-11-2024', 'issue_date': '26-11-2024'}
    ]
    print("=" * 13)
    print("Поиск заметок")
    print("=" * 13)
    print('''
Выберите критерий для поиска, необходимо ввести число (1, 2, 3):
1 - поиск по ключевому слову; 
2 - поиск по статусу; 
3 - поиск по обоим критериям (ключевое слово и статус).
Для выхода из поиска оставьте поле пустым.
''')
    # Цикл ввода данных от пользователя
    while True:
        value_for_search = input("Введите число от 1 до 3, либо оставьте поле пустым для выхода: ").strip()
        # Проверка для ввода десятичного числа
        if value_for_search.isdecimal():
            value_for_search = int(value_for_search)
        # Если поле оставлено пустым, идет завершение цикла
        if not value_for_search:
            print("Поиск заметок завершен")
            break

        elif value_for_search == 1:
            # Запрос ввода ключевого слова для поиска
            word_search = input('Введите ключевое слово: ').strip()
            # Поиск введенных данных
            found_notes = search_notes(notes, keyword=word_search)

        elif value_for_search == 2:
            # Запрос ввода статуса для поиска
            status_search = input('Введите статус (новая, в процессе, выполнена): ').strip().lower()
            # Список возможных статусов
            variable_status = ["новая", "в процессе", "выполнена"]
            # Обработка неправильного ввода
            while status_search not in variable_status:
                print(f"Ошибка ввода! Статус {status_search} не найден.")
                status_search = input('Введите статус (новая, в процессе, выполнена): ').strip().lower()
            # Поиск статуса в статусах существующих заметок
            found_notes = search_notes(notes, status=status_search)

        elif value_for_search == 3:
            # Запрашиваем ввод двух критериев
            word_search = input('Введите ключевое слово: ').strip()
            status_search = input('Введите статус (новая, в процессе, выполнена): ').strip().lower()
            # Поиск в существующих заметках по двум критериям
            found_notes = search_notes(notes, keyword=word_search, status=status_search)

        # Обработка ввода других значений
        else:
            # Сообщение об ошибке с возможным выбором
            print('''
Ошибка ввода, необходимо ввести число от 1 до 3.
Повторите ввод, либо оставьте поле пустым что бы завершить поиск заметок
''')
            # Откат в начало цикла
            continue
        # Если заметки не найдены и список заметок пуст, то выводим следующее сообщение
        if found_notes == []:
            print("=" * 20)
            print(" Заметка не найдена")
            print("=" * 20)
        # Если заметки найдены, выводим на экран
        else:
            print("\n" + "=" * 38)
            print("По вашему запросу найдены следующие заметки")
            print("=" * 38)
            for i in found_notes:
                print(f"""
Имя пользователя: {i['username']}
Заголовок: {i['title']}
Содержание: {i['specification']}
Статус: {i['status']}
Дата создания: {i['created_date']}
Дедлайн: {i['issue_date']}
""")
                print("=" * 62)