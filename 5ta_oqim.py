import threading
from datetime import timedelta

import httpx
import redis

con = redis.Redis(host='localhost', port=6379, decode_responses=True)


def oqim1():
    reg = httpx.get(url="https://kun.uz/").read()
    mystr = reg.decode("utf8")
    con.set(name="kun.uz", value=mystr, ex=timedelta(seconds=60))


def oqim2():
    reg = httpx.get(url="https://daryo.uz/").read()
    mystr = reg.decode("utf8")
    con.set(name="daryo.uz", value=mystr, ex=timedelta(seconds=60))


def oqim3():
    reg = httpx.get(url="https://qalampir.uz/").read()
    mystr = reg.decode("utf8")
    con.set(name="qalampir.uz", value=mystr, ex=timedelta(seconds=60))


def oqim4():
    reg = httpx.get(url="https://xabardor.uz/uz/").read()
    mystr = reg.decode("utf8")
    con.set(name="xabardor.uz", value=mystr, ex=timedelta(seconds=60))


def oqim5():
    reg = httpx.get(url="https://kundalik.com/userfeed").read()
    mystr = reg.decode("utf8")
    con.set(name="xabardor.uz", value=mystr, ex=timedelta(seconds=60))


if __name__ == '__main__':
    threeds = []
    thread1 = threading.Thread(target=oqim1)
    thread2 = threading.Thread(target=oqim2)
    thread3 = threading.Thread(target=oqim3)
    thread4 = threading.Thread(target=oqim4)
    thread5 = threading.Thread(target=oqim5)
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()