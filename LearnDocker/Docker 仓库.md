仓库（Repository）是集中存放镜像的地方。

## Docker Hub

Docker 官方维护了一个公共仓库 [Docker Hub](https://hub.docker.com/)。

### 登录和退出

```bash
# 登录
docker login
# 退出
docker logout
```

### 拉取/推送镜像

```bash
# 从Docker Hub查找镜像
docker search [OPTIONS] TERM
# 从镜像仓库中拉取或者更新指定镜像
docker pull [OPTIONS] NAME[:TAG|@DIGEST]
# 将本地的镜像上传到镜像仓库,要先登陆到镜像仓库
docker push [OPTIONS] NAME[:TAG]
```

## 私有仓库

请参考：

[私有仓库][https://yeasy.gitbooks.io/docker_practice/repository/registry.html]

[私有仓库高级配置][https://yeasy.gitbooks.io/docker_practice/repository/registry_auth.html]

[Nexus3.x 的私有仓库][https://yeasy.gitbooks.io/docker_practice/repository/nexus3_registry.html]

