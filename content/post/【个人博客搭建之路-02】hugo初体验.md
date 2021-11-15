---
title: '【个人博客搭建之路-02】Hugo初体验'
keywords: 个人博客，hugo
date: 2021-11-15T09:30:00+08:00
lastmod: 2021-01-15T09:30:00+08:00
draft: true
description: '搭建博客前的思考和技术选型'
categories: [技术]
tags: [个人博客, hugo]
comments: false
author: Loki
---





### hugo安装

##### macOS（homebrew）

参考[官方文档](https://gohugo.io/documentation/)，macOS使用homebrew，在terminal中执行以下命令

```
brew install hugo
```

验证，在命令行下能够执行`hugo version`即为成功。

![image-20211115173126688](https://raw.githubusercontent.com/Differlong/imgserver/main/img/image-20211115173126688.png)

##### Windows

1. 从[Hugo Releases](https://github.com/gohugoio/hugo/releases)中下载最新的二进制文件

<img src="https://raw.githubusercontent.com/Differlong/imgserver/main/img/image-20211115112609084.png" alt="image-20211115112609084" style="zoom:100%;" />

2. 放到某个地方，并把路径加入到环境变量，方便命令行执行。我是放在了D://MyDriver，并把D://MyDriver放入到环境变量Path中。

3. 验证，在命令行下`hugo`可用。

![image-20211115112923682](https://raw.githubusercontent.com/Differlong/imgserver/main/img/image-20211115112923682.png)



### hugo创建网站

参考官方文档快速开始[Quick Start | Hugo (gohugo.io)](https://gohugo.io/getting-started/quick-start/)。

1. 创建项目。在终端cd到目标文件夹，输入以下命令，则在当前文件家创建了一个名为quickstart的项目，里面包含hugo项目的标准文件。

   ```
   hugo new site quickstart
   ```

2. 进入到项目中。

    ```
    cd ./quickstart
    ```

3. 增加一个主题样式。网上有很多开源的hugo样式，可以在hugo官网上查看。我们需要从GitHub上下载一个theme放在./themes文件夹下。

    ```
    git init
    git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke.git themes/ananke
    ```

    这样在./themes中多了一个ananke文件夹。

    在配置文件config.toml中指定theme为ananke，命令行操作为

    ```
    echo theme = \"ananke\" >> config.toml
    ```

    当然可以直接打开config.toml自己编辑。

4. 增加一个博客文档。hugo的博客文件默认存放在content文件夹下。

    ```
    hugo new posts/my-first-post.md
    ```

    这样就在./content/posts/ 文件夹下创建了一个`my-first-post.md`的markdown文件，并写入了一些基本信息。我们可以自己编辑一下，等会看看效果。

5. 启动hugo server。

    ```
    hugo server -D
    ```

    如此启动了本地的hugo服务器，可以在浏览器去”localhost:1313“（默认地址，具体看执行完命令后的提示地址），看看自己的博客的样子。

    hugo服务器对于改动是实时响应的，所以可以边改边看效果。这就是折腾和探索的乐趣了。



6. 打开config.toml，可以修改参数。具体参考所选的theme和hugo官网[配置文档](https://gohugo.io/themes/customizing/)。

7. build静态网页。

    ```
    hugo -D
    ```

    默认生成在`./public/`里面，需要修改可以在config.toml中修改。如增加`publicDir="docs"`,则生成的配置文件在`./docs/`下。

### 参考

Hugo官网 [The world’s fastest framework for building websites | Hugo (gohugo.io)](https://gohugo.io/)

GitHub代码库 [gohugoio/hugo: The world’s fastest framework for building websites. (github.com)](https://github.com/gohugoio/hugo)

Hugo官方文档 [Hugo Documentation | Hugo (gohugo.io)](https://gohugo.io/documentation/)















































