# 使用说明

运行shopcanvas.py启动程序

```bash
python3 shopcanvas.py
```

使用按键0到5执行各项功能

1：测试，加入一条商品

2：测试，提交表单

3：测试，重置表单

4：售货模式，正常使用

5：连接客户端

0：退出



## 建议食用方法

运行程序，按5键连接atlas 200的多目标检测客户端。

连接一个触摸屏，将主界面显示给用户，提供按键4给顾客。

顾客看到的初始界面如下

![image-20210711152639927](C:\Users\djinni\AppData\Roaming\Typora\typora-user-images\image-20210711152639927.png)

用户将购买的商品放置在售货的货架上，点击确认后启动目标检测程序，检测货架上的所有货物，将结果显示在界面上。

![image-20210711154103571](C:\Users\djinni\AppData\Roaming\Typora\typora-user-images\image-20210711154103571.png)

用户确认支付后，将检测到的人脸上传到支付的api进行刷脸支付。