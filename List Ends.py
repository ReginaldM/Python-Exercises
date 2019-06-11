import random

def first_last_elements(list1):
    return print(f"{list1} \n[{list1[0]}, {list1[-1]}]")

listA = random.sample(range(0,87),19)

first_last_elements(listA)
