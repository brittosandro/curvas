import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set(style="ticks")


fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(7.5, 8.8))

fig.subplots_adjust(
                     left=0.13,
                     right=0.97,    # {Define as distâncias entre os extremos}
                     bottom=0.08,
                     top=.94,
                     hspace=0.33,   # Organiza espaçoes entre os subplots
                     wspace=0.24    # Organiza espaçoes entre os subplots
                    )

dados = np.loadtxt('outB0TMC2.avr.dat')
nmove = dados[:, 0]
U_N = dados[:, 1]
E_N = dados[:, 6]
dens = dados[:, 4]

ax1.plot(nmove, U_N, 'blue', alpha=0.55, linewidth=2.5)
ax1.set_xlabel('NMOVE')
ax1.set_ylabel('U/N')

ax2.plot(nmove, E_N, 'blue', alpha=0.55, linewidth=2.5)
ax2.set_xlabel('NMOVE')
ax2.set_ylabel('E/N')

ax3.plot(nmove, dens, 'blue', alpha=0.55, linewidth=2.5)
ax3.set_xlabel('NMOVE')
ax3.set_ylabel('Densidade')

plt.plot()
plt.show()
