# Continuing the RPG thematic, we will now give an example of Decorator
# Pattern Implementation, where a character may cast a magical attack
# against other, which can be buffered according to some features (decorators)
# the character may have

from random import randint


class Attack():
    def getDescription(self):
        return self.__class__.__name__

    def getTotalDamage(self):
        return self.__class__.damage


class BaseAttack(Attack):
    damage = 5


class MultiplyAttackDecorator(Attack):
    def __init__(self, attack):
        self.component = attack
        self.multiplier = randint(1,5)

    def getTotalDamage(self):
        return self.multiplier * self.component.getTotalDamage()

    def getDescription(self):
        if self.multiplier == 5:
            return self.component.getDescription() + ' Critical Attack!'
        else:
            return self.component.getDescription() + ' X' + '{}'.format(self.multiplier)


class AttackBufferDecorator(Attack):
    def __init__(self, attack):
        self.component = attack

    def getTotalDamage(self):
        return self.component.getTotalDamage() + Attack.getTotalDamage(self)

    def getDescription(self):
        return self.component.getDescription() + ' ' + Attack.getDescription(self)


class DivineBless(AttackBufferDecorator):
    damage = 20

    def __init__(self, attack):
        AttackBufferDecorator.__init__(self, attack)


class InFury(AttackBufferDecorator):
    damage = 15

    def __init__(self, attack):
        AttackBufferDecorator.__init__(self, attack)


class Meditated(AttackBufferDecorator):
    damage = 10

    def __init__(self, attack):
        AttackBufferDecorator.__init__(self, attack)


class Confused(AttackBufferDecorator):
    damage = -10

    def __init__(self, attack):
        AttackBufferDecorator.__init__(self, attack)


if __name__ == "__main__":
    normalAttack = MultiplyAttackDecorator(BaseAttack())
    print(normalAttack.getDescription() + ": " + str(normalAttack.getTotalDamage()))

    normalAttack = MultiplyAttackDecorator(BaseAttack())
    print(normalAttack.getDescription() + ": " + str(normalAttack.getTotalDamage()))

    normalAttack = MultiplyAttackDecorator(BaseAttack())
    print(normalAttack.getDescription() + ": " + str(normalAttack.getTotalDamage()))

    bufferedAttack = DivineBless(InFury(Meditated(normalAttack)))
    print(bufferedAttack.getDescription() + ": " + str(bufferedAttack.getTotalDamage()))

    debufferedAttack = Confused(normalAttack)
    print(debufferedAttack.getDescription() + ": " + str(debufferedAttack.getTotalDamage()))
