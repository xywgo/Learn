##  Docker Registry

一个 **Docker Registry** 中可以包含多个 **仓库**（`Repository`）；每个仓库可以包含多个 **标签**（`Tag`）；每个标签对应一个镜像。

获取镜像是可以通过这样的格式`<仓库名>:<标签>`得到指定的镜像版本，如不指定将以默认`latest`作为标签。

### 公有 Registry

* [Dicker Hub](https://hub.docker.com/)(默认/官方/最常用)
* [Quay.io](https://quay.io/repository/)（Google/CoreOS）
* [网易云镜像服务](https://c.163.com/hub#/m/library/)
* [DaoCloud 镜像市场](https://hub.daocloud.io/)
* [阿里云镜像库](https://cr.console.aliyun.com/) 

### 私有 Registry

* [Docker Registry](https://hub.docker.com/_/registry/)（Docker官方提供）



### 加速

* [阿里云加速](https://cr.console.aliyun.com/undefined/instances/mirrors)（需账号开通开发者）

