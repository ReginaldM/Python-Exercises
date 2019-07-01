import random

mIn = 1
mAx = 100

while True:
    ranum = random.randint(mIn,mAx)
    print(f"\n{ranum} \n")
    useR = input("Type 'exit' to quit. \nEnter: ").upper()
    if useR == 'exit':
        break
    elif useR == "CORRECT":
        print("Thank you!")
        break
    elif useR == "TOO LOW":
        mIn = ranum + 1
    elif useR == 'TOO HIGH':
        mAx = ranum - 1
    else:
        print("Sorry, I didn't understand")
        
