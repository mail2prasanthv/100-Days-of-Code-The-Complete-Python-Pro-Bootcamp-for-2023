# //importing

class Car:
    
    def __init__(self, seats):
        self.seats = seats
        self.follower =0#default value

car = Car(5)
print("Number of Seats:", car.seats, car.follower)
car.seats = 6
print("Number of Seats:", car.seats, car.follower)

