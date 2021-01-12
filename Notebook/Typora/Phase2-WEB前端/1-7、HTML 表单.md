# HTML 表单

## 一、表单概述

### 1、作用：

1. 用于为用户创建 HTML 表单,用于向服务器传输数据。
2. 表单能够包含 input 元素，比如文本字段、复选框、单选框、提交按钮等等。
3. 表单还可以包含 menus、textarea、fieldset、legend 和 label 元素。

### 2、格式

```
<form action="login.action" method="get">
  <p>First name: <input type="text" name="fname" /></p>
  <p>Last name: <input type="text" name="lname" /></p>
  <input type="submit" value="Submit" />
</form>

```

### 3、说明

1. 所有的表单内容，都要写在form标签里面
2. form标签中有两个比较重要的属性action和method以及enctype
   - action 提交地址（一般是服务器后台地址）
   - method 提交方式
   - enctype 设置采用什么样的形式提交数据

### 二 、标签

### 1、作用

标签用于为用户输入创建 HTML 表单

### 2、格式

```
<form 
    name="test" 
    action="form_action.action" 
    method="get">
</form>

```

### 3、常用属性：

1. name：表单提交时的名称
2. action：提交到的地址
3. method：规定用于发送 form-data 的 HTTP 方法，提交方式：get和post
4. enctype：规定在发送表单数据之前如何对其进行编码
   - application/x-www-form-urlencoded：在发送前编码所有字符（默认）
   - text/plain：空格转换为 "+" 加号，但不对特殊字符编码
   - multipart/form-data：使用包含文件上传控件的表单时，必须使用该值

### 4、总结

1. html form是表单区域标签，通常此标签内放输入框、单选、多选、多行文本框、下拉选项菜单等表单内容
2. form的action的值填写为将表单提交内容到后台控制层。

## 三 、input标签

### 1、作用

 input标签用于搜集用户信息。根据不同的 type 属性值，输入字段拥有很多种形式。输入字段可以是文本字段、复选框、掩码后的文本控件、单选按钮、按钮等等。

> ！！！如果说td是表格最核心的标签，那么input就是表单最核心的标签。 input标签有一个type属性，这个属性有很多类型的取值，取值的不同就决定了input标签的功能和外观不同。

### 2、格式

```
<input 
    name="username" 
    type="text" 
    placeholder="用户名" 
    maxlength=10 
    value=123 
/>

```

### 3、HTML4 Input 类型

#### 3.1、明文输入框

1. 作用：

   用户可以在输入框内输入内容

2. 输入明文文本内容

   ```
   <p>
     账号:<input type="text"/>
   </p>

   ```

3. 给输入框设置默认值

   ```
   <p>
     账号:<input type="text" value="xxx"/>
   </p>
   <p>
     密码:<input type="password" value="xxx"/>
   </p>

   ```

4. 规定输入字段中的字符的最大长度

   ```
   <p>
     密码:<input type="password" maxlength="15"/>
   </p>

   ```

#### 3.2、暗文输入框

1. 作用：

   用户可以在输入框内输入内容

2. 示例代码

   ```
   <p>
     密码:<input type="password"/>
   </p>
   也可以指定默认值，也可以指定最大长度。

   ```

#### 3.3、 单选框(radio)

1. 作用：

   用户只能从众多选项中选择其中一个

2. 单选按钮，

   天生是不互斥的，如果想互斥，**必须要有相同的name属性**

3. 示例

   ```
   篮球<input type="radio" name="a" value="basketball">
   足球<input type="radio" name="a" value="">
   皮球<input type="radio" name="a" value="">
   排球<input type="radio" name="a" value="">
   铅球<input type="radio" name="a" value="">

   ```

\>说明：value属性后期服务器获取值时才会用到

#### 3.4、多选框(checkbox)

1. 作用：

    用户只能从众多选项中选择多个

2. 复选框，

    最好也是有相同的name（虽然他不需要互斥）

3. 示例

   ```html
   篮球<input type="checkbox" name="a">
   足球<input type="checkbox" name="a">
   皮球<input type="checkbox" name="a">
   排球<input type="checkbox" name="a">
   铅球<input type="checkbox" name="a">

   ```

#### 3.5、按钮(button)

1. 作用：

   定义可点击按钮（多数情况下，用于通过 JavaScript 启动脚本，触发js事件）

2. 格式：

   ```
   <input type="button" value="按钮" />
   ```

#### 3.6、 图片按钮(image)

1. 作用：

   定义图像形式的提交按钮

