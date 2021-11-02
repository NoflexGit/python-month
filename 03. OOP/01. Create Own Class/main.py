class Car:
    def __init__(self, brand, model, year) -> None:
        self.brand = brand
        self.model = model
        self.year = year

    def show_model(self):
        print(self.model)


tesla = Car('Tesla', 'Model S', 2021)

tesla.show_model()
