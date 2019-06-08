import random

def first_last_elements(list1):
    print(f"{list1}\n")
    return print(f"[{list1[0]}, {list1[-1]}]")

listA = random.sample(range(0,87),15)

first_last_elements(listA)
