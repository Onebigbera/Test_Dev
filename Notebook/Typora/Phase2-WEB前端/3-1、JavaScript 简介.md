# JavaScript 简介

## 一、 简介

 JavaScript一种直译式脚本语言，是一种动态类型、弱类型、基于原型的语言，内置各种数据类型。它的解释器被称为JavaScript引擎，为浏览器的一部分，广泛用于客户端的脚本语言，最早是在HTML（标准通用标记语言下的一个应用）网页上,在1995年时，由Netscape公司的Brendan Eich，在网景导航者浏览器上首次设计实现而成。因为Netscape与Sun合作，Netscape管理层希望它外观看起来像Java，因此取名为JavaScript。但实际上它的语法风格与Self及Scheme较为接近。 用来给HTML网页增加动态功能。为了取得技术优势，微软推出了JScript，CEnvi推出ScriptEase，与JavaScript同样可在浏览器上运行。为了统一规格，因为JavaScript兼容于ECMA标准，因此也称为ECMAScript（简称ES）。

## 二、优点

### 1、易学性

1. 学习环境无处不在

   ```
   只要有浏览器，就能运行JavaScript程序；只要有文本编辑器，就能编写JavaScript程序。
   这意味着，几乎所有电脑都原生提供JavaScript学习环境，不用另行安装复杂的IDE（集成开发环境）和编译器。
   ```

2. 语法简单

   ```
   JavaScript的语法相对于其它强类型语言简单一些，本身的语法特性并不是特别多。
   而且，那些语法中的复杂部分，也不是必需要学会。你完全可以只用简单命令，完成大部分的操作
   ```

3. 与主流语言的相似性

   ```
   JavaScript的语法很类似C/C++和Java，如果学过这些语言，JavaScript的入门会非常容易。
   ```

### 2、强大的性能

1. 灵活的语法，表达力强

   ```
   JavaScript既支持类似C语言清晰的过程式编程，也支持灵活的函数式编程
   ```

2. 支持编译运行

   ```
   JavaScript语言本身，虽然是一种解释型语言，但是在现代浏览器中，JavaScript都是编译后运行。
   程序会被高度优化，运行效率接近二进制程序。而且，JavaScript引擎正在快速发展，性能将越来越好。
   ```

3. 事件驱动和非阻塞式设计

   ```
   JavaScript程序可以采用事件驱动（event-driven）和非阻塞式（non-blocking）设计，
   在服务器端适合高并发环境，普通的硬件就可以承受很大的访问量。
   js是采用事件驱动(event-driven)响应用户操作的。
   比如通过鼠标或者按键在浏览器窗口或者网页元素(按钮，文本框...)上执行的操作，我们称之为事件(Event)。
   由鼠标或热键引发的一连串程序的动作，称之为事件驱动(Event-Driver)。对事件进行处理程序或函数，
   我们称之为事件处理程序(Event Handler)
   ```

### 3、开放性

1. JavaScript是一种开放的语言。它的标准ECMA-262是ISO国际标准，写得非常详尽明确；该标准的主要实现（比如V8和SpiderMonkey引擎）都是开放的，而且质量很高。这保证了这门语言不属于任何公司或个人，不存在版权和专利的问题。
2. 语言标准由TC39委员会负责制定，该委员会的运作是透明的，所有讨论都是开放的，会议记录都会对外公布。
3. 不同公司的JavaScript运行环境，兼容性很好，程序不做调整或只做很小的调整，就能在所有浏览器上运行 

## 三、应用场景

1. 浏览器的平台化

   随着HTML 5的出现，浏览器本身的功能越来越强，不再仅仅能浏览网页，而是越来越像一个平台，JavaScript因此得以调用许多系统功能，比如操作本地文件、操作图片、调用摄像头和麦克风等等。这使得JavaScript可以完成许多以前无法想象的事情

2. Node

   Node项目使得JavaScript可以用于开发服务器端的大型项目，网站的前后端都用JavaScript开发已经成为了现实。有些嵌入式平台（Raspberry Pi）能够安装Node.js，于是JavaScript就能为这些平台开发应用程序

3. 数据库操作

   ```
   JavaScript甚至也可以用来操作数据库。NoSQL数据库这个概念，
   本身就是在JSON（JavaScript Object Notation，JavaScript对象表示法）格式的基础上诞生的，
   大部分NoSQL数据库允许JavaScript直接操作。基于SQL语言的开源数据库PostgreSQL支持JavaScript作为操作语言，
   可以部分取代SQL查询语言
   ```

