class bmw:
    def __init__(self, model):
        self.model = model

    def fuel(self):
        print(f"Fuel type for bmw{self.model} is petrol")

    def max_speed(self):
        print(f"Max Speed for bmw{self.model} is 240km/h")


class ferrari:
    def __init__(self, model):
        self.model = model

    def fuel(self):
        print(f"Fuel type for ferrari{self.model} is diesel")

    def max_speed(self):
        print(f"Max Speed for ferrari{self.model} is 300km/h")

bway = bmw('m5')
frrari = ferrari('spyder')
for i in (bway, frrari):
    i.fuel()
    i.max_speed()
