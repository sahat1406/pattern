class Pizza(object):
    class PizzaBuilder(object):

        def __init__(self):
            self.extra_cheese = False
            self.garlic = False

        def add_garlic(self):
            self.garlic = True
            return self

        def add_extra_cheese(self):
            self.extra_cheese = True
            return self

        def build(self):
            return Pizza(self)

    def __init__(self, builder):

        self.garlic = builder.garlic
        self.extra_cheese = builder.extra_cheese

def main():
    print("Building a pizza...")

    pizza = Pizza.PizzaBuilder().add_garlic().add_extra_cheese().build()

    if pizza.garlic:
        print("The pizza has garlic.")
    if pizza.extra_cheese:
        print("The pizza has extra cheese.")

if __name__ == "__main__":
    main()