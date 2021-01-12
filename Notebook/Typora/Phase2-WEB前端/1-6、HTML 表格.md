# HTML 表格

## 1、作用

 以表格形式将数据显示出来，当数据量非常大的时候，表格这种展现形式被认为是最为清晰的一种展现形式。

## 2 、格式

1. table定义表格

2. tr定义行

3. td定义单元格

   ```
   <table width=* height=* bgcolor=* border=* bordercolor=* cellspacing=* cellpadding=*>
       <body>
           <tr>
               <td>
                   此处加入内容
               </td>
           </tr>
       </body>
   </table>

   ```

## 3、常用属性

         1）width="表格的宽度"
         2）height="表格的高度"
         3）border="表格的边框"
         4）bgcolor="表格的背景色" bg=background
         5）bordercolor="表格的边框颜色"
         6）cellspacing="单元格与单元格之间的间距"
         7）cellpadding="单元格与内容之间的空隙"
         
         颜色： red, green blue, orange
            #FF00FF (红绿蓝 RGB颜色) 0~FF(0~255)  FF:15*16 + 15 = 15*17=255
            rgb(255, 0, 255)
     
         8）对齐方式：align="left/center/right";
         9)合并单元格属性：
         colspan=“所要合并的单元格的列数"合并列;
         rowspan=“所要合并单元格的行数”合并行;
         
         align="center" : 在table中表示表格居中
         align="center" : 在tr和td中表示文字居中
1. border： 默认情况下表格的边框宽度为0看不到, 通过border属性给表格指定边框宽度

2. width：默认情况下表格的宽度是由内容自动计算出来的, 可以通过width属性指定表格的宽度

3. cellspacing：外边距. 默认情况下单元格之间有2个像素的间隙, 可以通过cellpadding指定表格之间的间隙

4. cellpadding：内边距. 默认情况下单元格边缘距离内容有1个像素的内边距, 可以通过cellpadding属性指定单元格边缘和内容之间的内边距

5. align：

   - 作用: 规定表格相对周围元素的对齐方式, 它的取值有center、left、right
   - 例如：
     - 给table设置align属性, 是让表格在浏览器中居左/居右/居中
     - 给tr设置align属性, 是让当前行中所有内容居左/居右/居中
     - 给td设置align属性,是让当前单元格中所有内容居左/居右/居中
     - 该属性仅仅作为了解, 企业开发中用css代替, 因为HTML仅仅用于说明语义
     - 如果td中设置了align属性, tr中也设置了align属性, 那么单元格中的内容会按照td中设置的来对齐

6. bgcolor：

   - 作用：规定表格的背景颜色
   - 例如：
     - 给table设置bgcolor属性, 是给整个表格设置背景颜色
     - 给tr设置bgcolor属性, 是给当前行设置背景颜色
     - 给td设置bgcolor属性, 是给当前单元格设置背景颜色
     - 该属性仅仅作为了解, 企业开发中用css代替, 因为HTML仅仅用于说明语义

7. valign：

   - 作用：规定表格相对周围元素的对齐方式, 它的取值有center、left、right
   - 例如：
     - 给table设置valign属性, 无效
     - 给tr设置valign属性, 是让当前行中所有内容居上/居中/居下
     - 给td设置valign属性,是让当前单元格中所有内容居上/居中/居下
     - 如果td中设置了valign属性, tr中也设置了valign属性, 那么单元格中的内容会按照td中设置的来对齐

8. 其他：

   - 表单中有两种类型的单元格，一种是标准单元格td，一种是表头单元格th

   - th标签：给每一列设置标题，单元格中的内容会自动加粗、居中

   - caption标签：给整个表格设置标题一定要嵌套在table标签内部才有效

   - 例如：

     ```
     <table bgcolor="black" cellspacing="1px" width="800px" align="center">
         <caption>
             <h2>游戏排行榜</h2>
         </caption>
         <tr bgcolor="#a9a9a9">
             <th>排名</th>
             <th>游戏</th>
             <th>票数</th>
             <th>图片</th>
             <th>相关链接</th>
         </tr>
         <tr bgcolor="white" align="center">
             <td>1</td>
             <td>LOL</td>
             <td>26561</td>
             <td>
                 <img src="img/lol.jpg" width="100">
             </td>
             <td>
                 <a href="#">资料</a>
                 <a href="#">评测</a>
                 <a href="#">礼包</a>
             </td>
         </tr>
         <tr bgcolor="white" align="center">
             <td>2</td>
             <td>DOTA2</td>
             <td>20000</td>
             <td>
                 <img src="img/dota2.jpg"  width="100">
             </td>
             <td>
                 <a href="#">资料</a>
                 <a href="#">评测</a>
                 <a href="#">礼包</a>
             </td>
         </tr>
         <tr bgcolor="white" align="center">
             <td>3</td>
             <td>WOW</td>
             <td>18065</td>
             <td>
                 <img src="img/wow.jpg" width="100">
             </td>
             <td>
                 <a href="#">资料</a>
                 <a href="#">评测</a>
                 <a href="#">礼包</a>
             </td>
         </tr>
     </table>

     ```

