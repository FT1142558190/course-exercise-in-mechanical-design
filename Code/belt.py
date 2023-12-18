from math import pi,sin,ceil
class belt():
    '''
       每个皮带实例对象的属性和方法如下：
       P: 计算功率
       n1: 转速1
       i: 传动比
       P_ca: 计算功率
       type: 皮带类型
       dd1: 小带轮基准直径
       v: 带速
       dd20: 大带轮基准直径
       dd2: 大带轮基准直径
       a0: 中心距
       Ld0: 基准长度
       Ld: 基准长度
       a: 中心距
       a_min: 中心距下限
       a_max: 中心距上限
       alpha_1: 小带轮包角
       Pr: 单根V带的额定功率
       z: 皮带根数
       F0: 初拉力
       F_p: 压轴力
       shaft_d: 轴径
       wheel_dd: 小带轮基准直径和大带轮基准直径
       wheel_type: 小带轮结构和大带轮结构
       '''
    def __init__(self,P,n,i):
        print("\n-----------------")
        print("Now,begin the design of belt\n")
        self.P=P
        self.n1=n
        self.i=i
        self.belt_design()
    
    def belt_design(self):
        print('1.确定计算功率 P_ca\n载荷平稳工作16小时普通V带传动选择')
        self.K_A=1.1
        self.P_ca=self.K_A*self.P
        print('\t查7-5工作1.1系数 K_A=',self.K_A)
        print('\t计算功率 P_ca={}kW'.format(self.P_ca))
        print('2.根据7-12选择V带带型')
        self.type='A'
        print('\t根据P_ca、n1，选择{}型V带'.format(self.type))
        print('3.确定带轮的基准直径d_d,并验算带速 v')
        self.dd1=100#查表8-7、8-9、图8-11得
        self.v=pi*self.dd1*self.n1/60/1000
        self.dd20=self.dd1*self.i
        self.dd2=280#查表8-9 根据  计算值    取标准值
        print('\t初取小带轮基准直径 d_d1={}mm'.format(self.dd1))
        print('\t带速 v={}m/s'.format(self.v))
        if (self.v<25)&(self.v>5):
            print('\t带速在5m/s~25m/s之间，合适')
        else :
            print('\t带速不合适！！！')
        print('\t则大带轮基准直径 d_d2={}mm,取为 {}mm'.format(self.dd20,self.dd2))
        print('4.初定中心据确定V带的中心距a和基准直径L_d')
        self.X=0.7  #我们在0.7-2都可以
        self.a0=self.X*(self.dd1+self.dd2)
        self.a0=500#我们老师说选一个整点的数500
        self.Ld0=2*self.a0+pi/2*(self.dd1+self.dd2)+(self.dd2-self.dd1)**2/4/self.a0
        #初定v带基准长度  1613  不是标准长度 查表7-2  选1640 接近的选一个
        self.Ld=1640
        self.a=self.a0+(self.Ld-self.Ld0)/2
        #513.5  数和老师是一样的
        self.a_min=self.a-0.015*self.Ld
        self.a_max=self.a+0.030*self.Ld
        print('\t(1)初算中心距 a0={}mm'.format(self.a0))
        print('\t(2)初算带所需基准长度 L_d0={}mm,选为 {}mm'.format(self.Ld0,self.Ld))
        print('\t(3)（这个地方没讲  ）实际中心距 a={:.6}mm，可以  变化不用了范围为{:.6}~{:.6}mm'.format(self.a,self.a_min,self.a_max))
        print('5.验算小带轮上的包角 α1')
        self.alpha_1=180-(self.dd2-self.dd1)*57.3/self.a
        print('\t小带轮上的包角 α1={:.6}°'.format(self.alpha_1))
        if self.alpha_1>120:
            print("\t大于120°就算比较合理小带轮上的包角 α1 合适！")
        print('6.计算带的根数 z')
        print('\t(1)计算单根V带的额定功率 Pr')
        self.P0=0.77#插值法得到 1.3816kW  内查法    基本额定功率 那我选个0.47kw  7-6
        self.Delta_P0=0.09#插值法得到 1.1516kW       额定功率增量   0.05kw   7-7
        self.K_alpha=0.95 #包角修真 0.95
        self.K_L=0.99#表8-2  0.99
        self.Pr=(self.P0+self.Delta_P0)*self.K_alpha*self.K_L
        print('\t   单根V带的基本额定功率 P0={}kW'.format(self.P0))  
        print('\t   单根V带的额定功率增量 ΔP0={}kW'.format(self.Delta_P0)) 
        print('\t   修正系数 K_α={},K_L={}'.format(self.K_alpha,self.K_L))
        print("\t   单根V带的额定功率为 {} kW".format(self.Pr))
        print('\t(2)计算V带的根数率 z')
        self.z0=self.P_ca/self.Pr
        self.z=ceil(self.z0)
        print("\t   带的根数率 z={},取{}根".format(self.z0,self.z))
        print("7.确定带的初拉力 F0")
        if self.type=='B':
            self.q=0.170
        elif self.type=='A':
            self.q=0.1
        self.F0=500*(2.5-self.K_alpha)*self.P_ca/(self.K_alpha*self.z*self.v)+self.q*self.v**2
        print('\t{}型带的单位长度质量q={}kg/m'.format(self.type,self.q))
        print("\t单根V带的初拉力 F0={} N".format(self.F0))
        print("8.确定带的压轴力 F_p")
        self.F_p=2*self.z*self.F0*sin(self.alpha_1/2*pi/180)
        print("\t带的压轴力 F_p={} N".format(self.F_p))

    def belt_wheel(self,shaft_d):
        小带轮=0
        大带轮=1
        self.wheel_dd=[self.dd1,self.dd2]
        self.wheel_type=[]
        for d_d in [self.dd1,self.dd2]:
            if self.type=='B':
                b_d=14.0
                h_amin=3.5
                h_fmin=10.8
                e=19
                f_min=11.5
                delta_min=7.5
                if d_d<=190:
                    phi=34
                else:
                    phi=38
                d_a=d_d+h_amin+0.5
                
            if d_d<=2.5*shaft_d:
                self.wheel_type.append('实心式')
            elif d_d<=300:
                self.wheel_type.append('腹板式')
            elif d_d>300:
                self.wheel_type.append('轮辐式')
        print('小带轮基准直径为 {} mm,采用 {} 结构'.format(self.wheel_dd[小带轮],self.wheel_type[小带轮]))
        print('小带轮基准直径为 {} mm,采用 {} 结构'.format(self.wheel_dd[大带轮],self.wheel_type[大带轮]))
