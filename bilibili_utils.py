import requests, math
import http.cookiejar

# 获取用户视频列表
def getUserVidewBvids(userId):
    cookie_file = "./cookies/bilibili.txt"
    cookie = http.cookiejar.MozillaCookieJar()
    cookie.load(cookie_file, ignore_discard=True, ignore_expires=True)
    
    header = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"zh-CN,zh;q=0.9,en-US;q=0.8,en-GB;q=0.7,en;q=0.6",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
    }
    pagesize = 30
    pagenumber = 1
    
    response = requests.get("https://api.bilibili.com/x/space/wbi/arc/search?mid={}&ps={}&tid=0&pn={}".format(userId, pagesize, pagenumber), headers=header, cookies=cookie)
    data = response.json()["data"]
    bvids = [bvid["bvid"] for bvid in data["list"]["vlist"]]
    count = data["page"]["count"]
    pagenumber = 2
    while(pagenumber <= math.ceil(count/pagesize)):
        response = requests.get("https://api.bilibili.com/x/space/wbi/arc/search?mid={}&ps={}&tid=0&pn={}".format(userId, pagesize, pagenumber), headers=header, cookies=cookie)
        data = response.json()["data"]
        bvids = bvids + ([bvid["bvid"] for bvid in data["list"]["vlist"]])
        pagenumber +=1
    return bvids