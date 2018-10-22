#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 10:51:37 2018

@author: Rafiki
"""
import matplotlib.pyplot as plt
import numpy as np

I = [5.0,	 5.5, 6.0, 6.5, 7.0, 7.5 ,8.0 ,8.5, 9.0, 9.5, 10.0]
Ir = [0.069,	0.076, 0.083,	0.090, 0.097, 0.104, 0.111, 0.118, 0.125,	 0.132, 0.139]

reg = np.polyfit(I,Ir,1)
msg = ("I(Ir) = %.3f + %.3fx" %(reg[1],reg[0]))


plt.plot(I,Ir,"-o",label=msg)
plt.xlabel("I [mA]",fontsize = 14)
plt.ylabel("Ionerate [nA]",fontsize = 14)
plt.xticks(np.arange(5, 10, step=0.5))
plt.legend()
plt.title("Ionerate som funksjon av strøm", fontsize = 16, fontweight="bold", y=1.08)
plt.show()