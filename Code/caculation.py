from math import pi,sqrt
import belt,gear,shaft,coupling,rolling_bearing,key,load_anlysis
def total_design():
    '''
    '''
    print("\n-----------------")
    print("Now,begin the total design\n我们的电机是")
    print('Y100L2-4  1430转速3kw同步1500')#加点料FTyiming
    #运输带1400n  速度1.55ms  卷筒直径250mm
    #总效率n=带的 齿轮的 轴承的平方 联轴器的
    F=1400#measured in N
    v=1.55#measured in m/s
    D=0.25#measured in m          250mm=2.5m
    print('卷筒直径{}力{}转速{}'.format(D,F,v))
    nw=v/(D/2)/(2*pi)*60   #measured in r/min
    nw=v*60/(D*pi) #我们的带速怎么那么算呢rpm多少转   r
    print('我们传输带的转速'+str(nw))
    Pw=F*v/1000/0.96  #P is the total output power(kW);预计需要的功率

    # 变量 eta_belt 存储传动带效率，取值为 0.95
    eta_belt = 0.96

    # 变量 eta_coupler 存储联轴器效率，取值为 0.99
    eta_coupler = 0.99

    # 变量 eta_rolling_bearing 存储滚动轴承效率，取值为 0.985
    eta_rolling_bearing = 0.99

    # 变量 eta_sliding_bearing 存储滑动轴承效率，取值为 0.98
    eta_sliding_bearing = 0.99

    # 变量 eta_gear 存储齿轮效率，取值为 0.97
    eta_gear = 0.98

    # # 变量 eta_roll 存储滚筒效率，取值为 0.96
    # eta_roll = 0.96

    # eta=eta_belt*eta_coupler*eta_rolling_bearing**6*eta_sliding_bearing**2*eta_gear**2#*eta_roll
    eta = eta_belt * eta_coupler * eta_rolling_bearing  * eta_sliding_bearing *  eta_gear
    Pd=Pw/eta
    print("总的输出功率为 {} kW;\n总的传递效率为 {:.4}%;\n需要电动机的功率为 {:.3} kW\n".format(Pw,eta*100,Pd))

    nm=1430        #我选的电机也是满载转速960rpm  1430

    #Calculate the transmission ratio
    i=nm/nw      #总传动比
    print("总传动比为：{}".format(i))

    #选择周一的传动比为2.8
    i1=2.8     #带的传动比
    i2=sqrt(1.3*i/i1)
    i3=i/i1/i2
    i2=i/i1  #齿轮的传动
    i3=1           #联轴器的传动比
    #i3没用 就带的传动比和齿轮的传动比
    print("各级传动比分别为：\n\ti1={},\n\ti2={},\n\t（么用）i3={}".format(i1,i2,i3))
    i=[i1,i2,i3]
    #Calculate the rotate speed

    n1=nm/i1    #带的转速
    n2=n1/i2    #齿轮的转速
    n3=n2/i3       #没用上
    n4=n3               #没用
    print("各轴的转速分别为：\n\tn1={} r/min,\n\tn2={}r/min,\n\tn3={}r/min,\n\t（没用）n4={}r/min".format(n1,n2,n3,n4))
    n=[nm,n1,n2,n3,n4]
    #Calculate the power of each roller

    P1=Pd*eta_belt    #belt 带   轴一
    P2=P1*eta_gear*eta_rolling_bearing   #gear齿轮  滚动轴承  轴二
    P3=P2*eta_coupler*eta_rolling_bearing   #coupler联轴器  滚动轴承工作轴了 轴三
    P4=P3*eta_coupler*eta_rolling_bearing**2     #工作机
    print("各轴的输入功率分别为：\n\t带P1={}kW,\n\tP2={}kW,\n\tP3={}kW,\n\t（没用上）P4={}kW".format(P1,P2,P3,P4))
    P=[Pd,P1,P2,P3,P4]
    #print(P4*eta_roll*eta_sliding_bearing**2)


    #Calculate the torque of each roller
    Td=9550*Pd/nm   #电机的转矩 但轴的
    T11=Td*i1*n1
    T1=9550*P1/n1   #一轴
    T2=9550*P2/n2   #二轴
    T3=9550*P3/n3  #三轴
    T4=9550*P4/n4   #工作机
    print("各轴的输入功率分别为：\n\t轴一T1={} N·m,\n\t二T2={} N·m,\n\t三T3={} N·m,\n\t工作T4={} N·m\n\t注意要mm单位".format(T1,T2,T3,T4))
    T=[T1,T2,T3,T4]
    return i,n,P,T

i,n,P,T=total_design()
belt=belt.belt(P=P[0],n=n[0],i=i[0])      #带
gear1=gear.gear(P=P[1],n=n[1],i=i[1])       # 齿轮
gear2=gear.gear(P=P[2],n=n[2],i=i[2])
shaft1=shaft.shaft(P=P[1],n=n[1])            #）轴
shaft2=shaft.shaft(P=P[2],n=n[2])
shaft3=shaft.shaft(P=P[3],n=n[3])
shaft4=shaft.shaft(P=P[4],n=n[4])
couple=coupling.coupling(P=P[2],n=n[2])      #联轴器用到p2就行
rolling1=rolling_bearing.rolling(P=P[1],n=n[1],d=shaft1.d) #轴承
rolling2=rolling1
rolling3=rolling_bearing.rolling(P=P[2],n=n[2],d=shaft2.d)
rolling4=rolling3
rolling5=rolling_bearing.rolling(P=P[3],n=n[3],d=shaft3.d)
rolling6=rolling5

key1=key.key(T[0],64)
key2=key.key(T[1],60)
key3=key.key(T[2],82)         #键
key3=key.key(T[3],90)

load_anlysis.force_analyze(gear1)