# Добавление заголовков
title_roster = [] # Делаем пустой список для заголовков
title_notes = input("Введите заголовок заметки (или оставьте пустым для завершения):") # Добавляем функцию ввода
while title_notes != "":
    title_roster.append(title_notes)
    title_notes = input("Введите заголовок заметки (или оставьте пустым для завершения):")
    print("Заголовки:")
    title_roster.append(title_notes)
    for title_notes in title_roster:
        print(title_notes)






