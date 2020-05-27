import time
from random import randint
import getpass


def log(func):

    def wrapper(*args, **kwargs):
        f = open('machine.log', 'a')
        name = func.__name__
        name = name.replace("_", " ")
        name = name.title()
        av = time.time()
        func(*args, **kwargs)
        ap = time.time()
        dur = ap - av
        logi = getpass.getuser()
        if dur > 1:
            print(f"({logi}) Running: {name}".ljust(40)
                  + " [ exec-time = {:1.3f} s  ]".format(dur), file=f)
        else:
            print(f"({logi}) Running: {name}".ljust(40)
                  + " [ exec-time = {:1.3f} ms ]".format(dur*1000), file=f)
        f.close()
        return func(*args, **kwargs)
    return wrapper


class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    f = open('machine.log', 'w')
    f.close()
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
