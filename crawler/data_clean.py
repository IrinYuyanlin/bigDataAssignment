import pandas as pd
import pickle
from spider import Spider
from general import *
# in this session, we will collect table in each page_url
#----------------------------------------------------------------------


class dataFinder:
	path = ''
	url_set = set()
	url_list = list()
	dataDf = pd.DataFrame()

    def __init__(self, path):
    	self.path = path
    	dataFinder.loadurl()
    	url_list = list(url_set)
    	dataFinder.dataDf = pd.DataFrame()

    @staticmethod
    def loadurl(self.path):
    	dataFinder.url_set = file_to_set(self.path)

    @staticmethod
    def readTable(dataFinder.url_set):
    	for url in url_list:
    		try:
    			url_contents = pd.read_html(url) # it will get table in the given url, return a dataframe
    			url_contents = url_contents[1:] # we do not need the titles
    			dataFinder.concanateDf(dataFinder.dataDf, url_contents)
    			file_name = str(url_list.index(url)) + '.pickle'
    			f = open(file_name, 'wb')
    			pickle.dump(url_contents, f)
    			f.close()
    		except:
    			print("Error: can't read url.")
    	file_name = 'total.pickle'
    	f = open(file_name, 'wb')
    	pickle.dump(dataFinder.dataDf, f)
    	f.close()

    @staticmethod
    def concanateDf(dataFinder.dataDf, url_contents):
    	dataFinder.dataDf = pd.concat(dataFinder.dataDf, url_contents)
