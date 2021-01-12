# HTML 多媒体

## 一、简介

 Web 上的多媒体指的是音效、音乐、视频和动画。多媒体来自多种不同的格式。它可以是您听到或看到的任何内容，文字、图片、音乐、音效、录音、电影、动画等等

## 二、audio标签

### 1、作用

 播放音频

### 2、语法格式

1. 格式1

   ```
   <audio src="">
    </audio>

   ```

2. 格式2

   ```
   <audio>
      <source src="路径" type="audio/格式">
   </audio>
   ```

### 3、属性,格式和兼容性

1. 属性

   | 属性     | 值       | 描述                                                         |
   | -------- | -------- | ------------------------------------------------------------ |
   | autoplay | autoplay | 如果出现该属性，则音频在就绪后马上播放。                     |
   | controls | controls | 如果出现该属性，则向用户显示控件，比如播放按钮。             |
   | loop     | loop     | 如果出现该属性，则每当音频结束时重新开始播放。               |
   | muted    | muted    | 规定视频输出应该被静音。                                     |
   | preload  | preload  | 如果出现该属性，则音频在页面加载时进行加载，并预备播放。如果使用 "autoplay"，则忽略该属性。 |
   | src      | *url*    | 要播放的音频的 URL。                                         |

### 4、示例代码

1. 简单的播放

   ```
   <audio src="audio/演员.mp3" controls>
       您的浏览器不支持!!!
   </audio>
   ```

2. 带属性的播放

   ```
   <audio controls autoplay muted loop>
       <source src="audio/演员.mp3" type="audio/mpeg" >
       您的浏览器不支持!!!
   </audio>
   ```

## 三、video标签

### 1、作用

 播放视频

### 2、语法格式

1. 格式1

   ```
   <video src="">
   </video>

   ```

2. 格式2

   ```
   <video>
      <source src="路径" type="video/格式">
   </video>

   ```

### 3、属性,格式和兼容性

1. 属性

   | autoplay | autoplay | 如果出现该属性，则视频在就绪后马上播放。                     |
   | -------- | -------- | ------------------------------------------------------------ |
   | controls | controls | 如果出现该属性，则向用户显示控件，比如播放按钮。             |
   | height   | *pixels* | 设置视频播放器的高度。                                       |
   | loop     | loop     | 如果出现该属性，则当媒介文件完成播放后再次开始播放。         |
   | muted    | muted    | 规定视频的音频输出应该被静音。                               |
   | poster   | *URL*    | 规定视频下载时显示的图像，或者在用户点击播放按钮前显示的图像。 |
   | preload  | preload  | 如果出现该属性，则视频在页面加载时进行加载，并预备播放。如果使用 "autoplay"，则忽略该属性。 |
   | src      | *url*    | 要播放的视频的 URL。                                         |
   | width    | *pixels* | 设置视频播放器的宽度。                                       |

2. 格式和兼容性

   | 格式 | IE | Firefox | Opera | Chrome | Safari | | --- | --- | --- | --- | --- | --- | | Ogg | No | 3.5+ | 10.5+ | 5.0+ | No | | MPEG 4 | 9.0+ | No | No | 5.0+ | 3.0+ | | WebM | No | 4.0+ | 10.6+ | 6.0+ | No |

### 4、示例代码

1. 简单案例

   ```
   video src="audio/new.mp4"  width="320" height="240" controls >
   </video>

   ```

2. 带属性的播放

   ```
   <video width="320" height="240" controls >
       <source  src="audio/new.mp4"  type="video/mp4"/>
   </video>

   ```

### 5、注意事项

1. 当前通过video标签的第二种格式虽然能够指定所有浏览器都支持的视频格式, 但是想让所有浏览器都通过video标签播放视频还有一个前提条件, 就是浏览器必须支持HTML5标签, 否则同样无法播放
2. 在过去的一些浏览器是不支持HTML5标签的, 所以为了让过去的一些浏览器也能够通过video标签来播放视频, 那么我们以后可以通过一个JS的框架叫做html5media来实现

## 四、marquee标签

### 1、作用

 播放视频作用：跑马灯效果

### 2、属性

1. direction: 设置滚动方向 left/right/up/down
2. scrollamount: 设置滚动速度, 值越大就越快
3. loop: 设置滚动次数, 默认是-1, 也就是无限滚动
4. behavior: 设置滚动类型 slide滚动到边界就停止, alternate滚动到边界就弹回

### 3、示例代码

```
<<!--默认类型-->
<marquee>翻滚吧,蛋炒饭</marquee>
<!--从右边开始滚动-->
<marquee direction="right">翻滚吧,蛋炒饭</marquee>
<!--向上滚动-->
<marquee direction="up">翻滚吧,蛋炒饭</marquee>
<!--向下滚动-->
<marquee direction="down">翻滚吧,蛋炒饭</marquee>
<!--设置滚动速度-->
<marquee scrollamount="1">翻滚吧,蛋炒饭</marquee>
<marquee scrollamount="100">翻滚吧,蛋炒饭</marquee>
<!--设置滚动次数-->
<marquee loop="1">翻滚吧,蛋炒饭</marquee>
<!--设置滚动类型-->
<marquee behavior="slide">翻滚吧,蛋炒饭</marquee>
<marquee behavior="alternate">翻滚吧,蛋炒饭</marquee>
滚动图片：
<marquee>
    <img src="img/wow.jpg">
</marquee>
</body>
```