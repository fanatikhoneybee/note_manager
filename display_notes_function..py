# Функция отображения заметок

# Функция создания страниц, на одной странице по 3 заметки
def display_page(notes, page):
    start_index = 0 + page * 3 # Первая страница
    end_index = 3 + page * 3 # Вторая страница

# Функция для нумерации заметок
    for index, note in enumerate(notes[start_index:end_index], start=1):  # f строки f string
        print(f"""
        Номер заметки: {index}
        Имя пользователя: {note["username"]}
        Заголовок: {note["title"]}
        Описание: {note["specification"]}
        Статус: {note["status"]}
        Дата создания: {note["create_date"]}
        Дедлайн: {note["issue_date"]}
        """)
        # Разделение заметок на группы
        print("=" * 45)

# Функция отображения заметок
def display_notes(notes, page_number=0):
    # Проверка на пустой список заметок
    if len(notes) == 0:
        print("Список заметок пуст.")
    else:
        display_page(notes, page_number)

# Список заметок

if __name__ == '__main__':
    notes = [
        {"username": "Алексей", "title": "Список покупок", "specification": "Купить продукты на неделю",
         "status": "новая","create_date": "27-01-2025", "issue_date": "31-01-2025" },
        {"username": "Мария", "title": "Учеба", "specification": "Подготовиться к экзамену",
         "status": "новая","create_date": "27-01-2025", "issue_date": "31-01-2025"},
        {"username": "Валерия", "title": "Отдых", "specification": "Дождаться конца недели",
         "status": "новая","create_date": "27-01-2025", "issue_date": "02-02-2025"},
        {"username": "Иван", "title": "Планы", "specification": "Устроиться на работу",
         "status": "новая","create_date": "27-01-2025", "issue_date": "31-01-2025"},
        {"username": "Павел", "title": "Ремонт", "specification": "Починить крышку бака",
         "status": "новая","create_date": "27-01-2025", "issue_date": "31-01-2025"},
        {"username": "Михаил", "title": "Дисциплина", "specification": "Бросить курить",
         "status": "новая","create_date": "27-01-2025", "issue_date": "31-12-2025"},
    ]
    # Первая страницу списка
    display_notes(notes=notes, page_number=0)

    # Вторая страница списка
    display_notes(notes=notes, page_number=1)