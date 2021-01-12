# 文档处理

## 一、创建元素节点

### 1、使用函数创建新元素

1. 创建的新元素不会自动的把新元素插入到页面中，我们还需要明确的指定其插入到页面中的位置（比如使用append方法，指定其插入位置为某个元素的最后一个子元素）
2. 返回的jQuery对象中只包含html片段最顶层（外层）的元素，对于后代元素我们可以像处理页面中已有元素一样，使用children或find方法访问 也就是说alert($newElement);的结果应为1
3. 既然可以直接apend等方法插入html元素为何还要有这个创建新元素的功能？　使用$函数创建元素，是返回的是jQuery对象，我们可以使用jQuery对象里面的方法在创建的这个元素被插入到页面之前进行各种操作比如进行绑定事件处理函数！

### 2、克隆已有的元素

1. jQueryObject.clone( withDataAndEvents [, deepWithDataAndEvents ] )

2. 参数

   | 参数                    | 描述                                       |
   | --------------------- | ---------------------------------------- |
   | withDataAndEvents     | 可选/Boolean类型是否同时复制元素的附加数据和绑定事件，默认为`false`。 |
   | deepWithDataAndEvents | 可选/Boolean类型是否同时复制元素的所有子元素的附加数据和绑定事件，默认值即为参数`withDataAndEvents`的值。 |

3. 注意

   jQuery 1.5 新增支持：clone()支持第二个参数`deepWithDataAndEvents`。该参数指示是否同时复制被克隆元素的所有子元素的附加数据和绑定事件。

   *注意*：
   1、在jQuery 1.4之前，clone()函数只额外复制元素的绑定事件，从1.4版本开始，才开始支持复制元素的附加数据。
   2、1.5.0版本时(只有1.5.0)，参数withDataAndEvents的默认值被错误地设定为`true`，从1.5.1开始，其默认值才被改回`false`。

## 二、添加元素

### 1、内部添加

1. 向当前元素的内部追加内容添加到末尾

   ```
   append($(selector))  
   ```

2. 将当前元素在某元素内部追加。但由于会根据需要对当前元素进行移动，所以jQuery对象更改了，可用end()还原  

   ```
   appendTo($(selector))  
   ```

3. 向当前元素的内部前置内容  

   ```
   prepend($(selector))  
   ```

4. 将当前元素在某元素内部前置。类似于appendTo()，会改变对象 

   ```
   prependTo($(selector))   
   ```

### 2、外部添加

1. 向当前元素之后插入内容 

   ```
   after($(selector))  
   ```

2. 将当前元素插入到某元素之后。类似于appendTo()，会改变对象 

   ```
   insertAfter($(selector))  
   ```

3. 向当前元素之前插入内容  

   ```
   before($(selector))  
   ```

4. 将当前元素插入到某元素之前。类似于appendTo()，会改变对象

   ```
   insertBefore($(selector))  	
   ```

## 三、删除元素

1. 删除当前元素，该元素包含的文本内容和后代元素会一起删除掉，绑定的事件也不复存在

   ```
   remove()
   ```

2. 同样是删除当前元素，但是绑定的事件还是存在的

   ```
   detach()
   ```

3. 清空当前元素，该元素的文本内容和后代元素都将删除，但保留其本身

   ```
   empty()
   ```

## 四、替换元素

1. 移动页面上原有的元素来替换当前选定的页面元素，也可以添加新元素来替换 

   ```
   replaceWith($(selector))
   replaceWith($(html))  
   ```

2. 用当前选定的元素来替换某元素，可以使页面上原有元素，也可以是新元素。同样会根据需要复制当前元素副本，从而更改jQuery对象

   ```
    replaceAll($(selector))
    replaceAll($(html))  
   ```

### 