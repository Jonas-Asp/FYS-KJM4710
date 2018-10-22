    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 10:51:37 2018

@author: Rafiki
"""
import matplotlib.pyplot as plt
import numpy as np

Vr = [60, 80, 100, 120, 140, 160, 180, 200]
Ir = [0.139, 0.225, 0.320,	0.421, 0.529,	0.643, 0.764,	0.888]

msg = 2
irdiff = np.zeros(len(Ir)-1)
step = np.linspace(1,len(Ir)-1,len(Ir)-1)
t = 0
for i in range(len(Ir)-1):
    irdiff[i] = Ir[i+1]-Ir[i]



reg = np.polyfit(Vr,Ir,2)
msg = ("I(Ir) = %.5f + %.5fx+%.5fx^2" %(reg[2],reg[1],reg[0]))
#plt.plot(Vr,Ir,"o--",label=msg)
plt.plot(Vr,Ir,"o--")
plt.xlabel("V [kV]",fontsize = 14)
plt.ylabel("Ionerate [nA]",fontsize = 14)
plt.legend()
plt.title("Ionerate som funksjon av spenning", fontsize = 16, fontweight="bold", y=1.08)
plt.grid(linestyle='-', linewidth=0.5)
plt.show()

slope = np.polyfit(step,irdiff,2)
s = np.polyval(slope,step)
msg2 = ("Tilpasning av stigningstall: ")
plt.plot(step,s,"--",label=msg2)
plt.plot(step,irdiff,"o",label="Målte verdier")
plt.xlabel("Steglengde",fontsize = 14)
plt.ylabel("Ionerate stigningstall per steglengde",fontsize = 14)
plt.title("Stigningstall i ionerate per steglengde (20 kV)", fontsize = 16, fontweight="bold", y=1.08)
plt.legend()
plt.show()
print(slope)


vmax = np.array(Vr)
ssum = np.zeros(len(vmax))
for i in range(len(vmax)):
    v = np.linspace(1,vmax[i],vmax[i])
    w = vmax[i]-v
    plt.plot(v,w)    
    ssum[i] = sum(w)
plt.show()

plt.plot(vmax,ssum,"o--")
plt.show()
    

