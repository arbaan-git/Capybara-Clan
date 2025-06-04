from abc import ABC, abstractmethod


class Capybara(ABC):

    happiness = 0 #always increasing, never decreasing (design choice for now, maybe i will change it later)

    def __init__(self, name):
        self.__name = name
        self.__xp = 0
        self.__energy = 100

    def __gt__(self, other):
        return self.xp > other.xp #i am not checking if the other argument is a class object or not. reason: its just me so there is no chance of error currently

    @property
    def xp(self):
        return self.__xp

    @property
    def energy(self):
        return self.__energy

    @xp.setter
    def xp(self, value):
        if 0 <= value <= 100:
            self.__xp = value
        else:
            print("xp maxxed out")

    @energy.setter
    def energy(self, value):
        if 0 <= value <= 100:
            self.__energy = value
        else:
            print("energy maxxed out")

    def rest_and_regain(self):
        self.energy = 100
        Capybara.happiness+=10000 #its a big number but again - design choice

    @abstractmethod
    def train(self):
        pass

    @abstractmethod
    def mission(self):
        pass


class Warrior(Capybara):
    def train(self):
        print("The warrior has trained!")
        self.xp += 10
        self.energy -= 20

    def mission(self):
        print("The warrior has completed a mission")
        self.xp += 20
        self.energy -= 10


class Medic(Capybara):
    def train(self):
        print("The medic has trained!")
        self.xp += 10
        self.energy -= 20

    def mission(self):
        print("The medic has completed a mission")
        self.xp += 10
        self.energy -= 20


class Scout(Capybara):
    def train(self):
        print("The scout has trained!")
        self.xp += 10
        self.energy -= 20

    def mission(self):
        print("The scout has completed a mission")
        self.xp += 15
        self.energy -= 15


class Human:
    def __init__(self, name):
        self.name   = name  
    def eat(self):
        print(f"{self.name} ate")


def send_on_mission(capybara):
    if hasattr(capybara, "mission"):
        capybara.mission()

    else:
        print("This entity can't go on a mission")


warrior1 = Warrior("Thor")
medic1 = Medic("Jinna")
scout1 = Scout("Hange")
human1 = Human("Jessica")
for i in (warrior1, medic1, scout1, human1): #duck typing (aka jon jones typing) testing 
    send_on_mission(i)

#testing the 2 main method on each subclass
warrior1.train()
warrior1.mission()

medic1.train()
medic1.mission()

scout1.train()
scout1.mission()


print(warrior1 > scout1) #testing the gt magic operator

print(warrior1.energy)

while warrior1.energy: #emptying the energy for this object before using the rest_and_regain method on it
    warrior1.mission()

print(warrior1.energy)

warrior1.rest_and_regain()

print(warrior1.energy)

print(Capybara.happiness)