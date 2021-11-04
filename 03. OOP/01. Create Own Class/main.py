class Car:
    couldBeElectroCar = True

    def __init__(self, brand, model, year) -> None:
        self.brand = brand
        self.model = model
        self.year = year

    def show_model(self):
        print(self.model)

    def drive(self):
        print(f'I drive {self.brand} {self.model} {self.year}')


tesla = Car('Tesla', 'Model S', 2021)

tesla.show_model()
tesla.drive()
