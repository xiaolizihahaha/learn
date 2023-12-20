# Golang

## 1.环境配置

- **GOPATH**： go工作区， 即编写代码存放的目录
  - bin: 存储可执行bin文件(手动创建)
  - pkg: 编译完成的文件(`$GOPATH/pkg`目录在执行`go get -u 库名`会自动创建)
  - src: 源代码文件（手动创建，进行新项目的开发）
- **GOROOT**： go的安装目录

```
GOPATH="/Users/lifangyuan/go"

GOROOT="/usr/local/go"
```



## 2.创建新项目

- 创建project文件

  ```
  cd $GOPATH/src
  mkdir project
  cd project
  ```

- 为代码启用依赖项跟踪

  ```python
  go mod init example/hello
  go mod tidy #增加缺少的module， 删除无用的module
  ```

- 然后创建hello.go 并在hello.go 里面写代码
- 最后 go run . 启动项目



### 3.go mod 用法

```
go mod edit					#编辑go.mod文件

go mod init	+项目名	#初始化当前文件夹，创建go.mod 文件
go mod tidy					#增加缺少的包，删除没用的包
go mod download 		#下载依赖包到本地（默认为GOPATH/pkg/mod）（最好有镜像）
go mod vendor				#将下载好的依赖包移动到本项目目录下的vendor文件夹中，此时便可以使用依赖了

```

### 4.go语法

```go
#行分隔符：//  /* xxxx */
#标识符和C一样，换行即可，无需;
#变量初始化未赋值，默认值为0/nil/false/""
#a的地址：&a
#a的指针：*a

例：fmt.Println("Hello" + "world")
例：
var str1,str2 string = "hello","world"
fmt.Printf("IN:%s!%s",str1,str2)					#Printf 根据格式化参数生成格式化的字符串并写入标准输出。

例：
var str1 string = "hello"
var str2 string = "world"
var str3 string
str3 = fmt.Sprintf("IN:%s!%s",str1,str2)	#Sprintf 根据格式化参数生成格式化的字符串并返回该字符串。
fmt.Println(str3)

```

##### 

##### 4.1 声明变量

```
var str string = "hello" 
等价于
str := "hello"	#声明且赋值

#但是，var形式的声明可以出现在函数体外，:=形式的输出不可以出现在函数体外。

//强制转化 string -> int
var str string := "10"
var number int

number,_ = strconv.Atoi(str)		#后面的返回参数_是错误类型
str= strconv.Itoa(number)
```

##### 4.2声明常量

```
const identifier [type] = value

例：iota在枚举中的使用，依次+1，初始值为0，可以看作是枚举变量的行号-1

例：
func main() {
    const (
            a = iota   //0
            b          //1
            c          //2
            d = "ha"   //独立值，iota += 1
            e          //"ha"   iota += 1
            f = 100    //iota +=1
            g          //100  iota +=1
            h = iota   //7,恢复计数
            i          //8
    )
    fmt.Println(a,b,c,d,e,f,g,h,i)	#0 1 2 ha ha 100 100 7 8

}
例：
const (
    i=1<<iota
    j=3<<iota
    k
    l
)

func main() {
    fmt.Println("i=",i)
    fmt.Println("j=",j)
    fmt.Println("k=",k)
    fmt.Println("l=",l)
    #i= 1 j= 6 k= 12 l= 24

}
```

##### 4.3 声明数组

```go
var 数组名 [大小]类型 		#如： var number [99]int

初始化：
var 数组名 =[大小]类型{1,2,3,4}
等价于
数组名 = [大小]类型{1,2,3,4}

当数组大小不确定懒得计算时，
数组名:=[...]类型{1,2,3,4}


如果设置了数组的长度，我们还可以通过指定下标来初始化元素：

//  将索引为 1 和 3 的元素初始化
balance := [5]float32{1:2.0,3:7.0}
```

##### 

**#创建数组**

**变量名 := make([]变量类型，0，数组长度)**

（适用于结构体！）



##### 4.4 结构体

```go
//定义结构体
type 结构体名 struct{
  变量名 类型
  变量名 类型
  变量名 类型
}

//声明结构体
s1 := 结构体名{xx,xx,xx,xx}  or s1:=结构体名{key1=xx,key2=xx,key3=xx,key4=xx}

```



##### 4.5 切片

```go
//切片初始化
var slice []名称 = make([] 名称，长度,容量可有可无)

//例
slice :=[] int {1,2,3,4}
slice := arr[2:5]

//切片扩容append
var slice []int
slice = append(slice,0)   //允许扩容
slice = append(slice,1)		//增加了一个元素
slice = append(slice,2,3,4)	//增加了三个元素

//切片扩容 make copy
slice1 := make([]int,len(slice),(cap(slice))*2)  //cap(slice)是slice的容量
copy(slice1,slice)

```

##### 4.6 map和range

```go
func main() {
    map1 := make(map[int]float32)
    map1[1] = 1.0
    map1[2] = 2.0
    map1[3] = 3.0
    map1[4] = 4.0
  
  	//等价于
  	map1 :=map[int]float32{1:1.0,2:2.0,3:3.0,4:4.0}
  
  //删除键值对map1[1]=1.0
  	delete(map1,1)
    
    // 读取 key 和 value
    for key, value := range map1 {
      fmt.Printf("key is: %d - value is: %f\n", key, value)
    }

    // 读取 key
    for key := range map1 {
      fmt.Printf("key is: %d\n", key)
    }

    // 读取 value
    for _, value := range map1 {
      fmt.Printf("value is: %f\n", value)
    }
}
```



##### select 语句

select 是 Go 中的一个控制结构，类似于 switch 语句。

select 语句只能用于通道操作，每个 case 必须是一个通道操作，要么是发送要么是接收。

select 语句会监听所有指定的通道上的操作，一旦其中一个通道准备好就会执行相应的代码块。

如果多个通道都准备好，那么 select 语句会随机选择一个通道执行。如果所有通道都没有准备好，那么执行 default 块中的代码。（如果没有 default 子句，select 将阻塞，直到某个通道可以运行；Go 不会重新对 channel 或值进行求值。）



```go
package main
import ("fmt","time")

func main(){
  #创建了两个无缓冲的channel
  chan1 := make(chan int)
  chan2 := make(chan int)
  
  #通过两个goroutine向ch1，ch2两个通道发送数据
  go func(){
    chan1 <- 1
    time.Sleep(time.second)
  }
  
  go func(){
    chan2 <-3
    time.sleep(5 * time.second)
  }
  
  #通过select随机读取ch1，ch2的返回值
  select{
    case a:= <- chan1:
    fmt.Println("chan1:",a)
    
    case b:= <- chan2:
    fmt.Println("chan2:",b)
    
    default <- time.After(time.Second * 5):
    fmt.Println("time out")
  }
}

```





##### 函数返回

```go
func numbers()(int,int,string){
  a,b,c := 1,2,"hello"
  return a,b,c
}

func main(){	#_用于接收抛弃值，因为go中声明的变量必须被使用，不然会报错
  _,number,str := numbers()
  fmt.Println(numbers,str)
}
```

