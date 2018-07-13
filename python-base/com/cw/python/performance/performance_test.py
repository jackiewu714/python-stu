#! /usr/bin/env python
#coding=utf-8
import threading,datetime,time,queue,requests

que = queue.Queue() #函数执行结果池

def call_service():     #调用服务
    res = requests.post(url, data={'data':file})
    que.put(res.text)


def thread_space(threadnum):
    threads = []
    for i in range(threadnum):
        single_t = threading.Thread(target=call_service) #装载线程
        threads.append(single_t)

    starttime = datetime.datetime.now()    #标记开始时间

    for th in threads:
        th.setDaemon(True)  #设置守护
        time.sleep(0.1)
        th.start()         #启动进程
    th.join()

    finishtime = datetime.datetime.now()    #结束时间
    return finishtime - starttime  #返回标记的时间间隔


def test_process(threadnum):
    testvalue = time.strftime("%H:%M:%S", time.localtime(time.time())) + \
                '  ' + "cost:" + str(thread_space(threadnum))

    time.sleep(0.5) #等待线程获取结果
    result = len(file)

#    while not q.empty():
#        result.append(q.get())
    return (testvalue,result)

def write_file(data,count):
    data = str(data)
    count = str(count)
    file_url = 'D:/logs/F5Test/log.txt'
    fp = open(file_url, 'a')
    fp.write(data + ' timer:' + count + '\n')
    fp.close

count = 300
threadnum = 1
# url = "http://test.his.tjh.com:8080/test/TestServlet"
# url = "http://192.168.9.144:8080/test/TestServlet"
url = "http://192.18.100.95:8080/F5Test/TestServlet"
file = open('D:/logs/F5Test/20180713.txt', 'r').read()

while count > 0:
    file = file + str(count)
    message = test_process(threadnum)
    print(message)
    write_file(message, count)
    count = count - 1
    time.sleep(0.2)

