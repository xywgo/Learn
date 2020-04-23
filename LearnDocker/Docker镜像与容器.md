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

### 常用命令

#### docker run 

创建一个新的容器并运行一个命令

##### 语法

```bash
docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
```

常用选项（options）：

* **-d:** 后台运行容器，并返回容器ID；
* **-i:** 以交互模式运行容器，通常与 -t 同时使用；
* **-P:** 随机端口映射，容器内部端口**随机**映射到主机的高端口
* **-p:** 指定端口映射，格式为：**主机(宿主)端口:容器端口**
* **-t:** 为容器重新分配一个伪输入终端，通常与 -i 同时使用；
* **--name=" ":** 为容器指定一个名称；
* **--expose=[]:** 开放一个端口或一组端口；
* **--volume , -v:** 绑定一个卷

#### Docker start/stop/restart 

**docker start** :启动一个或多个已经被停止的容器

**docker stop** :停止一个运行中的容器

**docker restart** :重启容器

##### 语法

```bash
docker start [OPTIONS] CONTAINER [CONTAINER...]
docker stop [OPTIONS] CONTAINER [CONTAINER...]
docker restart [OPTIONS] CONTAINER [CONTAINER...]
```

#### Docker attach

**docker attach :**连接到正在运行中的容器。

##### 语法

```bash
docker attach [OPTIONS] CONTAINER
```

*注意：* 如果从这个 stdin 中 exit，会导致容器的停止。

#### docker exec

在运行的容器中执行命令

##### 语法

```bash
docker exec [OPTIONS] CONTAINER COMMAND [ARG...]
```

常用选项：

- **-d :**分离模式: 在后台运行
- **-i :**即使没有附加也保持STDIN 打开
- **-t :**分配一个伪终端

#### Docker export 

将文件系统作为一个tar归档文件（快照）导出到STDOUT。

##### 语法

```bash
docker export [OPTIONS] CONTAINER
```

选项说明：

- **-o :**将输入内容写到文件。

#### docker import 

从归档文件中创建镜像。

##### 语法

```bash
docker import [OPTIONS] file|URL|- [REPOSITORY[:TAG]]
```

OPTIONS说明：

- **-c :**应用docker 指令创建镜像；
- **-m :**提交时的说明文字；

#### docker rm 

删除一个或多个容器。

##### 语法

```bash
docker rm [OPTIONS] CONTAINER [CONTAINER...]
```

OPTIONS说明：

- **-f :**通过 SIGKILL 信号强制删除一个运行中的容器。
- **-l :**移除容器间的网络连接，而非容器本身。
- **-v :**删除与容器关联的卷。

```bash
# 清理所有处于终止状态的容器
docker container prune
```

更多文档：

[10张图带你深入理解Docker容器和镜像](http://dockone.io/article/783)

