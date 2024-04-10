#TASK 1: IDENTIFY THE GREATEST
    #FIRST attempt. Failed miserably lol.
 
# print('This program will have you select 3 numbers and tell you which one is the largest...hopefully')
# print()
# first_num = int(input('Enter first number: '))
# second_num = int(input('Enter second number: '))
# third_num = int(input('Enter third numbers: '))

# if first_num > second_num > third_num:
#     print('The largest number is', first_num)
# elif second_num > first_num > third_num:
#     print('The largest number is', second_num)
# elif third_num > first_num > second_num:
#     print('The largest number is', third_num)

    #SECOND attempt. Did not work. Super buggy especailly when all numbers entered are equal. 
    #Outputs incorrect numbers, my math is wrong.

# print('This program will have you select 3 numbers and tell you which one is the largest...hopefully')
# print()
# first_num = int(input('Enter first number: '))
# second_num = int(input('Enter second number: '))
# third_num = int(input('Enter third numbers: '))

# if first_num > second_num and third_num:
#     print('The largest number is', first_num)
# elif second_num > first_num and third_num:
#     print('The largest number is', second_num)
# elif third_num > first_num and second_num:
#     print('The largest number is', third_num)

    #THIRD attempt. Changed '>' to '>=' in order to fix equal number issue.
    #I was unable to produce any incorrect responses. Works fine.

print('This program will have you select 3 numbers and tell you which one is the LARGEST...hopefully')
print()
first_num = int(input('Enter first number: '))
second_num = int(input('Enter second number: '))
third_num = int(input('Enter third numbers: '))

if first_num >= second_num and first_num >= third_num:
    print('The largest number is', first_num)
elif second_num >= first_num and second_num >= third_num:
    print('The largest number is', second_num)
elif third_num >= first_num and third_num >= second_num:
    print('The largest number is', third_num)

#TASK 2: IDENTIFY THE SMALLEST
#Converted '>=' to '<='. No issues

print('This program will have you select 3 numbers and tell you which one is the SMALLEST...hopefully')
print()
first_num = int(input('Enter first number: '))
second_num = int(input('Enter second number: '))
third_num = int(input('Enter third numbers: '))
    #reversed the functions here. Changed '>=' to '<='
if first_num <= second_num and first_num <= third_num:      
    print('The smallest number is', first_num)
elif second_num <= first_num and second_num <= third_num:
    print('The smallest number is', second_num)
elif third_num <= first_num and third_num <= second_num:
    print('The smallest number is', third_num)

#BONUS...attempt
    #FIRST  attempt. Not even sure why I thought this would work. It does not.

# print('This program will have you select 3 numbers and tell you which one is the SMALLEST and the LARGEST...hopefully')
# print()
# first_num = int(input('Enter first number: '))
# second_num = int(input('Enter second number: '))
# third_num = int(input('Enter third numbers: '))
    
# if first_num <= second_num and first_num <= third_num:      
#     print('The smallest number is', first_num)
# elif first_num >= second_num and first_num >= third_num:
#         print('The largest number is', first_num)
# elif second_num <= first_num and second_num <= third_num:
#     print('The smallest number is', second_num)
# elif second_num >= first_num and second_num >= third_num:
#         print('The largest number is', second_num)
# elif third_num <= first_num and third_num <= second_num:
#     print('The smallest number is', third_num)
# elif third_num >= first_num and third_num >= second_num:
#         print('The largest number is', third_num)

    #SECOND attempt.
    #Works fine but output verbiage is incorrect. Don't know how to fix it but will try to change the verbiage that prints.

# print('This program will have you select 3 numbers and tell you which one is the SMALLEST and the LARGEST...hopefully')
# print()
# first_num = int(input('Enter first number: '))
# second_num = int(input('Enter second number: '))
# third_num = int(input('Enter third numbers: '))

# if first_num >= second_num and first_num >= third_num:
#     print('The largest number is', first_num)
# elif second_num >= first_num and second_num >= third_num:
#     print('The largest number is', second_num)
# elif third_num >= first_num and third_num >= second_num:
#     print('The largest number is', third_num)

# if first_num <= second_num and first_num <= third_num:      
#     print('The smallest number is', first_num)
# elif second_num <= first_num and second_num <= third_num:
#     print('The smallest number is', second_num)
# elif third_num <= first_num and third_num <= second_num:
#     print('The smallest number is', third_num)

    #THIRD attempt
    #it KINDA prints like the format requested lol but I just know there's a cleaner way.
    #Happy with my attempts.

print('This program will have you select 3 numbers and tell you which one is the LARGEST and the SMALLEST...hopefully')
print()
first_num = int(input('Enter first number: '))
second_num = int(input('Enter second number: '))
third_num = int(input('Enter third numbers: '))

if first_num >= second_num and first_num >= third_num:
    print('The largest number is', first_num)
elif second_num >= first_num and second_num >= third_num:
    print('The largest number is', second_num)
elif third_num >= first_num and third_num >= second_num:
    print('The largest number is', third_num)

if first_num <= second_num and first_num <= third_num:      
    print('and the smallest number is', first_num)
elif second_num <= first_num and second_num <= third_num:
    print('and the smallest number is', second_num)
elif third_num <= first_num and third_num <= second_num:
    print('and the smallest number is', third_num)