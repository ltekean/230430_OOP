class Car():
    def __init__(self, model, color, speed):
        self.model = "my_car"
        self.color = "my_color"
        self.speed = 0

    def accelerate(self, accels):
        self.speed += accels
        if (self.speed >= 100):
            self.speed = 100
    
    def brake(self, brakes):
        self.spped -= brakes
        if (self.speed <= 0):
            self.speed = 0
    
    def get_speed(self):
        return self.speed