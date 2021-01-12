#  DOM属性操作

## 一、常见的属性操作

1. 属性列表

  | 属性            | 版本   | 说明                                       |
  | ------------- | ---- | ---------------------------------------- |
  | attr()        | 1.0  | 设置或返回文档节点的属性。                            |
  | removeAttr()  | 1.0  | 移除文档节点的属性。                               |
  | prop()        | 1.6  | 设置或返回DOM元素的属性。                           |
  | removeProp()  | 1.6  | 移除每个匹配元素的属性。                             |
  | addClass()    | 1.0  | 添加CSS类名。                                 |
  | removeClass() | 1.0  | 移除CSS类名。                                 |
  | toggleClass() | 1.2  | 切换CSS类名(存在就删除，不存在就添加)。                   |
  | html()        | 1.0  | 设置或返回元素的html内容(即innerHTML)。              |
  | text()        | 1.0  | 设置或返回元素的文本内容(已过滤掉HTML标签，即IE中的innerText )。 |
  | val()         | 1.0  | 设置或返回元素的值(主要是表单元素的value值)。               |

2. 语法格式

   ```
   1.获取第一个匹配元素class属性
   $("selector").attr("class"); 

   2. 设置所有匹配元素的class属性为"code"
   $("selector").attr("class", "code"); 

   3.移除所有匹配元素的class属性
   $("selector").removeAttr("class");

   4.获取第一个匹配元素的checked属性值
   $("selector").prop("checked"); 

   5.设置所有匹配元素的checked属性值为true(意即选中所有匹配的复选框或单选框)
   $("selector").prop("checked", true);

   6.移除所有匹配元素的className属性
   $("selector").removeProp("className");

   7.获取第一个匹配元素的value值(一般用于表单控件)
   $("selector").val(); 

   8.设置所有匹配元素的value值为"xiaoming"
   $("selector").val("xiaoming"); 

   9.获取第一个匹配元素的innerHTML值
   $("selector").html();

   10.设置所有匹配元素的innerHTML值为"呵呵"
   $("selector").html("呵呵"); 

   11.获取第一个匹配元素的innerText值(jQuery已进行兼容处理)
   $("selector").text();

   12.设置所有匹配元素的innerText值为"哈哈"
   $("selector").text("哈哈"); 
   ```


## 二、val()方法 

### 1、作用

> 设置或者返回JQuery对象所匹配的DOM对象value的值

### 2、语法格式:

>$("selector").val( [ values ] )

### 3、参数

| 参数     | 说明                                    |
| ------ | ------------------------------------- |
| values | 可选/String/Array/Function类型用于设置的value值 |

### 4、返回值

>val()函数的返回值是String/Array/jQuery类型，返回值的实际类型取决于val()函数所执行的操作。
>如果val()函数执行的是设置操作，将返回当前jQuery对象本身。如果执行的是获取操作，将返回第一个匹配元素的value属性值，该值一般为字符串类型；如果该元素是多选的\<select>元素，则返回包含所有选中值的数组。

### 5、示例代码

1. HTML代码

  ```
  <form id="form_id" name="answer_form" method="post">
      <label for="username_id">用户名</label><input id="username_id" class="normal" name="username" type="text"><br>
      <label for="password_id">密 码</label><input id="password_id" class="normal" name="password" type="password"
                                                 value="123456"><br>
      <input id="user_normal_id" class="normal" name="username_id" type="hidden" disabled="disabled" value="1"><br>

      <input id="men_id" name="gender" type="radio" checked="checked" value="men"><label for="men_id">男</label>
      <input id="women_id" name="gender" type="radio" value="women"><label for="women_id">女</label><br>

      <label for="text_id">自我介绍</label> <br>
      <textarea id="text_id" name="content" rows="3" cols="80">这个是文本区域的内容</textarea><br>
      <label for="answer_id">您喜欢的明星</label><br>
      <select id="answer_id" name="answer">
          <option value="A">上原亚衣</option>
          <option value="B">天海翼</option>
          <option value="C">美祢藤</option>
          <option value="D">长泽梓</option>
          <option value="E" selected="selected">呵呵</option>
      </select>
  </form>
  ```

