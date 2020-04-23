## 网络端口映射

容器中可以运行一些网络应用，要让外部也可以访问这些应用，可以通过 **-P** 或 **-p** 参数来指定端口映射。

两种方式的区别是:

- **-P :**是容器内部端口**随机**映射到主机的高端口。
- **-p :** 是容器内部端口绑定到**指定**的主机端口。



`docker port` 命令列出指定的容器的端口映射，或者查找将PRIVATE_PORT NAT到面向公众的端口。

语法

```bash
docker port [OPTIONS] CONTAINER [PRIVATE_PORT[/PROTO]]
```

## 容器互联

```bash
# 新建一个网络
# 用-d 指定网络类型：bridge，overlay
docker network create -d <network_type> <name>

# 在运行<run>一个容器时指定 --network参数，可将它加入这个网络。
```

