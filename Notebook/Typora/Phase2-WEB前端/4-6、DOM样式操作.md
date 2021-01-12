# 样式操作

## 一、 概要

>  通过JavaScript获取dom元素上的style属性，我们可以动态的给元素赋予样式属性。在jQuery中我们要动态的修改style属性我们只要使用css()方法就可以实现了

## 二、CSS()

### 1、作用

>  css()函数用于**设置或返回当前jQuery对象所匹配的元素的css样式属性值**
>
>  如果需要删除指定的css属性，使用函数将其值设为空字符串("")

### 2、语法格式

1. 格式一

   ```
   $("selector").css(property [, value ])

   1>如果指定了value参数，则表示设置css属性的值为value；
   2> 如果没有指定value参数，则表示返回css属性的值
   ```

2. 格式二

   ```
   $("selector").css( object )
   1、以对象形式同时设置任意多个属性的值。对象object的每个属性对应property，属性的值对应value
   2、如果省略了value参数，则表示获取属性值；如果指定了该参数，则表示设置属性值。
   3、css()函数的所有"设置"操作针对的是当前jQuery对象所匹配的每一个元素；所有"读取"操作只针对第一个匹配的元素。
   ```

### 3、参数

| 参数           | 描述                                       |
| ------------ | ---------------------------------------- |
| propertyName | String/Array类型指定的css属性名称(用于设置或返回)，或者css属性名称数组(仅用于返回)。 |
| value        | 可选/String/Number/Function类型指定的属性值，或返回属性值的函数。 |
| object       | Object类型指定的对象，用于封装多个键值对，同时设置多项属性。        |

### 4、参数说明

1. jQuery 1.4 ：参数value可以是函数，css()将根据匹配的所有元素遍历执行该函数，函数中的this指针将指向对应的DOM元素。css()还会为函数传入两个参数：第一个参数就是该元素在匹配元素中的索引，第二个参数就是该元素css属性propertyName当前的值。函数的返回值就是为该元素的css属性propertyName设置的值。
2. jQuery 1.9 ：如果是"获取"操作(仅限"获取"操作)，参数propertyName还可以是多个css属性名称组成的数组，css()将以对象形式返回多个css属性(对象的属性名称对应css属性名称，属性值对应css属性值)

### 5、返回值

1. css()函数的返回值是任意类型，返回值的类型取决于当前css()函数执行的是"设置"操作还是"读取"操作。
2. 如果css()函数执行的是"设置"操作，则返回当前jQuery对象本身；如果是"读取"操作，则返回读取到的属性值。
3. 如果当前jQuery对象匹配多个元素，返回属性值时，css()函数只以其中第一个匹配的元素为准。如果该元素没有指定的属性，则返回undefined。

### 6、示例

1. HTML代码

   ```
   <h3>设置css属性</h3>
   <p id="p1">设置单个属性属性</p>
   <p id="p2">设置多个属性</p>
   <h3>获取css属性</h3>
   <p style="color: red ;margin: 30px ;background-color: aqua" id="p3">获取css属性</p>
   <h3>清除css属性</h3>
   <p id="p4" style="font-size: 16px" >清除属性</p>
   ```


2. JQ代码

   ```
     $(function () {

               var $p1 = $("#p1");
               var $p2 = $("#p2");
               var $p3 = $("#p3");
               $p1.css("color", "red")
                   .text("设置单个属性");

               $p2.css({
                   "font-size": "20px",
                   "color": "red",
                   "margin": "10px",
                   "padding": "10px",
                   "background": "greenyellow"
               })
                   .text("设置多个属性");
               /**
                * 获取属性
                * @type {*|jQuery}
                */
               $p1.css("color");//rgb(255, 0, 0)
               $p2.css("background");//rgb(173, 255, 47)
               $p3.css("margin");//30px

               /**
                * 清除样式
                */
               $("p4").css("font-size", "");

           });
   ```


### 7、注意事项

1、如果参数value为空字符串("")，则表示删除该css属性。

