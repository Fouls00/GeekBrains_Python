# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

# Создание исходных переменных по определению
time = int(input("Введите время в секундах:"))
time_hour = int((time / 3600))
time_minute = int(abs(time_hour * 60 - time / 60))
time_sec = int(abs(time - time_hour * 3600 - time_minute * 60))

# Вывод времени в формате чч:мм:сс
print(f" Время: {time_hour:02d}:{time_minute:02d}:{time_sec:02d}")

