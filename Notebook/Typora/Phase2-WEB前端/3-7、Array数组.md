# Array数组

## 一、概念

> 笔记：简单使用
>
> ```javascript
> //数组创建
> //创建数组常用方式
> var arr = ["小红",true,110,43.9];
> arr[99] = 100;//给数组添加元素，js数组不会出现数组越界
> var arr = ("dka",false,329,7.9);
> //通过构造方法创建(不推荐)
> var arr = new Array();
> var arr = new Array(length);//参数length表示数组的长度
> var arr = new Array("小红",21,true)//参数为每个元素的值
>
> //数组遍历
> //主要方式
> for (var i = 0;i<arr.length;i++){
>     console.log(arr[i]);//控制台打印
> }
> //不推荐使用（了解）ES5遍历的方式
> for (var index in arr) {
>     console.log(arr[index]);//注意这里的index变量指的是数组的下标
> }
> //使用数组对象的方法，循环数组length次
> arr.forEach(function (value,index,arr) {
>     console.log(value);//value参数代表数组元素的值
>     console.log(index);//index参数代表数组索引
>     console.log(arr);//arr代表整个数组的值，可以省略这个参数不写，就是本身
> })
> //ES6(ES2015标准)新增方式
> //新增一：遍历数组
> var newArr = arr.map(function(item){
>   //对元素进行处理规则的代码，可以不写，直接返回ele,即返回数组每个元素。
>     return item;
> });
> //新增二：过滤数据
> var newArr = arr.filter(function(item){
>     return XXX;
> })
> //新增三：判断是否存在满足条件的元素，只要存在一个就返回true
> var isexist = arr.some(function(item){
>     return item>2;
> });
> //
> for(let obj of arr){
>    
> }
> ```

### 1、什么是数组

### 1.1  数组的定义

方式一:  

​      new Array（参数，参数,...）: 只有一个数字参数时是数组的长度（new可以省略,但一般尽量写上）

例如: 

​     var arr = new Array();   //定义一个空数组 

​     var arr = new Array(10);  //创建一个包含 10 个元素的数组，没有赋值

​     var arr = new Array(“芙蓉姐姐”,30);  //创建一个数组有两个元素

方式二: 

​     var arr = [1,2,3,4,5];  //字面量定义方式

### 1.2  数组元素的获取(访问)

​     arr[0]: 表示数组的第一个元素，0是下标，也叫索引

​     arr[1]: 表示数组的第二个元素，1是下标 

 数组是指数据的有序列表,可以包含任意数据类型，并通过索引来访问每个元素

1. 数组中每个值称之为数组的一个元素。
2. 数组中的每个元素都有一个位置，这个位置称之为索引(下标、index)。**数组的索引是从 0 开始的**
3. 同一个数组中，元素的类型不做任何限制。也就是说，同一个数组中可以放Number、String、Boolean、Object对象等等。可以同时放入任何的类型。甚至数组中的元素可以是另外一个数组(构成多维数组)。

### 1.3  数组的遍历

​	一般使用普通for循环

​	length : 数组长度

### 1.4  数组的常用方法: 

​	push(): 接收任意数量的参数，把它们逐个添加到数组的末尾，并返回修改后数组的长度;

​     	pop(): 从数组末尾移除最后一个元素，减少数组的 length 值，然后返回移除的元素;

​	sort() : 从小到大排序 ,  原数组也被升序排序了

​         reverse() : 逆向排序, 原数组也被逆向排序了

​	slice() :  不修改原数组, 将原数组中的指定区域数据提取出来并返回一个新数组

​	splice() : 截取原数组中指定的数据, 会改变原数组

​	indexOf() : 获取数组中第一个出现指定元素的下标， 如果不存在则返回-1

​	join() : 将数组中的元素用指定字符连接，连接成为一个字符串，



### 2、分类

#### 1、单维数组

1. 语法结构

   ```
   var arr = [元素1,元素2,元素3....元素N ];

   ```

