# Функция создания заметок

from datetime import datetime

# Создаем функцию
def create_note():
    # Ввод данных пользователя в заметку
    print("=== Введите данные для создания новой заметки ===")
    # Ввод имени пользователя
    username = input("Введите имя пользователя:").strip()
    while not username:
        print("Не оставляйте имя пользователя пустым")
        username = input("Введите имя пользователя:").strip()

    # Ввод заголовка
    title = input("Введите название заголовка:").strip()
    while not title:
        print("Не оставляйте название заголовка пустым")
        title = input("Введите название заголовка:")

    # Ввод описания
    specification = input("Введите описание заметки:").strip()
    while not specification:
        print("Не оставляйте описание заметки пустым")
        specification = input("Введите описание заметки:")

    # Ввод статуса
    status_options = ["новая", "в процессе", "выполнено"]
    status = input(f"Введите статус заметки ({','.join(status_options)}: ").strip().lower()
    while not status_options:
        print(f"Неверный статус, выберите варианты: {','.join(status_options)}")
        status = input(f"Введите статус заметки ({','.join(status_options)}").strip().lower()

    # Автоматически получаем текущую дату
    created_date = datetime.now().strftime("%d-%m-%Y")

    # Ввод даты дедлайна
    issue_date = input("Введите дату дедлайна, в формате (день-месяц-год): ").strip()
    while not validate_date(issue_date):
        print("Неверный формат даты, используйте предложенный формат")
        issue_date_as_str = input ("Введите дату дедлайна, в формате (день-месяц-год): ").strip()
        issue_date = datetime.strptime(issue_date_as_str, "%d-%m-%Y")

    # Создаем новый словарь
    note = {
        "username": username,
        "title": title,
        "specification": specification,
        "status": status,
        "created_date": created_date,
        "issue_date": issue_date
    }

    # Возврат блокнота
    return note

# Определение даты
def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False

# Разделяем код
if __name__ == "__main__":
    note = create_note()
    print("\nЗаметка создана:")
    print(note)






