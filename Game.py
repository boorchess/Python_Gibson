
print('******ADVENTURE GAME******')
print('You are in a field.')
print('Your friends brought you here for a birthday party, but midway through, you fainted. A few hours later, you wake back up.')
print('Your friends brought you gifts:')
print('A cell phone')
print('A cake')
print('And a map')
print('You both play with the phone and eat the cake.')
print('Feeling adventurous, you decide to explore the area.')
print('From the map, you notice a cave, an old tower, and a mysterious forest path.')
print('Which will you explore?')
print('1: The cave')
print('2: The old tower')
print('3: The mysterious forest path')
choice = input('Enter your choice (1, 2, or 3): ')

if choice == '1':
    print('You decide to explore the cave.')
    print('You go in the cave...')
    print('You go deep in the cave.')
    print('You are LOST!')
    print('And the worst part is:')
    print('YOU CAN\'T FIND ANY GOODIES!')
    print('You have a map!')
    print('It\'s too dark!')
    action = input('Will you use a phone flashlight (F) or run away (R)? ')
    while action == 'F':
        print('The phone is dead!')
        print('You decide to run..')
        print('You see a light. Will you go towards it?')
        willornot = input('KEY: Go towards light (Y) don\'t go towards the light (N) ')
        if willornot == 'Y':
            print('You go towards the light')
            print('You escaped')
            print('*****YOU WIN******')
            break
        else:
            print('You don\'t go towards the light')
            print('Oh no! You fall in a pit!')
            print('******GAME OVER*******')
            break
    if action == 'R':
        print('You run away from the cave...')
        print('Oh no! you fall in a pit!')
        print('******GAME OVER*******')



elif choice == '2':
    print('You decide to explore the old tower.')
    print('As you approach the tower, you notice it’s covered in vines and looks abandoned for centuries.')
    print('Inside, you find a staircase spiraling upwards.')
    print('Do you want to go up the stairs or explore the ground floor first?')
    print('1: Go up the stairs')
    print('2: Explore the ground floor')
    tower_choice = input('Enter your choice (1 or 2): ')

    if tower_choice == '1':
        print('You cautiously climb the stairs.')
        print('At the top, you find a room with an old chest. Do you open it? (Y/N)')
        chest = input('Enter your choice (Y/N): ')
        if chest == 'Y':
            print('You found a treasure! Coins and jewels glitter inside the chest.')
            print('*****YOU WIN!*****')
        else:
            print('You decide not to open the chest. Suddenly, the floor gives way beneath you!')
            print('******GAME OVER******')

    elif tower_choice == '2':
        print('You explore the ground floor and find an old book with mysterious symbols.')
        print('Do you try to read the book? (Y/N)')
        book = input('Enter your choice (Y/N): ')
        if book == 'Y':
            print('As you read, the symbols start to glow! You\'ve unlocked a secret passage.')
            print('You follow the passage and find an exit.')
            print('*****YOU WIN!*****')
        else:
            print('You decide not to read the book. Suddenly, the tower begins to crumble!')
            print('******GAME OVER******')

elif choice == '3':
    print('You decide to walk down the mysterious forest path.')
    print('The path is dense with trees and the sounds of nature surround you.')
    print('As you walk, you find a crossroad: one path leads to a river, the other to a deep, dense part of the forest.')
    print('Which path will you take?')
    print('1: Head towards the river')
    print('2: Venture deeper into the forest')
    forest_choice = input('Enter your choice (1 or 2): ')

    if forest_choice == '1':
        print('You head towards the river and find a boat with a note: "Use me to find a hidden treasure."')
        print('Do you take the boat and search for the treasure? (Y/N)')
        boat = input('Enter your choice (Y/N): ')
        if boat == 'Y':
            print('You row the boat downstream and find an island with a buried treasure.')
            print('*****YOU WIN!*****')
        else:
            print('You decide not to take the boat. Suddenly, the ground shakes and you fall into a hidden pit!')
            print('******GAME OVER******')

    elif forest_choice == '2':
        print('You venture deeper into the forest and come across an ancient ruin.')
        print('Inside, there is a pedestal with a glowing gem. Do you take the gem? (Y/N)')
        gem = input('Enter your choice (Y/N): ')
        if gem == 'Y':
            print('The gem grants you magical powers! You teleport to safety and wealth.')
            print('*****YOU WIN!*****')
        else:
            print('You decide not to take the gem. The ruin collapses around you!')
            print('******GAME OVER******')

else:
    print('Invalid choice. Please restart the game and choose either 1, 2, or 3.')
