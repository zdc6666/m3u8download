# -*- coding:utf-8 -*-
import glob
import os
import ffmpy3
import requests
import re
import time
import openpyxl
import threading  # 多进程
import shipinxiazai
import random  # 随机数
# https://www.lnyzyw.com/
eeeeeeeeeeeeeeeeeeeee webeeeeeeeeeeee
#下载链接
import pandas as pd
aaa = pd.read_excel("qingdan.xlsx", 0, )  # header=None,
for z in aaa.values:
    shipinmingcheng = str(z).split("'")[1]#获取视频名称
    print(shipinmingcheng)
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36",
    }#伪装header
    # 视频搜索
    shipinwangzhi1 = f'https://www.lnyzyw.com/vodsearch/-------------.html?wd={shipinmingcheng}'
    import requests
    proxies = shipinxiazai.get_proxy()#get_proxy()为代理为None，任意数字为使用代理get_proxy(1)，或者get_proxy("任意字符")
    reschushi1 = requests.get(shipinwangzhi1.replace('"', ''), headers=headers, allow_redirects=True,stream=True,
                              #timeout=1,
                              #proxies=proxies,
                              )#timeout=(1, 1)用来分别设置请求超时时间和读取超时时间,单位为秒。
    reschushi1.encoding = reschushi1.apparent_encoding
    from bs4 import BeautifulSoup

    bs = BeautifulSoup(reschushi1.text, 'html.parser')
    # a标签下的class属性为down的，注意是class_，不是class
    # xiazaiwangzhi = xiazaiwangzhibf.find_all("a", class_="download")
    yingpian = bs.find_all("a", class_="btn btn-min btn-primary", )
    if yingpian == []:
        print(f"影片“{shipinmingcheng}” 未找到" )
        pass
    else:
        print(f"影片“{shipinmingcheng}” 已找到，准备爬取")

        aaa = "https://www.lnyzyw.com" + str(yingpian[0]).split('href="')[1].split('1.')[0] + '1' + ".html"  # 获取影片url
        yingpianwangzhi1 = requests.get(aaa.replace('"', ''), headers=headers, allow_redirects=True,stream=True,
                                        cookies=reschushi1.cookies)
        from bs4 import BeautifulSoup

        bs2 = BeautifulSoup(yingpianwangzhi1.text, 'html.parser')
        # a标签下的class属性为down的，注意是class_，不是class
        # xiazaiwangzhi = xiazaiwangzhibf.find_all("a", class_="download")
        wangzhi = bs2.find_all("div", class_="stui-pannel_bd col-pd clearfix")
        aaaa = re.findall(r'href="(.*?).html', str(wangzhi[0]))
        q = 0
        for w in aaaa:
            q = q + 1
            # 建立文件夹
            dir = f"./{shipinmingcheng}/{q}/"#q为第几集
            import os

            if not os.path.exists(dir):
                os.makedirs(dir)
            start = "https://www.lnyzyw.com" + w + ".html"#拼装视频播放url

            threading.Thread(target=shipinxiazai.getVideo,
                             args=[start, dir, q]).start()  # args=(start,)中逗号不能少,设置为守护线程.setDaemon(True) （如果主线程结束了，子也随之结束）

ffmpy3
import ffmpy3
pip install ffmpy3
ffmpeg_path('https://vip.lz-cdn3.com/20221230/16900_109d0a86/1800k/hls/mixed.m3u8', './text/gui.mp4')


# dest_file=f"./{shipinmingcheng}/第{q}集"
    # source_path=dir
    # shipinxiazai.merge_to_mp4(dest_file, source_path, delete=False)
#视频合并
aaa = pd.read_excel("qingdan.xlsx", 0, )  # header=None,
import os
import shipinxiazai
for z in aaa.values:
    shipinmingcheng = str(z).split("'")[1]
    #print(shipinmingcheng)
    dir = f"./{shipinmingcheng}/"
    try:
        for i in os.listdir(dir):
            source_path=dir+i+'/'
            #print(source_path)
            dest_file1=f'./结果/{shipinmingcheng}/'
            #print(dest_file1)
            if not os.path.exists(dest_file1):
                os.makedirs(dest_file1)
            dest_file=dest_file1+f'第{i}集.mp4'
            #判断是否合并过
            if not os.path.exists(dest_file):
                shipinxiazai.merge_to_mp4(dest_file=dest_file, source_path=source_path, delete=False,)
            else:
                pass
        #    if not os.path.exists(dest_file1):
        #           os.makedirs(dest_file1)
        #   dest_file=dest_file1+f'第{1}集.mp4'
            #shipinxiazai.merge_to_mp4(dest_file=dest_file, source_path=source_path, delete=False,)
    except FileNotFoundError as e:
        print(e)
        continue
https://blog.csdn.net/he_spectacular/article/details/126132584

#视频时长不合适的删除
import pandas as pd
os.system('taskkill /f /im ffmpeg.exe')
aaa = pd.read_excel("qingdan.xlsx", 0, )  # header=None,
import os
import shipinxiazai
import shichangpanduan
for z in aaa.values:
    shipinmingcheng = str(z).split("'")[1]
# print(shipinmingcheng)
    dir = f"./{shipinmingcheng}/"
    try:
        for i in os.listdir(dir):
            video_path = dir + i
            shichangpanduan.get_video_durationyou(video_path)
    except FileNotFoundError as e:
        print(e)
        continue
