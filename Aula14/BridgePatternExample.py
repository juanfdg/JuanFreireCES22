# This is a RPG game like example of Bridge Pattern Implementation
# A character may have one immutable race, out of three races, which are
# classes derived from character class, and one class (RPG, not OO class)
# implementation, which can be changed anytime through the game play

from abc import ABC, abstractmethod


class CharacterAbstractInterface(ABC):
    """ Target interface.

    This is the target interface, that clients use.
    """
    def __init__(self):
        self._HP = 0
        self._MP = 0
        self._stamina = 0

    def getHP(self):
        return self.__HP

    def getMP(self):
        return self.__MP

    def getStamina(self):
        return self.__stamina

    @abstractmethod
    def describeMyself(self):
        pass


class CharacterBridge(CharacterAbstractInterface):
    """ Bridge class.

        This class forms a bridge between the target
        interface and background implementation.
        """

    def __init__(self, classImplementation):
        super().__init__()
        self._class = classImplementation
        self._HP += self._class.getBonusHP()
        self._MP += self._class.getBonusMP()
        self._stamina += self._class.getBonusStamina()

    def setClassImplementation(self, classImplementation):
        self._HP -= self._class.getBonusHP()
        self._MP -= self._class.getBonusMP()
        self._stamina -= self._class.getBonusStamina()
        self._class = classImplementation
        self._HP += self._class.getBonusHP()
        self._MP += self._class.getBonusMP()
        self._stamina += self._class.getBonusStamina()

    @abstractmethod
    def describeMyself(self):
        pass


class ClassImplementationInterface(ABC):
    """ Interface for the background implementation.

    This class defines how the Bridge communicates
    with various background implementations.
    """

    def __init__(self):
        self._bonusHP = 0
        self._bonusMP = 0
        self._bonusStamina = 0
        self._description = 'None Class'

    def getBonusHP(self):
        return self._bonusHP

    def getBonusMP(self):
        return self._bonusMP

    def getBonusStamina(self):
        return self._bonusStamina

    def getDescription(self):
        return self._description


class Human(CharacterBridge):
    def __init__(self, classImplementation=ClassImplementationInterface()):
        super().__init__(classImplementation)
        self._HP += 300
        self._MP += 100
        self._stamina += 200

    def describeMyself(self):
        print("I am a Human " + self._class.getDescription())
        print("HP: " + "{:>4}".format(self._HP), " MP: " + "{:>4}".format(self._MP),
              "Stamina: " + "{:>4}".format(self._stamina))


class Elf(CharacterBridge):
    def __init__(self, classImplementation=ClassImplementationInterface()):
        super().__init__(classImplementation)
        self._HP = 200
        self._MP = 200
        self._stamina = 100

    def describeMyself(self):
        print("I am an Elf " + self._class.getDescription())
        print("HP: " + "{:>4}".format(self._HP), " MP: " + "{:>4}".format(self._MP),
              "Stamina: " + "{:>4}".format(self._stamina))


class Orc(CharacterBridge):
    def __init__(self, classImplementation=ClassImplementationInterface()):
        super().__init__(classImplementation)
        self._HP = 400
        self._MP = 20
        self._stamina = 250

    def describeMyself(self):
        print("I am an Orc " + self._class.getDescription())
        print("HP: " + "{:>4}".format(self._HP), " MP: " + "{:>4}".format(self._MP),
              "Stamina: " + "{:>4}".format(self._stamina))


class Mage(ClassImplementationInterface):
    def __init__(self):
        self._bonusHP = 20
        self._bonusMP = 50
        self._bonusStamina = 0
        self._description = "Mage"


class Warrior(ClassImplementationInterface):
    def __init__(self):
        self._bonusHP = 50
        self._bonusMP = 0
        self._bonusStamina = 30
        self._description = "Warrior"


class Thief(ClassImplementationInterface):
    def __init__(self):
        self._bonusHP = 20
        self._bonusMP = 20
        self._bonusStamina = 20
        self._description = "Thief"


if __name__ == "__main__":
    mage = Mage()
    warrior = Warrior()
    thief = Thief()

    character = Human(thief)
    character.describeMyself()

    print("")
    print("Lets change my class")
    print("")

    character.setClassImplementation(warrior)
    character.describeMyself()

    print("")
    print("Lets change my race now")
    print("")

    character = Orc()
    character.describeMyself()

    print("")
    print("Oops. Id better have some class")
    print("")

    character = Elf(mage)
    character.describeMyself()
