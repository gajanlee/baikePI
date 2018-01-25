import requests
from bs4 import BeautifulSoup
import re
from abc import ABC, abstractmethod
import sys

headers = { 'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',}

def log(msg):
    sys.stderr.write(msg + '\n')