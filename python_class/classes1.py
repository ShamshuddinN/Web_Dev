# Context: 
# Lets say we are creating an application to keep track of Seats available in a Flight,
# We have to make sure that seats are available for booking

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passengers(self, name):
        if not self.open_seats(): # Means self.open_seats == 0 meaning there are no open seats.
            return False

        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Shamshuddin", "Shahbaaz", "Surya", "Samarth"]

for person in people:
    if flight.add_passengers(person):
        print(f"Added {person} Successfully")
    else:
        print(f"No seats left for {person}")
        