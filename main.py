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
    while reroll != "destination" or reroll != "restaurant" or reroll != "transportation" or reroll != "entertainment":
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

print(f"""Hello user! For your randomly selected day trip, you will,
    visit the beautiful {randomDestination}
    dine at the lovely {randomRestaurant}
    and finally, take the {randomTransport}
    to enjoy {randomEntertainment} for the evening!""")

print("")

willReroll = input("If one or more of these options does not appeal to you, you may reroll them now. Would you like to reroll any of these options? Please enter yes or no. ")
willReroll = willReroll.casefold()
print ("")
willReroll = incorrectYesNoReturn(willReroll)
while willReroll == "yes":
    reselectChoice = input("Which option would you like to reroll? ")
    reselectChoice = reselectChoice.casefold()
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
    willReroll = willReroll.casefold()
    if willReroll == "no":
        print(f"""Your completed randomly selected day trip is:
    Destination: {randomDestination}
    Restaurant: {randomRestaurant}
    Transportation: {randomTransport}
    Entertainment: {randomEntertainment}""")
        dayComplete = print("Type 'yes' to confirm or 'no' to go back and change something. ")
