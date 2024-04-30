#принципы ооп, git: gitignore
# 4 наследование полиморфизм инкапсуляция абстракция

class Warrior:#супер класс родительский класс
    # магические методы
    def __init__(self, name, health,power):
        self.name = name
        self.health=health
        self.power = power

    # магический метод
    def __str__(self):
        return (f'name: {self.name}\n'
                f'hp: {self.health}\n'
                f'power: {self.power}\n')
    def attak(self,other):
        other.health=self.power-other.health


warrior1=Warrior("берсерк",200,100)
#ФУНКЦИЯ
print(warrior1)


print(warrior1)
warrior2=Warrior("лучник",100,120)
warrior1.attak(warrior2)
warrior1.attak(warrior2)
print(warrior2)


class Warrior2(Warrior):# дочерний класс
    def __init__(self,name,health,power,armor):
        Warrior.__init__(self,name,health,power)
        super().__init__(name,health,power)
        self.armor = armor

    def __str__(self):
       return (Warrior.__str__(self) +
                f'Armor: {self.armor}\n')

    def attak(self,other):

        other.health = other.health-self.power
        other.health+=other.armor

    # def __str__(self):
    #     return (f'name: {self.name}\n'
    #             f'hp: {self.health}\n'
    #             f'power: {self.power}\n'
    #             f'armor: {self.armor}\n')

berserk=Warrior2('keyn',1000,100,50)
berserk2=Warrior2('кайн',1000,100,50)
berserk2.attak(berserk)
print(berserk)
berserk2.attak(berserk)
print(berserk)
