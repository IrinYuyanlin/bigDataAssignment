import threading
import Queue
from spider import Spider
from general import *
from link_finder import *
import domain_parser

PROJECT_NAME = 'SINA_STOCK'
BASE_URL = 'http://vip.stock.finance.sina.com.cn/q/go.php/vIR_StockSearch/key/sz000895.phtml'
DOMAIN_NAME = domain_parser.get_domain_name(BASE_URL)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_THREAD = 4  # set four spiders to crawl urls
queue = Queue.Queue()

Spider(PROJECT_NAME, BASE_URL, DOMAIN_NAME)

def create_workers():
    for _ in range(NUMBER_THREAD):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()
        
def work():
    while True:
        url  = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()
    

def crawl():
    queue_links = file_to_set(QUEUE_FILE)
    if len(queue_links) > 0:
        print('there are ' + str(len(queue_links)) + ' in the queue_links')
        create_jobs()
        
create_workers()
crawl()
