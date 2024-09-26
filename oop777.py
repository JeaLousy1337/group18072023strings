class Car:
    def __init__(self, producer: str, brand: str, fuel_consumption: float, graduation_year: int = 2020):
        self.graduation_year = graduation_year
        self.producer = producer
        self.brand = brand
        self.run = 0
        self.fuel_consumption = fuel_consumption

    def __str__(self):
        return f'Сharacteristic of the {self.__class__.__name__}: ↓' \
               f'\n graduation year: {self.graduation_year}' \
               f'\n producer: {self.producer}' \
               f'\n brand: {self.brand}' \
               f'\n run: {self.run}' \
               f'\n fuel_consumption: {self.fuel_consumption}'

    def __del__(self):
        with open('cars_file_csv.csv', mode='a', encoding='utf-8') as file:
            file.write(f'{self.producer};{self.brand};{self.graduation_year}\n')


class Truck(Car):
    def __init__(self, carrying_capacity: int, producer: str, brand: str, fuel_consumption: float, graduation_year: int = 2020):
        super().__init__(producer=producer, brand=brand, fuel_consumption=fuel_consumption, graduation_year=graduation_year)
        self.carrying_capacity = carrying_capacity

    def __str__(self):
        return f'Сharacteristic of the {self.__class__.__name__}: ↓' \
               f'\n graduation year: {self.graduation_year}' \
               f'\n producer: {self.producer}' \
               f'\n brand: {self.brand}' \
               f'\n run: {self.run}' \
               f'\n fuel_consumption: {self.fuel_consumption}' \
               f'\n carrying_capacity: {self.carrying_capacity}'


class SportCar(Car):
    def __init__(self, producer: str, brand: str, fuel_consumption: float, speed: int, price: int = 12900, graduation_year: int = 2020):
        super().__init__(producer=producer, brand=brand, fuel_consumption=fuel_consumption, graduation_year=graduation_year)
        self.speed = speed
        self.price = price

    def __str__(self):
        return f'Сharacteristic of the {self.__class__.__name__}: ↓' \
               f'\n graduation year: {self.graduation_year}' \
               f'\n producer: {self.producer}' \
               f'\n brand: {self.brand}' \
               f'\n run: {self.run}' \
               f'\n fuel_consumption: {self.fuel_consumption}' \
               f'\n speed: {self.speed}' \
               f'\n price: {self.price}'


auto = Car(producer='BMW', brand="Rolls-Royce", fuel_consumption=15.2)
auto2 = Car(producer='Volkswagen', brand="Porsche", fuel_consumption=10.9, graduation_year=2077)
auto3 = Car(producer='Toyota', brand="Lexus", fuel_consumption=16.8, graduation_year=2023)
auto4 = Truck(producer='Lamborghini', brand='Lambo-Truck', fuel_consumption=18.8, carrying_capacity=200)
auto5 = SportCar(producer='Lanos', brand="Lada", fuel_consumption=16.8, speed=350, price=120000)

del auto
del auto2
del auto3
del auto4
del auto5
