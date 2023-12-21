# Go的web框架 Gin

### 1.安装导入

```
#安装
go get -u github.com/gin-gonic/gin

#导包
import "github.com/gin-gonic/gin"
```



### 2.标准过程

1. **导包**

   ```go
   //发包
   import "github.com/gin-gonic/gin"
   
   //statusOK
   import "net/http"
   
   //数据库
   import "database/sql"
   import _ "github.com/go-sql-driver/mysql"
       
   //系统print
   "log"
   ```

2. **创建并初始化gin.Engine**

   `mux :=gin.Default()`

3. **注册路由**

   ```go
   mux.GET('/time',func (c *gin.conText){
     m := map[string]string{
       'time' : time.Now.format('2006-01-02')
     }
     c.JSON(http.statusOK,m)
   })
   ```

4. 监听服务端口

   ```go
   err := mux.Run('0.0.0.0:8080')
   ```

   

### 3.总结

#记得下载了包之后 要：

```
go mod tidy
go mod download
go mod vendor
```



```go
package main

import (
	"fmt"
	"net/http"
	"time"

	"github.com/gin-gonic/gin"
)
func main() {
    mux := gin.Default()
  
    mux.GET("/time", func(c *gin.Context) {
        m := map[string]string{
            "time": time.Now().Format("2006-01-02"),
        }
        c.JSON(http.StatusOK, m)
    })
  
    err := mux.Run("0.0.0.0:3000")
  
    if err != nil {
        panic(err)
    }
  
}
```

#启动服务

```
go run *.go  或  go run test.go 或 go run .
```



#成功后登录

```
http://localhost:3000/time
```

#### 4.数据库插入多条

1. 通过postform 来接收参数 userList 

   ```json
   [{"user_name":"Lilei","user_password":"14133331111"},{"user_name":"Mr Zhang","user_password":"15122223333"},{"user_name":"路人二","user_password":"18113131111"}]
   ```

2. 存到user[]数组中

   ```go
   json.Unmarshal([]byte(usersList), &users)
   ```

3. 历遍users 进行insert操作，需要注意的是批插入过程如果失败需要全部撤回

   ```go
   tx, err := sql.DB.Begin()
   failSign := false
   
   //如果insert出错了
   failSign := true
   
   if failSign == true{
     tx.Rollback()
     return
   }else{
     tx.Commit()
     return
   }
   ```



#### 5.文件上传

1. 从postman的body中的formdata接收文件

   ![image-20230922160738249](/Users/lifangyuan/Desktop/learn/pic/image-20230922160738249.png)

2. 后端写：

   ```go
   //从前端接收文件到变量中
   file, err := c.Formfile("key")
   
   //将文件存到本地
   err := SaveUploadedFile(file, "file/"+file.Filename)
   ```



#### 6.获取参数

1. **c.Query("查询字段")**

   参数放在url中

   如

   ```go
   func main() {
       router := gin.Default()
   
       router.GET("/user", func(c *gin.Context) {
           fname := c.Query("firstname")
           lname := c.Query("lastname")
   
           c.String(http.StatusOK, "Hello %s %s ", fname, lname)
       })
   
       router.Run(":8080")
   }
   ```

   对于 http://localhost:3000/user	?**firstname=1&lastname=2&fullname=**

   c.Query("first name") 	  // "1"

   c.Query("lastname")		// "2"

   c.Query("fullname")		//  ""

   c.Query("hello")			   //  ""

2. **c.DefaultQuery("查询字段","默认值")**

   参数放在url中,类似 `Query()`，但是如果 `key` 不存在，会返回默认值

   对于 http://localhost:3000/user	?**firstname=1&lastname=2&fullname=**

   c.Query("first name","none") 	  // "1"

   c.Query("lastname","none")		// "2"

   c.Query("fullname","none")		//  ""

   c.Query("hello","none")			   //  "none"

3. **c.Param("路由参数")**

   路由参数放在url中

   如

   ```go
   func main() {
       router := gin.Default()
   
       router.GET("/user/:firstname/:lastname", func(c *gin.Context) {
           fname := c.Param("firstname")
           lname := c.Param("lastname")
   
           c.String(http.StatusOK, "Hello %s %s ", fname, lname)
       })
   
       router.Run(":8080")
   }
   
   ```

   对于 http://localhost:8080/user**/wohu/1104**

   c.Param("firstname")		//wohu

   c.Param("lastname")		//1104

4. **c.PostForm("字段")**

   获取对应的表单数据

   对应于postman body中的form-data

5. **c.Cookie("cookie名")**

   设置cookie用

   ```go
   在具体函数定义时：
   //❗️这里需要注意的是：err不可以利用log.Fatalln(err),或者打印出来，否则会报错
   func Cookie(c *gin.Context) {
   	cookie, err := c.Cookie("cookieName")
   	if err != nil {
   		cookie = "newCookie"
   		c.SetCookie("cookieName", cookie, 60*2, "/", "localhost", false, true)
       //（cookie名，cookie值，有效时间，cookie的服务器路径，cookie的域名，是否通过安全的HTTPS连接来传输cookie（false），是否可以通过js访问cookie（true））
   		message := fmt.Sprintf("cookie have changed to %s", cookie)
   		c.JSON(http.StatusOK, gin.H{
   			"code":    200,
   			"message": message,
   		})
   		return
   	}
   	message := fmt.Sprintf("cookie have't changed (%s)", cookie)
   	c.JSON(http.StatusOK, gin.H{
   		"code":    200,
   		"message": message,
   	})
   
   }
   ```

   

6. **c.BindJSON(&u)**

   获取json数据（结构体中对应的数据）

   对应于postman body 中的raw（json）

   ```go
   在模型定义时（定义结构体时），需要声明结构体内部的变量json
   	如：
   	type User struct {
   	User_id       int64  "json:user_id"
   	User_name     string "json:user_name"
   	User_password string "json:user_password"
   }
   
   然后在具体函数中，需要定义一个该结构体类型的变量（初始值为空），然后和gin.context类型的c绑定
   	如：
   	u := models.User{}
   	c.BindJSON(&u)
   	fmt.Println(u)
   
   一般是post请求
   ```

   

7. **c.Request.header()**

   获取request的header，是个map，可以直接输出`c.Request.Header()`，查看header；也可以看的更清楚些

   ```go
   header := c.Request.Header()
   for key,value := range header{
     fmt.Println(key,value)
   }
   
   //因为header是map类型，所以想提取header中的信息 直接 header["Cookie"]
   
   //输出：
   Sec-Fetch-Site [none]
   Cookie [cookie=lifangy]
   Sec-Ch-Ua ["Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"]
   Sec-Ch-Ua-Mobile [?0]
   Accept [text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7]
   Connection [keep-alive]
   Cache-Control [max-age=0]
   Sec-Fetch-Dest [document]
   Sec-Ch-Ua-Platform ["macOS"]
   User-Agent [Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36]
   Sec-Fetch-User [?1]
   Accept-Encoding [gzip, deflate, br]
   Accept-Language [zh-CN,zh;q=0.9]
   Upgrade-Insecure-Requests [1]
   Sec-Fetch-Mode [navigate]
   ```

   
