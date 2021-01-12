# CSS概述

## 一、什么是CSS?

1. CSS 指层叠样式表 (**C**ascading **S**tyle **S**heets)
2. 样式定义**如何显示**HTML 元素
3. 样式通常存储在**样式表**中
4. 把样式添加到 HTML 4.0 中，是为了**解决内容与表现分离的问题**
5. **外部样式表**可以极大提高工作效率
6. 外部样式表通常存储在**CSS 文件**中
7. 多个样式定义可**层叠**为一

## 二、为何使用CSS？

 CSS帮助您将文档信息的内容 和如何展现它的细节相分离,如何展现文档的细节即为样式(style)。您可以将样式从它的内容分离出来，能使我们在开发中：

1. 避免重复
2. 更容易维护

```
css: 层叠样式表， 修饰html， 为了让html节点好看

css样式属性

css的写法：
   1， 行间样式/内联样式，  使用style
   2, 内部样式， 写在style标签中
   3, 外部样式， 写在单独的css文件中，通过link标签引入
```





## 三、发展史

1. 1996年12月，发布了CSS 1.0规范。
2. 1998年 5月，发布了CSS 2.0规范。
3. 2004年 6月，发布了CSS 2.1规范。
4. 2011年 9月，发布了CSS 3.0规范。

## 四、如何使用CS

### 1、外部样式表(External style sheet)

1. 说明

   ```
   就是把css样式代码写在单独的一个文件中,文件以“.css”为扩展名，在 head 标签内使用 link 标签,将 css 样式文件链接到HTML文件内,当样式需要应用于很多页面时，一般我们都会使用外部样式表
   ```

2. 示例代码

   ```
   <head>
       <link href="css/style.css"  rel="stylesheet" type="text/css">
   </head>
   ```

3. 特点

   ```
   1、外部式css样式，写在单独的一个文件中
   ```

4. 注意事项

   1、css样式文件名称以有意义的英文字母命名，如 main.css。

   2、rel="stylesheet" type="text/css" 是固定写法不可修改。
   3、link 标签位置一般写在 head 标签之内最上面。

### 2、内部样式表(Internal style sheet)

1. 说明

   ```
    把样式代码写在 <style type="text/css"></style> 标签之间,
    当单个文档需要特殊的样式时，就应该使用内部样式表,我们可以使用 <style> 标签在文档头部定义内部样式表
   ```

2. 示例代码

   ```
   <head>
     <style type="text/css">
           div{
               width: 50px;
               height: 50px;
               background: red;
           }
       </style>
   </head>
   ```

3. 注意：

   ```
   嵌入式css样式必须写在 <style></style> 之间，并且一般情况下内部样式写在 <head></head> 之间
   ```

### 3、内联样式(Inline style)

1. 说明

   内联式css样式，直接写在在HTML标签中，同时css样式代码写在 style="" 双引号中，如果有多条css样式代码设置可以写在一起，中间用分号 ; 隔开。当样式只在一个元素使用一次时,可以直接元素上使用sytle属性,由于内联样式跟内容混合在一起,一般在开发中尽量不使用

   > 注意：这种写法不推荐使用，特别是对新手来说。这也完全违背了HTML内容和CSS样式显示分离的思想。

2. 示例代码

   ```
   <div style="width:50px;
               height:50px;
               background:red">
   </div>

   ```

### 4、多重样式(样式继承)

1. 说明

   ```
   如果某些属性在不同的样式表中被同样的选择器定义，那么属性值将从更具体的样式表中被继承过来

   ```

2. 示例代码

   ```
    <head>
       <style type="text/css">
           p{
               color:red;
               text-align:center;
               font-size:16px;
           }
           p{
               font-size:20px;
           }
       </style>
   </head>

   ```

   那么最终我们设置的p标签的样式应该为

   ```
   p{
    color:red;
    text-align:center;
    font-size:20px;
   }
   ```

3. 一般情况下的优先级

   ```
   优先级：权值相同的条件下，遵循的是就近原则（离被设置元素越近优先级别越高）。
   ```

   ```
   （内联样式）Inline style > （内部样式）Internal style sheet
    >（外部样式）External style sheet > 浏览器默认样式

   ```



### 5  CSS写法案例

#### 5.1  css外部导入和内联样式结合处理

​     （1）创建css文件demo.css  ,  css/demo.css， 内容如下：

```
div {font-size: 30px; font-family: "微软雅黑"; }
```

​    （2）在主html文件中引入外部css文件

头部定义和body体定义

```
<head>
<!--引入外部css文件， 外部样式-->
<link rel="stylesheet" href="css/demo.css" />
```

```
<!--写css的标签， 内部样式-->
<style>
   
   /*css注释*/
   /*div : 标签选择器*/
   div {background: green;}
   
</style>
</head>
```

```
<body>
   
   <!--
      css: 层叠样式表， 修饰html， 为了让html节点好看
      
      css样式属性
      
      css的写法： 
         1， 行间样式/内联样式，  使用style
         2, 内部样式， 写在style标签中
         3, 外部样式， 写在单独的css文件中，通过link标签引入
   -->
   <!--
      background: 复合属性
   -->
   <div style="width: 200px; height: 50px;">div1</div>
   
   <div>div2</div>
   
</body>
```



### 5.2 CSS样式的优先级

```
css这三种写法的优先级： 
   1， 行间样式优先级最高
   2， 内部样式和外部样式，就看谁写在后面（后面会覆盖前面的样式）
```

见例子2-1 css写法优先级.html





