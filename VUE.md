# VUE

## 1.环境准备

1. 安装node.js.     <!--下载地址：https://nodejs.org/en/-->     or  `brew install nodejs`

2. 检查安装是否成功。 `node -v`

3. 自带的包管理工具npm，**可以使用npm安装各种插件**，`npm -v`

4. 安装cnpm镜像 `npm install -g cnpm --registry=https://registry.npm.taobao.org`

5. 检测cnpm版本 `cnpm -v`

6. 安装webpack

7. webpack是当前前端最热门的前端资源模块化管理和打包工具，输入以下命令安装：

   ```text
   cnpm install webpack -g
   ```

8. 安装vue脚手架（自动搭建vue项目框架的工具）

   vue脚手架的作用是用来自动一键生成vue+webpack的项目模版，包括依赖库，免去你手动安装各种插件，寻找各种cdn并一个个引入的麻烦,输入以下命令安装：

   ```text
   npm install -g vite				——————vue-vite
   
   npm install vue-cli				——————vue3
   ```

   安装完成后输入`vue -V`(为大写的V),如果出现版本信息即为安装成功。

9. 创建vue项目

   ```text
   npm create vue@latest
   ```

   然后按步骤输入项目信息，注意Project name（默认项目名称vue-project）不支持大写字母为项目名，项目创建好后，它也给出了提示信息，继续操作即可。

   

10. 每一个项目都有一个package.json文件，里面有很多组件信息，使用`npm install`将按照package.json安装所需要的组件放在生成的node_modules文件夹中，项目下的每一个文件中都可以通过import引入node_modules的组件来加以使用,首先输入`cd myProject`进行项目目录中，然后输入以下命令:

    ```text
    npm install
    ```

    

11. 启动项目

    ```
    npm run dev					——————vue-vite
    
    npm run serve				——————vue3
    ```
    
11. 记得build一下(项目还没有构建的时候，环境还没好)

    ```
    npm run build
    ```
    



## 2.项目创建

1. 创建项目

   ```
   npm create vue@latest
   ```

2. 下载依赖

   ```
   npm install
   npm run build
   ```

3. 启动项目

   ```
   npm run dev
   ```

### 

## 3.目录结构

1、build：构建脚本目录
　1）build.js ==> 生产环境构建脚本；
　2）check-versions.js ==> 检查npm，node.js版本；
　3）utils.js ==> 构建相关工具方法；
　5）webpack.base.conf.js ==> webpack基本配置；
　6）webpack.dev.conf.js ==> webpack开发环境配置；
　7）webpack.prod.conf.js ==> webpack生产环境配置；

2、config：项目配置
　1）dev.env.js ==> 开发环境变量；
　2）index.js ==> 项目配置文件；
　3）prod.env.js ==> 生产环境变量；

3、node_modules：npm 加载的项目依赖模块

4、src：这里是我们要开发的目录，基本上要做的事情都在这个目录里。里面包含了几个目录及文件：
　1）assets：资源目录，放置一些图片或者公共js、公共css。这里的资源会被webpack构建；
　2）components：组件目录，我们写的组件就放在这个目录里面；
　3）router：前端路由，我们需要配置的路由路径写在index.js里面；
　**4）App.vue：根组件；**
　**5）main.js：入口js文件；**

5、static：静态资源目录，如图片、字体等。不会被webpack构建

**6、index.html：首页入口文件，可以添加一些 meta 信息等**

7、package.json：npm包配置文件，定义了项目的npm脚本，依赖包等信息

8、README.md：项目的说明文档，markdown 格式

9、.xxxx文件：这些是一些配置文件，包括语法配置，git配置等



------

**index.html   ->  main.js  ->   App.vue   ->  router/index.js  ->  view/xxx.vue**

1. **Main.js**

   作为入口文件，其中会包括构建app，使用插件和挂载

   ```
   如
   
   Const xx  = createApp(aaa)
   
   xx.use(插件，如router)
   
   xx.mount("#app")
   ```

   

2. **项目中所有页面都会先加载main.js**

   所以main.js里面要构建vue实例，存入常用的插件（router，axios，element-ui），常用的css，存储全局变量，挂载

   ```vue
   import {createApp} from 'Vue'
   import App from './App.vue'  #作为根主件
   import router from './router'
   import ElementUI from 'element-ui'
   import 'element-ui/lib/theme-chalk/index.css'
   
   
   #初始化vue实例，此时使用单文件App.vue作为根主件初始化Vue
   const Vue = createApp(App)
   
   #使用插件
   vue.use(router)
   vue.use(elementUI)
   (axios 一般不在main.js 里面写，有另外专用的文件写)
   
   #使用常用的css(常用的js也可以导入)
   import from './assets/css/common.css'
   import from './assets/css/public.css'
   
   
   
   #挂载
   Vue.mount('#app')   (挂载到了index.html)
   ```

   

