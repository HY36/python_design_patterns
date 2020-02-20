class Observable:
    def __init__(self):
        self.__observers = []

    def add_observer(self, observer):
        self.__observers.append(observer)

    def remove_observer(self, observer):
        self.__observers.remove(observer)

    def notify_observers(self, object=0):
        for o in self.__observers:
            o.update(self, object)


class Observer:
    def update(self, observer, object):
        pass


class WaterHeater(Observable):
    def __init__(self):
        super().__init__()
        self.__temperature = 25

    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, temperature):
        self.__temperature = temperature
        print(f"current temperature is: {self.__temperature}")
        self.notify_observers()


class WashingMode(Observer):
    def update(self, observable, object):
        if isinstance(observable,
                      WaterHeater) and 50 <= observable.get_temperature() < 70:
            print("水已烧好，温度正好！可以用来洗澡了。")


class DrinkingMode(Observer):
    def update(self, observable, object):
        if isinstance(observable, WaterHeater) and observable.get_temperature() >= 100:
            print("水已烧开！可以用来饮用了。")


def tes_water_heater():
    heater = WaterHeater()
    washing_obser = WashingMode()
    drinking_obser = DrinkingMode()
    heater.add_observer(washing_obser)
    heater.add_observer(drinking_obser)
    heater.set_temperature(40)
    heater.set_temperature(60)
    heater.set_temperature(100)


if __name__ == "__main__":
    tes_water_heater()
