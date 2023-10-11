class Vehicle:
    
    def __init__(self, wheel_size, wheel_number):
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number
        
    def go(self):
        return "vrrrrrrrooom!"
    
    def fill_up_tank(self):
        return "filling up!"
    
toyota = Vehicle(20, "AD2345")

print(toyota.wheel_number)
print(toyota.wheel_size)
print(toyota.go())
print(toyota.fill_up_tank())


