import threading
from queue import Queue
from spider import Spider
from general import *
from domain import *

PROJECT_NAME = 'wikepedia'

HOMEPAGE = 'https://www.wikipedia.org/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + './queue.txt'
CRAWLED_FILE = PROJECT_NAME + './crawled.txt'
NUMBER_OF_THREADS = 2
queue = Queue()
Spider(PROJECT_NAME,HOMEPAGE,DOMAIN_NAME)

#Each queue link is a new jobs

def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True #will exist when main closes
        t.start()

#Do the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name,url)
        queue.task_done()

def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()

def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + 'links in the queue')
        create_jobs()

create_workers()
crawl()