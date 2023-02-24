# m3u8download
## m3u8download是一个简易的根据提供的m3u8文件网址分段下载短视频的工具.可以下载常见的m3u8格式文件,使用AES.MODE_CBC解码方式对含有key的m3u8文件进行解密下载.操作简便,设置参数少
## 使用方法
### 例如m3u8地址为  https://v6.cdtlas.com/20220801/HPeWT1KN/hls/index.m3u8
### 将下载的短文件存储在当前目录下一个新的文件夹命名为test
    import m3u8download
    m3u8url = r'https://v6.cdtlas.com/20220801/HPeWT1KN/hls/index.m3u8'
    filename = "test"
    m3u8download(m3u8url, filename)
### 下载完成后,会出现"下载完成！共用时：XX秒.
### 一般晚上开机下载一晚上就好,应该没有人每次只下载一个视频吧.批量下载操作如下:
### 先将m3u8download.py文件、merge.py、和downloadlist.xlsx保存在同一个文件夹内
### 先将下载的网址填如到文件名为downloadlist.xlsx  excel表格中.其中第一列填m3u8的网址,第二列填需要将文件下载的文件夹名称(可以任意填,不能出现文件夹非法的字符,如 \ / * ? : "<> | 中的任意一个).
### 在含有
  
    



