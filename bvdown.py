import you_get, sys, json
import bilibili_utils as utils
from threading import Thread

cookiesPath = "./cookies/bilibili.txt"
# bvid = ["bvid1", "bvid2", "bvid3"]
bvids = []
downloadPath = "./download"

def download(url, path, cookiesPath):
    # you-get --format=dash-flv --cookies=./cookies/bilibili.txt --output-dir=./download --no-caption https://www.bilibili.com/video/bvid
    print("downloading ", " ".join(urls))
    sys.argv = ['you-get', '--format=dash-flv','--cookies={}'.format(cookiesPath), '--output-dir={}'.format(path), '--no-caption', url]
    you_get.main()

    
if __name__ == '__main__':
    urls = ["https://www.bilibili.com/video/"+bvid+"/" for bvid in bvids]
    for url in urls:
        download(url, downloadPath, cookiesPath)