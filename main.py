import random, abc
animals_all = []
class Animal(abc.ABC):
    health = 'normal'
    sound = ''
    def __init__(self, name):
        self.name = name
        animals_all.append(self)

    def eating(self):
        self.satiety = int(self.satiety + (self.satiety / 100) * 25) #Для примера, одно кормление = 25 % от нормы
        print('{} накормлен'.format(self.name))
        if self.satiety > 100:
            self.health = 'death'
            print('Вы перекормили зверюгу по имени {}. Она лопнула. Собирайте ошметки по сараю.'.format(self.name))

    def speak(self):
        print(self.sound)

    @abc.abstractmethod
    def service(self, mode):
        if mode == 'eggs':
            print('У {} собраны яйца'.format(self.name))
        elif mode == 'milk':
            print('Вы подоили {}'.format(self.name))
        elif mode == 'shave':
            print('{} побрит'.format(self.name))
        else:
            print('Укажите правильный метод взаимодействия')

    def __gt__(self, other):
        return self.weight > other.weight


class Goose(Animal):
    def service(self):
        print('У {} собраны яйца'.format(self.name))

    satiety = random.randrange(0, 101)  # % сытости на момент создания объекта
    sound = 'GA-GA'
    weight = random.randrange(5000, 8000)

class Cow(Animal):
    def service(self):
        print('Вы подоили {}'.format(self.name))

    satiety = random.randrange(0, 101)  # % сытости на момент создания объекта
    sound = 'MU-MU'
    weight = random.randrange(400000, 600000)

    def service(self):
        if self.health == 'normal':
            print('Вы подоили {}'.format(self.name))
        elif self.health == 'death':
            print('Ваша живность скончалась. Но это не повод не доиться ;)')


class Sheep(Animal):
    def service(self):
        print('{} побрит'.format(self.name))
    satiety = random.randrange(0, 101)  # % сытости на момент создания объекта
    sound = 'ME-ME'
    weight = random.randrange(70000, 80000)

class Chicken(Animal):
    def service(self):
        print('У {} собраны яйца'.format(self.name))
    satiety = random.randrange(0, 101)  # % сытости на момент создания объекта
    sound = 'KO-KO'
    weight = random.randrange(3000, 4000)

class Goat(Animal):
    satiety = random.randrange(0, 101)  # % сытости на момент создания объекта
    sound = 'BE-BE'
    weight = random.randrange(50000, 150000)

    def service(self):
        if self.health == 'normal':
            print('Вы подоили {}'.format(self.name))
        elif self.health == 'death':
            print('Ваша живность скончалась. Но это не повод не доиться ;)')

class Duck(Animal):
    def service(self):
        print('У {} собраны яйца'.format(self.name))
    satiety = random.randrange(0, 101)  # % сытости на момент создания объекта
    sound = 'Krya-Krya'
    weight = random.randrange(700, 1600)

gees1 = Goose('Серый')
gees1.eating()
gees1.service()

gees2 = Goose('Белый')
gees2.eating()
gees2.service()

cow = Cow('Манька')
cow.eating()
cow.service()

sheep1 = Sheep('Барашек')
sheep1.eating()
sheep1.service()

sheep2 = Sheep('Кудрявый')
sheep2.eating()
sheep2.service()

chicken1 = Chicken('Ко-Ко')
chicken1.eating()
chicken1.service()

chicken2 = Chicken('Кукареку')
chicken2.eating()
chicken2.service()

goat1 = Goat('Рога')
goat1.eating()
goat1.service()

goat2 = Goat('Копыта')
goat2.eating()
goat2.service()

duck = Duck('Кряква')
duck.eating()
duck.service()

total_weight = 0
for animal in animals_all:
    total_weight += animal.weight
print('Общий вес всех животных {} грамм'.format(total_weight))
print('Самое большое животное на ферме зовут : {}'.format(max(animals_all).name))
