#Ülesannne 1
try:
    number = float(input("Введите число: "))
    
    if number > 0:
        print("Число положительное.")
        
        if int(number) == number:  
            if int(number) % 2 == 0:
                print("Число четное.")
            else:
                print("Число нечетное.")
        else:
            print("Число не является целым, поэтому четность/нечетность не проверяется.")
    elif number < 0:
        print("Число отрицательное.")
    else:
        print("Число равно нулю.")
except ValueError:
    print("Ошибка! Пожалуйста, введите корректное число.")

# Ülesanne 2
try:
    угол1 = float(input("Введите первый угол: "))
    угол2 = float(input("Введите второй угол: "))
    угол3 = float(input("Введите третий угол: "))
    
    if угол1 > 0 and угол2 > 0 and угол3 > 0:
        if угол1 + угол2 + угол3 == 180:
            print("Углы могут быть углами треугольника.")
            
            if угол1 == угол2 == угол3:
                print("Это равносторонний треугольник.")
            elif угол1 == угол2 or угол2 == угол3 or угол1 == угол3:
                print("Это равнобедренный треугольник.")
            else:
                print("Это разносторонний треугольник.")
        else:
            print("Углы не могут быть углами треугольника, так как их сумма не равна 180.")
    else:
        print("Все углы должны быть положительными.")
except ValueError:
    print("Ошибка! Пожалуйста, введите корректные числа.")

# Ülesanne 3

def day_of_week(number):
    days = {
        1: "Понедельник",
        2: "Вторник",
        3: "Среда",
        4: "Четверг",
        5: "Пятница",
        6: "Суббота",
        7: "Воскресенье"
    }
    return days.get(number, None)

answer = input("Хотите расшифровать порядковый номер дня недели? (да/нет): ").strip().lower()

if answer == "да":
    try:
        number = int(input("Введите число от 1 до 7: "))
        
        if 1 <= number <= 7:
            print(f"Это {day_of_week(number)}.")
        else:
            print("Ошибка! Число должно быть от 1 до 7.")
    except ValueError:
        print("Ошибка! Пожалуйста, введите корректное число.")
else:
    print("Хорошо, всего доброго!")

# Ülesanne 4

def zodiac_sign(day, month):
    if month == 1:
        return "Козерог" if day <= 19 else "Водолей"
    elif month == 2:
        return "Водолей" if day <= 18 else "Рыбы"
    elif month == 3:
        return "Рыбы" if day <= 20 else "Овен"
    elif month == 4:
        return "Овен" if day <= 19 else "Телец"
    elif month == 5:
        return "Телец" if day <= 20 else "Близнецы"
    elif month == 6:
        return "Близнецы" if day <= 20 else "Рак"
    elif month == 7:
        return "Рак" if day <= 22 else "Лев"
    elif month == 8:
        return "Лев" if day <= 22 else "Дева"
    elif month == 9:
        return "Дева" if day <= 22 else "Весы"
    elif month == 10:
        return "Весы" if day <= 22 else "Скорпион"
    elif month == 11:
        return "Скорпион" if day <= 21 else "Стрелец"
    elif month == 12:
        return "Стрелец" if day <= 21 else "Козерог"
    else:
        return None  

try:
    day = int(input("Введите день вашего рождения (1-31): "))
    month = int(input("Введите месяц вашего рождения (1-12): "))

    if 1 <= month <= 12:
        if 1 <= day <= 31:
            if (month == 2 and day > 29) or (month in [4, 6, 9, 11] and day > 30):
                print("Некорректный день для указанного месяца.")
            else:
                sign = zodiac_sign(day, month)
                print(f"Ваш знак зодиака: {sign}.")
        else:
            print("День должен быть в диапазоне от 1 до 31.")
    else:
        print("Месяц должен быть в диапазоне от 1 до 12.")
except ValueError:
    print("Ошибка! Пожалуйста, введите корректные числовые значения.")

