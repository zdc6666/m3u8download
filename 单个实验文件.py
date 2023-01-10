# -*- coding：utf-8 -*-
import glob
import os
import requests
import re
import time
import pandas as pd
import openpyxl
import threading  # 多进程
import random  # 随机数


start=r"https://www.lnyzyw.com/vodplay/801-1-3.html"#小仵作
start=r"https://www.lnyzyw.com/vodplay/43865-1-1.html"#阿凡达

start=r"https://www.69mj.com/index.php/vod/play/id/35846/sid/1/nid/1.html"




import os
q=1
dir = f"./阿凡达/{q}/"
if not os.path.exists(dir):
    os.makedirs(dir)
def getVideo(start,dir,q):
    pathUrl = start
    dir=dir
    q=q
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36",
    }
    # 如果输入excel表中是原始网址，需要先拿到index.m3u8文件，该段注释释放出来
    reschushi = requests.get(pathUrl.replace('"', ''), headers=headers, allow_redirects=True, stream=True)
    # from bs4 import BeautifulSoup
    # bf=BeautifulSoup(reschushi.text, 'html.parser')
    # xiazaiwangzhi = bf.find_all("a", class_="download")
    #####################################################'''

    aaa = re.findall('"url":(.*?),', reschushi.text)
    bbb = aaa[1].replace('\\', '')
    ccc = bbb.split("/")[2]
    reschushi2 = requests.get(bbb.replace('"', ''), headers=headers, stream=True, allow_redirects=True, )
    ddd = reschushi2.text.split('\n')[2]
    pathUrl = "https://" + ccc + ddd

    pathUrl = r"https://hls.cache.xiamm.cc/private/cache/20230106/1312/29336847311320d779f0ef93ec795a88.m3u8?st=bYsRxG0_vPCgNr_dOfXAIw&e=1672937062"
    res = requests.get(pathUrl.replace('"', ''), headers=headers, stream=True, allow_redirects=True, )
    res.encoding = res.apparent_encoding  # 网页文字编码
    keyurl=re.findall('#EXT-X-KEY:METHOD=AES-128,URI="(.*?)"', res.text)
    if keyurl: # 存在值即为真
        print('有key.key值')
        key=requests.get(keyurl[0].replace('"', ''), headers=headers,stream=True,allow_redirects=True,)
        keykey=key.text
    else:# 不存在时跳过
        keykey=[]
        print('无key.key值')
        pass


    if res.status_code != 200:
        print(f'{dir}第{q}集m3u8文件获取失败')
        pass
    else:
        # 拿取视频的全部路径列表
        urlList = re.findall(r',\n(.*?)\n#', res.text)

        print(f'{dir}第{q}集m3u8文件获取成功')
        count = 0
        for item in urlList:

            item=urlList[0]


            # 慢慢拿取，假装人为，一共395个文件，没加sleep，我只拿取了170个，加了全拿下来了
            time.sleep(random.uniform(0, 0.6))
            count += 1
            try:  # 报错防止跳出
                if os.path.exists(f'{dir}demo{count}.mp4'):
                    # print(f"电视剧{dir} + 'demo{count}.mp4  文件已存在，跳过")
                    pass
                else:
                    res2 = requests.get(item, stream=True, headers=headers, allow_redirects=True, timeout=30)
                    res2.encoding = res2.apparent_encoding
                    print(f'电视剧{dir}，总共有{len(urlList)}个片段，第{str(count)}个已下载完成，状态为{res2.status_code}')
                    with open(dir + 'demo{}.mp4'.format(str(count)), "wb") as mp4:
                        if keykey :#判断keykey不为为空时
                            from Crypto.Cipher import AES  # pip install pycryptodome(只限windows）
                            cryptor = AES.new(keykey.encode('utf-8'), AES.MODE_CBC)
                            # 边拿边从内存写到硬盘里
                            for chunk in res2.iter_content(chunk_size=1024 * 1024):
                                if chunk:
                                    mp4.write(cryptor.decrypt(chunk))
                                    print('加密下载完成')
                        else:#判断keykey为空时
                            for chunk in res2.iter_content(chunk_size=1024 * 1024):
                                if chunk:
                                    mp4.write(chunk)
                                    print('未加密下载完成')
                                mp4.seek(0x00)
                                mp4.write(b'\xff\xff\xff\xff')
                                mp4.flush()
                                mp4.close()
            except requests.exceptions.RequestException as e:
                print(f'{dir}第{q}集，总共有{len(urlList)}个片段，第{str(count)}个已下载失败，状态为{res2.status_code}')
                continue

https://ali2.a.kwimgs.com/ufile/adsocial/c8c090d1-4b4f-4936-ae3e-aa0d7aef30d9.jpg

https: // hls.cache.xiamm.cc / private / cache / 20230105 / 5255 / 0cd4c70526b04f039ab3f60f78a03176.m3u8?st = w325v6efRnTtFA_WpqNe5Q & e = 1672928730
https://cdn5.hls.shenglinyiyang.cn/hls/103c6c88266e13120523382e80e4e09d37779b0809f89c5b464f34195fc2bcb6af43123e8effb05b74d175fd8b40592da24ce5347b9b85d2fad6894389c84dadeba49f936b414a2dc1a93504db9cc37581.ts
?auth_key=1672970130-839e8102d637d8eef8f8cceb71da8839-0-a18c83f6efe594701a33f98b3c4a7a69&e=1672970130


