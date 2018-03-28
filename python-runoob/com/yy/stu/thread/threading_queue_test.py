import threading;
import queue;
import time;

exitFlag = 0;

class MyThread(threading.Thread):
    def __init__(self, threadId, threadName, workQueue):
        threading.Thread.__init__(self);
        self.threadId = threadId;
        self.threadName = threadName;
        self.workQueue = workQueue;

    def run(self):
        print("开启线程：%s, %s" % (self.threadId, self.threadName));
        process_data(self.threadId, self.threadName, self.workQueue);
        print("退出线程：%s, %s" % (self.threadId, self.threadName));

def process_data(threadId, threadName, workQueue):
    while not exitFlag:
        queueLock.acquire();
        if not workQueue.empty():
            data = workQueue.get();
            queueLock.release();
            print("%s, %s processing %s" % (threadId, threadName, data));
        else:
            print("%s, %s, workQueue is empty." % (threadId, threadName));
            queueLock.release();
        time.sleep(1);

threadNameList = ["Thread-1", "Thread-2", "Thread-3"];
wordList = ["one", "two", "three", "four", "five", "six"];
queueLock = threading.Lock();
workQueue = queue.Queue(10);
threadList = [];
threadId = 1;

# 填充队列
queueLock.acquire();
for word in wordList:
    workQueue.put(word);
queueLock.release();

# 创建新线程
for tName in threadNameList:
    thread = MyThread(threadId, tName, workQueue);
    thread.start();
    threadList.append(thread);
    threadId += 1;

# 等待队列清空
while not workQueue.empty():
    pass;

# 通知线程是时候退出
exitFlag = 1;

# 等待所有线程完成
for t in threadList:
    t.join();

print("退出主线程");