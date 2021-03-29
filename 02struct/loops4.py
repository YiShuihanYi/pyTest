# -*- encoding: utf-8 -*-
# threading的用法
import logging
import time
import threading
logging.basicConfig(level=logging.INFO)
loops = [2, 4]
# 定义自己的线程锁
class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        # 参数前面带*，表示传给某个值
        self.func(*self.args)

def loop3(nloop, nsec):
    logging.info(f"start loop {nloop} at {time.ctime}")
    # 循环睡多长时间
    time.sleep(nsec)
    logging.info(f"end loop {nloop} at {time.ctime}")

def main():
    nloops = range(len(loops))
    # 进程锁列表
    threads = []
    for i in nloops:
        # 调用自己定义的线程方法
        t = MyThread(loop3, (i, loops[i]), loop3.__name__)
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    logging.info(f"end all at {time.ctime}")

main()