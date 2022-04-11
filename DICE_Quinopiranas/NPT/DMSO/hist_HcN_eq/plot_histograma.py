from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns



sns.set(style="ticks")

fig, ax = plt.subplots(2, 2, figsize=(7, 7))
fig.subplots_adjust( left=0.075,
                     right=0.965,    # {Define as distâncias entre os extremos}
                     bottom=0.125,
                     top=0.945,
                     hspace=0.265,    # Organiza espaçoes entre os subplots
                     wspace=0.175)    # Organiza espaçoes entre os subplots

dados_mol1 = np.loadtxt('IA_DMSO_EQ_Hc_nmove.dat')
nmove_mol1 = dados_mol1[:, 0]
dens_mol1 = dados_mol1[:, 1]
                    
dados_mol2 = np.loadtxt('IB_DMSO_EQ_Hc_nmove.dat')
nmove_mol2 = dados_mol2[:, 0]
dens_mol2 = dados_mol2[:, 1]

dados_mol3 = np.loadtxt('IC_DMSO_EQ_Hc_nmove.dat')
nmove_mol3 = dados_mol3[:, 0]
dens_mol3 = dados_mol3[:, 1]

dados_mol4 = np.loadtxt('ID_DMSO_EQ_Hc_nmove.dat')
nmove_mol4 = dados_mol4[:, 0]
dens_mol4 = dados_mol4[:, 1]

# ------------------- Molecula 1 --------------------------------------
# Distribuição da Densidade Molecula 1
mu = np.average(dens_mol1)
sigma = np.std(dens_mol1)
num_bins = 60
n, bins, patches = ax[0, 0].hist(dens_mol1, num_bins, density=True, 
                                 facecolor='#0000ff', alpha=0.55)
y = norm.pdf(bins, mu, sigma)
ax[0, 0].plot(bins, y, '--', linewidth=1.5, color='black')
ax[0, 0].set_title('IA - DMSO', fontsize = 'large',
                   fontweight = 'bold')


# -------------------- Molecula 2 -------------------------------------
# Distribuição da Densidade Molecula 2
mu = np.average(dens_mol2)
sigma = np.std(dens_mol2)
num_bins = 60
n, bins, patches = ax[0, 1].hist(dens_mol2, num_bins, density=True, 
                                 facecolor='#008080', alpha=0.55)
y = norm.pdf(bins, mu, sigma)
ax[0, 1].plot(bins, y, '--', linewidth=1.5, color='black')
ax[0, 1].set_title('IB - DMSO', fontsize = 'large',
                   fontweight = 'bold')



# -------------------- Molecula 3 -------------------------------------
# Distribuição da Densidade Molecula 3
mu = np.average(dens_mol3)
sigma = np.std(dens_mol3)
num_bins = 60
n, bins, patches = ax[1, 0].hist(dens_mol3, num_bins, density=True, 
                                 facecolor='#B22222', alpha=0.55)
y = norm.pdf(bins, mu, sigma)
ax[1, 0].plot(bins, y, '--', linewidth=1.5, color='black')
ax[1, 0].set_title('IC - DMSO', fontsize = 'large',
                   fontweight = 'bold')


# -------------------- Molecula 4 -------------------------------------
# Distribuição da Densidade Molecula 4
mu = np.average(dens_mol4)
sigma = np.std(dens_mol4)
num_bins = 60
n, bins, patches = ax[1, 1].hist(dens_mol4, num_bins, density=True, 
                                 facecolor='#ff0000', alpha=0.55)
y = norm.pdf(bins, mu, sigma)
ax[1, 1].plot(bins, y, '--', linewidth=1.5, color='black')
ax[1, 1].set_title('ID - DMSO', fontsize = 'large',
                   fontweight = 'bold')


fig.text(0.52,                                        # Ordena Posição x
         0.039,                                       # Ordena Posição y
         'Entalpia Conf. por Molécula (kcal/mol)',    # Texto A ser colocado
         ha='center',                                 # Alinha texto horizontalmente
         va='center',                                 # Alinha texto verticalmente
         fontsize = 'xx-large')



plt.savefig(
             'distribuicoes.png',
             dpi=300,
             orientation = 'portrait',
             transparent = True,
             format='png')
            
plt.plot()
plt.show()
