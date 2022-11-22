# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Factory:
    def __init__(self, name):
         self.name = name


class Car:
    def __init__(self, name):
        self.name = name
        self._factory = None
        self.motor = None

    def insert_motor(self, name):
        if self.motor is not None:
            print('O carro ja tem um motor')
        else:
            self.motor = name
            print(f'Foi inserido o motor {self.motor} no {self.name}')
    
    def remove_motor(self):
        if self.motor is None:
            print(f'O {self.name} não possui nenhum motor')
        else:
            self.motor = None
            print(f'foi removido o motor do {self.name}')


    @property
    def factory(self):
        return self._factory

    @factory.setter
    def factory(self, factory):
        self._factory = factory


class Motor:
    def __init__(self, name):
        self.name = name


chevrolet = Factory('Chevrolet')
wolkvagem = Factory('Wolksvagem')
toyota = Factory('Toyota')

opala = Car('Opala')
gol = Car('Gol')
corola = Car('Corola')

opala.factory = chevrolet.name
gol.factory = wolkvagem.name
corola.factory = toyota.name

motor1 = Motor('1.0')
motor2 = Motor('2.0')
motor3 = Motor('1.6')

gol.insert_motor(motor1.name)
opala.insert_motor(motor2.name)
corola.insert_motor(motor2.name)

print()
opala.remove_motor()

name_car = gol
print('\n################')
print( f'fabricante: {name_car.factory}\nCarro: {name_car.name}\nMotor: {name_car.motor}')
