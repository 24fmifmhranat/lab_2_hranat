import datetime

# Словничок смайликів за днем тижня
emoji_by_day = {
    "Monday": ">:(",       # Дуже злий
    "Tuesday": ":-/",      # Трохи добріший
    "Wednesday": ":-|",    # Нейтральний
    "Thursday": ":-)",     # Майже веселий
    "Friday": ":-D",       # Веселий
    "Saturday": "^_^",     # Дуже веселий
    "Sunday": ":-("        # Засмучений
}

# Отримуємо день тижня
today = datetime.datetime.today().strftime("%A")

# Результат
print("Hello from Docker!")
print(f"Сьогодні {today} — настрій: {emoji_by_day.get(today, '🤔')}")
