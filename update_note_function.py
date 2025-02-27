# Функция обновления заметок

import datetime

def validate_date(date_str):
    try:
        # Определение даты

        datetime.datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False
# Функция обновления

def update_note(note):
    print("===Обновление заметки===")
    print("Текущие данные:")
    for key, value in note.items():
        print(f"{key}: {value}")

    updatable_fields = ["username", "title", "specification", "status", "issue_date"]

    while True:
        field = input(f"\nЧто вы хотите обновить? ({','.join(updatable_fields)}): ").strip().lower()

        if field not in updatable_fields:
            print(f"Ошибка: поле '{field}' не найдено, пожалуйста, выберите поле из списка")
            continue

        if field == "issue_date":
            new_value = input(f"Введите новое значение для {field} (день-месяц-год):").strip()
            if not validate_date(new_value):
                print("Ошибка: Неверный формат даты, используйте формат 'день-месяц-год'.")
                continue
        elif field == "status":

            # Проверка на статус
            pass
        else:
            new_value = input(f"Введите новое значение для {field}: ").strip()
            if not new_value:
                print(f"Ошибка: Значение для {field} не может быть пустым")
                continue

        note[field] = new_value
        print(f"\nЗаметка успешно обновлена: {field} -> {new_value}")

        another_update = input("\nХотите обновить еще одну заметку? (да/нет): ").strip().lower()
        if another_update != "да":
            break


    return note

if __name__ == "__main__":
    note = {
        "username": "Алексей",
        "title": "Список покупок",
        "specification": "Купить продукты на неделю",
        "status": "новая",
        "created_date": "25-01-2024",
        "issue_date": "31-01-2024"
    }

    updated_note = update_note(note)
    print("\nОбновлённая заметка:")
    print(updated_note)