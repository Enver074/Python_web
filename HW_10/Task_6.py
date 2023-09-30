from Task_5 import Dog, Cat, Bird

class Factory:


    def create_pet(self, animal_tipe, name, age, spec):
        if animal_tipe.lower() == 'dog':
            return Dog(name, age, spec)
        elif animal_tipe.lower() == 'cat':
            return Cat(name, age, spec)
        elif animal_tipe.lower() == 'bird':
            return Bird(name, age, spec)
        else:
            return ValueError

fact = Factory()

dog = fact.create_pet('dog', 'Butcher', '3', 'bite')
cat = fact.create_pet('cat', 'Leopold', 5, 'sleep')
bird = fact.create_pet('bird', 'Kesha', 2, 'talk')

for pet in [dog, cat, bird]:
    print(f'{pet.name} {pet.get_spec()}')
