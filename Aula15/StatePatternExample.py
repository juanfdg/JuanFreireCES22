import abc
import time


class Semaphore:
    def __init__(self, state):
        self._state = state

    def set_state(self, state):
        self._state = state

    def request(self):
        self._state.handle()


class State(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def handle(self):
        pass


class GreenLight(State):
    def handle(self):
        print("Green Light - You are free to go")


class YellowLight(State):
    def handle(self):
        print("Yellow Light - Be aware")


class RedLight(State):
    def handle(self):
        print("Red Light - Stop!")


if __name__ == "__main__":
    green_light = GreenLight()
    yellow_light = YellowLight()
    red_light = RedLight()

    semaphore = Semaphore(green_light)
    states = [green_light, yellow_light, red_light]

    state = 0
    while True:
        semaphore.set_state(states[state])
        semaphore.request()
        state = (state+1) % len(states)
        time.sleep(5)

