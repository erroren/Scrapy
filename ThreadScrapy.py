import requests
from lxml import etree
from fake_useragent import UserAgent
import chardet
import lxml
import os
import queue
import threading
from threading import Thread

class crawlThread(threading.Thread):
    def __init__(self,threadName):
        threading.Thread.__init__(self)
        self.threadName = threadName

    def run(self):
        print('线程{}开始'.format(self.threadName))
        self.crawlSpider()
        print('线程{}结束'.format(self.threadName))

    def crawlSpider(self):
        while not page_Queue.empty():
            if page_Queue_Lock.acquire():
                page = page_Queue.get()
                page_Queue_Lock.release()
            url = 'https://www.qiushibaike.com/8hr/page/'+str(page)+'/'
            print('spider:{}   page:{}'.format(self.name, page))
            userAgent = UserAgent()
            ua = userAgent.random
            headers = {'User-Agent': ua}
            timeout = 4
            while timeout >0:
                timeout -= 1
                try:
                    response = requests.get(url,headers=headers)
                    html = response.text
                    data_Queue.put(html)
                    break
                except Exception as e:
                    print(e)

class parserThread(threading.Thread):
    def  __init__(self,threadName):
        threading.Thread.__init__(self)
        self.threadName = threadName

    def run(self):
        print('starting',self.threadName)
        while not exitFlag_Parser:
            try:
                item = data_Queue.get(False)
                self.parse_data(item)
                done = data_Queue.task_done()
            except queue.Empty as empty:
                pass
            except Exception as e:
                print(e)

        print('Exiting',self.threadName)

    def parse_data(self,item):
        dom = etree.HTML(item)
        nodeList = dom.xpath('//div[@class="recommend-article"]/ul/li')
        print(len(nodeList))

def main():
    for i in range(1,11):
        page_Queue.put(i)
    crawlThreads = []

    for i in range(1,4):
        threadName = "crawl" + str(i)
        thread = crawlThread(threadName= threadName)
        thread.start()
        crawlThreads.append(thread)
    parserThreads = []
    for i in range(1,):
        threadName = 'parser' +str(i)
        thread = parserThread(threadName=threadName)
        thread.start()
        parserThreads.append(thread)
    while not page_Queue.empty():
        pass
    for t in crawlThreads:
        t.join()
    while not data_Queue.empty():
        pass
    global  exitFlag_Parser
    exitFlag_Parser = True
    for t in parserThreads:
        t.join()
    print('exiting main Thread')

if __name__ == '__main__':
    data_Queue = queue.Queue()
    page_Queue = queue.Queue(50)
    exitFlag_Parser = False
    page_Queue_Lock = threading.Lock()
    data_Queue_Lock = threading.Lock()
    main()