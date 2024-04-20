# Function to check the availability of a seat
def check_seat_availability(seat_map, row, column):
    #return 1 if seat is empty
    #return 2 if seat is a hall
    #return 3 if seat is a bag area
    #return 4 if seat is booked
    if seat_map[row][column] == 'F':
        return 1
    elif seat_map[row][column] == 'X':
        return 2
    elif seat_map[row][column] == 'S':
        return 3
    elif seat_map[row][column] == 'R':
        return 4

# Function to book a seat
def book_seat(seat_map, row, column):
    #to check the situation of the seat
    situation = check_seat_availability(seat_map, row, column)
    #return 1 means the seat is empty, then book it
    #return 2 or 3 means this is not seat area
    #return 4 means the seat is booked
    if situation == 1:
        seat_map[row][column] = 'R'
        print("Seat booked successfully!")
    elif situation == 4:
        print("Seat is already booked.")
    elif situation == 2 or situation == 3:
        print("This is not seat area.")

# Function to free a seat
def free_seat(seat_map, row, column):
    #to check the situation of the seat
    situation = check_seat_availability(seat_map, row, column)
    #return 4 if the seat is booked, then free it
    #return 1 if this is a free seat
    #return 2, 3 if this is not seat area
    if situation == 4:
        seat_map[row][column] = 'F'
        print("Seat freed successfully!")
    elif situation == 1:
        print("Seat is already free.")
    elif situation == 2 or situation == 3:
        print("This is not seat area.")

# Function to show the booking state
def show_booking_state(seat_map):
    for row in seat_map:
        for seat in row:
            print(seat, end=' ')
        print()

# Create the initial seat map
seat_map = [['F' for _ in range(80)] for _ in range(7)]
seat_map[3] = ['X' for _ in range(80)]
seat_map[4][75] = 'S'
seat_map[5][75] = 'S'
seat_map[6][75] = 'S'
seat_map[4][76] = 'S'
seat_map[5][76] = 'S'
seat_map[6][76] = 'S'

# Menu loop
while True:
    print("Menu:")
    print("1. Check availability of seat")
    print("2. Book a seat")
    print("3. Free a seat")
    print("4. Show booking state")
    print("5. Exit program")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        row = int(input("Enter the row number: "))
        column = int(input("Enter the column number: "))
        if check_seat_availability(seat_map, row, column):
            print("Seat is available.")
        else:
            print("Seat is not available.")

    elif choice == '2':
        row = int(input("Enter the row number: "))
        column = int(input("Enter the column number: "))
        book_seat(seat_map, row, column)

    elif choice == '3':
        row = int(input("Enter the row number: "))
        column = int(input("Enter the column number: "))
        free_seat(seat_map, row, column)

    elif choice == '4':
        show_booking_state(seat_map)

    elif choice == '5':
        break

    else:
        print("Invalid choice. Please try again.")

print("Program terminated.")