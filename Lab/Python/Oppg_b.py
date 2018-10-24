    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 10:51:37 2018

@author: Rafiki
"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error

Vr = [60, 80, 100, 120, 140, 160, 180, 200]
Ir = [0.139, 0.225, 0.320,	0.421, 0.529,	0.643, 0.764,	0.888]

msg = 2
irdiff = np.zeros(len(Ir)-1)
step = np.linspace(1,len(Ir)-1,len(Ir)-1)
t = 0
for i in range(len(Ir)-1):
    irdiff[i] = Ir[i+1]-Ir[i]




reg1 = np.polyfit(Vr,Ir,1)
reg2 = np.polyfit(Vr,Ir,2)
s1 = np.polyval(reg1,Vr)
s2 = np.polyval(reg2,Vr)
msg1 = ("Førstegradspolynom")
msg2 = ("Andregradspolynom")
plt.plot(Vr,Ir,"ro",label="Målte verdier")
plt.plot(Vr,s1,":",color="orange",label=msg1)
plt.plot(Vr,s2,"--",color="green",label=msg2)
plt.xlabel("V [kV]",fontsize = 14)
plt.ylabel("Ionerate [nA]",fontsize = 14)
plt.legend()
plt.title("Ionerate som funksjon av spenning", fontsize = 16, fontweight="bold", y=1.08)
plt.grid(linestyle='-', linewidth=0.5)
plt.show()

print(mean_squared_error(Ir,s1))
print(mean_squared_error(Ir,s2))

#slope1 = np.polyfit(step,irdiff,1)
#slope2 = np.polyfit(step,irdiff,2)
#s1 = np.polyval(slope1,step,)
#s2 = np.polyval(slope2,step)
#msg2 = ("Tilpasning første grad")
#msg3 = ("Tilpasning annen grad")
#plt.plot(step,s1,"g--",color="orange",label=msg2)
#plt.plot(step,s2,"--",color="green",label=msg3)
#plt.plot(step,irdiff,"ro",label="Målte verdier")
#plt.xlabel("Steglengde",fontsize = 14)
#plt.ylabel("Ionerate stigningstall per steglengde",fontsize = 14)
#plt.title("Stigningstall i ionerate per steglengde (20 kV)", fontsize = 16, fontweight="bold", y=1.08)
#plt.legend()
#plt.show()
#
#print(mean_squared_error(irdiff,s1))
#print(mean_squared_error(irdiff,s2))


vmax = np.array(Vr)
ssum = np.zeros(len(vmax))
diff = np.zeros(len(vmax))
for i in range(len(vmax)):
    v = np.linspace(1,vmax[i],vmax[i])
    w = vmax[i]-v
    plt.plot(v,w)    
    ssum[i] = sum(w)
    diff[i] = 0.5*vmax[i]**2
plt.xlabel("kV",fontsize = 14)
plt.ylabel("$Psi$",fontsize = 14)
plt.show()

plt.plot(vmax,ssum,"o--")
plt.plot(vmax,diff)
plt.show()
    