2. 示例图

   ![img](http://opzv089nq.bkt.clouddn.com/17-8-22/15580468.jpg)

#### 2、多维数组

1. 语法结构

   ```
   var  arr =  [[数组1],[数组2],[数组3],[数组N]];

   ```

2. 示例图

   ![img](http://opzv089nq.bkt.clouddn.com/17-8-22/48377237.jpg)

### 3、特性

1. 数组长度可以动态改变。
2. 同一个数组中可以存储不同的数据类型。
3. 数据的有序集合
4. 每个数组都有一个**length**属性，表示的是数组中元素的个数

## 二、创建方法

### 1、数组字面量(推荐)

1. 创建一个空数组

   ```
   var arr = [];

   ```

2. 创建一个包含1项的数组

   ```
    var arr= [20];

   ```

3. 创建一个包含N个字符串的数组

   ```
   var arr = ["元素1","元素2","元素3",...."元素N"];

   ```

### 2、构造函数(了解)

1. 创建一个length为0的空数组

   ```
   var array = new Array();
   ```

2. 创建一个指定长度的空数组

   ```
   var array = new Array(size);
   ```

3. 指定元素数组

   ```
   var array = new Array(元素1,元素2,....元素N);
   ```

## 三、基本操作

### 1、访问数组

1. 通过索引获取元素的值

   ```
   1. 单维数组
       var 变量名 = 数组名 [下标索引]
   2. 多维数组 
       var 变量名 = 数组名 [外层数组下标索引][内存元素下标索引

   ```

2. 通过循环遍历

   ```
   1. 普通for循环
   2. for... in
   3. for each ( ES5 新增)
   4. for…of ( ES6新增 )

   ```

3. 索引示例代码

   ```
   1.通过索引查找
        var arr = [1, 2, 3, 4, 5];
        var value = arr[0]; //value为1
   2. var arr = [[1,2,3], [4,5,6], [7,8,9]];
        var value = arr[0][0]; //value为1
         var value = arr[1][0]; //value为4

   ```

4. 普通for循环遍历

   ```
   var arr = [50, 20, 10, 5, 15, 6];        
   for(var i = 0; i < arr.length; i++){    //数组长度多长，就遍历多少次。  循环变量作为数组的下标
     console.log(arr[i]);
   }
   ```

5. for...in 遍历

   ```
   var arr = [50, 20, 10, 5, 15, 6];
   // 每循环一轮，都会把数组的下标赋值给变量index，然后num就拿到了每个元素的下标。 
   //注意:这里index是元素的下标,不是与元素
   //对数组来说，index从从0开始顺序获取下标
   for (var index in arr) {
     console.log(num);  //循环输出： 0 1 2 3 4 5
   }
   //这里var 关键字也是可以省略的，但是不建议省略。
   for(i in arr){
     console.log(arr[i]);
   }
   ```

6. forEach遍历

   ```
   var arr = [50, 20, 10, 5, 15, 6];
   /**调用数组的forEach方法，传入一个匿名函数
    *匿名函数接受两个参数：   
    *参数1--迭代遍历的那个元素  
    *参数2：迭代遍历的那个元素的下标
    *参数3:遍历的数组对象
    */
   arr.forEach( function(element, index,arr) {
     console.log(element);//打印数组的元素
     console.log(element);//打印索引
   });
   ```

### 2、增加元素

1. 说明

   ```
   使用"[]"运算符指定一个新下标

   ```

2. 示例代码:

   ```
   var arr =  new Array();
   arr[0] = 1;
   arr[100] = "隔壁老宋"
   说明:
   如果把length设置为大于最大index+1的值的时候，数组也会自动扩张，但是不会为数组添加新元素，只是在尾部追加空空间
   arr[1]-arr[99]的值全部是undefined

   ```

### 3、删除元素

1. 说明

   ```
    delete 数组名[下标]
   ```

2. 示例代码

   ```
   var arr = [1, 2, 3, 4, 5];
   delete  arr[0];

   说明:
   这样和直接把arr[0]赋值为undefined，不会改变数组长度，也不会改变其他数据的index和value对应关系, 
   在实际开发中我们可能希望删除中间一个元素后，后面元素的index都自动减一，数组length同时减一

   ```

## 四、常用方法(移步官方文档)

1、[官方文档](http://www.w3school.com.cn/jsref/jsref_obj_array.asp)

2、Array 对象属性

| 属性          | 描述                |
| ----------- | ----------------- |
| constructor | 返回对创建此对象的数组函数的引用。 |
| length      | 设置或返回数组中元素的数目。    |
| prototype   | 使您有能力向对象添加属性和方法。  |

3、Array 对象方法

| 方法               | 描述                              |
| ---------------- | ------------------------------- |
| concat()         | 连接两个或更多的数组，并返回结果。               |
| join()           | 把数组的所有元素放入一个字符串。元素通过指定的分隔符进行分隔。 |
| pop()            | 删除并返回数组的最后一个元素                  |
| push()           | 向数组的末尾添加一个或更多元素，并返回新的长度。        |
| reverse()        | 颠倒数组中元素的顺序。                     |
| shift()          | 删除并返回数组的第一个元素                   |
| slice()          | 从某个已有的数组返回选定的元素                 |
| sort()           | 对数组的元素进行排序                      |
| splice()         | 删除元素，并向数组添加新元素。                 |
| toSource()       | 返回该对象的源代码。                      |
| toString()       | 把数组转换为字符串，并返回结果。                |
| toLocaleString() | 把数组转换为本地数组，并返回结果。               |
| unshift()        | 向数组的开头添加一个或更多元素，并返回新的长度。        |
| valueOf()        | 返回数组对象的原始值                      |



## 五、数组检测

 如何检测一个对象是不是一个Array

1. 使用instanceof运算符。
2. 使用Array.isArray(arr) 方法。

