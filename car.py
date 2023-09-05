class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_describe_car(self):
        print(f"modelo {self.model} tipo {self.make} ano {self.year}")

    def reading_odometer(self):
        print(f"milhas rodadas {self.odometer_reading}")

    def update_odometer(self, value):
        if value >= self.odometer_reading:
            self.odometer_reading = value
            return

        print(f"valor nao permitido")

    def incremente_odometer(self, value):
        self.odometer_reading += value