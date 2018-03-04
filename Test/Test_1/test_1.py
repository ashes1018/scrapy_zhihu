#encoding=utf8
import urllib.request
from bs4 import BeautifulSoup
import requests
import time

User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
# header = {}
header = {'Accept': '*/*',
           'Accept-Language': 'en-US,en;q=0.8',
           'Cache-Control': 'max-age=0',
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
           'Connection': 'keep-alive'
           # 'Referer': 'http://www.baidu.com/'
           }
# header['User-Agent'] = User_Agent


class proxies():
    def __init__(self):
        pass


    def getip(self):
        url = 'http://www.xicidaili.com/nn/1'
        # for i in range(1,2):
        # url = url_1 + str(i)
        # print(url)
        req = urllib.request.Request(url,headers=header)
        res = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(res, 'lxml')
        ips = soup.findAll('tr')
        f = open("C:\\Users\yulan\Desktop\\temp.txt", "wt")
        for x in range(1,len(ips)):
            ip = ips[x]
            tds = ip.findAll("td")
            ip_temp = tds[1].contents[0]+"\t"+tds[2].contents[0]+"\n"
            f.write(ip_temp)
        f.close()

    def varify(self):
        self.getip()
        f = open("C:\\Users\yulan\Desktop\\temp.txt")
        lines = f.readlines()
        proxys = []
        for i in range(0, len(lines)):
            ip = lines[i].strip("\n").split("\t")
            proxy_host = "http://" + ip[0] + ":" + ip[1]
            proxy_temp = {"http": proxy_host}
            proxys.append(proxy_temp)
        url = "http://ip.chinaz.com/getip.aspx"
        for proxy in proxys:
            try:
                res = requests.get(url, proxies=proxy,timeout = 1).status_code
                with open("C:\\Users\yulan\Desktop\\temp1.txt", 'a') as ff:
                    temp = str(proxy).split(',')[0][17:len(str(proxy).split(',')[0]) - 2]
                    # ff.write(string)
                    # print(temp)
                    if res == 200:
                        temp2 = '{' + '"' + 'ipaddr' + '"' + ':' + '"' + temp + '"' + '}' + ','
                        ff.write(temp2 + '\n')
                        print(res)
                        print(proxy)
                    ff.close()
            except:
                continue

temp = proxies()
while 1==1:
    temp.varify()
    print("该次爬取结束")
    time.sleep(600)
    with open("C:\\Users\yulan\Desktop\\temp1.txt", 'w') as fff:
        fff.truncate()
        fff.close()














