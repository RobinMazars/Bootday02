from time import sleep


def progressebar(listy):
    maxi = max(listy) + 1
    for x in listy:
        yield x
        pourc = (x/maxi)*100
        # print(pourc)
        print("[{:>3.0f}%]".format(pourc), end="")
        print("[{:=>{}}>{}]".format("", pourc, (100-int(pourc))*" "), end="")
        print(f" x = {x}/{maxi}")


listy = range(100)
ret = 0
for elem in progressebar(listy):
    ret += elem
    sleep(0.5)
    # print(ret)
print()
# print(ret)
