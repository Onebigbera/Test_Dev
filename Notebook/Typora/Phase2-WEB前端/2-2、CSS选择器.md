## CSS语法规范

- 语法：css 样式由选择符和声明组成，而声明又由属性和值组成。

- 选择符：又称选择器，指明网页中要应用样式规则的元素。

- 声明：大括号 ｛｝ 中的就是声明，属性和值之间用英文冒号 ： 分隔。当有多条声明时，中间可以英文分号 ; 分隔。

- 例如：

  ```css
  <style type="text/css">
      h1{  background: black;}
      /*选择器{属性 ：值}*/
  </style>
  ```



## CSS选择器

#### 1 基本选择器

- id选择器（id是唯一的，一个HTML尽量不要存在相同的id,否则只会匹配其中一个）：

  - CSS：`#id_test {}`（#+id属性值{}）
  - HTML：`<div id="id_test">天青色等烟雨</div>`

- class选择器：（class可以重复，所有相同class都能匹配成功）

  - CSS：`.class_test {}`（.+class属性值{}）
  - HTML：`<div class="class_test">天青色等烟雨</div>`

- 标签选择器：（对制定元素都起作用）

  - CSS：`div {}`(标签名{})
  - HTML：`<div>天青色等烟雨</div>`

- 通配符选择器：匹配界面上的所有元素（一般用来去除默认的样式）

  CSS:   `* { }`

#### 2 子元素选择器

格式：

```
 选择器 > 选择器 { }
```

> 笔记：说明
>
> 1、子元素选择器只能设置一级关系标签的（子标签）样式，不能设置多级标签（孙子标签及以下级别标签）样式
>
> ```html
> <head>
>   <style type="text/css">
>   	#c > p {
>               background: rebeccapurple;
>               font-size: 50px;
>           }
>   </style>
> </head>
>
> <body>
>   <div id="c">
>     <p>儿子</p>   <!--只有该子标签会被设置样式-->
>     <div>
>       <p>孙子</p>  <!--该孙子标签不会被设置样式-->
>     </div>
>   </div>
> </body>
> ```

示例一：

```html
ul > li {}
```

要求必须是`ul`标签的子标签`li`才起作用。

示例二：

```html
div > #id_test {}
```

要求必须是`div`标签的子标签的 id为`id_test`才起作用。

示例三：

```html
#id_test > .class_test {}
```

要求必须是 id为`id_test`标签的子标签的class为`class_test`才起作用。

#### 3 后代选择器

格式：

```
选择器1 [空格] 选择器2
```

> 笔记：说明
>
> 1、只要选择器2是选择器1里面的一个子（孙子）标签就会被设置样式
>
> ```html
> <head>
>   <style type="text/css">
>   	#c p {
>               background: rebeccapurple;
>               font-size: 50px;
>           }
>   </style>
> </head>
>
> <body>
>   <div id="c">
>     <p>儿子</p>   <!--该子标签会被设置样式-->
>     <div>
>       <p>孙子</p>  <!--该孙子标签也会被设置样式-->
>     </div>
>   </div>
> </body>
> ```

示例一：

```html
ul  li {}
```

要求必须是`ul`标签的子(或孙子)标签`li`才起作用。

示例二：

```html

```

示例三：

```html
#id_test  .class_test {}
```

要求必须是 id为`id_test`标签的子(或孙子)标签的class为`class_test`才起作用。

> 提示：尽量少使用后代选择器，一般使用class代替后代选择器。

#### 4 伪类选择器

##### 1、动态伪类选择器

```css
a:link {color: #FF0000}		/* 未访问的链接 */
a:visited {color: #00FF00}	/* 已访问的链接 */
a:hover {color: #FF00FF}	/* 鼠标移动到链接上(重要) */  
a:active {color: #0000FF}	/* 选定的链接 */
/*a代表选择器*/
```

>提示：在 CSS 定义中，a:hover 必须被置于 a:link 和 a:visited 之后，才是有效的。
>
>提示：在 CSS 定义中，a:active 必须被置于 a:hover 之后，才是有效的。
>
>提示：伪类名称对大小写不敏感。
>
>（即说这几个有一定的顺序，可以默认不写其中的某些，但写了的话就不要乱了顺序）

##### 2、目标伪类选择器(重点)

```
a:target{}
```

##### 3、状态伪类选择器

```
选择器：checked  表示元素被选中的状态样式（checkbox radio使用）
选择器：enabled  表示匹配所有启用的元素的状态样式
选择器：disabled  表示匹配所有禁用的元素的状态样式
```

##### 4、结构伪类选择器

```
选择器：after{}
选择器：before{}
选择器：empty{}
```

>说明
>
>1、  ":before" 伪元素可以在元素的内容前面插入新内容。
>
> 2、  ":after" 伪元素可以在元素的内容之后插入新内容。
>
>3、empty匹配所有的没有内容的元素

##### 5、归纳

