## 什么是Docker

**Docker**是一种运行于 Linux 和 Windows 上的软件，用于创建、管理和编排容器。

## Docker核心组件

1. Docker引擎（客户端和服务器）
2. 镜像（Image)
3. 容器（Container)
4. 仓库（Resository)



**Docker镜像**，用于创建 Docker 容器的模板。

**Docker容器**独立运行的一个或者一组容器。启动Images后会生成Container，。一个Image可以启动多次生成多个Container。

**Docker仓库**，用来保存镜像。

## Docker与传统虚拟机对比

| 特性       | 容器               | 虚拟机      |
| :--------- | :----------------- | :---------- |
| 启动       | 秒级               | 分钟级      |
| 硬盘使用   | 一般为 `MB`        | 一般为 `GB` |
| 性能       | 接近原生           | 弱于        |
| 系统支持量 | 单机支持上千个容器 | 一般几十个  |