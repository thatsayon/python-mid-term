class Star_Cinema:
    hall_list = []

    @classmethod
    def entry_hall(self, hall_data):
        self.hall_list.append(hall_data)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self.__seats = {} 
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
    
    def entry_show(self, id, movie_name, time):
        data = (id, movie_name, time)
        self.__show_list.append(data)
        seats = [[0 for i in range(self.__cols)] for j in range(self.__rows)]
        self.__seats[id] = seats
    
    def book_seats(self, sid, row, col):
        print("-"*20)
        if row <= self.__rows and col <= self.__cols:
            if self.__seats[sid][col-1][row-1] == 0:
                self.__seats[sid][col-1][row-1] = 1
                print(f"Seat ({row}, {col}) booked for show {sid}")
            else:
                print("This seat isn't available\nChoose another seat")
        else:
            print("Trying to access invalid seat")

    def view_show_list(self):
        print("-"*20)
        for data in self.__show_list:
            print(f"MOVIE NAME: {data[1]} SHOW ID: {data[0]} TIME: {data[2]}")
    
    def view_available_seats(self, sid):
        print("-"*20)
        if sid in self.__seats:
            for data in self.__seats[sid]:
                print(data)
        else:
            print("Enter a valid show id")

hall1 = Hall(6, 6, 1)
Star_Cinema.entry_hall(hall1)
hall1.entry_show(111, "Jawan", "07/10/2023 12:00 PM")
hall1.entry_show(222, "Nun 2", "07/10/2023 4:00 PM")
while True:
    print("-"*20)
    print("1. VIEW ALL SHOW TODAY \n2. VIEW AVAILABLE SEATS \n3. BOOK TICKET \n4. Exit")
    user_in = int(input("ENTER OPTION: "))

    if user_in == 1:
        hall1.view_show_list()
    elif user_in == 2:
        show_id = int(input("ENTER SHOW ID: "))
        hall1.view_available_seats(show_id)
    elif user_in == 3:
        sid = int(input("Show Id: "))
        nt = int(input("Number of Ticket?: "))
        for i in range(nt):
            r = int(input("Enter Seat Row: "))
            c = int(input("Enter Seat Col: "))
            hall1.book_seats(sid, r, c)
    elif user_in == 4:
        break
