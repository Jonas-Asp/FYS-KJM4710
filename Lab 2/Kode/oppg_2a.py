import numpy as np
import matplotlib.pyplot as plt


D = np.array([3.022E-15, 2.967E-15, 2.590E-15, 2.591E-15, 2.376E-15]) / 3.022E-15
t = np.array([0.5, 1.0, 1.5, 2.0,2.5]) * 1e-1
lnD = np.log(D)

z, cov = np.polyfit(t, lnD, 1, cov=True)
print(z)
print(np.sqrt(np.diag(cov)))
x = np.linspace(0.05,0.25,2)
pz = np.exp(np.polyval(z,x))

plt.figure(figsize=(10,10))
plt.semilogy(t, D, 'o:', label="Målinger")
plt.semilogy(x,pz,'--', label="Tilpasning")
plt.xlabel('Kobber tykkelse [cm]',fontsize="16")
plt.ylabel('Relativ dose',fontsize="16")
plt.title("250 keV monoenergiske fotoner - Dose i H2O detektor variabel primærfilter(cu) tykkelse", fontsize="16", fontweight="bold", y=1.04)
plt.legend()


plt.show()
