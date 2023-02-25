# m3u8download
## m3u8download是一个简易的根据提供的m3u8文件网址分段下载短视频的工具.可以下载常见的m3u8格式文件,自动使用AES.MODE_CBC解码方式对含有key的m3u8文件进行解密下载.操作简便,设置参数极少。
## 使用方法
### 例如m3u8地址为: https://v6XXXX/hls/index.m3u8
### 一般晚上开机下载一晚上就好,应该没有人每次只下载一个视频吧.批量下载操作如下:
### 1先将m3u8download.py文件、merge.py、和downloadlist.xlsx保存在同一个文件夹内，文件夹命名为download
### 2将需要下载的网址填到文件名为downloadlist.xlsx  excel表格中.其中第一列填m3u8的网址,第二列填需要将文件下载的文件夹名称，填好保存excel并关闭。(第二列可以任意填,但不能出现文件夹非法的字符,如 \ / * ? : "<> | 中的任意一个).
### 3打开windows系统自带的cmd命令窗口，将工作目录切换到download文件夹下（按住SHIFT+鼠标右键download文件夹内空白位置,单击 在终端中打开 进入cmd），输入以下命令实现下载    
    py ./m3u8download
### 4下载完成后,会出现"下载完成！共用时：XX秒.（下载完成后建议在重复下步骤3，因为会有一些短的视频因为网络等原因没有下载到，后面merge后存在缺少视频片段的现象，这个位置其实还可以优化成自动再次下载未下载成功的文件，以后有时间再进行优化）
### 5下载完成后，在download会自动生成数个新的文件夹，新的文件夹内会有很多mp4结尾的文件。这就完整下载好了m3u8内的小文件了。甚至m3u8内含有的加密都顺便解了。
### 6再在cmd命令行中输入以下命令就可以将视频文件合并了
    py ./merge.py
### 7打开download文件夹下的 下载视频 文件夹下的相关文件即可看到合并好的下载文件。
#### 再次强调下，该工具仅仅作为交流学习使用，由该工具下载视频产生的版权问题一概与本工具无关。
  
    