2、对于多个单词构成的css属性，你可以使用其css格式("-")或者DOM格式(驼峰式)，jQuery都能理解。例如background-color，你可以将propertyName设为background-color或backgroundColor。建议优先以驼峰式来获取(jQuery底层也是通过DOM来获取的，DOM元素的属性均以驼峰式命名)。

3、有些时候获取到的css属性值与你在样式表中设置的值并不完全相同。例如：某些表示尺寸的属性值，你可能在样式表中设置的单位是em、px、ex或者%，但jQuery获取的是经过浏览器计算后css属性值，其单位多数情况下为像素。此外，不同浏览器对于颜色(color)属性值的文本表示也不一致，以white为例，浏览器可能返回white、#FFF、#ffffff、rgb(255,255,255)等，当然它们在逻辑上都表示白色。

4、对于一些速写的css属性，例如margin、padding、background、border。尽管某些浏览器提供了此功能，但它的结果是无法保证的，有些浏览器也并不支持。以margin为例，你可能需要通过css("marginTop")、css("marginRight")等方式来分别获取。

## 三、height()

### 1、作用

> 用于设置或返回当前匹配元素的高度

### 2、语法格式

1. 格式

   ```
   $("selector").height( [ value ] )
   1、如果省略了value参数，则表示获取高度；如果指定了该参数，则表示设置高度。
   2、height()函数的"设置"操作针对的是当前jQuery对象所匹配的每一个元素；"读取"操作只针对第一个匹配的元素。
   ```


### 3、参数

| 参数    | 描述                   |
| ----- | -------------------- |
| value | 可选/Number类型用于设置的高度值。 |

### 4、参数说明

1. 参数value可以为函数，则height()将根据匹配的所有元素遍历执行该函数，函数中的this将指向对应的DOM元素。
2. 函数可以两个参数：第一个参数就是当前元素在匹配元素中的索引，第二个参数就是该元素当前的高度值。函数的返回值就是需要设置的高度值。

### 5、返回值

1. height()函数的返回值为jQuery/Number类型，返回值的类型取决于height()函数当前执行的是"设置"操作还是"读取"操作
2. 如果height()函数执行的是"设置"操作，则返回当前jQuery对象本身；如果是"读取"操作，则返回第一个匹配元素的高度值

### 6、示例

1. HTML代码

   ```
   <div id="div1"></div>
   <div id="div2"></div>
   <a href="#">aaaa</a>
   ```

2. jq代码

   ```
   var $d1 = $("#div1");
   var $d2 = $("#div2");

   $d1.height(); // 0
   $d1.height(); // 100

   var $divs = $("div");
   // 如果匹配多个元素，只返回第一个元素的height
   $divs.height(); // 0
   $d1.height(100);
   // 设置所有div元素的height不能小于100px(小于100的设为500，其它不变)
   $divs.height( function(index, height){
       return Math.max(height, 500);        
   } );
   ```


## 四、width()

### 1、作用

> 用于设置或返回当前匹配元素的宽度

### 2、语法格式

1. 格式一

   ```
   $("selector").width( [ value ] )
   ```

### 3、参数

| 参数    | 描述                   |
| ----- | -------------------- |
| value | 可选/Number类型用于设置的宽度值。 |

### 4、参数说明

1. 参数value可以为函数，则width()将根据匹配的所有元素遍历执行该函数，函数中的this将指向对应的DOM元素。
2. 如果参数是函数可以传入两个参数:第一个参数就是当前元素在匹配元素中的索引，第二个参数就是该元素当前的宽度值。函数的返回值就是需要设置的宽度值。

### 5、返回值

1. width()函数的返回值为jQuery/Number类型，返回值的类型取决于width()函数当前执行的是"设置"操作还是"读取"操作。
2. 如果width()函数执行的是"设置"操作，则返回当前jQuery对象本身；如果是"读取"操作，则返回第一个匹配元素的宽度值。

### 6、示例

1. HTML代码

   ```
   <div id="d1" style="padding: 10px; width: 150px; height:150px;"></div>
   <div id="d2" style="width: 200px; height:100px;"></div>
   ```

