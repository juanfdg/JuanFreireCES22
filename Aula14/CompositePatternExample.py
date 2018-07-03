from Aula14.BridgePatternExample import *

class GuildMember(object):
    def __init__(self, name, character):
        self.__name = name
        self.__character = character
        self.__subordinates = []

    def appendSubbordinate(self, subordinate):
        self.__subordinates.append(subordinate)

    def removeChild(self, subordinate):
        self.__subordinates.remove(subordinate)

    def describeMyself(self):
        print(self.__name + ': ')
        self.__character.describeMyself()
        print('')

    def getSubordinates(self):
        return self.__subordinates


if __name__ == "__main__":
    Galdur = GuildMember("Galdur the Wise", Human(Mage()))
    Erandur = GuildMember("Erandur the Grey", Elf(Mage()))
    Faendal = GuildMember("Faendal the Dirty", Elf(Thief()))
    Abzug = GuildMember("Abzug the BoneBreaker", Orc(Warrior()))

    Galdur.appendSubbordinate(Abzug)
    Galdur.appendSubbordinate(Erandur)
    Erandur.appendSubbordinate(Faendal)

    Galdur.describeMyself()

    for member in Galdur.getSubordinates():
        member.describeMyself()
        for anothermember in member.getSubordinates():
            anothermember.describeMyself()

    # Erandur left the guild, and so did Faendal

    Galdur.removeChild(Erandur)

    for member in Galdur.getSubordinates():
        member.describeMyself()
        for anothermember in member.getSubordinates():
            anothermember.describeMyself()





