# jQuery入门

## 一、什么是jQuery

> jQuery是一个非常流行的快速、小巧、功能强大的开源JavaScript库。就像官方所宣称的那样——"Write less，do more"，它使得我们常用的HTML文档遍历、DOM操作、事件处理、动画效果、Ajax、工具方法等功能代码的实现变得非常简单。更重要的是，它还为我们做了跨浏览器的兼容。绝大多数时候，妈妈再也不用担心我的JS兼容问题了(由于浏览器bug等因素，jQuery也无法100%地实现跨浏览器兼容，官方对这些少数API一般也作了特殊说明，而且这种情况极少遇到，因此可以忽略不计)。
>
> 一般而言，需要编写几十行甚至更多的原生JS代码才能实现的功能；使用jQuery，只需要简单的几行甚至一行代码就可以搞定。此外，jQuery还具有灵活的插件扩展机制，这允许第三方人员开发基于jQuery的插件，甚至你也可以快速地编写一个自己的插件。这极大地提高了前端开发人员的开发效率。因此，谷歌、微软、IBM、Facebook等全世界前10000名的网站中有65%以上都使用了jQuery，其它数以百万计的网站也都在使用jQuery
>
> 

​    js是语言,JQuery是建立在这个语言上的一个基本库(框架),利用JQuery可以更简单的使用js。
   举例子:

​    就像是木头和做好的木板,木头是基本的原材料,利用木头你可以做各种家具。但是利用做好的木板你
可以更简单的做各种家具

## 二、jQuery的优势

1. 轻量级、体积小，使用灵巧(只需引入一个js文件)
2. 强大的选择器
3. 出色的DOM操作的封装
4. 出色的浏览器兼容性
5. 可靠的事件处理机制
6. 完善的Ajax
7. 链式操作、隐式迭代方便的选择页面元素(模仿CSS选择器更精确、灵活)
8. 动态更改页面样式/页面内容(操作DOM，动态添加、移除样式)
9. 控制响应事件(动态添加响应事件)
10. 提供基本网页特效(提供已封装的网页特效方法)
11. 快速实现通信(ajax)
12. 易扩展、插件丰富

## 三、如何使用

### 1、下载

1. [官方下载地址](http://jquery.com/download/)

   production jQuery x.x.x 上线版,压缩过 development jQuery x.x.x 开发版,能看源码

### 2、其他库替代

1. Google 和 Microsoft 对 jQuery 的支持都很好。如果您不愿意在自己的计算机上存放 jQuery 库，那么可以从 Google 或 Microsoft 加载 CDN jQuery 核心文件。使用 Google 的 CDN

2. [使用 Microsoft 的 CDN](https://docs.microsoft.com/en-us/aspnet/ajax/cdn/overview#jQuery_Releases_on_the_CDN_0)

   ```
   <script src="http://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.2.1.min.js"></script>
   <head>
   <script type="text/javascript" src="http://ajax.microsoft.com/ajax/jquery
   /jquery-1.4.min.js"></script>
   </head>

   ```

3. 国内的

   ```
    [百度](http://cdn.code.baidu.com)
    [新浪](http://lib.sinaapp.com/?path=/jquery)

   ```

4. 示例代码

   ```
      <!-- 引入jQuery库的js文件 -->
      <script src="//code.jquery.com/jquery-x.x.x.js" type="text/javascript"></script>
      <!-- 编写JS代码并使用jQuery -->
      <script type="text/javascript">
      // 以下代码将把id为username的元素的value值改为"Hello CodePlayer!"。
      jQuery("#username").val("Hello CodePlayer!");
      </script>

   ```

## 四、如何选择jQuery版本

1. 1.x

   > 自jQuery 1.0 发布以来，已经过多次更新，其中增加了许多新的属性和方法，同时也移除了少数过时的属性和方法。目前最新的 1.x 版本为 1.12.4。

2. 2.x (支持IE9以及IE9+)

   > jQuery还有 2.x 版本(当前最新版本为 2.2.4)，它的API与 1.x 相同，但jQuery 2.x 不再支持IE 6 ~ IE 8。如果你希望兼容IE 6 ~ IE 8，推荐使用 1.x。

3. 3.x版本 (不在支持 ie9)

   > 3.1 桌面浏览器
   >
   > Chrome: (Current - 1) and Current Edge: (Current - 1) and Current Firefox: (Current - 1) and Current Internet Explorer: 9+ Safari: (Current - 1) and Current Opera: Current
   >
   > 3.2 移动端
   >
   > Stock browser on Android 4.0+ Safari on iOS 7+

4. 一般建议

   > 使用最新版本的jQuery。如果你需要使用某个已经被移除的属性或方法，你可以使用包含该属性或方法的jQuery版本

## 五、ready() 函数(准备就绪时执行代码)

1. 如果我们在`<head>`中引入jQuery库文件，并编写相应的jQuery代码来操作DOM元素。这很可能导致操作无法成功，因为此时`<body>`内的元素可能还没有加载出来，也就获取不到对应的元素。因此，我们一般会将自己的jQuery代码写在ready()事件函数中。ready()函数的作用相当于window.onload，它用于在当前文档加载准备就绪后执行对应的函数

   ```
   $(document).ready(function(){
       // DOM准备就绪后执行的代码
   });
   简写
   $(function(){
       //在DOM准备就绪后执行的代码
   } );

   ```

2. jQuery的`ready()`函数可以重复调用，绑定的回调函数将在DOM准备就绪后按照绑定顺序依次执行。此外，`ready()`和*window.onload*并不兼容，因此不要混合使用

   ```
   $(function () {
       console.log("第一次ready()");
     });

   $(function () {
       console.log("第二次ready()");
   })

   ```

3. onload和JQuery中ready方法的区别

   > - 执行时机：onload事件必须等页面完全加载完毕后才能执行；ready当页面节点加载完毕后就可以执行。比onload要早一点
   > - 添加个数：onload事件只能添加一个，如果添加了多个，则最后执行的onload事件会覆盖前边的事件;ready事件可以添加多个，且互相之间不会覆盖。（onload事件和ready时间之间也不会互相覆盖）
   > - 简化写法：onload没有简化写法；ready事件可以简化为:$(function(){});

4. 建议

   > js文件和内嵌的js代码一般不建议放在`<head>`标签中，而应该放在内容主体的结束标签`</body>`之前。从而让浏览器先加载页面内容，然后再加载并解析执行js代码。这样可以让网速较慢的用户能够更快地看到页面的展示内容，提高用户体验

5. 命名冲突解决

   ```
   1. jQuery 使用 $ 符号作为 jQuery 的简介方式；
   2. 某些其他 JavaScript 库中的函数（比如 Prototype）同样使用 $ 符号；  
   3. jQuery 使用名为 noConflict() 的方法来解决该问题； 
   4. var jq=jQuery.noConflict() ，帮助您使用自己的名称（比如 jq）来代替 $ 符号
   ```

   ​



## 六、jQuery框架核心功能

1. 操作DOM对象
2. 动态操作样式css
3. 数据访问
4. 控制响应事件等

## 七、初学JQuery最容易混淆的几个概念

1. jQuery对象不等于dom对象
2. jQuery对象与dom对象之间的转换
3. jQuery的ready 不等于JavaScript的 load