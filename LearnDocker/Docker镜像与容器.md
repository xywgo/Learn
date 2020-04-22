## 什么是镜像

**Docker镜像**是由多层文件系统叠加而成。每一层的文件系统也可以理解成一个镜像，依次叠加，依次依赖。最底端是一个引导文件系统，即bootfs，。第二层是root文件系统rootfs，它位于引导文件系统之上。再往上是专有镜像层。

每一层都是只读层，当从一个**Docker镜像**启动容器时，会在最顶层加载一层读写层（容器）。







![](https://tva1.sinaimg.cn/large/007S8ZIlgy1ge08d5ozc8j30cs0a4gma.jpg)

## 拉取镜像

命令格式：

```bash
docker pull [选项] [Docker Registry 地址[:端口号]/]仓库名[:标签]
```

- Docker 镜像仓库地址：地址的格式一般是 `<域名/IP>[:端口号]`。默认地址是 Docker Hub。
- 仓库名：仓库名是两段式名称，`<用户名>/<软件名>`。对于 Docker Hub，如果不给出用户名，则默认为 `library`，也就是官方镜像。



### 列出镜像

命令格式：

```bash
docker image ls [选项] [镜像仓库源[:标签]]
```

参数说明

- `-a`:列出所有的镜像（默认会藏中间层镜像）
- `-f`：基于所给条件过滤
- `-q`：只显示ID

#### 镜像体积

通过以下命令来便捷的查看镜像、容器、数据卷所占用的空间

```bash
docker system df
```

#### 虚悬镜像

在查看镜像列表是有时会看到下面这样的无标签的。

```bash
<none>               <none>              00285df0df87        5 days ago          342 MB
```

这类无标签镜像也被称为 **虚悬镜像(dangling image)** ，已经没什么用了。下面的命令可以专门查看。

```bash
docker image ls -f dangling=true
```

删除这些镜像的命令

```bash
docker image prune
```

### 删除镜像

命令格式：

```bash
docker image rm [选项] <镜像1> [<镜像2> ...]
```

其中，`<镜像>` 可以是 `镜像短 ID`、`镜像长 ID`、`镜像名` 或者 `镜像摘要`。

参数说明：

* `-f`，`--force`:强制删除

## 什么是容器

**容器**是**镜像**运行时的实体。



更多文档：

[10张图带你深入理解Docker容器和镜像](http://dockone.io/article/783)

