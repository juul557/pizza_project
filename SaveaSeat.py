# TO DO:

#make pricing ##
#make seat list ##
#class choice function ##
#reserving seat choice function ##
#destination choice function ##
# calculate price ##

firstClass_Price = 20
secondClass_Price = 10
seatReservationCost = 3.50
seats = ["A1", "A2", "A3", "A4", "A5", "A6"]
destinations = ["Eindhoven", "Tilburg", "Utrecht", "Amsterdam", "Zutphen"]

def display_seats():
    print("Available seats:")
    for i, seat in enumerate(seats, 1):
        print(f"{i}. {seat}")

def classChoice():
    while True:
        classChoice = input("Enter 'F' for first class or 'S' for second class: ").upper()
        if classChoice == "F":
            return "First Class", firstClass_Price
        elif classChoice == "S":
            return "Second Class", secondClass_Price
        else:
            print("Invalid choice. Please enter 'F' or 'S'.")

def destinationChoice():
    while True:
        print("Available destinations:")
        for i, destination in enumerate(destinations, 1):
            print(f"{i}. {destination}")
        destinationChoice = input("Enter the number of your destination: ")
        if destinationChoice.isdigit() and 1 <= int(destinationChoice) <= len(destinations):
            return destinations[int(destinationChoice) - 1]
        else:
            print("Invalid destination choice. Please try again.")

def ticketSale():
    print("Welcome to the train ticket booking system!") 
    while True:
        userChoice = input("Would you like to buy a ticket? Y/N: ").upper()
        if userChoice == "Y":
            class_name, price = classChoice()
            destination = destinationChoice()
            display_seats()
            while True:
                seatChoice = input("Enter the number of your preferred seat: ")
                if seatChoice.isdigit() and 1 <= int(seatChoice) <= len(seats):
                    seatChoice = seats[int(seatChoice) - 1]
                    reserve_seat = input("Would you like to reserve your seat? Y/N: ").upper()
                    if reserve_seat == "Y":
                        total_price = price + seatReservationCost
                    else:
                        total_price = price
                    print(f"Your ticket has been booked. Seat: {seatChoice}, Class: {class_name}, Price: ${total_price:.2f}, Destination: {destination}")
                    seats.remove(seatChoice)
                    break
                else:
                    print("Invalid seat choice. Please try again.")
        elif userChoice == "N":
            print("Thank you for using our system!")
            break

ticketSale()