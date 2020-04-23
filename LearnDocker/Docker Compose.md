### Compose 简介

Compose 是用于定义和运行多容器 Docker 应用程序的工具。

## 安装与卸载

`Docker Desktop for Mac/Windows` 自带 `docker-compose` 二进制文件，安装 Docker 之后可以直接使用。

### Linux下安装

```bash
# 下载
sudo curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
# 赋予权限
sudo chmod +x /usr/local/bin/docker-compose
```

更多安装方式参考：

[Install Docker Compose](https://docs.docker.com/compose/install/)

## 卸载

如果是二进制包方式安装的，删除二进制文件即可。

```bash
$ sudo rm /usr/local/bin/docker-compose
```

如果是通过 `pip` 安装的，则执行如下命令即可删除。

```bash
$ sudo pip uninstall docker-compose
```

## Compose 命令说明

### 格式

```bash
docker-compose [-f=<arg>...] [options] [COMMAND] [ARGS...]
```

### 命令选项

- `-f, --file FILE` 指定使用的 Compose 模板文件，默认为 `docker-compose.yml`，可以多次指定。
- `-p, --project-name NAME` 指定项目名称，默认将使用所在目录名称作为项目名。
- `--x-networking` 使用 Docker 的可拔插网络后端特性
- `--x-network-driver DRIVER` 指定网络后端的驱动，默认为 `bridge`
- `--verbose` 输出更多调试信息。
- `-v, --version` 打印版本并退出。

### 常用命令

#### `build`

格式为 `docker-compose build [options] [SERVICE...]`。

构建（重新构建）项目中的服务容器。

选项包括：

- `--force-rm` 删除构建过程中的临时容器。
- `--no-cache` 构建镜像过程中不使用 cache（这将加长构建过程）。
- `--pull` 始终尝试通过 pull 来获取更新版本的镜像。

#### `config`

验证 Compose 文件格式是否正确，若正确则显示配置，若格式错误显示错误原因。

#### `down`

此命令将会停止 `up` 命令所启动的容器，并移除网络

#### `exec`

进入指定的容器。

#### `help`

获得一个命令的帮助。

#### `images`

列出 Compose 文件中包含的镜像。

#### `kill`

格式为 `docker-compose kill [options] [SERVICE...]`。

通过发送 `SIGKILL` 信号来强制停止服务容器。

支持通过 `-s` 参数来指定发送的信号。

#### `logs`

格式为 `docker-compose logs [options] [SERVICE...]`。

查看服务容器的输出。默认情况下，docker-compose 将对不同的服务输出使用不同的颜色来区分。可以通过 `--no-color` 来关闭颜色。

#### `pause`

格式为 `docker-compose pause [SERVICE...]`。

暂停一个服务容器。

#### `port`

格式为 `docker-compose port [options] SERVICE PRIVATE_PORT`。

打印某个容器端口所映射的公共端口。

选项：

- `--protocol=proto` 指定端口协议，tcp（默认值）或者 udp。
- `--index=index` 如果同一服务存在多个容器，指定命令对象容器的序号（默认为 1）。

#### `ps`

格式为 `docker-compose ps [options] [SERVICE...]`。

列出项目中目前的所有容器。

选项：

- `-q` 只打印容器的 ID 信息。

#### `pull`

格式为 `docker-compose pull [options] [SERVICE...]`。

拉取服务依赖的镜像。

选项：

- `--ignore-pull-failures` 忽略拉取镜像过程中的错误。

#### `push`

推送服务依赖的镜像到 Docker 镜像仓库。

#### `restart`

格式为 `docker-compose restart [options] [SERVICE...]`。

重启项目中的服务。

选项：

- `-t, --timeout TIMEOUT` 指定重启前停止容器的超时（默认为 10 秒）。

#### `rm`

格式为 `docker-compose rm [options] [SERVICE...]`。

删除所有（停止状态的）服务容器。推荐先执行 `docker-compose stop` 命令来停止容器。

选项：

- `-f, --force` 强制直接删除，包括非停止状态的容器。一般尽量不要使用该选项。
- `-v` 删除容器所挂载的数据卷。

#### `run`

格式为 `docker-compose run [options] [-p PORT...] [-e KEY=VAL...] SERVICE [COMMAND] [ARGS...]`。

在指定服务上执行一个命令。

选项：

- `-d` 后台运行容器。
- `--name NAME` 为容器指定一个名字。
- `--entrypoint CMD` 覆盖默认的容器启动指令。
- `-e KEY=VAL` 设置环境变量值，可多次使用选项来设置多个环境变量。
- `-u, --user=""` 指定运行容器的用户名或者 uid。
- `--no-deps` 不自动启动关联的服务容器。
- `--rm` 运行命令后自动删除容器，`d` 模式下将忽略。
- `-p, --publish=[]` 映射容器端口到本地主机。
- `--service-ports` 配置服务端口并映射到本地主机。
- `-T` 不分配伪 tty，意味着依赖 tty 的指令将无法运行。

#### `scale`

格式为 `docker-compose scale [options] [SERVICE=NUM...]`。

设置指定服务运行的容器个数。

选项：

- `-t, --timeout TIMEOUT` 停止容器时候的超时（默认为 10 秒）。

#### `start`

格式为 `docker-compose start [SERVICE...]`。

启动已经存在的服务容器。

#### `stop`

格式为 `docker-compose stop [options] [SERVICE...]`。

停止已经处于运行状态的容器，但不删除它。通过 `docker-compose start` 可以再次启动这些容器。

选项：

- `-t, --timeout TIMEOUT` 停止容器时候的超时（默认为 10 秒）。

#### `top`

查看各个服务容器内运行的进程。

#### `unpause`

格式为 `docker-compose unpause [SERVICE...]`。

恢复处于暂停状态中的服务。

#### `up`

格式为 `docker-compose up [options] [SERVICE...]`。

该命令十分强大，它将尝试自动完成包括构建镜像，（重新）创建服务，启动服务，并关联服务相关容器的一系列操作。

选项：

- `-d` 在后台运行服务容器。
- `--no-color` 不使用颜色来区分不同的服务的控制台输出。
- `--no-deps` 不启动服务所链接的容器。
- `--force-recreate` 强制重新创建容器，不能与 `--no-recreate` 同时使用。
- `--no-recreate` 如果容器已经存在了，则不重新创建，不能与 `--force-recreate` 同时使用。
- `--no-build` 不自动构建缺失的服务镜像。
- `-t, --timeout TIMEOUT` 停止容器时候的超时（默认为 10 秒）。

#### `version`

格式为 `docker-compose version`。

打印版本信息。

## Compose 模板文件

详细可参考：[Compose file version 3 reference](https://docs.docker.com/compose/compose-file/)

### version

指定本 yml 依从的 compose 哪个版本制定的。

### build

指定为构建镜像上下文路径：

可以在`build:`直接指定Dockerfile路径（默认为当前目录），也可使用的进一步指令：

- context：上下文路径。
- dockerfile：指定构建镜像的 Dockerfile 文件名。
- args：添加构建参数，这是只能在构建过程中访问的环境变量。
- labels：设置构建镜像的标签。
- target：多层构建，可以指定构建哪一层。
- `ache_from` 指定构建镜像的缓存

### `cap_add, cap_drop`

指定容器的内核能力（capacity）分配。

例如，让容器拥有所有能力可以指定为：

```yaml
cap_add:
  - ALL
```

去掉 NET_ADMIN 能力可以指定为：

```yaml
cap_drop:
  - NET_ADMIN
```

### `command`

覆盖容器启动后默认执行的命令。

```yaml
command: echo "hello world"
```

### `cgroup_parent`

指定父 `cgroup` 组，意味着将继承该组的资源限制。

### `container_name`

指定容器名称。默认将会使用 `项目名称_服务名称_序号` 这样的格式。

```yaml
container_name: docker-web-container
```

### `devices`

指定设备映射关系。

### `depends_on`

解决容器的依赖、启动先后的问题。

### `dns`

自定义 `DNS` 服务器。可以是一个值，也可以是一个列表。

#### `dns_search`

配置 `DNS` 搜索域。可以是一个值，也可以是一个列表。

### `tmpfs`

挂载一个 tmpfs 文件系统到容器。

### `env_file`

从文件中获取环境变量，可以为单独的文件路径或列表。

### `environment`

设置环境变量。你可以使用数组或字典两种格式。

### `expose`

暴露端口，但不映射到宿主机，只被连接的服务访问。

仅可以指定内部端口为参数

### `extra_hosts`

类似 Docker 中的 `--add-host` 参数，指定额外的 host 名称映射信息。

### `healthcheck`

通过命令检查容器是否健康运行。

### `image`

指定为镜像名称或镜像 ID。如果镜像在本地不存在，`Compose` 将会尝试拉取这个镜像。

### `labels`

为容器添加 Docker 元数据（metadata）信息。例如可以为容器添加辅助说明信息。

### `logging`

配置日志选项。

目前支持三种日志驱动类型。

```yaml
driver: "json-file"
driver: "syslog"
driver: "none"
```

`options` 配置日志驱动的相关参数。

### `network_mode`

设置网络模式。使用和 `docker run` 的 `--network` 参数一样的值。

### `networks`

配置容器连接的网络。

### `pid`

跟主机系统共享进程命名空间。打开该选项的容器之间，以及容器和宿主机系统之间可以通过进程 ID 来相互访问和操作。

### `ports`

暴露端口信息。

使用宿主端口：容器端口 `(HOST:CONTAINER)` 格式，或者仅仅指定容器的端口（宿主将会随机选择端口）都可以。

### `secrets`

存储敏感数据，例如 `mysql` 服务密码。

### `security_opt`

指定容器模板标签（label）机制的默认属性（用户、角色、类型、级别等）。

### `stop_signal`

设置另一个信号来停止容器。在默认情况下使用的是 SIGTERM 停止容器。

### `sysctls`

配置容器内核参数。

### `ulimits`

指定容器的 ulimits 限制值。

### `volumes`

数据卷所挂载路径设置。可以设置为宿主机路径(`HOST:CONTAINER`)或者数据卷名称(`VOLUME:CONTAINER`)，并且可以设置访问模式 （`HOST:CONTAINER:ro`）。

该指令中路径支持相对路径。

