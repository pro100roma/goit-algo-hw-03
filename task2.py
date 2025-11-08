import random

def get_numbers_ticket(min, max, quantity):
    if min < 1:
        return []
    
    if min >= max:
        return []
    
    if quantity > (max - min + 1):
        return []
    
    if quantity < 1:
        return []
    
    rand_list = random.sample(range(min, max + 1), quantity)
    
    rand_list.sort()
    
    return rand_list


print("Коректні дані (1, 49, 6):")
print(get_numbers_ticket(1, 49, 6))

print("\nНекоректні дані (-10, 10, 5) - min < 1:")
print(get_numbers_ticket(-10, 10, 5))

print("\nНекоректні дані (10, 4, 5) - min >= max:")
print(get_numbers_ticket(10, 4, 5))

print("\nНекоректні дані (10, 14, 6) - quantity > доступних чисел:")
print(get_numbers_ticket(10, 14, 6))

print("\nКоректні дані (1, 36, 5):")
print(get_numbers_ticket(1, 36, 5))

        