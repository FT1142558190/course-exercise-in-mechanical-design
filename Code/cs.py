from math import pi,sin,cos,tan,atan,acos,sqrt,ceil,floor,radians,degrees

z1=24
z2=104
beta=17
m_n=2.0
a0=(z1+z2)*m_n/(2*cos(radians(beta)))  #
print("中心距{}".format(a0))
a0=135
print("实际中心距{}".format(a0))
b=(z1+z2)*m_n/2/a0
print("实际螺旋半径{}".format(b))
b=degrees(acos(b))
print("实际螺旋角{}".format(b))

d1=m_n*z1/cos(b*pi/180) #分度园1
print("分度园1  {}".format(d1))
d2=m_n*z2/cos(b*pi/180) #分度园2
print("分度园2  {}".format(d2))
chikuang=0.8*d1
chikuang=65#比轴要宽
b2=chikuang
b1=b2+5


#输出轴

T1 = 44451.0686972031
D1 = 50.5318043227294
Ft=2*T1/D1
print("切向力{}".format(Ft))

Fr=(Ft*tan(20*pi/180))/cos(b)
print("径向力{}".format(Fr))
Fx=Ft*tan(b*pi/180)
print("轴向力{}".format(Fx))
# print(tan(20*pi/180))
# print(cos(b))                 #傻逼角度弧度值
# 轴的强度计算

FZ=Ft/2
LD=65  #轴承到齿轮中心
LX=34.5         #危险截面轴承中心到危险截面

M=FZ*LD

print(acos(0))