2. 格式

   ```
   <input type="image" src="cancel.png" />
   ```

#### 3.7、 重置按钮(reset)

1. 作用：

   定义重置按钮。重置按钮会清除表单中的所有数据

2. 格式：

   ```
   <input type="reset" value ="重置"/>
   ```

3. 说明：

   - 这个按钮不需要写value自动就有“重置”文字
   - reset只对form表单中表单项有效果

#### 3.8、 提交按钮(submit)

1. 作用：

   定义提交按钮。提交按钮会把表单数据发送到action属性指定的页面

2. 格式：

   ```
   <input type="submit" value="提交"/>

   ```

3. 说明：

   - 这个按钮不需要写value自动就有“提交”文字
   - 要想通过submit提交数据到服务器, 被提交的表单项都必须设置name属性
   - 默认明文传输(GET)不安全，可以将method属性设置为POST改为非明文传输(学到Ajax再理解)

4. 示例代码：

   ```
   <form action="http://www.baidu.com" method="get">
       账号: <input type="text" name="user"/><br>
       密码: <input type="text" name="psw"/><br>
       <input type="submit"/>
   </form>
   ```

#### 3.9、 图片按钮(image)

1. 作用

   定义图像形式的**提交按钮**

2. 格式：

   ```
   <input type="image" src="icon.png" />
   ```

3. 说明

   与submit效果类似，只不过是图片按钮。

#### 3.10、多行文本框(textarea)

1. 作用:

   textarea标签用于在表单中定义多行的文本输入控件

2. 格式：

   ```
   <textarea rows="10" cols="30"></textarea>
   <!--cols属性表示columns“列”, 规定文本区内的可见宽度 -->
   <!-- rows属性表示rows“行”, 规定文本区内的可见行数-->

   ```

#### 3.11、隐藏域(hidden)

1. 作用：

   定义隐藏的输入字段（一般用于传递隐藏数据，用的不多）

2. 格式：

   ```
   <input type="hidden">
   ```

#### 3.12、下拉框(select)

1、属性disable：禁止选中

2、属性select=“selected”：默认选中

```
<select id="cars">
    <option value="benz">奔驰</option>
    <option value="bmw">宝马</option>
    <option value="audi">奥迪</option>
    <option value="landrover">路虎</option>
    <option value="maserati">玛莎拉蒂</option>
    <option value="bentley">宾利</option>
     <option value="lamborghini">兰博基尼</option>
</select>
请输入你的车型: <input type="text" list="cars">
```

>说明：
>
>```javascript
>在js代码中,清除option的操作：
>1、直接使用Dom操作的remove删除
>var select_ele = document.getElementByid("select_id");
>var children = select_ele.children;
>for(var i = 0;i<children.length; ){
>  children[i].remove;
>}
>2、直接获取所有options,然后通过改变他的长度进行删除，从后面开始删。
>var select_ele = document.getElementByid("select_id");
>select_ele.options.length=0;
>```



#### 3.13、文件上传（file）

1、用于文件上传，默认是单文件，如果想上传多个文件 加上multiple属性

2、格式：

```php+HTML
单文件上传<input type="file"/>
多文件上传<input type="file" multiple/>
只上传图片<input type="file" accept="image/*"> <!--accept属性指定上传文件的类型-->

```

### 4、HTML5智能表单

1. type = "email" 限制用户输入必须为Email类型
2. type="url" 限制用户输入必须为URL类型
3. type="date" 限制用户输入必须为日期类型
4. type="datetime" 显示完整日期 含时区
5. type="datetime-local" 显示完整日期 不含时区
6. type="time" 限制用户输入必须为时间类型
7. type="month" 限制用户输入必须为月类型
8. type="week" 限制用户输入必须为周类型
9. type="number" 限制用户输入必须为数字类型
10. type="range" 生成一个滑动条
11. type="search" 具有搜索意义的表单results="n"属性
12. type="color" 生成一个颜色选择表单
13. type="tel" 显示电话号码

### 5、HTML5新增表单属性

1. required:内容不能为空

2. placeholder 表单提示信息

   ```
   <input type="text" placeholder="请输入用户名"/>
   ```

3. autofocus:自动聚焦

4. pattern: 正则表达式 输入的内容必须匹配到指定正则范围

5. autocomplete:是否保存用户输入值

   - 默认为on，
   - 关闭提示选择off

6. formaction: 在submit里定义提交地址

7. datalist: 输入框选择列表配合list使用 list值为datalist的id值

8. output: 计算或脚本输出

