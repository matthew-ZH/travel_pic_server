import urllib.request
import re

__author__ = 'mattlyzheng'

def getHtml(url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36',
            'Upgrade-Insecure-Requests': '1',
            'Referer': 'http://lvyou.baidu.com/pictravel/',
            'Proxy-Connection': 'keep-alive'
        }
        req = urllib.request.Request(
            url=url,
            headers=headers
        )
        proxy_support = urllib.request.ProxyHandler({'http': 'http://web-proxy.oa.com:8080'})
        opener = urllib.request.build_opener(proxy_support, urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        page = urllib.request.urlopen(req)
        html = page.read().decode('utf-8')
        return html


def getImg(html):
    reg = r'"water_url":"(http.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    return imglist