2. JS代码

   ```
      $(function () {
               //获取元素值
               var $user_value = $("#username_id").val();
   //            alert($user_value);
               //设置元素值 返回对象
               var $user_input = $("#username_id").val("abcd");
   //            alert($user_value);
               var select_val = $("#answer_select_id:selected").val();
               $("#submit_id").click(function () {
                   var $checks = $("input:checkbox:checked");
                   $checks.each(function () {
                       var val = $(this).val();
                   })
               })
           });
   ```


## 三、html()

### 1、作用

> 函数用于设置或返回当前jQuery对象所匹配的DOM元素内的html内容。
>
> 该函数的用途相当于设置或获取DOM元素的innerHTML属性值。

### 2、语法格式

> $("selector").html( [ htmlString ] )

### 3、参数

| 参数         | 描述                                |
| :--------- | --------------------------------- |
| htmlString | 可选/String/Function类型用于设置的html字符串。 |

### 4、参数说明

>如果没有指定htmlString参数，则表示获取第一个匹配元素的html内容；如果指定了htmlString参数，则表示设置所有匹配元素的html内容。
>
>jQuery 1.4 新增支持：参数htmlString可以为函数。html()将根据匹配的所有元素遍历执行该函数，函数中的this将指向对应的DOM元素。
>
>html()还会为函数传入两个参数：第一个参数就是该元素在匹配元素中的索引，第二个参数就是该元素当前的html内容。函数的返回值就是需要为该元素设置的html内容。
>
>如果参数htmlString不是字符串或函数类型，则会被转换为字符串类型( toString() )。如果参数为null或undefined，则将其视作空字符串("")。

### 5、返回值

1. html()函数的返回值是String/jQuery类型，返回值的实际类型取决于html()函数所执行的操作。
2. 如果html()函数执行的是设置操作，将返回当前jQuery对象本身。如果执行的是获取操作，将返回第一个匹配元素的html内容，该值为字符串类型。

### 6、示例代码

1. HTML代码

   ```
   <div id="div1">
       <p id="p1">呵呵</p>
       <p id="p2">
           <span id="p3">为全栈工程狮而奋斗</span>
           <span id="p4"></span>
       </p>
   </div>
   ```

2. js代码

   ```
     $(function () {
               var $html = $("#p1").html();
               console.log($html);
               var $html2 = $("#p2").html();
               console.log($html2);
               //设置内容
               $("#p4").html("哈哈");
               $("p").html(function (index, currentHtml) {
                   // 函数内的this指向当前迭代的p元素
                   return "第" + (index + 1) + "个p元素，id为" + this.id;
               });
           });
   ```

   ​


## 四、text()

### 1、作用

1. 函数用于设置或返回当前jQuery对象所匹配的DOM元素内的text内容。所谓text内容，就是在该元素的html内容(即innerHTML属性值)的基础上过滤掉所有HTML标记后的文本内容(即IE浏览器的DOM元素特有的innerText属性值)。
2. 如果jQuery对象匹配的元素不止一个，则text()返回合并了每个匹配元素(包含其后代元素)中的文本内容后的字符串。该函数属于jQuery对象(实例)。

### 2、语法

> $("selector").text( [ textString ] )

### 3、参数

| 参数         | 描述                                |
| ---------- | --------------------------------- |
| textString | 可选/String/Function类型用于设置的text字符串。 |

### 4、参数说明

1. 如果没有指定textString参数，则表示获取合并了每一个匹配元素中的内容后的text内容；如果指定了textString参数，则表示设置所有匹配元素的text内容。

2. jQuery 1.4 新增支持：参数textString可以为函数。text()将根据匹配的所有元素遍历执行该函数，函数中的this将指向对应的DOM元素。

3. 如果参数textString不是字符串或函数类型，则会被转换为字符串类型( toString() )。如果参数为null或undefined，则将其视作空字符串("")。

