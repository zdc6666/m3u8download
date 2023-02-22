import os
import re
import glob
def merge_to_mp4(name, delete=False):
    rstr = r"[\/\\\:\*\?\"\<\>\|\r\n]" # '/ \ : * ? " < > |'    https://blog.csdn.net/weixin_39880490/article/details/113642415
    #rstr = r'[\\/:*?"<>|\r\n]+'#在[]中*不需要转义,此时*不表示多次匹配,就表示本身的字符
    name = re.sub(rstr, "_", name)# 替换为下划线
    # glob.glob(source_path + '/*.mp4')筛选mp4结尾的文件，按照修改时间排序
    # files = sorted(glob.glob(source_path + '/*.mp4'),key=os.path.getmtime)
    # source_path='./dpcq/'+ 'demo1'
    # print(source_path)
    # aaa=glob.glob(source_path + '/*.mp4')
    # 筛选mp4结尾的文件，按照数字排序
    mp4path = f'./下载视频/{name}/'
    if not os.path.exists(mp4path):
        os.makedirs(mp4path)
    if os.path.exists(f'./下载视频/{name}/{name}.mp4'):
        os.remove(f'./下载视频/{name}/{name}.mp4')
    with open(f'./下载视频/{name}/{name}.mp4', 'wb') as fw:
        files = sorted(glob.glob(f'./{name}/' + '*.mp4'),
                       key=lambda x: int(x.split('\\ts')[1].split('.mp4')[0]))  # int(x[4:-4])指文件名 数字 所在的起始 结束 位置
        for file in files:
            print(file)
            with open(file, 'rb') as fr:
                fw.write(fr.read())
                print(f'\r{file} Merged! Total:{len(files)}', end="     ")
            if delete:
                os.remove(file)#删除文件
        if delete:
            os.rmdir(f'./{name}/')#删除文件夹,文件夹需要为空
            #shutil.rmtree(f'./{name}/')#可以删除带文件的文件夹
