import random


destinationList = ["Greece", "Sweden", "Germany", "Australia", "Japan", "Italy"]
restaurantList = ["Applebees", "Olive Garden", "Red Lobster",  "LG's Prime Steakhouse", ]
transportationList = ["bus", "train", "monorail"]
entertainmentList = ["a movie", "board games", "bowling", "a concert", "a theater play"]
randomDestination = random.choice(destinationList)
randomRestaurant = random.choice(restaurantList)
randomTransport = random.choice(transportationList)
randomEntertainment = random.choice(entertainmentList)
def incorrectYesNoReturn (inputStr):
    inputStr = inputStr.casefold()
    if inputStr == "yes" or inputStr == "no":
        pass
    else:
        while inputStr != "yes" and inputStr != "no":
            inputStr = input("I'm sorry that's an incorrect input, please try again! ")
            inputStr = inputStr.casefold()
    output = inputStr
    output = output.casefold()
    return output
def incorrectInputReturn (inputStr):
    inputStr = inputStr.casefold()
    if inputStr == "destination" or inputStr == "restaurant" or inputStr == "transportation" or inputStr == "entertainment":
        pass
    else:
        while inputStr != "destination" and inputStr != "restaurant" and inputStr != "transportation" and inputStr != "entertainment":
            inputStr = input("I'm sorry that's an incorrect input, please try again! ")
            inputStr = inputStr.casefold()
    output = inputStr
    output = output.casefold()
    return output

def reselect (reroll):
    while incorrectInputReturn(reroll):
        if reroll == "destination":
            newDestination = random.choice(destinationList)
            return newDestination
        elif reroll == "restaurant":
            newRestaurant = random.choice(restaurantList)
            return newRestaurant
        elif reroll == "transportation":
            newTransport = random.choice(transportationList)
            return newTransport
        elif reroll == "entertainment":
            newEntertainment = random.choice(entertainmentList)
            return newEntertainment
        else:
            reroll = input("Incorrect input, please try again! ")
            reroll = reroll.casefold()

print(f"""Hello user! For your randomly selected day trip, you will:
    Visit the beautiful {randomDestination},
    dine at the lovely {randomRestaurant},
    and finally, take the {randomTransport}
    to enjoy {randomEntertainment} for the evening!""")

print("")

willReroll = input("""If one or more of these options does not appeal to you, you may reroll them now.
Would you like to reroll any of these options? Please enter yes or no. """)
print ("")
willReroll = incorrectYesNoReturn(willReroll)
if willReroll == "no":
    print (f"We hope you enjoy your trip!")

while willReroll == "yes":
    reselectChoice = input("Which option would you like to reroll? ")
    reselectChoice = incorrectInputReturn (reselectChoice)
    newChoice = reselect(reselectChoice)
    if reselectChoice == "restaurant":
        restaurantList.remove(randomRestaurant)
        randomRestaurant = newChoice
    elif reselectChoice == "destination":
        destinationList.remove(randomDestination)
        randomDestination = newChoice
    elif reselectChoice == "transportation":
        transportationList.remove(randomTransport)
        randomTransport == newChoice
    elif reselectChoice == "entertainment":
        entertainmentList.remove(randomEntertainment)
        randomEntertainment = newChoice
    print ("")
    print(f"Your new {reselectChoice} selection is {newChoice}!")
    willReroll = input("Would you like to reroll another option? ")
    print ("")
    willReroll = incorrectYesNoReturn(willReroll)
    if willReroll == "no":
        print(f"""For your NEW randomly selected day trip, you will:
    Visit the beautiful {randomDestination},
    dine at the lovely {randomRestaurant},
    and finally, take the {randomTransport}
    to enjoy {randomEntertainment} for the evening!
    We hope you enjoy your trip!""")
    print("")