### 5、返回值

1.    text()函数的返回值是String/jQuery类型，返回值的实际类型取决于text()函数所执行的操作。
2.    如果text()函数执行的是设置操作，将返回当前jQuery对象本身。如果执行的是获取操作，将返回合并了每一个匹配元素中的内容后的text内容，该值为字符串类型。

### 6、示例代码

1. HTML代码

   ```
   <div id="d1">
       <p id="p2">
           <span id="p2">青春就像一张破裂的网,遗落了我太多年轻的时候梦想,大哥能不能给我QQ冲个会员</span>
           <span id="p3"></span>
       </p>
       <ul>
           <li>JAVA</li>
           <li>H5</li>
           <li>Android</li>
       </ul>
   </div>
   ```

2. js代码

  ```
     $(function () {
              /* 实例化p标签 */
              var $p1 = $("#p1");
              /*  设置文本内容*/
              $p1.text("跟哥玩感情我会让你哭的很有节奏!!!");
              var text = $("p").text();
              console.log(text);
              var $p2 = $("#p2");
              /*返回的是过滤掉HTML标记的文本内容*/
              console.log($p2.text());

              var $s2 = $("#s2");
              $s2.text('<h1>Hello World</h1>');
              console.log($s2.text());
              //清空所有匹配的元素的文本内容
              $("span").text("");

              /*
               * index 将所有li元素的text内容修改成索引
               * text 每个li的文本内容
               */
              $("li").text(function (index, text) {
                  console.log(text);
                  return index;
              });
          });
  ```

## 五、attr()

### 1、作用

>函数用于设置或返回当前jQuery对象所匹配的元素节点的属性值。该函数属于jQuery对象(实例)。如果需要删除DOM元素节点的属性，请使用[removeAttr()]函数

### 2、语法

> $(selector).attr(attribute)

### 3、参数

| 参数            | 描述                                    |
| ------------- | ------------------------------------- |
| attributeName | String类型指定的属性名称。                      |
| value         | 可选/String/Function类型指定的属性值，或返回属性值的函数。 |
| object        | Object类型指定的对象，用于封装多个键值对，同时设置多项属性      |

### 4、参数说明

1. 为被选元素设置一个以上的属性和值

   ```
   $(selector).attr({attribute:value, attribute:value ...})
   以对象形式同时设置任意多个属性的值。对象object的每个属性对应attributeName，属性的值对应value。
   注意：attr()函数的所有"设置属性"操作针对的是当前jQuery对象所匹配的每一个元素；所有"读取属性"的操作只针对第一个匹配的元素。
   ```

2. 设置被选元素的属性和值。

   ```
   $(selector).attr(attribute,function(index,oldvalue))
   注:如果参数value既不是函数类型，也不是字符串类型，则会调用toString()方法，将其转为字符串
   ```


>| 参数                         | 描述                                      |
>| -------------------------- | --------------------------------------- |
>| *attribute*                | 规定属性的名称。                                |
>| *function(index,oldvalue)* | 规定返回属性值的函数。该函数可接收并使用选择器的 index 值和当前属性值。 |

### 5、返回值

1. attr()函数的返回值是任意类型，返回值的类型取决于当前attr()函数执行的是"设置属性"操作还是"读取属性"操作。
2. 如果attr()函数执行的是"设置属性"操作，则返回当前jQuery对象本身；如果是"读取属性"操作，则返回读取到的属性值。
3. 如果当前jQuery对象匹配多个元素，返回属性值时，attr()函数只以其中第一个匹配的元素为准。如果该元素没有指定的属性，则返回undefined。


### 6、示例代码

1. HTML代码

   ```
   <div id="d1">
       <p id="p_id" >这个是网站内容</p>
       <input id="name_id" name="name" type="text" label="姓名" >
       <img id="img_id" alt="提示" src="/image/blank.gif" >
       <img id="login_id" alt="logo" title="测试" src="/img/logo" >
       <ul id="ul_id">
           <li id="l1_id" uid="1">1</li>
           <li id="l2_id" uid="2">2</li>
           <li id="l3_id" uid="3">3</li>
       </ul>
   </div>
   ```

