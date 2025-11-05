from datetime import datetime

def str_to_date(str):
    return datetime.strptime(str, "%Y-%m-%d")

def get_days_from_today(date_str):
    conv_date = str_to_date(date_str)
    today = datetime.now()
    days_count = conv_date.toordinal() - today.toordinal()
    return days_count

print(get_days_from_today("2026-01-01"))

