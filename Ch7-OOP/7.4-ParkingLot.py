class ParkingLot:
    def __init__(self, max_space):
        self.space = []
        self.max_space = max_space

    def park(self, car):
        if self.is_full():
            return print("Parking Lot is full")
        else:
            self.space.append(car)

    def is_full(self):
        if len(self.space) == self.max_space:
            return True
        return False

    def leave(self, car):
        self.space.pop(self.space.index(car))


class Car:
    def __init__(self, license_plate):
        self.lp = license_plate


if __name__ == "__main__":
    car1 = Car("1234")
    car2 = Car("345")
    car3 = Car("789")
    p1 = ParkingLot(3)
    p1.park(car1)
    p1.park(car2)
    p1.park(car3)
    print(p1.is_full())
    car4 = Car("4546")
    p1.park(car4)
