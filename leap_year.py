#LEAP YEAR EXPLORER
#Task 1: Leap year checker

#FIRST attempt. Forgot the 'divisible by 400' condition.

# year = int(input('Enter a year (YYYY) and I will tell you if its  a leap year: '))

# if year % 4 == 0 and year % 100 != 0:
#     print(year, 'is a leap year')
# else:
#     print(year, 'is not a leap year')

#SECOND attempt. Works fine.

year = int(input('Enter a year (YYYY) and I will tell you if its a leap year: '))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, 'is a leap year')
else:
    print(year, 'is not a leap year')    