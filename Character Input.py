import datetime

currentDate = datetime.date.today().strftime("%Y")


print(currentDate)





##print(currentDate.strftime(' %A %b %d, %Y'))

userInput = input('Please enter your next Birthdate (DD/MM/YYYY): ')

userDoB = datetime.datetime.strptime(userInput,'%d/%m/%Y').date()

##userYear = datetime.datetime.strptime(userInput,'%d/%m/%Y').year()

print(userDoB)

## nextBirthDate = \
##              datetime.datetime.strptime('30/01/2020','%d/%m/%Y').date()

##differenceBwtn = userDoB - currentDate

##print(differenceBwtn)

##testeddate = '4/25/2015'
##dt_obj = datetime.datetime.strptime(testeddate,'%m/%d/%Y')
##print(dt_obj)
