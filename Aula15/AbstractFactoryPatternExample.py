import abc


class AbstractFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_suv_car(self):
        pass

    @abc.abstractmethod
    def create_economic_car(self):
        pass


class FordFactory(AbstractFactory):
    def create_suv_car(self):
        return EcoSport()

    def create_economic_car(self):
        return FordKa()


class HyundaiFactory(AbstractFactory):
    def create_suv_car(self):
        return IX35()

    def create_economic_car(self):
        return HB20()


class AbstractSUVCar(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def describeMyself(self):
        return "SUV car"


class EcoSport(AbstractSUVCar):
    def describeMyself(self):
        return AbstractSUVCar.describeMyself(self) + ' - EcoSport'


class IX35(AbstractSUVCar):
    def describeMyself(self):
        return AbstractSUVCar.describeMyself(self) + ' - EcoSport'


class AbstractEconomicCar(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def describeMyself(self):
        return "Economic car"


class FordKa(AbstractEconomicCar):
    def describeMyself(self):
        return AbstractEconomicCar.describeMyself(self) + ' - Ford Ka'


class HB20(AbstractEconomicCar):
    def describeMyself(self):
        return AbstractEconomicCar.describeMyself(self) + ' - EcoSport'


if __name__ == "__main__":
    for factory in (FordFactory(), HyundaiFactory()):
        product_a = factory.create_suv_car()
        product_b = factory.create_economic_car()
        print(product_a.describeMyself())
        print(product_b.describeMyself())
