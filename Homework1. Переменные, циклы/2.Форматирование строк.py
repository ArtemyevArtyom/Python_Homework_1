# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите
# в формате чч:мм:сс. Используйте форматирование строк.
seconds = int(input("Введите время в секундах: "))
minutes = seconds / 60
hours = seconds / 3600
print(f"Время в формате чч:мм:сс: {hours:.2f} : {minutes:.2f} : {seconds}")