| 属性                                       | 描述                    | CSS版本 |
| ---------------------------------------- | --------------------- | ----- |
| [:active](mk:@MSITStore:C:\Users\Administrator\Desktop\W3School离线手册(2017.03.11版).chm::/www.w3school.com.cn/cssref/pr_pseudo_active.asp.htm) | 向被激活的元素添加样式。          | 1     |
| [:focus](mk:@MSITStore:C:\Users\Administrator\Desktop\W3School离线手册(2017.03.11版).chm::/www.w3school.com.cn/cssref/pr_pseudo_focus.asp.htm) | 向拥有键盘输入焦点的元素添加样式。     | 2     |
| [:hover](mk:@MSITStore:C:\Users\Administrator\Desktop\W3School离线手册(2017.03.11版).chm::/www.w3school.com.cn/cssref/pr_pseudo_hover.asp.htm) | 当鼠标悬浮在元素上方时，向元素添加样式。  | 1     |
| [:link](mk:@MSITStore:C:\Users\Administrator\Desktop\W3School离线手册(2017.03.11版).chm::/www.w3school.com.cn/cssref/pr_pseudo_link.asp.htm) | 向未被访问的链接添加样式。         | 1     |
| [:visited](mk:@MSITStore:C:\Users\Administrator\Desktop\W3School离线手册(2017.03.11版).chm::/www.w3school.com.cn/cssref/pr_pseudo_visited.asp.htm) | 向已被访问的链接添加样式。         | 1     |
| [:first-child](mk:@MSITStore:C:\Users\Administrator\Desktop\W3School离线手册(2017.03.11版).chm::/www.w3school.com.cn/cssref/pr_pseudo_first-child.asp.htm) | 向元素的第一个子元素添加样式。       | 2     |
| :nth-child(n)                            | 向元素的第n个子元素添加样式        | 3     |
| :last-child                              | 向元素的最后一个元素添加样式        |       |
| [:lang](mk:@MSITStore:C:\Users\Administrator\Desktop\W3School离线手册(2017.03.11版).chm::/www.w3school.com.cn/cssref/pr_pseudo_lang.asp.htm) | 向带有指定 lang 属性的元素添加样式。 | 2     |

6、示例

- hover 伪列，鼠标移过该元素 触发选择器效果。

  - 示例：

    ```html
    <style type="text/css">>
      	#id_test:hover {
    		color: yellow;
    	}
    </style>
    ```

- active 伪列：鼠标按下后触发选择器效果

  - 示例：

    ```html
    <style type="text/css">>
      	#id_test:active {
    		color: yellow;
    	}
    </style>
    ```

> 伪列选择器有很多，我们不是专门写前端开发，只需要了解即可。

#### 5 属性伪类选择器

##### 1、"first-line" 伪元素

```
选择器：first-line{}
```

> 说明
>
> 1、 "first-line" 伪元素用于向文本的首行设置特殊样式。
>
> 2、 "first-line" 伪元素只能用于块级元素。
>
> 3、下面的属性可应用于 "first-line" 伪元素：
>
> - font
> - color
> - background
> - word-spacing
> - letter-spacing
> - text-decoration
> - vertical-align
> - text-transform
> - line-height
> - clear

##### 2、first-letter 伪元素

```
选择器：first-letter{}
```

> 说明
>
>  1、"first-letter" 伪元素用于向文本的首字母设置特殊样式
>
>  2、"first-letter" 伪元素只能用于块级元素。
>
> 3、下面的属性可应用于 "first-letter" 伪元素：
>
> - font
> - color
> - background
> - margin
> - padding
> - border
> - text-decoration
> - vertical-align (仅当 float 为 none 时)
> - text-transform
> - line-height
> - float
> - clear

##### 3、归纳

| 属性                                       | 描述               | CSS  |
| ---------------------------------------- | ---------------- | ---- |
| [:first-letter](mk:@MSITStore:C:\Users\Administrator\Desktop\W3School离线手册(2017.03.11版).chm::/www.w3school.com.cn/cssref/pr_pseudo_first-letter.asp.htm) | 向文本的第一个字母添加特殊样式。 | 1    |
| [:first-line](mk:@MSITStore:C:\Users\Administrator\Desktop\W3School离线手册(2017.03.11版).chm::/www.w3school.com.cn/cssref/pr_pseudo_first-line.asp.htm) | 向文本的首行添加特殊样式。    | 1    |
| [:before](mk:@MSITStore:C:\Users\Administrator\Desktop\W3School离线手册(2017.03.11版).chm::/www.w3school.com.cn/cssref/pr_pseudo_before.asp.htm) | 在元素之前添加内容。       | 2    |
| [:after](mk:@MSITStore:C:\Users\Administrator\Desktop\W3School离线手册(2017.03.11版).chm::/www.w3school.com.cn/cssref/pr_pseudo_after.asp.htm) | 在元素之后添加内容。       | 2    |

