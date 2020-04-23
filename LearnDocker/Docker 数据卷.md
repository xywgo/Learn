## 数据卷

Docker中提供了两种挂载方式，-v和-mount.

在用docker run命令的时候，使用--mount或 -v 标记来将数据卷挂载到容器里。

```bash
# 创建一个数据卷
docker volume create <volume_name>
# 查看所有的 数据卷
docker volume ls
# 查看详细信息
docker volume inspect <volume_name>
# 删除数据卷
docker volume rm <volume_name>
# 清理无主的数据卷
docker volume prune
```

更详细的参考文档：

[Manage data in Docker](https://docs.docker.com/storage/)

