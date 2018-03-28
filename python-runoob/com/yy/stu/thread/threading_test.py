import threading;
import time;

exitFlag = 0;

class MyThread(threading.Thread):
    def __init__(self, threadId, threadName, delay):
        threading.Thread.__init__(self);
        self.threadId = threadId;
        self.threadName = threadName;
        self.delay = delay;

    def run(self):
        print("开始线程 %s, %s" % (self.threadId, self.threadName));
        # 获取锁，用于线程同步
        threadLock.acquire();
        print_time(self.threadId, self.threadName, self.delay, 5);
        # 释放锁
        threadLock.release();
        print("退出线程 %s, %s" % (self.threadId, self.threadName));

def print_time(threadId, threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit();
        time.sleep(delay);
        print("%s, %s, %s" % (threadId, threadName, time.ctime(time.time())));
        counter -= 1;

# 线程同步锁
threadLock = threading.Lock();
threads = [];

# 创建新线程
thread1 = MyThread("t1", "Thread-1", 1);
thread2 = MyThread("t2", "Thread-2", 2);

# 开启新线程
thread1.start();
thread2.start();
# thread1.join();     # join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
# thread2.join();     # join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。

# 添加线程到线程列表
threads.append(thread1);
threads.append(thread2);

for t in threads:
    t.join();

print("退出主线程");