# img_combine
利用手Q对PNG显示方式，形成缩略图和点开原图不同的效果

## 效果

在图片没点开时，看起来是这样的

![font](font.jpg)

点开之后就显示这样的

![back](back.jpg)

## 用法

安装 skimage 库，放入你想要的“前景图”(font.jpg)和“背景图”(back.jpg)

`python combine.py`

得到result.png，发到手机里就可以了

![result](result.png)

参考代码：https://github.com/hfutxqd/ImageConverter