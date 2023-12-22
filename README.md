# -用于《机械设计课程设计》中的减速箱设计的计算

## Requirement
- `Python 3+` 
## 1. Overview
几乎所有高校的机械类专业都有《机械设计课程设计》课程，课程内容几乎都是设计一个减速箱。可能是一级减速，二级减速等，可能是直齿齿轮减速，斜齿轮减速等。在进行课程设计时，齿轮、带传递、蜗轮蜗杆等传动部件的计算量庞大，而且极容易出错。有的同学可能是手按计算器，一步一步来，这样效率是极低的。为了提高计算效率以及优化设计，我在进行课设的时候，借助了Python语言计算。现在将我的程序上传到Github，帮助大家的学习。

程序已经上传Github，有需要的小伙伴可以去下载程序。也欢迎大家在知乎或者CSDN下评论。

Github 链接：https://github.com/HuimingPan/course-exercise-in-mechanical-design

CSDN 链接：https://blog.csdn.net/weixin_46191033/article/details/113738206

知乎链接：https://zhuanlan.zhihu.com/p/349813060
## 2. Structure
- caculation.py 是主程序；
- belt.py 带传动计算；
- coupling.py 滚动轴承计算；
- gear.py 齿轮传动计算；
- key.py 键连接计算；
- load_anlysis.py 轴上载荷计算；
- rolling_bearing.py 滚动轴承计算；
- shaft.py 轴直径的初步计算；
## 3. Deficiency
由于是在进行课设的时候写的程序，时间仓促，有很多不足待改进，也有很多想法没有能够实现。如果大家看到了这篇，希望能够一起来改进这个程序。
- 没有建立《课程设计》中涉及的国标数据库，在调用的时候，需要手动查表并输入；
- 没有建立AutoCAD的接口，使自动绘图；
- 不能进行优化设计；
- 没有引入机械动力学计算；
                                    



我来
进行带轮设计 大带轮输入轴开孔式

小带轮 实心式
D直径28  E长度60 F键槽长度8mm   轴的长度是60   轮毂做成62

大带轮 开孔式  输入轴的最细段

D直径28  E长度60 F键槽长度8mm

轴颈选个偶数 轴的直径20  那大带轮24吧内径



大带轮宽宽度64mm  3x15+2x10  宽度

带轮 比轴长点  轴选 62 长度

大带轮画一个草图
                    
	取A_0=110,[τ_T]=28MPa
	估算轴的直径 d=18.36618537926532mm
	考虑键槽的影响，扩大轴的直径
	    轴上有 1 个键槽，直径增大5%
	    则 d=20mm
                       
确定带轮结构
    小带轮,采用实心结构
大带轮采用孔板式结构
d1=1。8d=1.8×26=46.8mm
查设计资料表7—8得  e=15，f=10,he =12，δ=6，φ=340，ba=11mm, =2.75

键的校核  键选  56

![img_3.png](img/img_3.png)

44.45106869720314
σ_bs= 41.34213978534518
第一根24mm的吧
对于第 2 根轴
	取A_0=110,[τ_T]=34MPa
	估算轴的直径 d=29.59609186162023mm
	考虑键槽的影响，扩大轴的直径
	    轴上有 1 个键槽，直径增大5%
	    则 d=32mm
                      

联轴器40mm的孔径

轴的设计

![img.png](img5/img.png)
                   

