import random


destinationList = ["Greece", "Sweden", "Germany", "Australia", "Japan", "Italy"]
restaurantList = ["Applebees", "Olive Garden", "Red Lobster",  "LG's Prime Steakhouse", ]
transportationList = ["Bus", "Car", "Train", "Monorail"]
entertainmentList = ["Movie", "Board Games", "Bowling", "Hiking", "Concert", "Theater"]
randomDestination = random.choice(destinationList)
randomRestaurant = random.choice(restaurantList)
randomTransport = random.choice(transportationList)
randomEntertainment = random.choice(entertainmentList)
def incorrectInputReturn (inputStr):
    if inputStr == "destination" or inputStr == "restaurant" or inputStr == "transportation" or inputStr == "entertainment":
        pass
    else:
        while inputStr != "destination" and inputStr != "restaurant" and inputStr != "transportation" and inputStr != "entertainment":
            inputStr = input("I'm sorry that's an incorrect input, please try again! ")
    output = inputStr
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

print(f"""Hello user! Your randomly selected day trip is:
Destination: {randomDestination}
Restaurant: {randomRestaurant}
Transportation: {randomTransport}
Entertainment: {randomEntertainment}""")

print("")

willReroll = input("Would you like to reroll any of these options? Please enter yes or no. ")
willReroll = willReroll.casefold()
print ("")
while willReroll != "yes" and willReroll != "no":
    willReroll = input("I'm sorry, that's an incorrect input, please try again! ")
    willReroll = willReroll.casefold()
while willReroll == "yes":
    reselectChoice = input("Which option would you like to reroll? ")
    reselectChoice = reselectChoice.casefold()
    reselectChoice = incorrectInputReturn (reselectChoice)
    reselectChoice = reselectChoice.casefold()
    newChoice = reselect(reselectChoice)
    if reselectChoice == "restaurant":
        randomRestaurant = newChoice
    elif reselectChoice == "destination":
        randomDestination = newChoice
    elif reselectChoice == "transportation":
        randomTransport == newChoice
    elif reselectChoice == "entertainment":
        randomEntertainment = newChoice
    print(f"Your new {reselectChoice} selection is {newChoice}!")
    willReroll = input("Would you like to reroll another option? ")
    willReroll = willReroll.casefold()
if willReroll == "no":
    print(f"""Your completed randomly selected day trip is:
Destination: {randomDestination}
Restaurant: {randomRestaurant}
Transportation: {randomTransport}
Entertainment: {randomEntertainment}""")
dayComplete = print("Type 'yes' to confirm or 'no' to go back and change something. ")
