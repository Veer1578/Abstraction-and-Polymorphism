class cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'I am a cat named {self.name} and aged {self.age}')

    def sound(self):
        print('Meow')


class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'I am a dog named {self.name} and aged {self.age}')

    def sound(self):
        print('Bark')


cyatt = cat('Kitty', 2.5)
dawg = dog('Tommy', 3)
for i in (cyatt, dawg):
    i.info()
    i.sound()
