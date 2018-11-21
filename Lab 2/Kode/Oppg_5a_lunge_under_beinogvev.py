import numpy as np
import matplotlib.pyplot as plt
D = [ 2.7913E-12,  4.8956E-12,  5.0175E-12,  5.0000E-12,  4.9413E-12,  5.0526E-12,  4.7928E-12,  4.7192E-12,  4.6226E-12,  4.5653E-12,  4.5695E-12,  4.5151E-12,  4.4786E-12,  4.4135E-12,  4.3489E-12,  4.3124E-12,  4.2411E-12,  4.1893E-12,  4.1416E-12,  4.0716E-12,  4.0139E-12,  3.9250E-12,  3.8536E-12,  3.7320E-12,  3.7277E-12,  3.6838E-12,  3.7425E-12,  3.7225E-12,  3.7251E-12,  3.6437E-12,  3.6671E-12,  3.6102E-12,  3.3203E-12]
D =  (1/4.9452E-12) * np.array(D)
x = np.linspace(0.17,5.61,33)

plt.plot(x,D,'o-')
plt.show()

""" Tissue Bone """
D2 = [ 4.2875E-12,  5.0807E-12,  5.0730E-12,  4.9716E-12,  4.8804E-12,  4.8917E-12,  4.5707E-12,  4.4503E-12,  4.3527E-12,  4.2087E-12,  4.0515E-12,  3.8015E-12,  3.7217E-12,  3.5953E-12,  3.4516E-12,  3.2728E-12,  3.0772E-12,  2.9702E-12,  2.8104E-12,  2.6442E-12]
x2 = np.linspace(0.5,10,20)

plt.plot(x2,D2,'o-')
plt.show()

""" Pb Tissue """
D3 = [ 6.6689E-12,  5.6696E-12,  3.0776E-12,  3.0147E-12,  2.9242E-12,  2.7958E-12,  2.8239E-12,  2.7519E-12,  2.6690E-12,  2.5970E-12,  2.4481E-12,  2.3978E-12,  2.2959E-12,  2.2835E-12,  2.1556E-12,  2.1004E-12,  2.0362E-12,  2.0686E-12,  1.9576E-12,  1.8399E-12,  1.7989E-12,  1.7785E-12,  1.6732E-12,  1.6444E-12,  1.5668E-12,  1.5153E-12,  1.4775E-12,  1.3863E-12,  1.3186E-12,  1.2977E-12,  1.2348E-12,  1.2361E-12

      ] 
D3 = (1/6.6689E-12) *np.array(D3)
x3 = np.linspace(0.5, 0.5*32, 32)

plt.figure(figsize=(10,10))
plt.plot(x3,D3,'o-')
plt.xlabel('Dybde Z [cm]',fontsize="16")
plt.ylabel('Relativ dose',fontsize="16")
plt.title("1 MeV monoenergiske fotoner med 1 cm Pb deretter 15 cm bløtvev", fontsize="16", fontweight="bold", y=1.04)
plt.legend()


plt.show()