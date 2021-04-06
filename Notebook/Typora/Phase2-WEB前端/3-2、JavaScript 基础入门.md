# JavaScript 基础入门

## 一、HTML中使用JavaScript代码

1. 在html文件中，在一对script标记中，直接编写

   ```
   <script type="text/javascript">
    //js代码
   </script>

   ```

2. 在js文件中，直接编写，在html中，使用一对script标记直接引用

   ```
   <script src="js/demo.js" language="javascript">
   //如果引入了外部文件 请不要在这里写代码,不会执行到
   //如果引入了外部文件 请不要在这里写代码,不会执行到
   //如果引入了外部文件 请不要在这里写代码,不会执行到
   </script>
   1. language：引用的语言 javascript、php、c#、VBSCRIPT 
   2. src：引用一个外部的js文件

   ```

>笔记：
>
>简单使用
>
>```
>1、外部导入<script src="js/home.js" type="text/javascript"></script>，注意这种方式不要在标签内部写代码，因为不会执行
>2、标签内部写代码
><script type="text/javascript">
>//代码
></script>
>3、注释和java一样  // 为单行注释； /**/为多行注释；
>4、type可以省略，JavaScript 是所有现代浏览器以及 HTML5 中的默认脚本语言。但为了兼容旧版浏览器，最好不要省略
>5、type 可以换成language属性
><script language="javascript"></script>
>6、<script>标签可以写在head和body里面
>```



## 二、基本语法规则

1. JavaScript脚本程序须嵌入在HTML文件中
2. JavaScript脚本程序中不能包含HTML标记代码

## 三、什么是标识符

 标识符就是一个名字,在JavaScript中,标识符就是用来对变量,函数进行命名的,或者用来作为JavaScript代码中某些循环语句中跳转位置的标记,JavaScript标识符必须以字母,下划线_或者美元符号开始,后续的字符可以是字母,数字,下划线,或者美元

注意事项

1. 标识符不能以数字开头


1. 不能包含保留字


1. 标识符不能包含空格


1. 区分大小写。A 和a 是两个完全不同的标示符
2. 长度无限制。（习惯，不要超过15个字符）

## 四、保留字-关键字

### 1、JavaScript 保留关键字

1. 注意事项

   ```
   Javascript 的保留关键字不可以用作变量、标签或者函数名。有些保留关键字是作为 Javascript 以后扩展使用
   ```

2. 示意图

   ![img](http://opzv089nq.bkt.clouddn.com/17-8-21/15295401.jpg)

### 2、JS对象、属性和方法

1. 注意事项

   ```
   js对象、属性和方法不可以用作变量、标签或者函数名
   ```

2. 示意图

   ![img](http://opzv089nq.bkt.clouddn.com/17-8-21/7418350.jpg)

### 3、Java 保留关键字

1. 说明

   ```
   JavaScript 经常与 Java 一起使用。您应该避免使用一些 Java 对象和属性作为 JavaScript 标识符
   ```

2. 示例图

   ![img](http://opzv089nq.bkt.clouddn.com/17-8-21/93681007.jpg)

### 4、Windows 保留关键字

1. 注意事项

   ```
   JavaScript 可以在 HTML 外部使用。它可在许多其他应用程序中作为编程语言使用。
   在HTML中，为了可移植性,避免使用 HTML 和 Windows 对象和属性的名称作为 Javascript 的变量及函数名
   ```

2. 示例代码

   ![img](http://opzv089nq.bkt.clouddn.com/17-8-21/40843066.jpg)

### 5、HTML 事件

1. 示例图

   ![img](http://opzv089nq.bkt.clouddn.com/17-8-21/46224657.jpg)

## 五、分号

 JavaScript和其他语言一样,是用分号(;)将语句分开,这个对于增加代码的整洁性,和可读性非常重要,缺少分隔符,一条语句的结束可能就成了一条语句的开始

## 七、类型 值

 在我们程序运行在计算机中经常要对值进行操作,在编程语言中,能够表示操作值的类型的叫数据类型,所以在编程语言最基本的特性就是支持多种数据类型.当程序需要将值保存起来以备将来用到,便将值赋值给变量,变量就是这个值的名称,通过这个名称我们就可以操作这个值的引用.变量也是编程语言的基本特性