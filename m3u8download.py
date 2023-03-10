# -*- coding：utf-8 -*-
import requests
import re
import time
import random  # 随机数
import datetime
from Crypto.Cipher import AES  # pip install pycryptodome(只限windows)
import pandas as pd
import threading
def m3u8download(m3u8url, filename):
    #rstr = r"[\/\\\:\*\?\"\<\>\|\r\n]" # '/ \ : * ? " < > |'    https://blog.csdn.net/weixin_39880490/article/details/113642415
                 #rstr = r'[\\/:*?"<>|\r\n]+'#在[]中*不需要转义,此时*不表示多次匹配,就表示本身的字符
    #filename = re.sub(rstr, "_", filename)# 替换为下划线
    start = datetime.datetime.now().replace(microsecond=0)
    headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36"}
    m3u8 = requests.get(m3u8url.replace('"', ''), headers=headers, stream=True, allow_redirects=True)
    m3u8.encoding = m3u8.apparent_encoding  # 网页文字编码
    keyurl = re.findall('#EXT-X-KEY:METHOD=AES-128,URI="(.*?)"', m3u8.text)
    if keyurl:  # 存在值即为真
        key = requests.get(keyurl[0].replace('"', ''), headers=headers, stream=True, allow_redirects=True)
        keykey = key.text
    else:  # 不存在时跳过
        keykey = []
        # print('无key.key值')
        pass
    if m3u8.status_code != 200:
        print(f'{filename} m3u8文件获取失败')
        pass
    else:
        # 拿取视频的全部路径列表
        m3u8list = re.findall(r',\n(.*?)\n#', m3u8.text)  # \n开始，\n#结束。就是单个ts文件地址汇总
        print(f'{filename} m3u8文件获取成功')
        if not os.path.exists(f'./{filename}/'):
            os.makedirs(f'./{filename}/')
        count = 0
        for tsurl in m3u8list:
            count += 1
            time.sleep(random.uniform(0, 0.6))  # 慢慢下载每一个
            try:  # 报错防止跳出
                if os.path.exists(f'./{filename}/ts{count}.mp4'):
                    print(f"视频{filename}  'ts{count}.mp4  文件已存在，跳过下载")  # 文件已存在，跳过
                    pass
                else:
                    ts = requests.get(tsurl, stream=True, headers=headers, allow_redirects=True,
                                      timeout=10)  # 核心代码，下载每一个ts文件
                    ts.encoding = ts.apparent_encoding
                    print(
                        f'视频{filename}，总共有{len(m3u8list)}个ts片段，第{str(count)}个已下载完成，key为{keykey},状态为{ts.status_code}')
                    with open(f'./{filename}/ts{count}.mp4', "wb") as mp4:
                        if keykey:  # 判断keykey不为为空时
                            cryptor = AES.new(keykey.encode('utf-8'), AES.MODE_CBC)
                            # 边拿边从内存写到硬盘里
                            for chunk in ts.iter_content(chunk_size=1024 * 1024):
                                if chunk:
                                    mp4.write(cryptor.decrypt(chunk))
                                    # print('含key视频下载完成')
                        else:  # 判断keykey为空时
                            for chunk in ts.iter_content(chunk_size=1024 * 1024):
                                if chunk:
                                    mp4.write(chunk)
                                    # print('无加密key视频下载完成')
                        mp4.seek(0x00)  # 伪装成png格式需要更改头部信息，seek代表指针跳到0的位置     0x代表16进制   00代表0的位置
                        mp4.write(b'\xff\xff\xff\xff')  # \x代表16进制   写入4个ff
                        mp4.flush()
                        mp4.close()
            except requests.exceptions.RequestException as e:
                print(
                    f'视频{filename}，总共有{len(m3u8list)}个ts片段，第{str(count)}个下载失败(可能断网)，状态为{ts.status_code}{e}')
                # tsurl count
                continue
    end = datetime.datetime.now().replace(microsecond=0)
    print("下载完成！共用时：%s 秒" % (end - start))

aaa = pd.read_excel("downloadlist.xlsx", 0, )  # header=None,
for z in aaa.values:
    m3u8url = z[0]
    dir = f"./m3u8download/{z[1]}/"
    import os
    if not os.path.exists(dir):
        os.makedirs(dir)
    threading.Thread(target=m3u8download, args=[m3u8url, dir]).start()