3. **App.vue**

   作为根文件，所有其他的vue页面都基于此，内部通常为

   ```vue
   <template>
     <Routerview/>
   </template>
   ```

   

4. **router/index.js**

   里面配置了各个页面的路由，router = createRouter(history,routes)

   最后记得 export default router 

   

   设置初始页面也在index.js中，需要import xxx from ‘../view/home.vue’引入初始页面，然后compoent:xxx

   

5. **Vite.config.vue**

   跨域时，设置代理

   

6. **utils/request.js**

   引入axios，创建并初始化axios，然后进行请求拦截和响应拦截

   ```vue
   import axios from 'axios'
   
   //初始化service
   const servise = axios.create({
   	baseURL: process.env.VUE_APP_BASE_API,
   	timeout: 10000000 
   })
   
   //请求拦截
   service.interceptors.request.use(
   config =>{
   	return config
   },
   error =>{
   	return Promise.reject(error)
   }
   )
   
   
   //响应拦截
   service.interceptors.response.use(
   res =>{
   	return res
   },
   error =>{
   	return Promise.reject(error)
   }
   )
   
   export default service
   ```

   

   

   一般情况，请求拦截 与token有关的，响应拦截则有较多要拦截的内容

   ```
   if(localStorage.getItme('token')){
     service.interceptors.request.use(
     config =>{
     	const token = 'Bear '+ localStorage.getItme('token')
     	if(token){
     		config.headers.Authorization = token
     	}
       return config
     },
     error =>{
       return Promise.reject(error)
     }
     )
   }
   ```

   

   ```
   service.interceptors.response.use(response => {
   
       return response
   }, error => {
       /***** 接收到异常响应的处理开始 *****/
       if (error && error.response) {
           // 1.公共错误处理
           // 2.根据响应码具体处理
           switch (error.response.status) {
               case 400:
                   error.message = '错误请求'
                   break;
               case 401:
                   error.message = '未授权，请重新登录'
                   break;
               case 403:
                   error.message = '拒绝访问'
                   break;
               case 404:
                   error.message = '请求错误,未找到该资源'
                   // window.location.href = "/NotFound"
                   break;
               case 405:
                   error.message = '请求方法未允许'
                   break;
               case 408:
                   error.message = '请求超时'
                   break;
               case 500:
                   error.message = '服务器端出错'
                   break;
               case 501:
                   error.message = '网络未实现'
                   break;
               case 502:
                   error.message = '网络错误'
                   break;
               case 503:
                   error.message = '服务不可用'
                   break;
               case 504:
                   error.message = '网络超时'
                   break;
               case 505:
                   error.message = 'http版本不支持该请求'
                   break;
               default:
                   error.message = `连接错误${error.response.status}`
           }
       } else {
   
           if (JSON.stringify(error).includes('timeout')) {
               // Message.error('服务器响应超时，请刷新当前页')
           }
           error.message = '连接服务器失败'
       }
   
       // Message.error(error.message)
   
       return Promise.resolve(error.response)
   })
   ```

   

7. **http.js**

   引入request，定义具体的config(get，post，put，delete、update)，最后return request(config),

   ```
   import request from './request'
   
   const http = {
   	get(url,params){
   		const config = {
   			method : 'get',
   			url : url
   		}
   		if (param)config.params = params
   		return request(comfig)
   	},
   	
   	post(url, params){
   		const config = {
   			method : 'post',
   			url : url
   		}
   		if(params)config.params = params
   		return request(config)
   		
   		...
   		
   	}
   }
   
   export default http
   ```

   

8. **api.js**

   引入http，进行具体功能的参数传递

   ```
   import http from '../utils/http'
   
   export default{
   	login(name,phone){
   	let params={
   	'name':name,
   	'phone':phone,
   	}
   	return http.post('/xxx',params)
   	}
   	...
   }
   ```

   

   在网页中具体发送请求：

   ```
   引入api
   
   api.login(xx,xx).then(
   	res =>{
   	if(res.status == 200){
   	
   	}
   	}.catch(err=>{
   	console.log(err)
   	})
   )
   ```

   

9. 

   

### 4.项目使用

1. 数据绑定

   ```vue
   <template>
   <div>
     {{ message }}
     </div>
   </template>
   
   
   <script>
   export default{
     data(){
       return{
         message:"xxx",
       }
     },
   }
   </script>
   
   ```

   

2. 



