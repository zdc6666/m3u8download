# m3u8download
## m3u8download是一个简易的根据提供的m3u8文件网址分段下载短视频的工具.可以下载常见的m3u8格式文件,使用AES.MODE_CBC解码方式对含有key的m3u8文件进行解密下载.操作简便,设置参数少
## 使用方法
### 例如m3u8地址为  https://v6.cdtlas.com/20220801/HPeWT1KN/hls/index.m3u8
### 将下载的短文件存储在当前目录下一个新的文件夹命名为test
    m3u8url = r'https://v6.cdtlas.com/20220801/HPeWT1KN/hls/index.m3u8'
    filename = "test"
    m3u8download(m3u8url, filename)



