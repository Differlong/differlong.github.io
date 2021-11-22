---
title: "【个人博客搭建之路 03】Hugo踩坑实录"
draft: true
keywords: 个人博客, Hugo
date: 2021-11-21T13:08:20+08:00
lastmod: 2021-11-21T13:08:20+08:00
draft: true
description: '记录hugo搭建过程中遇到的坑和解决方案'
categories: [技术]
tags: [个人博客,Hugo]
comments: false
author: Loki
---

### 大致了解

搭建完Hugo的初始页面，随意编写几个测试的md，调用`hugo server -D`即可看到实际效果和改动变化。再没有配置参数的情况下，页面非常简陋，而且会有一些bug出来。如何调试出令人满意的页面呢？

如果不会，先去看文档。先后看了[Hugo文档页面](https://gohugo.io/getting-started/configuration/)关于参数的描述，之后去hugo theme的GitHub页面去看安装说明，对于整体情况有一个大致的了解。

hugo的参数配置在`config.toml`中。每个theme的文件夹中，其中有一个`exampleSite`的文件夹，里面是一个示例网站的配置，可以把`config.toml`文件复制到主文件夹，即可看到示例的效果。改动配置文件的一些参数成自己的参数，在浏览器`localhost:1313`中可以看到实时的效果改变。

### 解决bug

这样一个基本的博客网站搭成了，当还有一些小bug。以下记录我曾经遇到的小bug和解决办法。

1. 修改了配置文件但是`localhost:1313`页面没啥改变。

   可以在命令行中用`ctrl + c`关掉服务器，然后再重启，这样效果就出来了。

2. 更新了图标一直刷新不出来。

   浏览器有一些缓存的机制，用`ctrl+shift+R`强制刷新。即可看到更新的图标。

3. 配置的主题里面放了一堆国外的链接，像国内知乎豆瓣的网站的图标没有。

   这个没啥办法，主题是外国人做的，所以css里面存的都是国外的常用网址。要用国内的一些常用网址，需要选用国内人制作的theme。我是去网上搜中国人的用Hugo做的博客和相关主题，我用的是jane这个主题。然后clone下别人的博客，研究别人的做法，从模仿开始。这个过程让我进步很大。自己博客还是不完成品，改动是要做加法，而做加法是一个需要不断试错的过程。而研究别人的博客，是在完成品的基础上做减法，自己改动了哪里，效果一下子自己出来了，立刻就明白了这么参数的意义是什么了。国人做的博客，常用的中国网站都有图标。这样就很省很多事情，自己去重新做一个还是蛮麻烦的一件事情。

4. 网站的logo怎么设置？

   网站logo需要.ico文件和不同尺寸的png文件。找一张自己的图片，然后在网上搜“ico 在线”，即可看到一些在线编辑的网站。我用的是[favicon制作 - 在线工具 (tool.lu)](https://tool.lu/favicon/)，还是挺好用的。然后把下载来的图片放到./static的文件夹下，并且重命名。加载图标的文件地址在`./themes/主题/layout/partials/custom_favicon.html`中，名字对应即可。在浏览器查看时需要`ctrl+shift+R`强制刷新加载，不然一直看不出变化，我被坑了很久。
   
5. 遇到一个诡异的bug：在本地测试一切正常，上传到GitHub上也一切正常。但是在移动端下，点击横幅的那个按钮，打不开横幅，导致无法切换掉其他页面。在浏览器下调试，说是一个校验的问题， 人都要傻了。

   ```
   Failed to find a valid digest in the 'integrity' attribute for resource 'xxx' with computed SHA-256 integrity 'xxx'. The resource has been blocked.
   Unknown error occurred while trying to verify integrity.
   ```

   解决办法。各种网上查，没啥办法，我也不想去改前端和后端的代码，都不知道bug出在哪一行。最后的看到一个办法，把工程重新编译一遍，可能是编译的问题。死马当活马医，删除掉`./docs`下的文件，重新`hugo -D`，上传到GitHub。竟然发现问题解决了。

   神奇的bug。build的时候也能够出错的吗？

### 感想

整个调试的过程就是一个代码debug的过程，不断发现问题，然后想尽各种办法去寻找解决方案。最烦恼在这，最快乐也在这。





























