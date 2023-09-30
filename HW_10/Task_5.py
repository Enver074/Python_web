class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.spec = None

    def get_spec(self):
        return self.spec

class Dog(Animal):

    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec

    def show_info(self):
        return (f'{self.name} can {self.command}')


class Cat(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec

    def show_info(self):
        return (f'{self.name} sleeps {self.sleep_time} hours')


class Bird(Animal):

    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec

    def show_info(self):
        return (f'{self.name} sing {self.sing_power}dB')


pet_1 = Dog('Bob', 5, 'лает')
pet_2 = Cat('Felix', 5, 'мурлыкает')
pet_3 = Bird('Aro', 5, 'поет')


# for pet in [pet_1, pet_2, pet_3]:
#     print(f'{pet.name} {pet.get_spec()}')