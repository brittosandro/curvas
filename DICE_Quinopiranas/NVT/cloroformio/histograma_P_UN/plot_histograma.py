from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns



sns.set(style="ticks")

fig, ax = plt.subplots(2, 2, figsize=(7, 7))
fig.subplots_adjust(
                     left=0.120,
                     right=0.980,    # {Define as distâncias entre os extremos}
                     bottom=0.095,
                     top=0.855,
                     hspace=0.235,   # Organiza espaçoes entre os subplots
                     wspace=0.175)    # Organiza espaçoes entre os subplots
                    

dados = np.loadtxt('arq_dados_eq_out_NVT.dat')
#Cilclos monte carlo
nmove = dados[:, 0]
#Energia total por molécula
U_N = dados[:, 2]
#Energia de interação da molécula 1 com as demais
U_1 = dados[:, 3]
#Pressão
pressao = dados[:, 6]

# ------------------- Energis total ----------------------------------
# Evolução da Energia Total por molécula no NVT 
ax[0, 0].plot(nmove, U_N, '#0000ff', alpha=0.55)
ax[0, 0].tick_params(labelcolor='k', labelsize='small', width=1.0)
#ax[0, 0].set_ylim(-7.20, -6.50)
#ax[0, 0].set_yticks(np.arange(-7.20, -6.51, 0.2))
ax[0, 0].set_xlabel('NMOVE', )
ax[0, 0].set_ylabel('Energia Total por Molécula ($kcal/mol$)', )

# Dirtribuição da Energia toral
mu = np.average(U_N)
sigma = np.std(U_N)
num_bins = 60

n, bins, patches = ax[0, 1].hist(U_N, num_bins, density=True, 
                                 facecolor='blue', alpha=0.55)
y = norm.pdf(bins, mu, sigma)
ax[0, 1].plot(bins, y, '--', linewidth=1.5, color='#B22222')
#ax[0, 1].set_xlabel('Energia Total por Molécula $kcal/mol$', )
# -----------------------------------------------------------------------------

# -------------------- Pressao ----------------------------------------------
# Evolução da pressao 
ax[1, 0].plot(nmove, pressao, '#0000ff', alpha=0.55)
ax[1, 0].tick_params(labelcolor='k', labelsize='small', width=1.0)
ax[1, 0].set_xlabel('NMOVE', )
ax[1, 0].set_ylabel('Pressao (atm)',)

#Distribuição da Pressao
mu = np.average(pressao)
sigma = np.std(pressao)
num_bins = 60

n, bins, patches = ax[1, 1].hist(pressao, num_bins, density=True, facecolor='blue', alpha=0.55)
y = norm.pdf(bins, mu, sigma)
ax[1, 1].plot(bins, y, '--', linewidth=1.5, color='#B22222')
#ax[1, 1].set_xlabel('Pressao (atm)', )


fig.text(0.52,                           # Ordena Posição x
         0.91,                          # Ordena Posição y
         'IA - Clorofórmio $NVT$',      # Texto A ser colocado
         ha='center',                   # Alinha texto horizontalmente
         va='center',                   # Alinha texto verticalmente
         fontsize = 'xx-large')



plt.savefig(
             'distribuicoes.png',
             dpi=300,
             orientation = 'portrait',
             transparent = True,
             format='png')
            
'''
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
'''
plt.plot()
plt.show()
