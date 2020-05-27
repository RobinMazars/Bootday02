import math


class TinyStatistician():
    """docstring for TinyStatistician."""

    def __init__(self):
        pass

    def mean(self, x):
        if len(x) != 0:
            return sum(x)/len(x)
        else:
            return None

    def median(self, x):
        le = len(x)
        if le != 0:
            x = sorted(x)
            med = (le)/2
            med = int(math.ceil(med))
            return float(x[med-1])
        else:
            return None

    def quartiles(self, x, percentile):
        le = len(x)
        if le != 0:
            x = sorted(x)
            if percentile == 25:
                med = le/4
            if percentile == 75:
                med = le*(3/4)
            med = int(math.floor(med))
            return float(x[med])
        else:
            return None

    def pow2(self, x):
        return pow(x, 2)

    def var(self, x):
        if len(x) != 0:
            car = list(map(self.pow2, x))
            car = sum(car)/len(x)
            moye = pow(self.mean(x), 2)
            return car - moye
        else:
            return None

    def std(self, x):
        if len(x) != 0:
            return math.sqrt(self.var(x))
        else:
            return None


a = [1, 42, 300, 10, 59]
tstat = TinyStatistician()
print(f"moy {tstat.mean(a)}")
print(f"25% {tstat.quartiles(a, 25)}")
print(f"50% {tstat.median(a)}")
print(f"75% {tstat.quartiles(a, 75)}")
print(f"var {tstat.var(a)}")
print(f"std {tstat.std(a)}")
