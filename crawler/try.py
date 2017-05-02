import pandas as pd

PROJECT_NAME = 'SINA_STOCK'
BASE_URL = 'http://vip.stock.finance.sina.com.cn/q/go.php/vIR_StockSearch/key/sz000895.phtml'
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_THREAD = 4  # set four spiders to crawl urls

df = pd.read_html(BASE_URL)
print(df[1:3][1])