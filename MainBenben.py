import bs4
from bs4 import BeautifulSoup
import requests
import lxml
import time
from lxml import etree
import PostBenben
import os

from goto import with_goto
 

headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

version = 'Luogu Benben v1.5\n按Ctrl+C发犇犇\n_______________________________________\n'
import signal
 
def signal_handler(signal,frame):
    PostBenben.post()
 
signal.signal(signal.SIGINT,signal_handler)


"""
def get_proxy():
    return requests.get("http://123.207.35.36:5010/get/").content

def delete_proxy(proxy):
    requests.get("http://123.207.35.36:5010/delete/?proxy={}".format(proxy))

def getHtml():
    retry_count = 10
    proxy = get_proxy()
    while retry_count > 0:
        try:
            html = requests.get(url = 'https://www.luogu.org/feed/all', headers = headers, timeout = 10 ,proxies={"http": "http://{}".format(proxy)})
            # 使用代理访问
            return html
        except Exception:
            retry_count -= 1
    # 出错5次, 删除代理池中代理
    delete_proxy(proxy)
    return None
"""

def getHtml():
    html = requests.get(url = 'https://www.luogu.org/feed/all', headers = headers, timeout = 10 )
    return html
@with_goto
def get():
    Comment_last = 0
    '''
    global Comment1 
    global Comment2 
    global Comment3 
    global Comment4 
    global Comment5 
    global Comment6 
    global Comment7 
    global Comment8 
    global Comment9 
    global Comment10
    Comment1 = ""
    Comment2 = ""
    Comment3 = ""
    Comment4 = ""
    Comment5 = ""
    Comment6 = ""
    Comment7 = ""
    Comment8 = ""
    Comment9 = ""
    Comment10 = ""
    '''
    label .start
    response = getHtml()

    content = response.content
    html_raw = content.decode()
    html = etree.HTML(html_raw)
    name = html.xpath('/html/body/li[1]/div[2]/header/div/span/a')
    for i in name:
        Name = i.text
    ttime = html.xpath('/html/body/li[1]/div[2]/header/div/text()')
    for i in ttime:
        Time = i
    bsdata = bs4.BeautifulSoup(content, 'html.parser')
    comment_raw = bsdata.find("span",class_="feed-comment")
    Comment = comment_raw.get_text()
    '''
    comment1 = html.xpath('/html/body/li[1]/div[2]/div/span/p')
    for i in comment1:
        Comment1 = i.text
    comment2 = html.xpath('/html/body/li[1]/div[2]/div/span/p/a[1]')
    for i in comment2:
        Comment2 = i.text
    comment3 = html.xpath('/html/body/li[1]/div[2]/div/span/p/text()[2]')
    for i in comment3:
        Comment3 = i
    comment4 = html.xpath('/html/body/li[1]/div[2]/div/span/p/a[2]')
    for i in comment4:
        Comment4 = i.text
    comment5 = html.xpath('/html/body/li[1]/div[2]/div/span/p/text()[3]')
    for i in comment5:
        Comment5 = i
    comment6 = html.xpath('/html/body/li[1]/div[2]/div/span/p/a[3]')
    for i in comment6:
        Comment6 = i.text
    comment7 = html.xpath('/html/body/li[1]/div[2]/div/span/p/text()[4]')
    for i in comment7:
        Comment7 = i
    comment8 = html.xpath('/html/body/li[1]/div[2]/div/span/p/a[5]')
    for i in comment8:
        Comment8 = i.text
    comment9 = html.xpath('/html/body/li[1]/div[2]/div/span/p/text()[5]')
    for i in comment9:
        Comment9 = i	
    Comment = '%s%s%s%s%s%s%s%s%s' % (Comment1, Comment2, Comment3 , Comment4 , Comment5, Comment6, Comment7, Comment8, Comment9)
    '''
    if(Comment==Comment_last):
        time.sleep(1)
    else:
        print('\n')
        print(Name + Time)
        print(Comment)
    time.sleep(1)
    Comment_last = Comment
    goto .start
    
os.system('cls')  
# 等待代理池
# time.sleep(2)
print(version)
get()
os.system('cls')  
