#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Aladdin'

urls = [
    'http://baidu.com.com',
    'https://www.csdn.net/',
    'https://blog.csdn.net/',
    'https://edu.csdn.net/',
]
urls = urls*10 #生成40个url
import time
import requests
from tomorrow import threads
@threads(100)
def download(url):
    try:
        return requests.get(url,timeout=0.7)
    except:
        pass
start = time.time()
responses = [download(url) for url in urls]
html = [response.text for response in responses if hasattr(response,"text")]
end = time.time()
print ("Time: %f seconds" % (end - start))

# 调用100各线程总时间为1.91s,一个一个访问为26.13s