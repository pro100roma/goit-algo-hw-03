from datetime import datetime

def str_to_date(str):
    try:
        return datetime.strptime(str, "%Y-%m-%d")
    except ValueError:
        return None

def get_days_from_today(date_str):
    try:
        conv_date = str_to_date(date_str)
        
        if conv_date is None:
            print(f"Неправильний формат дати '{date_str}'. Потрібен формат YYYY-MM-DD")
            return None
        
        today = datetime.now()
        days_count = conv_date.toordinal() - today.toordinal()
        return days_count
    except Exception as e:
        print(f"Непередбачена помилка: {e}")
        return None


print("Коректний формат:")
print(get_days_from_today("2026-01-01"))

print("\nНеправильний формат (2000.12.12):")
print(get_days_from_today("2000.12.12"))

print("\nНеправильний формат (2024-13-01):")
print(get_days_from_today("2024-13-01"))


