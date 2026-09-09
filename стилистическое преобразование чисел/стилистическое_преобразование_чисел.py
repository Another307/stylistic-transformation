import datetime

def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_day_of_week(day: int, month: int, year: int) -> str:
    return datetime.date(year, month, day).strftime("%A")

def calculate_age(day: int, month: int, year: int) -> int:
    today = datetime.date.today()
    age = today.year - year
    if (today.month, today.day) < (month, day):
        age -= 1
    return age

def draw_number(num: int) -> list[str]:
    digits = {
        0: [" *** ", "*   *", "*   *", "*   *", " *** "],
        1: ["  *  ", " **  ", "  *  ", "  *  ", " *** "],
        2: [" *** ", "    *", " *** ", "*    ", " *** "],
        3: [" *** ", "    *", " *** ", "    *", " *** "],
        4: ["*   *", "*   *", " *** ", "    *", "    *"],
        5: [" *** ", "*    ", " *** ", "    *", " *** "],
        6: [" *** ", "*    ", " *** ", "*   *", " *** "],
        7: [" *** ", "    *", "    *", "    *", "    *"],
        8: [" *** ", "*   *", " *** ", "*   *", " *** "],
        9: [" *** ", "*   *", " *** ", "    *", " *** "]
    }
    return digits[num]

def draw_date(day: int, month: int, year: int) -> None:
    parts = [day // 10, day % 10, month // 10, month % 10, year // 1000, year % 1000 // 100, year % 100 // 10, year % 10]
    lines = [""] * 5
    for p in parts:
        digit_lines = draw_number(p)
        for i in range(5):
            lines[i] += digit_lines[i] + "  "
    for line in lines:
        print(line)

try:
    d = int(input("День рождения: "))
    m = int(input("Месяц рождения: "))
    y = int(input("Год рождения: "))
    
    print(f"День недели: {get_day_of_week(d, m, y)}")
    print(f"Високосный год: {'Да' if is_leap_year(y) else 'Нет'}")
    print(f"Возраст: {calculate_age(d, m, y)} лет")
    print("Дата в стиле электронного табло:")
    draw_date(d, m, y)
except ValueError:
    print("Ошибка: введите корректные числа.")
except Exception as e:
    print(f"Ошибка: {e}")
