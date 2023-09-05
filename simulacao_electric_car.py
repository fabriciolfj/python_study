from electricCar import ElectricCar as EC
from battery import Battery as BT

car = EC("pejo", "206", "2004", BT(65))
car.get_describe_car()
car.battery.describe_battery()
car.battery.get_range()