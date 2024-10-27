class Flower:
    def __ini__(self, name: str, petals: int, price: float):
        self.name = name
        self.petals = petals
        self.price = price

    def name_setter(self, name):
        self.name = name
    def price_setter(self, price):
        self.price = price
    def num_petals(self, petals):
        self.petals = petals
    
    def get_name(self, name):
        return self.name
    def get_price(self, price):
        return self.price
    def get_num_petals(self, petals):
        return self.petals