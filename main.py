import random

destinationList = ["Greece", "Sweden", "Germany", "Australia", "Japan", "Italy"]
restaurantList = ["Applebees", "Olive Garden", "Red Lobster",  "LG's Prime Steakhouse", ]
transportationList = ["Bus", "Car", "Train", "Monorail"]
entertainmentList = ["Movie", "Board Games", "Bowling", "Hiking", "Concert", "Theater"]
randomDestination = random.choice(destinationList)
randomRestaurant = random.choice(restaurantList)
randomTransport = random.choice(transportationList)
randomEntertainment = random.choice(entertainmentList)
def reselect (reroll):
    while reroll != "destination" or reroll != "restaurant" or reroll != "transportation" or reroll != "entertainment":
        if reroll == "destination":
            newDestination = random.choice(destinationList)
            print (f"Your new destination is {newDestination}!")
            return newDestination
        elif reroll == "restaurant":
            newRestaurant = random.choice(restaurantList)
            print(f"Your new restaurant choice is {newRestaurant}!")
            return newRestaurant
        elif reroll == "transportation":
            newTransport = random.choice(transportationList)
            print(f"Your new form of transportation is {newTransport}!")
            return newTransport
        elif reroll == "entertainment":
            newEntertainment = random.choice(entertainmentList)
            print(f"Your new entertainment choice is {newEntertainment}!")
            return newEntertainment
        else:
            reroll = input("Incorrect input, please try again! ")
            reroll.casefold()