2. jq代码

   ```
   var $d1 = $("#d1");
   var $d2 = $("#d2");

   $d1.width(); // 100
   $d2.width(); // 200

   var $divs = $("div");
   // 如果匹配多个元素，只返回第一个元素的width
   $divs.width(); // 100

   // 设置所有div元素的width不能小于300px(小于300的设为300，其它保持不变)
   $divs.width( function(index, width){
       return Math.max(width, 300);
   } );

   // 设置n1的width为20px
   $d1.width( 20 );
   ```

## 五、innerHeight(),innerWidth()

### 1、作用

> 置或返回当前匹配元素的内宽度或者高度

### 2、语法格式

1. 格式一

   ```
   $("selector").innerHeight( [ value ] )
   $("selector").innerWidth( [ value ] )
   ```

### 3、参数

| 参数    | 描述                        |
| ----- | ------------------------- |
| value | 可选/Number类型用于设置的内高度值(宽度)。 |

### 4、参数说明

1. 参数value可以为函数，则width()将根据匹配的所有元素遍历执行该函数，函数中的this将指向对应的DOM元素。
2. 如果参数是函数可以传入两个参数:第一个参数就是当前元素在匹配元素中的索引，第二个参数就是该元素当前的宽度值。函数的返回值就是需要设置的宽度值。

### 5、返回值

1. width()函数的返回值为jQuery/Number类型，返回值的类型取决于width()函数当前执行的是"设置"操作还是"读取"操作。
2. 如果width()函数执行的是"设置"操作，则返回当前jQuery对象本身；如果是"读取"操作，则返回第一个匹配元素的宽度值。

### 6、示例

1. HTML代码

   ```
   <div id="d1" style="padding: 10px; height: 100px; border: 1px solid #000;"></div>
   <div id="d2" style="height: 150px; background: #999;"></div>
   ```

2. jq代码

   ```
   var $d1 = $("#d1");
   var $d2 = $("#d2");
   $d1.innerHeight(); // 120
   $d2.innerHeight(); // 150
   var $divs = $("div");
   // 如果匹配多个元素，只返回第一个元素的innerHeight
   $divs.innerHeight(); // 120

    <h1>1.8.0及之后版本</h1>

   // 设置所有div元素的innerHeight不能小于200px(小于200的设为200，其它保持不变)
   $divs.innerHeight( function(index, innerHeight){
       return Math.max(innerHeight, 200);      
   } );
   // 设置n1的innerHeight为20px
   $n1.innerHeight( 20 );
   ```



## 六、outerHeight(),outerWidht()

### 1、作用

> 获取当前匹配元素的外高度(外宽度)

### 2、语法格式

1. 格式一

   ```
   $("selector").outerHeight( [ includeMargin ] )
   $("selector").outerWidth( [ includeMargin ] )
   ```

### 3、参数

| 参数            | 描述                                       |
| ------------- | ---------------------------------------- |
| includeMargin | 可选/Boolean类型指示是否包含外边距部分的高度(宽度)，默认为`false` |

### 4、返回值

1. outerHeight()函数的返回值为Number类型，返回第一个匹配元素的外高度。
2. 如果当前jQuery对象匹配多个元素，返回外高度时，outerHeight()函数只以其中第一个匹配的元素为准。如果没有匹配的元素，则返回null

### 6、示例

1. HTML代码

   ```
   <div id="d1" style="margin:5px; padding: 10px; height: 100px; border: 1px solid #000;"></div>
   <div id="d2" style="height: 150px; background: #999;"></div>
   ```

2. jq代码

   ```
   var $d1 = $("#d1");
   var $d2 = $("#d2");

   // outerHeight() = height(100) + padding(10*2) + border(1*2) = 122 
   $d1.outerHeight(); // 122
   $d2.outerHeight() ); // 150

   var $divs = $("div");
   // 如果匹配多个元素，只返回第一个元素的outerHeight
   document.writeln( $divs.outerHeight() ); // 122
   //outerHeight(true) = height(100) + padding(10*2) + border(1*2) + margin(5*2) = 132 
   $n1.outerHeight(true); // 132
   $n2.outerHeight(true); // 150
   ```

