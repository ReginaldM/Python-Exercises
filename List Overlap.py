import random

def commonNumbers(list1,list2):
    print(f"List A = {listA} \n\nList B = {listB} \n\n")
    return f"{set(list1) & set(list2)}"
##    return f"{set(list1).intersection(set(list2))}"


listA = random.sample(range(1,100),50)
listB = random.sample(range(1,100),20)


print("Common matches: " + commonNumbers(listA,listB))
