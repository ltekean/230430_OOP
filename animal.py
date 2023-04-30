class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound
        
    def speak(self):
        pass
    
class Dog(Animal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)       
    
    def speak(self):
        return '멍멍'

class Cat(Animal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
    
    def speak(self):
        return '야옹'
