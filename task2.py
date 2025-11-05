import random

def findSmallest(arr):
    sm = arr[0]
    sm_i = 0
    for i in range(1, len(arr)):
        if arr[i] < sm:
            sm = arr[i]
            sm_i = i
    return sm_i

def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        sm = findSmallest(arr)
        new_arr.append(arr.pop(sm))
    return new_arr

def get_numbers_ticket(min, max, quantity=2):
    if min >= max:
        return "Max mast be higher than min"
    if quantity > (max - min):
        return "Quantity can't be higher than difference between max and min"
    rand_list = random.sample(range(min, max), quantity)

    return rand_list

print(selection_sort(get_numbers_ticket(1, 25, 5)))
        