#### 6 群组选择器（分组选择器）

1、格式

```css
选择器，选择器，选择器...{}
```

2、说明

​	当多个选择器指定的元素有相同样式时可以使用分组选择器，同时能够实现多个元素所需的样式，这样能够使得我们样式的代码更为简洁。

#### 7 属性选择器

1、格式

```css
1、选择器[属性]{}/*只要选择器指定的元素中包含指定属性则匹配成功*/
2、选择器[属性1][属性2]{}/*只有选择器指定元素同时包含指定的多个属性时才匹配成功*/
3、选择器[属性="value"]{}/*除了选择拥有某些属性的元素，还可以进一步缩小选择范围，只选择有特定属性值的元素,属性与属性值必须完全匹配*/
4、选择器[属性~="value"]{}/*根据属性值中的词列表的某个词进行选择，则需要使用波浪号（~）*/
```

2、CSS 选择器参考手册

| 选择器                                                       | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [[*attribute*\]](mk:@MSITStore:C:\Users\Administrator\Desktop\W3School离线手册(2017.03.11版).chm::/www.w3school.com.cn/cssref/selector_attribute.asp.htm) | 用于选取带有指定属性的元素。                                 |
| [[*attribute*=*value*\]](mk:@MSITStore:C:\Users\Administrator\Desktop\W3School离线手册(2017.03.11版).chm::/www.w3school.com.cn/cssref/selector_attribute_value.asp.htm) | 用于选取带有指定属性和值的元素。                             |
| [[*attribute*~=*value*\]](mk:@MSITStore:C:\Users\Administrator\Desktop\W3School离线手册(2017.03.11版).chm::/www.w3school.com.cn/cssref/selector_attribute_value_contain.asp.htm) | 用于选取属性值中包含指定词汇的元素，该值必须是属性的某个完整的值。 |
| [[*attribute*\|=*value*\]](mk:@MSITStore:C:\Users\Administrator\Desktop\W3School离线手册(2017.03.11版).chm::/www.w3school.com.cn/cssref/selector_attribute_value_start.asp.htm) | 用于选取带有以指定值开头的属性值的元素，该值必须是整个单词。 |
| [[*attribute*^=*value*\]](mk:@MSITStore:C:\Users\Administrator\Desktop\W3School离线手册(2017.03.11版).chm::/www.w3school.com.cn/cssref/selector_attr_begin.asp.htm) | 匹配属性值以指定值开头的每个元素。                           |
| attribute$=value                                             | 匹配属性值以指定值结尾的每个元素。                           |
| attribute=value                                              | 匹配属性值中包含指定值的每个元素。                           |

#### 8 相邻兄弟选择器

1、**相邻兄弟选择器（Adjacent sibling selector）可选择紧接在另一元素后的元素，且二者有相同父元素**

2、格式

```
选择器 + 选择器 {}
```

3、说明：

​      请记住，用一个结合符只能选择两个相邻兄弟中的第二个元素



### 9 选择器例子

（1）标签选择器， id选择器，class选择器, 见 css选择器.html

```
<!DOCTYPE html>
<html>
   <head>
      <meta charset="UTF-8">
      <title></title>
      <style>
         
         /*css选择器*/
         /*标签选择器*/
         div {font-size: 30px;}
         
         /*id选择器*/
         #box {color: red; background: green;}
         
         /*class选择器*/
         .foo {background: orange;}
         
         /*通配符选择器*/
         /*样式重置*/
         * {font-family: "微软雅黑";}
         
         /*群组选择器*/
         #box,p {width: 100px;}
         
         
         /*层级选择器*/
         /*后代选择器： 使用空格*/
         /*#box1的所有标签名称为div的后代节点*/
         /*#box1 div {color: red;}*/
         /*#box1 #box3 {color: red;}*/
         /*#box1 #box2 #box3 {color: red;}*/
         
         /*子元素选择器: 使用>*/
         /*#box1 div {border: 1px solid green;}*/
         #box1 > div {border: 1px solid green;}
         
      </style>
   </head>
   <body>
      <div class="foo">div</div>
      <div id="box">div</div>
      <div class="foo">div</div>
      <p class="foo">段落</p>
      
      <ul>
         <li>1</li>
      </ul>
      
      <div id="box1">box1
         <div id="box2">box2
            <div id="box3">box3</div>
         </div>
         <p>段落</p>
      </div>
      
   </body>
</html>
```



(2) CSS选择器的优先级

```
<!DOCTYPE html>
<html>
   <head>
      <meta charset="UTF-8">
      <title></title>
      <style>

         #box {background: green;}
         
         .foo {background: orange;}
         
         div {background: red;}

         /*
           css选择器的优先级(权重)： 
            行间样式 > id选择器（1000） > class选择器（100） > 标签选择器（10）
          
          */
         
      </style>
   </head>
   <body>
      <div id="box" class="foo" style="background: pink;">div</div>
   </body>
</html>

```



