from scipy.stats import norm
from distutils.spawn import find_executable
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.use('Agg')
import numpy as np
import seaborn as sns


sns.set(style="ticks")

fig, ax = plt.subplots()
fig.subplots_adjust( left=0.115,
                     right=0.965,    # {Define as distâncias entre os extremos}
                     bottom=0.145,
                     top=0.945,
                     hspace=0.265,    # Organiza espaçoes entre os subplots
                     wspace=0.175)    # Organiza espaçoes entre os subplots

diedros1 = np.loadtxt('died_4-6-1-13.dat')
diedros2 = np.loadtxt('died_5-4-6-1.dat')
diedros3 = np.loadtxt('died_5-4-6-2.dat')
diedros4 = np.loadtxt('died_11-3-4-6.dat')

# intervalo de passos em que salvamos os ciclos monte carlo
stepmult = 50
nmove = [diedro*stepmult for diedro in range(1, len(diedros1)+1)]

if find_executable('latex') and find_executable('dvipng'):
    mpl.rcParams.update({'font.size':14, 'text.usetex':True, 
                         'font.family':'serif', 'ytick.major.pad':4})
else:
    mpl.rcParams.update({'font.size':14, 'font.family':'serif', 
                          'ytick.major.pad':4})


# ------------------- Molecula 1 --------------------------------------
# Distribuição da Molecula 1
mu = np.average(diedros1)
sigma = np.std(diedros1)
num_bins = 60
n, bins, patches = ax.hist(diedros1, num_bins, density=True, 
                                 facecolor='#FF9999', alpha=0.55, label='4-6-1-13')
y = norm.pdf(bins, mu, sigma)
fig1 = ax.plot(bins, y, '--', linewidth=1.5, color='black')
#ax[0, 0].set_title('IA - DMSO', fontsize = 'large',fontweight = 'bold')


# -------------------- Molecula 2 -------------------------------------
# Distribuição da Molecula 2
mu = np.average(diedros2)
sigma = np.std(diedros2)
num_bins = 60
n, bins, patches = ax.hist(diedros2, num_bins, density=True, 
                                 facecolor='#6666FF', alpha=0.55, label='5-4-6-2')
y = norm.pdf(bins, mu, sigma)
fig2 = ax.plot(bins, y, '--', linewidth=1.5, color='black')


# -------------------- Molecula 3 -------------------------------------
# Distribuição da Molecula 3
mu = np.average(diedros3)
sigma = np.std(diedros3)
num_bins = 60
n, bins, patches = ax.hist(diedros3, num_bins, density=True, 
                                 facecolor='#00CC66', alpha=0.55, label='5-4-6-1')
y = norm.pdf(bins, mu, sigma)
fig3 = ax.plot(bins, y, '--', linewidth=1.5, color='black')


# -------------------- Molecula 4 -------------------------------------
# Distribuição da Molecula 4
mu = np.average(diedros4)
sigma = np.std(diedros4)
num_bins = 60
n, bins, patches = ax.hist(diedros4, num_bins, density=True, 
                                 facecolor='#999900', alpha=0.55, label='11-3-4-6')
y = norm.pdf(bins, mu, sigma)
fig4 = ax.plot(bins, y, '--', linewidth=1.5, color='black')

fig.legend(loc='upper right', shadow=False, fontsize='small', 
           bbox_to_anchor=(0.95, 1.01), frameon=False, ncol=4)

fig.text(0.52,                 # Ordena Posição x
         0.039,                # Ordena Posição y
         'Diedro ($\phi$)',    # Texto A ser colocado
         ha='center',          # Alinha texto horizontalmente
         va='center',          # Alinha texto verticalmente
         fontsize = 'xx-large')



plt.savefig(
             'distribuicoes_diedro1.png',
             dpi=300,
             orientation = 'portrait',
             transparent = True,
             format='png')

plt.savefig('distribuicoes_diedro2.pdf',
             dpi=300,
             orientation = 'portrait',
             transparent = True,
             format='pdf')              
            
#plt.plot()
#plt.show()

