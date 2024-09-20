class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return (
            f'{self.__class__.__name__}(name='
            f'{self.name!r}, price={self.price})'  # !r -- означает привести к кавычкам
        )

    def __repr__(self):
        return f'<Product {self.name!r}>'

    def make_discount(self, discount_percent):
        """
        Applies discount in %

        :param discount_percent:
        :return:
        """
        self.price *= (100 - discount_percent) / 100


def apply_discount(product, discount):
    product.price *= (100 - discount) / 100


laptop = Product("Laptop", 2000)
print(laptop.__dict__)
print(laptop)
print(repr(laptop))

laptop.make_discount(10)
print(laptop)
apply_discount(laptop, 10)
print(laptop)