class Star_Cinema:
    hall_list = []

    @classmethod
    def entry_hall(self, hall_data):
        self.hall_list.append(hall_data)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self.seats = {} 
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
    
    def entry_show(self, id, movie_name, time):
        data = (id, movie_name, time)
        self.show_list.append(data)
        seats = [[0 for i in range(self.cols)] for j in range(self.rows)]
        self.seats[id] = seats
    
    def book_seats(self, sid, row, col):
        self.seats[sid][row-1][col-1] = 1

    def view_show_list(self):
        for data in self.show_list:
            print(f"MOVIE NAME: {data[1]} SHOW ID: {data[0]} TIME: {data[2]}")
    
    def view_available_seats(self, sid):
        for data in self.seats[sid]:
            print(data)

hall1 = Hall(6, 6, 1)
Star_Cinema.entry_hall(hall1)
hall1.entry_show(111, "Jawan", "12:00 PM")
hall1.entry_show(222, "Nun 2", "4:00 PM")
print(hall1.show_list)
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
        r = int(input("Enter Seat Row: "))
        c = int(input("Enter Seat Col: "))
        hall1.book_seats(sid, r, c)
    elif user_in == 4:
        break
