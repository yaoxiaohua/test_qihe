# coding :utf-8
import requests
from bs4 import BeautifulSoup

muick = open('muick.txt', 'a',encoding='utf8')
name = []
URL = []
sc = []
bf = []
r = 0
l = 0
d = 0
while d < 1225:
    url = 'https://music.163.com/discover/playlist?order=hot&cat=%E6%B0%91%E8%B0%A3&limit=35&offset='+'%s'%d
    print(url)
    h = {
        'Host': 'music.163.com',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4094.1 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'https://music.163.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8'
    }
    s = requests.session()
    w = s.get(url,headers=h)   #verify=False
    t = w.text
    soup = BeautifulSoup(t, 'lxml')
    list = soup.select('a.tit')
    for z1 in list:
        name.append(z1.string)
        muick.writelines(z1.string)
        muick.writelines('\n')
    for l in range(len(list)):
        url2 = 'https://music.163.com'+list[l]['href']
        w2 = s.get(url2)
        URL.append(url2)
        muick.writelines(url2)
        muick.writelines('\n')
        t2 = w2.text
        soup2 = BeautifulSoup(t2, 'lxml')
        list2 = soup2.select('a.u-btni-fav i')
        sc.append('收藏：' )
        muick.writelines('收藏：' )
        sc.append(list2[0].string)
        muick.writelines(list2[0].string)
        muick.writelines('\n')
        list3 = soup2.select('div.more')
        bf.append(soup2.select('div.more')[0].get_text())
        muick.writelines(soup2.select('div.more')[0].get_text())
        muick.writelines('\n')
        print('第%s首'%l)
        l+=1
    d+=35
