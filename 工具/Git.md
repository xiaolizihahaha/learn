# Git

#Git版本

git --version



#关于节点和分支

仓库有各个分支， 比如master分支、dev分支，开发人员一般使用dev分支，所有开发人员克隆代码后都有一个本地dev分支（与远程dev分支是多对一的关系）。进行修改后执行add、commit、push，向远程dev提交合并请求。



- 修改文件后，文件的状态：新的未追踪的文件（Untracked files）
- add 后，文件的状态：1.已追踪的文件，暂存状态（changes to be committed）<!--add后，文件没再被修改，这种情况下可以直接commit-->  2.已追踪的文件，不可提交（changes not staged for commit）<!--add后，文件进行了修改，这种情况下需要先add 在commit-->





## 1.本地代码初始化使用git

#将本地已存在目录初始化为仓库，并进行提交

1. 在github创建一个新的项目
2. 切换到本地项目目录下  cd ~/Project/newproject
3. 初始化本地仓库  git init
4. 复制github上仓库的地址
5. 添加远程仓库地址到本地  git remote add origin 远程仓库地址
6. 将远程仓库拉取下来  git pull origin master(第一次pull会出错 不用管)
7. 添加文件到本地仓库  git add .
8. 提交文件  git commit -m "first commit"
9. push 到远程仓库  git push -u origin master



## 2.远程仓库克隆

#克隆现有仓库

git clone 远程仓库地址  <!--之后进行pull add commit push-->



## 3.文件操作

#查看现在文件状态

git status



#添加文件1到暂存区

git add file

#添加所有文件到暂存区

git add .



#提交文件

git commit -m "描述"



#推送文件

git push

#拉取文件

git pull



#本地远程都删除文件

git rm file  <!--如果只是rm file会报changes not stages for commit-->



#文件重命名

git mv file1 file2



#撤销提交

git reset HEAD~1 <!--更改历史 现在HEAD指向HEAD~1的位置 对团队无效-->

git revert HEAD <!--在HEAD下创建一个新的节点 并将HEAD指向它 相当于撤销之前HEAD节点的操作 团队有效-->

## 4.分支

#查看分支

git branch



#创建分支

git branch 分支名



#切换分支(修改HEAD位置)

git checkout 分支名 <!--后面可加^ 表示HEAD到该分支上面一个父节点，加^^ 表示HEAD到该分支上面两个父节点以此类推  后面加~3 表示HEAD到该分支上面3个父节点-->



#调整分支节点位置

git branch -f main HEAD~3 <!--将main分支节点位置调整到HEAD^3的位置-->



#并行合并分支

git merge 分支名 <!--给当前分支进行修改 另一个分支没变-->



#顺序合并分支

git rebase main <!--当前分支产生副本作为新的节点 顺序连接main -->



#删除分支

git branch -d







## 5.远端

#列出远端

git remote



#添加一个远端

git remote add 名称 远程仓库地址



## 6.版本

#查看提交历史

git log <!--里面会有版本号，便于版本切换-->

#查看提交历史并查看每次提交的差异

git log -p



#版本回退

git reset --hard 版本号



## 7.忽略文件

#创建一个.gitignore文件，列出要忽略的文件的格式。

```console
$ cat .gitignore
*.[oa]
*~
```



