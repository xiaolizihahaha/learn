# 进程、别名、配置、ssh

## 1.进程

#命令后面加 & 后缀使得该任务在后台执行

如 sleep 10 &



#停止当前的执行命令

control + c

#停止某个执行命令

kill %任务编号



#暂停执行命令

control + z



#暂停结束 继续前台执行任务

fg

#暂停结束 继续后台执行全部任务

bg



#列出当前终端尚未完成的全部任务及其任务编号

jobs



#选取任务

% 任务编号



#选取最近的一个任务

$!



## 2.别名（在配置文件中设置）

#设置别名

alias 缩略名=“实际命令” <!--alias gc=“git commit”-->



#禁用别名

unalias 缩略名



#获取别名的定义

alias 缩略名



## 3.配置文件（.bashrc .zshrc .vimrc）

#对于bash来说，配置文件为 ~/.bashrc 和 ~/.bash_profile

#对于git来说，配置文件为 ~/.gitconfig

#对于vim来说，配置文件为 ~/.vimrc 和 ~/.vim

#对于ssh来说，配置文件为~/.ssh/config

#对于tmux来说，配置文件为~/.tmux.conf

#对于服务器来说，配置文件为/etc/ssh/sshd_config



## 4.远程登录ssh

#登录

ssh 用户名@服务器ip  <!-- foo@192.168.1.42  /  ssh foo@bar.mit.edu -->



## 5.github 配置密钥

#查看是否存在现有SSH密钥

ls -al ~/.ssh  <!--若存在id_rsa或id_ecdsa或id_ed25519 则已存在密钥，直接查看密钥-->



#配置生成密钥

git config --global user.name "用户名"

git config --global user.email "邮箱地址"

ssh-keygen -t rsa -C "邮箱地址"。<!--之后三次回车，再查看密钥-->



#查看密钥

cat ~/.ssh/id_rsa



#将密钥复制到github上的ssh key里  <!--新建-->



#测试ssh连接

ssh -T git@github.com  <!-- 连接成功为 Hi xiaolizihahaha! You've successfully authenticated, but GitHub does not provide shell access. -->