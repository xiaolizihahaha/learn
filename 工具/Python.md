# Python

### 0.路径问题

python3.9 默认解释器路径：~/.pyenv/versions/3.9.5/bin/python

Pip3.9 默认路径: (~/.pyenv/versions/3.9.5/bin/pip)



python3.6 默认解释器路径:(/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6)

Pip3.6 默认路径:(/Library/Frameworks/Python.framework/Versions/3.6/bin/pip)



python3.7 默认解释器路径:(/usr/local/bin/python3)

Pip3.7 默认路径:(/usr/local/bin/pip3)



python3.11  默认解释器路径:(/usr/local/bin/python3.11)

pip3.11默认路径:(/usr/local/bin/pip3.11)



**Pip 失败：**

pip install xxx -i http://pypi.douban.com/simple --trusted-host pypi.douban.com



### 1.安装、查看、转换解释器

- 官网下载（推荐）

- 如果安装了Homebrew，直接通过命令 brew install python3 安装即可

- Pyenv 安装

  1. pyenv install --list		#查看能够安装的版本

  2. pyenv install 3.6.0 -v  #安装需要的版本

  3. pyenv rehash               #完成后更新数据库

  4. pyenv versions            #查看系统已安装的版本(＊号表示系统当前正在使用的版本)

  5. pyenv global 3.6.2      #切换python版本

  6. python --version          #确认python版本

  7. pyenv uninstall 3.6.x.  #卸载python

  
  
- 查看位置：python3 -c 'import sys;print(sys.path)'



### 2.pip 指定版本

​	pip install robotframework==2.8.7



### 3. tips

#### 1.list.append	VS	list.extend

```
music_media.append(object) 向列表中添加一个对象object
music_media.extend(sequence) 把一个序列seq的内容添加到列表中 (跟 += 在list运用类似， music_media += sequence)

1、使用append的时候，是将object看作一个对象，整体打包添加到music_media对象中。
2、使用extend的时候，是将sequence看作一个序列，将这个序列和music_media序列合并，并放在其后面。

music_media = []
music_media.extend([1,2,3])
print music_media
#结果: 
#[1, 2, 3]
            
music_media.append([4,5,6])
print music_media
#结果: 
#[1, 2, 3, [4, 5, 6]]
            
music_media.extend([7,8,9])
print music_media
#结果: 
#[1, 2, 3, [4, 5, 6], 7, 8, 9]

```



#### 2. array[ : : -1]

[::-1] 顺序相反操作
[-1] 读取倒数第一个元素
[3::-1] 从下标为3（从0开始）的元素开始翻转读取
同样适用于字符串

    a=[1,2,3,4,5]
    b=a[::-1]
    
    [5, 4, 3, 2, 1]


    b=a[-1]
    
    5


    b=a[3::-1]
    
    [4, 3, 2, 1]





#### 3. For  循环

for index,val in enumerate(list)   可以获取到元素的index和val

for x,y in zip(list1,list2)    可以同时遍历两个list



#### 4.acsii

ord（字符） 得到ascii码

chr（ascii码）得到字符



#### 5.list个string的互相转化

'(连接符号)'.join(list)		list -> string

list(string)						string -> list



#### 6.排序

sort(key = lambda x:(-len(x),x) )



#### 7.集合set的运算：并交补

并：set1 | set2

交：set1 & set2

补：set1 - set2



#### 8.python 的排序树

```
from sortedcontainers import SortedList

s = SortedList()
s.add(value)
s.remove(value)

最大最小值对应
s[0]
s[-1]
```