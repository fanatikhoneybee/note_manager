username = input("Введите имя пользователя:")
content = input ("Введите описание заметки:")
status = input("Введите статус заметки:")
created_date = input ("Ведите дату создания заметки (в формате дд.мм.гг.):")
issue_date = input ("Введите дату истечения заметки (в формате дд.мм.гг.):")
title1 = input("Введите заголовок заметки:")
title2 = input("Введите заголовок заметки:")
title3 = input ("Введите заголовок заметки:")
title_roster= [title1, title2, title3]
note = [username, content, status, created_date[0:10],issue_date[0:10], title_roster]
print(note)