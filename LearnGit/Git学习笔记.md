## Git简介

[Git](https://git-scm.com/)是目前世界上最先进的分布式[^1]版本控制系统[^2]。

## 安装Git

参考官方下载安装地址：https://git-scm.com/downloads

## 常用命令

```bash
# 创建版本库（repository)
# 将当前目录变成git管理的仓库
# 会在目录下生成一个隐藏的.git目录用于跟踪管理当前仓库
git init <repositoryname>

# 将文件添加到仓库，需文件已经存在于目录中
git add [文件名]...

# 将文件提交到仓库, -m后为说明，可以随便写
git commit -m 'message'

# 查看文件变更内容
git diff [文件名]

# 查看工作区的状况
git status

# 查看历史版本记录
git log
# 简化输出
git log --pretty=oneline

# 退回到某个版本
# HEAD^（^）表示上（上）一个版本
git reset --hard commit ID
# 如不记得commit id 可通过下面命令查看历史命令得到
git reflog

# 删除文件
# 通过其他方式删除的文件也要执行下面命令在git版本库中删除
git rm file

#删除后还需要再commit
#如果删错了，并且还没提交到版本库里（版本库里还有）可以通过下面命令恢复。
git checkout -- filename
```

## 工作区和暂存区

工作区（Working Directory)就是git管理的可见的当前目录。而隐藏的.git目录就是版本库（Repository).

版本库中包含的很重要的一部分就是暂存区（stage/index).还有就是master分支及其指针（HEAD)。

![Git](https://www.liaoxuefeng.com/files/attachments/919020037470528/0)

`git add` 命令就是把文件修改提交到暂存区，`git commit`就是把暂存区的所有内容提交到当前分支。

Git跟踪并管理的是修改，而非文件。

```bash
# 查看工作区与版本库中文件的区别
git diff HEAD -- 文件名
```

## 远程仓库

```bash
# 要关联一个远程库，使用命令
git remote add origin git@server-name:path/repo-name.git
# 关联后第一次推送
git push -u origin master
#之后推送
git push origin master

# 从远程库克隆
git clone git@server-name:path/repo-name.git

# 查看远程仓库信息
git remote
# 查看更详细的信息
git remote -v

# 推送分支
# 如果失败，先用git pull抓取远程的新提交
git push origin branch-name
# 在本地创建和远程对应的分支，使用
git checkout -b branch-name origin/brance-name
# 建立本地分支与远程分支的关联
git branch --set-upstream branch-name origin/branch-name
# 从远程抓取分支，使用git pull，如果有冲突，要先处理冲突

# rebase操作可以把本地未push的分叉提交历史整理成直线
git rebase

```

## 分支管理

```bash
# 查看分支
git branch
# 创建分支
git branch <name>
# 切换分支 2种命令效果一样
git checkout <name> 
git switch <name>
# 创建并切换分支 下面2个命令效果一样
git checkout -b <name> 
git switch -c <name>
# 合并某分支到当前分支
git merge <name>
# 删除分支
git branch -d <name>
# 丢弃一个没有合并过的分支
git branch -D <name>

# 当Git无法自动合并分支时，就必须首先解决冲突。解决冲突后，再提交，合并完成。
# 解决冲突就是把Git合并失败的文件手动编辑为我们希望的内容，再提交。
# 用下面命令可以查看分支合并图
git log --graph

# 通常Git默认会采用Fast forward模式进行合并，但这样会丢掉分支信息。
# 可以在合并时通过下面的参数禁用Fast forward模式采用普通模式，保留分支信息。
# 通过普通模式会创建一个新的commit,所以还需要添加-m参数及说明信息
git merge --no-ff -m 'massage'

# 当某个分支的工作还没完成（还不能提交）但需去其他分支工作时可以用下面命令暂存工作现场
git stash
# 需要从暂存区恢复的命令
git stash pop

# 要把其他分支的修改（如Bug修复），同步应用的当前工作分支.
git cherry-pick <commit id>
```

## 标签管理

```bash
# 新建一个标签，默认是HEAD，也可以指定一个commit id
git tag <tagname>
# 指定标签信息
git tag -a <tagname> -m 'blablabla'
# 查看所有标签
git tag
# 查看标签信息
git show <tagname>

# 推送一个本地标签
git push origin <tagname>
# 推送所有本地标签
git push origin --tags
# 删除一个本地标签
git tag -d <tagname>
# 删除一个远程标签
git push origin :refs/tags/<tagname>
```

## 自定义Git

#### 忽略特殊文件

[配置模版](https://github.com/github/gitignore)

```bash
# 强制添加忽略的文件
git add -f <filename>

# 配置全局命令别名
git config --global alias.别名 <原命令>
```

### 配置文件

配置Git的时候，加上`--global`是针对当前用户起作用的，如果不加，那只针对当前的仓库起作用。

每个仓库的Git配置文件都放在`.git/config`文件中。

当前用户的Git配置文件放在用户主目录下的一个隐藏文件`.gitconfig`中。

配置别名也可以直接修改这个文件。

#### 搭建Git服务器

以Ubuntu为例

```bash
# 安装Git
sudo apt-get install git
# 创建git用户
sudo adduser git
# 创建证书登录，把所有公钥导入到/home/git/.ssh/authorized_keys文件里
# 初始化Git仓库，更改权限
sudo git init --bare sample.git
sudo chown -R git:git sample.git
# 禁用shell登录，编辑/etc/passwd
# 将
git:x:1001:1001:,,,:/home/git:/bin/bash
# 修改为
git:x:1001:1001:,,,:/home/git:/usr/bin/git-shell
# 克隆远程仓库
git clone git@server:/srv/sample.git

# 剩下的都一样了
# 完成


```



[^1]:可以不需要中央服务器，在本地有独立的版本库。
[^2]:管理记录文件变更的一套方法




