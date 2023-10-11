from vehicle import Vehicle

class Car(Vehicle):
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"
    
volvo = Car(78, "QB789KL")
# volvo2 = Car(Vehicle)

print(volvo.go())
# print(volvo.wheel_number)
# print(volvo.wheel_size)