import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number):
    pattern = r"\D"
    # pattern = r'[^0-9\+]'
    num = re.sub(pattern, '', phone_number)
    num = num.removeprefix('38')
    num = num.removeprefix('+38')
    num = num.removeprefix('+3')
    num = num.removeprefix('+')
    num = f"+38{num}"

    return num

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)