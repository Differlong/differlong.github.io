---
title: "【个人博客搭建之路 04】github_page配置和图床"
draft: true
keywords: 个人博客, hugo
date: 2021-11-21T13:52:49+08:00
lastmod: 2021-11-21T13:52:49+08:00
draft: true
description: '个人博客上传到GitHub以及设置图床'
categories: [技术]
tags: [个人博客,hugo]
comments: false
author: Loki
---

### Github Page配置

Hugo本地博客配置完之后，要把静态文件生成到`./docs`文件夹下。先在`config.toml`中加入`publishDic='docs'`，然后在当前文件夹下命令行调用`hugo -D`。这样生成的静态博客页面就在`./docs`下了。本地的git建好。github上创建一个名字为`你的GitHub用户名.github.io`的repo。然后把本地的git上传到这个repo上来。在setting中配置一下路径。

![image-20211121140019728](https://raw.githubusercontent.com/Differlong/imgserver/main/img/image-20211121140019728.png)



看到GitHub上的build成功提示，即可打开`用户名.github.io`上查看的你在线博客了。

![image-20211121141334833](https://raw.githubusercontent.com/Differlong/imgserver/main/img/image-20211121141334833.png)



看到我的在线博客可以在线访问，完成的满足感不由自主的生发出来。

![image-20211121141535097](https://raw.githubusercontent.com/Differlong/imgserver/main/img/image-20211121141535097.png)

### GitHub图床配置

要用markdown写博客，不可避免的一个问题是图片该怎么办？简单的办法就是放到当前博客的/static文件的目录下，然后编辑的时候使用相对路径。这样写出来的博客自然是可以在线查看，当缺点是写的时候无法查看，因为网络需要的路径和本地的绝对路径或相对路径都不一样。为了在线的展示，必须牺牲掉本地的浏览体验，我是无法接受的。那么只能够选择在线图床。

图床是图片的存储仓库。这样你的博客中用的都是一个在线地址，这样本地浏览和博客访问都是可以正常进行。网上图床很多，大致分为免费的和付费的两种。免费的问题在于加载速度慢，以及无法保证安全性，说不定哪天就关掉了，毕竟人家没有收你钱。付费的当然好，当自己一个小小博客，平时也没几张图片，为了这个花钱实在不值当。有没有既是免费，而且还能够保证安全性的呢？

当然有，万能的GitHub！！！GitHub的repo可以当作图床来用。

如果每次一张图片都要git push一次，然后自己去copy他的地址，再放到md文件中来，操作非常繁琐，对我这种懒人也太不友好了。有没有像正常写md文件的一样，软件自动上传到GitHub图床呢？

你还别说，真有！

我用的是typora写markdown文档，然后用PicGo上传到GitHub上，typora自动把本地的地址转成在线的地址。实现了全自动操作，自己再也不用为图片而烦恼了。

#### PicGo设置

下载PicGo，正常流程配置即可。最重要的是一个GitHub token的获取。在[Personal Access Tokens (github.com)](https://github.com/settings/tokens)页面，点击`generate new token`，过期时间选择无限，然后勾选以下的几个权限。把生成的token填写到PicGo的配置文件中即可。

![image-20211121140511403](https://raw.githubusercontent.com/Differlong/imgserver/main/img/image-20211121140511403.png)

#### Typora配置

在typora的`偏好设置/图片`中，如下设置好采用PicGo上传图片。

![image-20211121143033993](https://raw.githubusercontent.com/Differlong/imgserver/main/img/image-20211121143033993.png)

然后你就可以开心愉快的写博客了！！