4. 跨移动平台

   ```
   PhoneGap项目就是将JavaScript和HTML5打包在一个容器之中，使得它能同时在iOS和安卓上运行。
   Facebook的React Native项目则是将JavaScript写的组件，编译成原生组件，从而使它们具备优秀的性能。
   Mozilla基金会的手机操作系统Firefox OS，更是直接将JavaScript作为操作系统的平台语言。
   ```

5. 内嵌脚本语言

   ```
   越来越多的应用程序，将JavaScript作为内嵌的脚本语言，比如Adobe公司的著名PDF阅读器Acrobat、Linux桌面环境GNOME 3

   ```

6. 跨平台的桌面应用程序

   ```
   Chromium OS、Windows 8等操作系统直接支持JavaScript编写应用程序。
   Mozilla的Open Web Apps项目、Google的Chrome App项目、Github的Electron项目、以及TideSDK项目，
   都可以用来编写运行于Windows、Mac OS和Android等多个桌面平台的程序，不依赖浏览器
   ```

## 四、JavaScript与ES的关系

1. 1996年8月，微软模仿JavaScript开发了一种相近的语言，取名为JScript（JavaScript是Netscape的注册商标，微软不能用），首先内置于IE 3.0。Netscape公司面临丧失浏览器脚本语言的主导权的局面
2. 1996年11月，Netscape公司决定将JavaScript提交给国际标准化组织ECMA（European Computer Manufacturers Association），希望JavaScript能够成为国际标准，以此抵抗微软。ECMA的39号技术委员会（Technical Committee 39）负责制定和审核这个标准，成员由业内的大公司派出的工程师组成，目前共25个人。该委员会定期开会，所有的邮件讨论和会议记录，都是公开的
3. 1997年7月，ECMA组织发布262号标准文件（ECMA-262）的第一版，规定了浏览器脚本语言的标准，并将这种语言称为ECMAScript。这个版本就是ECMAScript 1.0版。之所以不叫JavaScript，一方面是由于商标的关系，Java是Sun公司的商标，根据一份授权协议，只有Netscape公司可以合法地使用JavaScript这个名字，且JavaScript已经被Netscape公司注册为商标，另一方面也是想体现这门语言的制定者是ECMA，不是Netscape，这样有利于保证这门语言的开放性和中立性。因此，ECMAScript和JavaScript的关系是，**前者是后者的规格，后者是前者的一种实现。在日常场合，这两个词是可以互换的**
4. ECMAScript只用来标准化JavaScript这种语言的基本语法结构，与部署环境相关的标准都由其他标准规定，比如DOM的标准就是由W3C组织（World Wide Web Consortium）制定的。ECMA-262标准后来也被另一个国际标准化组织ISO（International Organization for Standardization）批准，标准号是ISO-1626

## 五、JavaScript和Java的关系

1. JavaScript和Java是两种不一样的语言，但是它们之间存在联系。
2. JavaScript的基本语法和对象体系，是模仿Java而设计的。但是，JavaScript没有采用Java的静态类型。正是因为JavaScript与Java有很大的相似性，所以这门语言才从一开始的LiveScript改名为JavaScript。基本上，JavaScript这个名字的原意是“很像Java的脚本语言”。
3. 在JavaScript语言中，函数是一种独立的数据类型，以及采用基于原型对象（prototype）的继承链。这是它与Java语法最大的两点区别。JavaScript语法要比Java自由得多。
4. 另外，Java语言需要编译，而JavaScript语言则是运行时由解释器直接执行。
5. 总之，JavaScript的原始设计目标是一种小型的、简单的动态语言，与Java有足够的相似性，使得使用者（尤其是Java程序员）可以快速上手。

## 六、重大事件

