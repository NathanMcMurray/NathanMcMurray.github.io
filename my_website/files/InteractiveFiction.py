import sys

def A1RightA2Climb():
    print('They notice you and come down to get you')
    choice6 = raw_input('Do you tell them where you are from? (Yes/No)')
    if choice6 == 'Yes':
        print('They have a prejudiced against your city')
        print('They land in the middle of nowhere and force you out of the helicopter')
        print('Congrats, you played yourself')
        Restart()
        sys.exit()
    if choice6 == 'No':
        print('They take you to a city and help you get to an airport')
        print('You call your family and have them send you the money to buy a ticket home')
        print('You get back to them, but they are mad that you made them spend money on a ticket because you went on an adventure and got lost')
        Restart()
        sys.exit()
            
def A1Right():
    Restart()
    print('You are walking through some hills')
    print('There is a helicopter above you')
    print('You want to try and get its attention')
    choice5 = raw_input('How do you try? (Flail your arms/Climb a hill)')
    if choice5 == 'Flail your arms':
        print('You just make yourself tired. They did not see you.')
        print('You have wasted your only opportunity')
        print('You are now lost in the hills and to tired to go anywhere')
        Restart()
        sys.exit()
    if choice5 == 'Climb a hill':
        A1RightA2Climb()
            
def A1LeftA2Continue():
    print('You pass the field and come to a city.')
    print('You go in and see two people on the street, one of them is heavily tattooed and the other is in a nice suit.')
    choice4 = raw_input('Which guy do you talk to? (Tattooed/Suit)')
    if choice4 == 'Tattooed':
        print('He takes you to the nearest bar and you use a phone to get in contact with your family.')
        print('They find where you are and the nearest airport that you can fly back home with.')
        print('The tattooed man takes you to the airport and buys your ticket for you.')
        print('Your family picks you up from the airport you flew into and takes you home.')
        Restart()
        sys.exit()
    if choice4 == 'Suit':
        print('He thinks you are below him and leaves you alone') 
        print('No one is around anymore to ask for help and you are forced to leave.')
        print('You never find your way home and live forever in this strange land as a begger.')
        Restart()
        sys.exit()

def A1Left():
    print('After some walking, you see a field on the side of the road.')
    choice3 = raw_input('Do you lay in the field or continue walking? (Lay in the field/Continue on)')
    while choice3 != 'Lay in the field':
        if choice3 == 'Continue on':
            A1LeftA2Continue()
        else:
            return
    else:
        print('You decide to take a nap')
        print('You sleep longer than you wanted to and it gets dark.')
        print('You die of hypothermia. The End.')
        Restart()
        sys.exit()

def Story():
    print('You come to a split in the path')
    choice2 = raw_input('Do you go left or right? (Left/Right)')
    while choice2 != 'Left':
        if choice2 == 'Right':
            A1Right()
        else:
            return
    else:
            A1Left()

def start():
    choice = raw_input('Would you like to start? (Yes/No)')
    while choice != 'Yes':
        if choice == 'No':
            print('Alright. Take your time.')
            print('Time is up.')
            choice = raw_input('Would you like to start? (Yes/No)')
        else:
            print('That was not an answer.')
            choice = raw_input('Would you like to start? (Yes/No)')
    else:
        Story()
        
def Restart():
    choice = ''
    choice2 = ''
    choice3 = ''
    choice4 = ''
    choice5 = ''
    choice6 = ''