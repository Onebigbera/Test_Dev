## DOM操作的原则

### 一、 Get and Set in One(读写一体) 原则

1. 为了更加易于使用，jQuery提供了简洁的DOM操作API，其方法往往是**读写一体**的。也就是说，某个方法既可用于读取操作，也可用于设置操作。如果没有为其传入表示值的参数，则表示获取操作，将返回获取到的数据；如果为其传入了表示值的参数，则表示设置操作，它将设置DOM元素指定属性的值。

2. 示例代码

   ```
   // 没有传入value参数，返回第一个匹配元素的value元素
   var $a = $("a");
   //只会取第一个匹配的
   var $color = a.css("color");
   //// 传入了value参数，设置所有匹配元素的color样式为"red"
   $a.css("color", "red");

   ```

### 二、 Get first Set all(读取第一个,写操作所有) 原则

1. jQuery对象几乎所有的DOM操作方法都遵守"Get first Set all"原则。简而言之，假设当前jQuery对象匹配多个元素，如果使用jQuery对象的方法来获取数据("读"数据)，则只会获取**第一个匹配元素**的数据；如果使用jQuery对象的方法来设置元素数据("写"数据)，则会对**所有匹配元素**都进行设置操作

2. 示例代码

   ```
   var $lis = $("ul li"); // 匹配ul元素的所有后代li元素
   var $className = $lis.attr("class"); // 只获取第一个匹配的li元素的class属性
   $lis.attr("class", "left"); // 将所有匹配的li元素的class属性设为"left"
   ```

### 三、链式编程风格

1. **jQuery对象的所有实例方法，在没有特殊的返回需求的情况下，一般都会返回该jQuery对象本身(或者其它jQuery对象)**，因此我们可以继续调用返回的jQuery对象上的方法

2. 示例代码

   ```
   $("div") // 返回一个匹配所有div元素的jQuery对象
   .find("ul") // 返回匹配这些div元素中的所有后代ul元素的jQuery对象
   .children() // 返回匹配这些ul元素中的所有子代元素的jQuery对象
   .css("color", "red") // 为这些子代元素设置css样式"color: red，并返回当前对象本身
   .hide(); // 隐藏这些子代元素，并返回当前对象本身

   ```

### 四、智能DOM操作，静默容错

> 在JS原生DOM操作中，如果通过getElementById()、getElementsByName()等方式获取不到对应的元素，那么将返回*null*，在*null*上访问属性或方法，将会抛出异常。
>
> 与此不同的是，jQuery在匹配不到对应元素时将返回一个空的jQuery对象，我们仍然可以调用jQuery对象的方法，而且并不会报错。因为jQuery会智能地处理这种情况。如果该方法用于获取数据，则返回*null*或*undefined*；如果该方法用于设置数据，则忽略设置操作，并返回该空对象本身；如果该方法用于筛选元素，则同样返回一个新的jQuery空对象

