#encoding=utf8
import urllib.request
import urllib
import socket
import requests
socket.setdefaulttimeout(3)
f = open("C:\\Users\yulan\Desktop\\temp.txt")
lines = f.readlines()
proxys = []
for i in range(0,len(lines)):
    ip = lines[i].strip("\n").split("\t")
    proxy_host = "http://"+ip[0]+":"+ip[1]
    proxy_temp = {"http":proxy_host}
    proxys.append(proxy_temp)
url = "http://ip.chinaz.com/getip.aspx"
for proxy in proxys:
    try:
        res = requests.get(url, proxies = proxy)
        with open("C:\\Users\yulan\Desktop\\temp1.txt", 'a') as ff:
            temp = str(proxy).split(',')[0][17:len(str(proxy).split(',')[0])-1]
            temp2 = '{' + '"' + 'ipaddr' + '"' + ':' + '"' + temp + '"' + '}' + ','
            ff.write(temp2+'\n')
            print (res)
            print(proxy)
    except:
        continue
# f.close()