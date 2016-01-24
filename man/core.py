__author__ = 'kevin.zhu'
#coding:utf-8

import urllib

from bs4 import BeautifulSoup
from qrencode import genQRcode

url = 'http://www.ishadowsocks.com/'
urlopen = urllib.urlopen(url)
soup = BeautifulSoup(urlopen,"lxml")
tag = soup.find_all(name='div',class_=['col-lg-4'],limit=1)[0]
h4_tags = tag.find_all('h4')
hostname = h4_tags[0].text.split(':')[1]
port = h4_tags[1].text.split(':')[1]
password = h4_tags[2].text.split(':')[1]
method = h4_tags[3].text.split(':')[1]
qr_code = genQRcode(method, password, hostname, port)







