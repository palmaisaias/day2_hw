# TASK 1 Original Buggy Code

# place = input("Choose a place: forest or cave? ")

# if place = "forest":  # i think '==' are needed
#     action = input("climb a tree or cross a river?")  #maybe in the wrong place
#     if action = "climb a tree":
#         print("You found a bird's nest!")
#     else action = "cross a river": #else would end the program. must be at end
#         print("You found a boat!")
# elif place = "cave":  #should be after an if statement but before and else statement
#     print("You find a hidden treasure!")

    #FIRST attempt at correcting. Both 'forest' and 'cave' were triggering "action". 
    #Actually any entry is triggering action response

# place = input('Choose a place: forest or cave? ')
# action = input('climb a tree or cross a river? ') #definitely in the wrong place this time

# if place == 'forest':
#     print(action) #removing this
#     if action == 'climb a tree':
#             print('You found a birds nest!')
#     elif action == 'cross a river':
#             print('You found a boat!')
#     else:
#             print('You must chose a designated place') #not sure 'else' is even necessary

# if place == 'cave':
#        print('You found a hidden treasure!')

    #SECOND attempt. Cleaned it up a bit. Could possibly inlude 'else' for user friendliness
    #This one works

place = input('Choose a place: forest or cave? ')

if place == 'forest':
    action = input('climb a tree or cross a river? ')
    if action == 'climb a tree':
            print('You found a birds nest!')
    elif action == 'cross a river':
            print('You found a boat!')
    elif place == 'cave':
           print('You found a hidden treasure')

#TASK 2 SETTING THE SCENE
#Mostly copied and pasted the original action set and filled in the options

place = input('Choose a place: forest or cave? ')

if place == 'forest':
    action = input('climb a tree or cross a river? ')
    if action == 'climb a tree':
            print('You found a birds nest!')
    elif action == 'cross a river':
            print('You found a boat!')
elif place == 'cave':       #Reduced indentation for readability
        action = input('light a torch or proceed in the dark? ')
        if action == 'light a torch':
            print('You see a glimmer in the distance!')
        elif action == 'proceed in the dark':
            print('You cant see much. You hear a sharp click behind you...')
          
# TASK 3 DEFAULT PATH

place = input('Choose a place: forest or cave? ')

if place == 'forest':
    action = input('climb a tree or cross a river? ')
    if action == 'climb a tree':
            print('You found a birds nest!')
    elif action == 'cross a river':
            print('You found a boat!')
    else:  
          pass  #placeholder
elif place == 'cave':  
        action = input('light a torch or proceed in the dark? ')
        if action == 'light a torch':
            print('You see a glimmer in the distance!')
        elif action == 'proceed in the dark':
            print('You cant see much. You hear a sharp click behind you...')
        else:
              pass  #placeholder      