def reverseString(String):
    newString = String.split(" ",50)
    return print(" ".join(newString[::-1]))

reverseString("My name is Michele")
