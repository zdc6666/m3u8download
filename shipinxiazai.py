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

#"https://www.lnyzyw.com/vodplay/27298-1-1.html"
# https://www.lnyzyw.com/


def get_proxy(*zhuangtai):#get_proxy()为代理为None，任意数字为使用代理get_proxy(1)，或者get_proxy("任意字符")
    if zhuangtai:
        import requests
        url = 'https://bz.nulls.cn/getIpProxy'
        proxy = requests.get(url).json()
        proxies = {"http": f"http://{proxy['data']['proxy']}"}
    else:
        proxies = {'http': None, 'https': None}
    return proxies




def getVideo(start,dir,q):
    pathUrl = start
    dir=dir
    q=q
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36",
    }
    proxies = get_proxy()#get_proxy()为代理为None，任意数字为使用代理get_proxy(1)，或者get_proxy("任意字符")
    # 需要先拿到index.m3u8文件
    reschushi = requests.get(pathUrl.replace('"', ''), headers=headers, allow_redirects=True, stream=True,proxies=proxies)#打开播放视频网页
    # from bs4 import BeautifulSoup
    # bf=BeautifulSoup(reschushi.text, 'html.parser')
    # xiazaiwangzhi = bf.find_all("a", class_="download")
    ##################################找到m3u8的url
    aaa = re.findall('"url":(.*?),', reschushi.text)##整个项目最核心代码，在视频播放页f12，元素中搜索m3u8或者url或者aaa，找到m3u8的网址，m3u8的实际网址在播放页面的JS代码中找到！！！！！几乎所有网站的视频都能刚刚找到
    ##################################################################################
    bbb = aaa[1].replace('\\', '')
    ccc = bbb.split("/")[2]
    reschushi2 = requests.get(bbb.replace('"', ''), headers=headers, stream=True, allow_redirects=True,proxies=proxies )
    ddd = reschushi2.text.split('\n')[2]
    pathUrl = "https://" + ccc + ddd
    res = requests.get(pathUrl.replace('"', ''), headers=headers, stream=True, allow_redirects=True,proxies=proxies )
    res.encoding = res.apparent_encoding  # 网页文字编码
    keyurl=re.findall('#EXT-X-KEY:METHOD=AES-128,URI="(.*?)"', res.text)
    if keyurl: # 存在值即为真
        #print(f'有key.key值,使用代理为{proxies}，')
        key=requests.get(keyurl[0].replace('"', ''), headers=headers,stream=True,allow_redirects=True,proxies=proxies)
        keykey=key.text
    else:# 不存在时跳过
        keykey=[]
        #print('无key.key值')
        pass


    if res.status_code != 200:
        print(f'{dir}第{q}集m3u8文件获取失败，代理为{proxies}')
        pass
    else:
        # 拿取视频的全部路径列表
        urlList = re.findall(r',\n(.*?)\n#', res.text)#\n开始，\n#结束。就是单个ts文件地址汇总
        print(f'{dir}第{q}集m3u8文件获取成功，代理为{proxies}')
        count = 0
        for item in urlList:
            time.sleep(random.uniform(0, 0.6))# 慢慢下载每一个
            count += 1
            try:  # 报错防止跳出
                if os.path.exists(f'{dir}demo{count}.mp4'):
                    print(f"电视剧{dir} + 'demo{count}.mp4  文件已存在，跳过")#文件已存在，跳过
                    pass
                else:
                    res2 = requests.get(item, stream=True, headers=headers, allow_redirects=True, timeout=10, proxies=proxies)#核心代码，下载每一个ts文件
                    res2.encoding = res2.apparent_encoding
                    print(f'电视剧{dir}，总共有{len(urlList)}个片段，第{str(count)}个已下载完成，状态为{res2.status_code}，代理为{proxies}')
                    with open(dir + 'demo{}.mp4'.format(str(count)), "wb") as mp4:
                        if keykey :#判断keykey不为为空时
                            from Crypto.Cipher import AES  # pip install pycryptodome(只限windows）
                            cryptor = AES.new(keykey.encode('utf-8'), AES.MODE_CBC)
                            # 边拿边从内存写到硬盘里
                            for chunk in res2.iter_content(chunk_size=1024 * 1024):
                                if chunk:
                                    mp4.write(cryptor.decrypt(chunk))
                                    print('含key视频下载完成')
                        else:#判断keykey为空时
                            for chunk in res2.iter_content(chunk_size=1024 * 1024):
                                if chunk:
                                    mp4.write(chunk)
                                    print('无加密key视频下载完成')
                                mp4.seek(0x00)#伪装成png格式需要更改头部信息，seek代表指针跳到0的位置     0x代表16进制   00代表0的位置  
                                mp4.write(b'\xff\xff\xff\xff')#\x代表16进制   写入4个ff
                                mp4.flush()
                                mp4.close()
            except requests.exceptions.RequestException as e:
                print(f'{dir}第{q}集，总共有{len(urlList)}个片段，第{str(count)}个下载失败(可能断网)，状态为{res2.status_code}，代理为{proxies}')
                continue

def merge_to_mp4(dest_file, source_path, delete=False):
        # glob.glob(source_path + '/*.mp4')筛选mp4结尾的文件，按照修改时间排序
		# files = sorted(glob.glob(source_path + '/*.mp4'),key=os.path.getmtime)
		# source_path='./dpcq/'+ 'demo1'
		# print(source_path)
		# aaa=glob.glob(source_path + '/*.mp4')
        # 筛选mp4结尾的文件，按照数字排序
    with open(dest_file, 'wb') as fw:
        files = sorted(glob.glob(source_path + '*.mp4'), key=lambda x: int(x.split('\\demo')[1].split('.mp4')[0]))  # int(x[4:-4])指文件名 数字 所在的起始 结束 位置
        for file in files:
            print(file)
            with open(file, 'rb') as fr:
                fw.write(fr.read())
                print(f'\r{file} Merged! Total:{len(files)}', end="     ")
            if delete:
                os.remove(file)


                # ————————————————
                # 版权声明：本文为CSDN博主「Edward.W」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
                # 原文链接：https://blog.csdn.net/u013379032/article/details/120705889