1. JavaScript伴随着互联网的发展一起发展。互联网周边技术的快速发展，刺激和推动了JavaScript语言的发展。
2. 1996年，样式表标准CSS第一版发布。
3. 1997年，DHTML（Dynamic HTML，动态HTML）发布，允许动态改变网页内容。这标志着DOM模式（Document Object Model，文档对象模型）正式应用。
4. 1998年，Netscape公司开源了浏览器套件，这导致了Mozilla项目的诞生。几个月后，美国在线（AOL）宣布并购Netscape。
5. 1999年，IE 5部署了XMLHttpRequest接口，允许JavaScript发出HTTP请求，为后来大行其道的Ajax应用创造了条件。
6. 2000年，KDE项目重写了浏览器引擎KHTML，为后来的WebKit和Blink引擎打下基础。这一年的10月23日，KDE 2.0发布，第一次将KHTML浏览器包括其中。
7. 2001年，微软公司时隔5年之后，发布了IE浏览器的下一个版本Internet Explorer 6。这是当时最先进的浏览器，它后来统治了浏览器市场多年。
8. 2001年，Douglas Crockford提出了JSON格式，用于取代XML格式，进行服务器和网页之间的数据交换。JavaScript可以原生支持这种格式，不需要额外部署代码。
9. 2002年，Mozilla项目发布了它的浏览器的第一版，后来起名为Firefox。
10. 2003年，苹果公司发布了Safari浏览器的第一版。
11. 2004年，Google公司发布了Gmail，促成了互联网应用程序（Web Application）这个概念的诞生。由于Gmail是在4月1日发布的，很多人起初以为这只是一个玩笑。
12. 2004年，Dojo框架诞生，为不同浏览器提供了同一接口，并为主要功能提供了便利的调用方法。这标志着JavaScript编程框架的时代开始来临。
13. 2004年，WHATWG组织成立，致力于加速HTML语言的标准化进程。
14. 2005年，苹果公司在KHTML引擎基础上，建立了WebKit引擎。
15. 2005年，Ajax方法（Asynchronous JavaScript and XML）正式诞生，Jesse James Garrett发明了这个词汇。它开始流行的标志是，2月份发布的Google Maps项目大量采用该方法。它几乎成了新一代网站的标准做法，促成了Web 2.0时代的来临。
16. 2005年，Apache基金会发布了CouchDB数据库。这是一个基于JSON格式的数据库，可以用JavaScript函数定义视图和索引。它在本质上有别于传统的关系型数据库，标识着NoSQL类型的数据库诞生。
17. 2006年，jQuery函数库诞生，作者为John Resig。jQuery为操作网页DOM结构提供了非常强大易用的接口，成为了使用最广泛的函数库，并且让JavaScript语言的应用难度大大降低，推动了这种语言的流行。
18. 2006年，微软公司发布IE 7，标志重新开始启动浏览器的开发。
19. 2006年，Google推出 Google Web Toolkit 项目（缩写为GWT），提供Java编译成JavaScript的功能，开创了将其他语言转为JavaScript的先河。
20. 2007年，Webkit引擎在iPhone手机中得到部署。它最初基于KDE项目，2003年苹果公司首先采用，2005年开源。这标志着JavaScript语言开始能在手机中使用了，意味着有可能写出在桌面电脑和手机中都能使用的程序。
21. 2007年，Douglas Crockford发表了名为《JavaScript: The good parts》的演讲，次年由O'Reilly出版社出版。这标志着软件行业开始严肃对待JavaScript语言，对它的语法开始重新认识，
22. 2008年，V8编译器诞生。这是Google公司为Chrome浏览器而开发的，它的特点是让JavaScript的运行变得非常快。它提高了JavaScript的性能，推动了语法的改进和标准化，改变外界对JavaScript的不佳印象。同时，V8是开源的，任何人想要一种快速的嵌入式脚本语言，都可以采用V8，这拓展了JavaScript的应用领域。
23. 2009年，Node.js项目诞生，创始人为Ryan Dahl，它标志着JavaScript可以用于服务器端编程，从此网站的前端和后端可以使用同一种语言开发。并且，Node.js可以承受很大的并发流量，使得开发某些互联网大规模的实时应用变得容易。
24. 2009年，Jeremy Ashkenas发布了CoffeeScript的最初版本。CoffeeScript可以被转化为JavaScript运行，但是语法要比JavaScript简洁。这开启了其他语言转为JavaScript的风潮。
25. 2009年，PhoneGap项目诞生，它将HTML5和JavaScript引入移动设备的应用程序开发，主要针对iOS和Android平台，使得JavaScript可以用于跨平台的应用程序开发。
26. 2009，Google发布Chrome OS，号称是以浏览器为基础发展成的操作系统，允许直接使用JavaScript编写应用程序。类似的项目还有Mozilla的Firefox OS。
27. 2010年，三个重要的项目诞生，分别是NPM、BackboneJS和RequireJS，标志着JavaScript进入模块化开发的时代。
28. 2011年，微软公司发布Windows 8操作系统，将JavaScript作为应用程序的开发语言之一，直接提供系统支持。
29. 2011年，Google发布了Dart语言，目的是为了结束JavaScript语言在浏览器中的垄断，提供更合理、更强大的语法和功能。Chromium浏览器有内置的Dart虚拟机，可以运行Dart程序，但Dart程序也可以被编译成JavaScript程序运行。
30. 2011年，微软工程师Scott Hanselman提出，JavaScript将是互联网的汇编语言。因为它无所不在，而且正在变得越来越快。其他语言的程序可以被转成JavaScript语言，然后在浏览器中运行。
31. 2012年，单页面应用程序框架（single-page app framework）开始崛起，AngularJS项目和Ember项目都发布了1.0版本。
32. 2012年，微软发布TypeScript语言。该语言被设计成JavaScript的超集，这意味着所有JavaScipt程序，都可以不经修改地在TypeScript中运行。同时，TypeScript添加了很多新的语法特性，主要目的是为了开发大型程序，然后还可以被编译成JavaScript运行。
33. 2012年，Mozilla基金会提出asm.js规格。asm.js是JavaScript的一个子集，所有符合asm.js的程序都可以在浏览器中运行，它的特殊之处在于语法有严格限定，可以被快速编译成性能良好的机器码。这样做的目的，是为了给其他语言提供一个编译规范，使其可以被编译成高效的JavaScript代码。同时，Mozilla基金会还发起了Emscripten项目，目标就是提供一个跨语言的编译器，能够将LLVM的位代码（bitcode）转为JavaScript代码，在浏览器中运行。因为大部分LLVM位代码都是从C / C++语言生成的，这意味着C / C++将可以在浏览器中运行。此外，Mozilla旗下还有LLJS（将JavaScript转为C代码）项目和River Trail（一个用于多核心处理器的ECMAScript扩展）项目。目前，在可以被编译成JavaScript的语言列表上，共有将近40种语言。
34. 2013年，Mozilla基金会发布手机操作系统Firefox OS，该操作系统的整个用户界面都使用JavaScript。
35. 2013年，ECMA正式推出JSON的国际标准，这意味着JSON格式已经变得与XML格式一样重要和正式了。
36. 2013年5月，Facebook发布UI框架库React，引入了新的JSX语法，使得UI层可以用组件开发。
37. 2014年，微软推出JavaScript的Windows库WinJS，标志微软公司全面支持JavaScript与Windows操作系统的融合。
38. 2014年11月，由于对Joyent公司垄断Node项目、以及该项目进展缓慢的不满，一部分核心开发者离开了Node.js，创造了io.js项目，这是一个更开放、更新更频繁的Node.js版本，很短时间内就发布到了2.0版。三个月后，Joyent公司宣布放弃对Node项目的控制，将其转交给新成立的开放性质的Node基金会。随后，io.js项目宣布回归Node，两个版本将合并。
39. 2015年3月，Facebook公司发布了React Native项目，将React框架移植到了手机端，可以用来开发手机App。它会将JavaScript代码转为iOS平台的Objective-C代码，或者Android平台的Java代码，从而为JavaScript语言开发高性能的原生App打开了一条道路。
40. 2015年4月，Angular框架宣布，2.0版将基于微软公司的TypeScript语言开发，这等于为JavaScript语言引入了强类型。
41. 2015年5月，Node模块管理器npm超越CPAN，标志着JavaScript成为世界上软件模块最多的语言。
42. 2015年5月，Google公司的Polymer框架发布1.0版。该项目的目标是生产环境可以使用WebComponent组件，如果能够达到目标，Web开发将进入一个全新的以组件为开发基础的阶段。
43. 2015年6月，ECMA标准化组织正式批准了ECMAScript 6语言标准，JavaScript语言正式进入了下一个阶段，成为一种企业级的、开发大规模应用的语言。这个标准从提出到批准，历时10年，而JavaScript语言从诞生至今也已经20年了。
44. 2015年6月，Mozilla在asm.js的基础上发布WebAssembly项目。这是一种JavaScript语言编译后的二进制格式，类似于Java的字节码，有利于移动设备加载JavaScript脚本，解析速度提高了20+倍。这意味着将来的软件，会发布JavaScript二进制包