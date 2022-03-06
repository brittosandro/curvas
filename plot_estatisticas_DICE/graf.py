import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm


sns.set(style="ticks")

#fig, ax1 = plt.subplots()

fig, ax = plt.subplots(3, 2, figsize=(7.5, 8.8))

fig.subplots_adjust(
                     left=0.11,
                     right=0.97,    # {Define as distâncias entre os extremos}
                     bottom=0.08,
                     top=.94,
                     hspace=0.33,   # Organiza espaçoes entre os subplots
                     wspace=0.24    # Organiza espaçoes entre os subplots
                    )

dados = np.loadtxt('arq_dados.dat')
nmove = dados[:, 0]
Hc_N = dados[:, 2]
U_1 = dados[:, 3]
densy = dados[:, 4]

# ------------------- Entantia conformacinal ----------------------------------
# Evolução da Entalpia Conformacional
ax[0, 0].plot(nmove, Hc_N, 'blue', alpha=0.55)
ax[0, 0].tick_params(labelcolor='k', labelsize='small', width=1.0)
ax[0, 0].set_xlabel('NMOVE', )
ax[0, 0].set_ylabel('Hc/N', )

# Dirtribuição da Entalpia conformacinal
mu = np.average(Hc_N)
sigma = np.std(Hc_N)
num_bins = 60

n, bins, patches = ax[0, 1].hist(Hc_N, num_bins, density=True, facecolor='blue', alpha=0.55)
y = norm.pdf(bins, mu, sigma)
ax[0, 1].plot(bins, y, '--', linewidth=1.5, color='red')
ax[0, 1].set_xlabel('Hc/N', )
# -----------------------------------------------------------------------------

# -------------------- Densidade ----------------------------------------------
# Evolução temporal da Densidade
ax[1, 0].plot(nmove, densy, 'blue', alpha=0.55)
ax[1, 0].tick_params(labelcolor='k', labelsize='small', width=1.0)
ax[1, 0].set_xlabel('NMOVE', )
ax[1, 0].set_ylabel('Densidade',)

#Distribuição da Densidade
mu = np.average(densy)
sigma = np.std(densy)
num_bins = 60

n, bins, patches = ax[1, 1].hist(densy, num_bins, density=True, facecolor='blue', alpha=0.55)
y = norm.pdf(bins, mu, sigma)
ax[1, 1].plot(bins, y, '--', linewidth=1.5, color='red')
ax[1, 1].set_xlabel('Densidade', )

# ---------------------- Energia Interna --------------------------------------
# Evolução temporal da energia interna do soluto
ax[2, 0].plot(nmove, U_1, 'blue', alpha=0.55)
ax[2, 0].tick_params(labelcolor='k', labelsize='small', width=1.0)
ax[2, 0].set_xlabel('NMOVE', )
ax[2, 0].set_ylabel('U_1', )

# Distribuição da energia interna do solvente
mu = np.average(U_1)
sigma = np.std(U_1)
num_bins = 60

n, bins, patches = ax[2, 1].hist(U_1, num_bins, density=True, facecolor='blue', alpha=0.55)
y = norm.pdf(bins, mu, sigma)
ax[2, 1].plot(bins, y, '--', linewidth=1.5, color='red')
ax[2, 1].set_xlabel('U_1', )

plt.plot()
plt.show()
