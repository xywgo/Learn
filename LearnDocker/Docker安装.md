## 安装Docker

Docker 分为 CE（Community Edition） 和 EE（Enterprise Edition） 两大版本。CE 即社区版（免费，支持周期 7 个月），EE 即企业版，强调安全，付费使用，支持周期 24 个月。

Docker CE 分为 `stable` `test` 和 `nightly` 三个更新频道。

**[官方教程](https://docs.docker.com/get-docker/)**

### Ubuntu 安装Docker Engine (CE版）

#### 系统要求：

- Eoan 19.10
- Bionic 18.04 (LTS)
- Xenial 16.04 (LTS)

及64位X86平台或ARM平台。

#### 卸载老版本

```bash
sudo apt-get remove docker docker-engine docker.io containerd runc
```

#### 从库安装

##### 设置源库

1.更新apt包索引

```bash
 sudo apt-get update
```

2.安装包以允许通过HTTPS使用软件存储库：

```bash
sudo apt-get install \\
    apt-transport-https \\
    ca-certificates \\
    curl \\
    software-properties-common
```

3.添加Docker的官方GPG密钥：

```bash
curl -fsSL <https://download.docker.com/linux/ubuntu/gpg> | sudo apt-key add -

# 如因网络问题可选择国内镜像源
# curl -fsSL https://mirrors.ustc.edu.cn/docker-ce/linux/ubuntu/gpg | sudo apt-key add -
```

通过搜索指纹的最后8个字符，确认您现在拥有指纹9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88的密钥。

```bash
sudo apt-key fingerprint 0EBFCD88

pub   4096R/0EBFCD88 2017-02-22
      Key fingerprint = 9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
uid                  Docker Release (CE deb) <docker@docker.com>
sub   4096R/F273FCD8 2017-02-22
```

4.使用以下命令设置稳定存储库。即使您还想从边缘或测试存储库安装构建，您始终需要稳定的存储库。要添加边缘或测试存储库，请在以下命令中的单词stable之后添加单词edge或test（或两者）。 *注意：下面的lsb_release -cs子命令返回Ubuntu发行版的名称，例如xenial。有时，在像Linux Mint这样的发行版中，您可能需要将$（lsb_release -cs）更改为您的父Ubuntu发行版。例如，如果您使用的是Linux Mint Rafaela，则可以使用trusty。*

```bash
sudo add-apt-repository \\
   "deb [arch=amd64] <https://download.docker.com/linux/ubuntu> \\
   $(lsb_release -cs) \\
   stable"
```

##### 安装Docker CE

```bash
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

#### 使用脚本自动安装

可以通过 `--mirror` 选项使用国内源进行安装：

```bash
curl -fsSL get.docker.com -o get-docker.sh
sudo sh get-docker.sh
 
# 使用镜像
# sudo sh get-docker.sh --mirror Aliyun
# sudo sh get-docker.sh --mirror AzureChinaCloud
```

##### 非Root用户使用Docker

```bash
sudo usermod -aG docker your-user
# 将your-user替换成你的用户名
```



#### 卸载Docker Engine

1. 卸载Docker Engine, CLI等：

   ```bash
   sudo apt-get purge docker-ce docker-ce-cli containerd.io
   ```

2. 删除镜像、容器、卷：

   ```bash
   sudo rm -rf /var/lib/docker
   ```

   配置文件需要手动删除。