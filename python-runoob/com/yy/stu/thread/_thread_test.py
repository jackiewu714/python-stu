import _thread;
import time;
import sys;

# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0;
    while count<5:
        time.sleep(delay);
        count += 1;
        print("%s: %s" % (threadName, time.ctime(time.time())));

try:
    _thread.start_new_thread(print_time, ("thread-1", 2));
    _thread.start_new_thread(print_time, ("thread-2", 3));
except:
    print("启动线程失败，原因：", sys.exc_info());

while 1:
    pass;