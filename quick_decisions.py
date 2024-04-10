#THE EVENT PLANNER
#TASK 1: Code Correction

#Buggy Code:
# attendees = input('Enter number of atendees: ')
# venue = 'large hall' if attendees > 100 else 'conference room'
# print(venue)

#Corrected Code. Simple fix and works fine

attendees = int(input('Enter number of atendees: '))    #integer issue
venue = 'large hall' if attendees > 100 else 'conference room'
print(venue)

#TASK 2: Catering Choices

vegetarian = (input('Would you like vegetarian food? yes or no: ')) 
food_option = 'Veggie Delight Caterers' if vegetarian == 'yes' else 'Gourmet Meals Caterers'
print('I recommend', food_option) 