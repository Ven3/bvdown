# BV Down

B站视频下载工具

## 依赖

you-get

```shell
pip install you-get
```

FFmpeg 

[Download FFmpeg](https://ffmpeg.org/download.html)

## 使用 - 以Edge为例

1. 打开Edge浏览器, 安装扩展插件 [Cookie-Editor - Microsoft Edge Addons](https://microsoftedge.microsoft.com/addons/detail/cookieeditor/neaplmfkghagebokkhpjpoebhdledlfi?hl=zh-CN)
2. 登录B站
3. 登录B站成功之后, 点击Cookie-Edit插件, 点击右下角的Export按钮
4. 将复制的Cookie内容粘贴在[./cookies/bilibili.txt](./cookies/bilibili.txt) 文件中
5. 打开bvdown.py, 将要下载的视频bvid粘贴到bvids = [] 里面
6. 控制台输入 python bvdown.py 开始执行下载

```shell
python bvdown.py
```

## Bvid获取

1. 可以通过bilibili_utils.py获取
   在编辑好cookie.txt文件后, 通过bilibili_utils.py文件的getUserVidewBvids方法, 传入要获取bvid的用户id, 即可获取该用户的所有视频bvid
2. 从浏览器中复制对应视频的bvid
