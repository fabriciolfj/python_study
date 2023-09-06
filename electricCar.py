from car import Car


class ElectricCar(Car):

    def __init__(self, make, model, year, battery):
        super().__init__(make, model, year)
        self.battery = battery

    def get_describe_car(self):
        print(f"is car eletric {self.make}")
