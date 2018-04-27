import abc


class BaseAnimal(object):
    __metaclass__ = abc.ABCMeta

    @staticmethod
    def kill(animal):
        del animal

    @classmethod
    def assexuate_reproduce(cls):
        return cls()

    @classmethod
    @abc.abstractmethod
    def sex(cls, other):
        """Returns whether a coupling with another animal was sucesfull or not"""

    @classmethod
    def sexuate_reproduce(cls, other):
        return cls(cls.sex(cls, other))
