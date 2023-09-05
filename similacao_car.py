from car import Car

my_car = Car("padrao", "fusca", 72)
my_car.get_describe_car()

my_car.odometer_reading = 23
my_car.reading_odometer()

my_car.update_odometer(33)
my_car.reading_odometer()

my_car.update_odometer(29)
my_car.reading_odometer()

my_car.incremente_odometer(9)
my_car.reading_odometer()