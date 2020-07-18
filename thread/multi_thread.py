# encoding: utf-8

import threading
import time


def greet(index):
    print 'hello world - %d' % index
    time.sleep(0.5)


def line_run():
    for x in range(5):
        greet(x)


def async_run():
    for x in range(5):
        thread = threading.Thread(target=greet, args=[x])
        thread.start()


if __name__ == "__main__":
    line_run()
    async_run()