2. jq代码

   ```
   $(function () {
                       //改变img的src属性
                       $("#logo").attr("src", "img/22.jpg");
                       //获取src属性的值  注意只会获取第一个的值,
                       var $attr = $("#logo").attr("src");
                       /**
                        * 如果要获取多个值 可以直接添加函数
                        * 函数的参数1  属性的索引
                        * 函数的参数2  属性的值
                        * @type {string|any|JQuery<TElement>|jQuery|HTMLElement|*}
                        */
                       var $attr = $("#logo").attr("src", function (index, value) {
                           if (value !== undefined) {
                               // 获取value的值操作
                           }
                       });
                       //遍历title属性 如果有属性这个属性改变值 没有就设置值
                       $("img").attr('alt', function (index, attrValue) {
                           return attrValue === undefined ? this.alt = "呵呵" : "还是呵呵";
                       });
                       //如果使用attr获取返回boolean类型的属性时返回undefined
                       var $disabled_attr = $("#i1").attr("disabled");
                       var $checked_attr = $("#div").find(":checkbox").attr("checked");
                   });
   ```

   ​


## 六、prop()

### 1、作用

>函数用于**设置或返回当前jQuery对象所匹配的元素的属性值**。该函数属于`jQuery`对象(实例)。如果需要删除DOM元素的属性，请使用[removeProp()]函数。

### 2、语法格式

1. 返回属性的值：

   ```
   $(selector).prop(property)
   ```

2. 设置属性和值：

   ```
   $(selector).prop(property,value)
   ```

3. 使用函数设置属性和值：

     ```
     $(selector).prop(property,function(index,currentvalue))
     ```

4. 设置多个属性和值：

     ```
     $(selector).prop({property:value, property:value,...})
     ```

### 3、参数

| 参数                             | 描述                                       |
| ------------------------------ | ---------------------------------------- |
| *property*                     | 属性的名称。                                   |
| *value*                        | 属性的值。                                    |
| function(*index,currentvalue*) | 返回要设置的属性值的函数。*index* - 检索集合中元素的 index 位置。*currentvalue* - 检索被选元素的当前属性值。 |

### 4、示例代码

 1.  HTML代码

     ```
     <div>
         <span id="s1">prop操作针对的是元素(Element对象)的属性，而不是元素节点(HTML文档)的属性</span>
         <form>
             <label for="boy">男</label><input id="boy" disabled="disabled" name="sex" type="checkbox" checked value="1">
             <label for="girl">女</label><input id="girl"  name="sex" type="checkbox" value="2">
         </form>
     </div>
     ```

 2. jq代码

     ```
     $(function () {
                 var $sp = $("#s1");
                 //prop操作针对的是元素(Element对象)的属性，而不是元素节点(HTML文档)的属性
                 $sp.prop("prop1", "test1");
                 $sp.attr("attr1", "test2");

                 var $girl = $("#girl");

                 $girl.change(function () {
                     var attr1 = $girl.attr("checked");
                     console.log(attr1);
                     var attr2 = $girl.prop("checked");
                     console.log(attr2);
                     console.log($("#boy").prop("disabled"))
                     console.log($("#boy").attr("disabled"))

                 });
             });
     ```


### 5、与attr主要区别

1. prop()函数针对的是DOM元素(JS Element对象)的属性
2. attr()函数针对的是DOM元素所对应的文档节点的属性
3. 官方建议:**具有 true 和 false 两个属性的属性，如 checked, selected 或者 disabled 使用prop()，其他的使用 attr()**

## 七、常见的取值和赋值函数

1. html() 返回或设置被选元素的内容 (inner HTML)    
2. text() 取出或设置text内容      
3. attr() 取出或设置某个属性的值    
4. width() 取出或设置某个元素的宽度    
5. height() 取出或设置某个元素的高度  
6. val() 取出或设置html内容 取出某个表单元素的值 


