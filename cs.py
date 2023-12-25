from math import pi,sin,cos,tan,atan,acos,sqrt,ceil,floor,radians,degrees

z1=24
z2=104
beta=13
m_n=2.0
a0=(z1+z2)*m_n/2/cos(radians(beta))
print(a0)
a0=131.36692579755413
a0=135

b=acos(radians((z1+z2)*m_n/2/a0))
b=(z1+z2)*m_n/2/a0
print(b)
print(degrees(acos(b)))
b=degrees(acos(b))#18
d1=m_n*z1/cos(b) #分度园1
d2=m_n*z2/cos(b) #分度园2
chikuang=0.8*d1
chikuang=65#比轴要宽
b2=chikuang
b1=b2+5
print(b1)

