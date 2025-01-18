from datetime import datetime, date

# Определение текущей даты
today = date.today() # Получение текущей даты с помощью оператора .today
current_date = today.strftime('%d-%m-%Y') # Преобразование даты в требуемый формат
print("\nТекущая дата: ", current_date, "\n") # Вывод на экран текущей даты в нужном формате

# Ввод и проверка дедлайна
while True: # Цикл проверки правильного формата
    try:
        Issue_date = input(f'Введите дедлайн в формате "день-месяц-год": ')
        datetime.strptime(Issue_date,"%d-%m-%Y")  # Если строка (Issue_date) и код формата (%d-%m-%Y),
        # не совпадают, возникает ошибка ValueError.
        break  # выход из цикла
    except ValueError:  # обработка ошибки
        print("Дата некорректна, повторите ввод дедлайна в требуемом формате.")
print('\nДедлайн:', Issue_date, "\n")  # вывод дедлайна в требуемом формате

# Анализ и обработка дедлайна
deadline = datetime.strptime(Issue_date,"%d-%m-%Y")  # преобразование дедлайна в формат datetime
deadline = deadline.date()  # преобразование дедлайна в формат date
delta = deadline - today  # получение дельты м/у дедлайна и текущей датой в формате класса timedelta
day = delta.days  # получение дельты м/у дедлайна и текущей датой в днях с помощью аргумента .day класса timedelta
if day > 0:
    print(f"До дедлайна осталось {day} дн.")
elif day == 0:
    print("Внимание дедлайн истекает сегодня.")
else:
    day = day * -1  # делаем положительной дельту для вывода на экран
    print(f"Внимание дедлайн истек {day} дн. назад!")