
seats = [False] * 20
taken_seats = [3,7,14]
for t in taken_seats:
    seats[t-1] = True

first_class = [1, 2, 3, 4]
emergency = [9, 10, 11, 12]

print("Welcome to the Fleur Air Seat Purchase System!")

running = True

while running:

    # Display seats
    print("\nCurrent Seat Status:")
    for i in range(20):
        label = ""
        if (i + 1) in first_class:
            label = "(First Class)"
        elif (i + 1) in emergency:
            label = "(Emergency Row)"

        status = "TAKEN" if seats[i] else "OPEN"
        print(f"Seat {i+1}: {status} {label}")

    buy = input("\nWould you like to purchase a seat? (yes/no): ").lower()

    if buy == "no":
        print("Thank you for using the system!")
        break

    # Ask for number of seats
    try:
        num = int(input("How many seats would you like to buy?: "))
    except:
        print("Invalid input.")
        continue

    for _ in range(num):
        try:
            seat_number = int(input("\nEnter seat number (1–20): "))
        except:
            print("Invalid input.")
            continue

        if seat_number < 1 or seat_number > 20:
            print("Invalid seat number.")
            continue

        if seats[seat_number - 1]:
            print("That seat is already taken! Kindly choose another.")
            continue

        if seat_number in first_class:
            print("This is a FIRST-CLASS seat and requires a $150 fee.")
            confirm = input("Do you want to continue? (yes/no): ").lower()
            if confirm != "yes":
                print("Seat purchase canceled.")
                continue

        if seat_number in emergency:
            print("This is an EMERGENCY EXIT ROW seat.")
            print("You must be willing and able to help in an emergency.")
            confirm = input("Do you accept this responsibility? (yes/no): ").lower()
            if confirm != "yes":
                print("Seat assignment canceled.")
                continue

        seats[seat_number - 1] = True
        print(f"Seat {seat_number} has been purchased successfully!")

    print("\nPurchase session complete.\n")

