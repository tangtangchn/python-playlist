# encoding: utf-8
# 生产者/消费者模式

import threading
import random
import time

# 全局线程锁
g_lock = threading.Lock()


def producer():
    while True:
        global MONEY
        random_money = random.randint(10, 100)
        # 加锁
        g_lock.acquire()
        MONEY += random_money
        # 解锁
        g_lock.release()
        # 获取当前线程
        print 'producer - %s，生产了%d元' % (threading.current_thread, random_money)
        time.sleep(0.5)


def consumer():
    while True:
        global MONEY
        random_money = random.randint(10, 100)
        if MONEY > random_money:
            print 'consumer - %s，消费了%d元' % (threading.current_thread, random_money)
            # 加锁
            g_lock.acquire()
            MONEY -= random_money
            # 解锁
            g_lock.release()
        else:
            print 'consumer - %s，拟消费%d元，余额为%d元' % (threading.current_thread, random_money, MONEY)
        time.sleep(0.5)


def p_c_test():
    # 执行3个线程，充当producer
    for x in range(3):
        thread = threading.Thread(target=producer)
        thread.start()
    # 执行3个线程，充当consumer
    for x in range(3):
        thread = threading.Thread(target=consumer)
        thread.start()


if __name__ == "__main__":
    MONEY = 50
    p_c_test()
