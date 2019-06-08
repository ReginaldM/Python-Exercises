import random

numList = random.sample(range(0,25),15)

print(f"numList = {numList} \n\n{[i for i in numList if i<8]}")
