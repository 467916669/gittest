import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
a=['1.27','1.30','2.2','2.5','2.8','2.10','2.15','2.20','2.23','2.29','3.3']
b=[1771,1982,2829,3694,2653,2484,2009,892,416,579,120]
c=[2077,4812,5173,5328,3916,3516,1918,1614,620,132,143]

plt.plot(a,b,"ro-",label="新增确诊病例")
plt.plot(a,c,"bo-",label="新增疑似病例")
plt.xlabel("日期")
plt.ylabel("人数")
plt.legend()
plt.show()