## 4 、表格的复杂应用

#### 4.1、表格的结构

 开发中经常需要动态的修改单元格中的某一部分内容,如果设置了,我们就可以配合AJAX去动态的更新表格的内容

1. thead标签:用来存放当前列的表头，如果没有加css页面默认将表头中的高度设置变小

2. tbody标签:一般用来存放页面中的主体数据，如果不写会自动加上

3. tfoot标签:用来存放表格的页脚（脚注或表注)，如果没有加css页面默认将表头中的高度设置变小，一般不会出现

4. 示例代码

   ```
   <table>
       <caption>表格的标题</caption>
       <thead>
           <tr>
               <th>每一列的标题</th>
           </tr>
       </thead>
       <tbody>
           <tr>
               <td>数据</td>
           </tr>
       </tbody>
       <tfoot>
           <tr>
               <td>数据</td>
           </tr>
       </tfoot>
   </table>

   ```

> 注意：
>
> 1. 表格结构的意义主要是用于SEO(Search Engine Optimization), 便于搜索引擎优化指定哪部分的内容是需要抓取的重要内容，一般情况下搜索引擎会优先抓取tbody中的内容。
> 2. 由于有一部分浏览器对table的这种结构支持不是很好，所以在企业开发中一般都不用严格的按照这种结构来编写

#### 4.2、合并单元格

1. 横向合并
   - colspan：合并当前行的哪几个单元格，注意colspan只会向后合并，不会向前合并。
   - 例如：
   - 说明：把当前单元格当做两个单元格来看待
2. 纵向合并
   - rowspan:合并当前列的哪几个单元格，注意rowspan只会向后合并，不会向前合并。
   - 例如：
   - 说明：把当前单元格当做两个单元格来看待

## 5、案例



1. 注册页面

![register](register.png)

上述注册完整HTML代码如下

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
	</head>
	<body>
		<h2>百度</h2>
		<table cellpadding="5" cellspacing="0" align="center">
			<tr>
				<td align="right">手机/邮箱</td>
				<td>
					<input type="text" placeholder="手机/邮箱" style="width: 200px; height: 26px;" />
				</td>
			</tr>
			<tr>
				<td align="right">密码</td>
				<td>
					<input type="text" placeholder="密码" style="width: 200px; height: 26px;" />
				</td>
			</tr>
			<tr>
				<td align="right">验证码</td>
				<td>
					<input type="text" placeholder="验证码" style="width: 100px; height: 26px;" />
					<a href="#">换一张</a>
				</td>
			</tr>
			<tr>
				<td></td>
				<td>
					<input type="checkbox" checked="checked"/>我已阅读并接受<a href="#"><百度协议></a>
				</td>
			</tr>
			<tr>
				<td></td>
				<td>
					<input type="button" value="注册" style="width: 200px; height: 30px; background: #00AA88;"/>
				</td>
			</tr>
		</table>
	</body>
</html>
```






2. 天气预报

![img](http://opzv089nq.bkt.clouddn.com/17-8-14/77975409.jpg)



上述天气预报表格的完整代码如下：

```html

<table width="1000" style="text-align: center; " bgcolor="#e9967a" border="1" cellpadding="10" cellspacing="0">
    <tr>
        <th colspan="3">日期</th>
        <th colspan="2">天气现象</th>
        <th>气温</th>
        <th>风向</th>
        <th>风力</th>
    </tr>
    <tr>
        <td rowspan="2" colspan="2">22日 星期五</td>
        <td>白天</td>
        <td><img src="img/weathy_01.png"></td>
        <td>晴间多云</td>
        <td>高温 7C</td>
        <td>无持续风向</td>
        <td>微风</td>
    </tr>
    <tr>
        <td>夜间</td>
        <td><img src="img/weathy_01.png"></td>
        <td>晴间多云</td>
        <td>低温 -4C</td>
        <td>无持续风向</td>
        <td>微风</td>
    </tr>

    <tr>
        <td rowspan="2" colspan="2" style="margin-top: 10px"> 23日 星期六</td>
        <td>白天</td>
        <td><img src="img/weathy_01.png"></td>
        <td>晴间多云</td>
        <td>高温 7C</td>
        <td>无持续风向</td>
        <td>微风</td>
    </tr>

    <tr>
        <td>夜间</td>
        <td><img src="img/weathy_01.png"></td>
        <td>晴间多云</td>
        <td>低温 -4C</td>
        <td>无持续风向</td>
        <td>微风</td>
    </tr>
</table>

```

