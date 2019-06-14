##def collatz(number):
##    if number%2==0:
##        number = number//2
##    elif number%2==1:
##        number = 3 * number + 1
##    print(number)
##    return number if number == 1 else collatz(number)
##
##collatz(3)


def collatz(number):
    if number%2==0:
        number = number//2
    elif number%2==1:
        number = 3 * number + 1
    return number

x = int(input("Enter: "))

while x != 1:
    x = collatz(x)
    print(x)
