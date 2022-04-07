import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import seaborn as sns

dados = np.loadtxt('IA_DMSO_EQ_Hc_nmove.dat', comments='#')
x = dados[:, 0]
y = dados[:, 1]

dados1 = np.loadtxt('IB_DMSO_EQ_Hc_nmove.dat', comments='#')
x1 = dados1[:, 0]
y1 = dados1[:, 1]

dados2 = np.loadtxt('IC_DMSO_EQ_Hc_nmove.dat', comments='#')
x2 = dados2[:, 0]
y2 = dados2[:, 1]

dados3 = np.loadtxt('ID_DMSO_EQ_Hc_nmove.dat', comments='#')
x3 = dados3[:, 0]
y3 = dados3[:, 1]

sns.set(style="ticks")

fig, ax = plt.subplots(2, 2, figsize=(8.9, 7.6))

fig.subplots_adjust(left=0.110,
                    right=0.965,   # {Define as distâncias entre os extremos}
                    bottom=0.110,
                    top=0.895,
                    hspace=0.245,  # Organiza espaçoes entre os subplots
                    wspace=0.1855)  # Organiza espaçoes entre os subplots


# ------------------- Subplot IA --------------------------------------
ax[0, 0].plot(x, y, '#0000ff', lw=2.5)
ax[0, 0].tick_params(labelcolor='k', labelsize='small', width=1.1)
ax[0, 0].set_xlim(0, 60000)
ax[0, 0].set_ylim(-12.5, -11.4)
ax[0, 0].set_yticks(np.arange(-12.5, -11.21, 0.3))
ax[0, 0].set_title('IA - DMSO', fontsize = 'large',
                   fontweight = 'bold')

# ------------------- Subplot IB --------------------------------------
ax[0, 1].plot(x1, y1, '#008080', lw=2.5)
ax[0, 1].tick_params(labelcolor='k', labelsize='small', width=1.1)
ax[0, 1].set_xlim(0, 60000)
ax[0, 1].set_ylim(-12.5, -11.4)
ax[0, 1].set_yticks(np.arange(-12.5, -11.21, 0.3))
ax[0, 1].set_title('IB - DMSO', fontsize = 'large',
                   fontweight = 'bold')

# ------------------- Subplot IC --------------------------------------
ax[1, 0].plot(x2, y2, '#B22222', lw=2.5)
ax[1, 0].tick_params(labelcolor='k', labelsize='small', width=1.1)
ax[1, 0].set_xlim(0, 60000)
ax[1, 0].set_ylim(-12.5, -11.4)
ax[1, 0].set_yticks(np.arange(-12.5, -11.21, 0.3))
ax[1, 0].set_title('IC - DMSO', fontsize = 'large', fontweight = 'bold')

# ------------------- Subplot ID --------------------------------------
ax[1, 1].plot(x3, y3, '#ff0000', lw=2.5)
ax[1, 1].tick_params(labelcolor='k', labelsize='small', width=1.1)
ax[1, 1].set_xlim(0, 60000)
ax[1, 1].set_ylim(-12.5, -11.4)
ax[1, 1].set_yticks(np.arange(-12.5, -11.21, 0.3))
ax[1, 1].set_title('ID - DMSO', fontsize = 'large', fontweight = 'bold')

fig.text(0.5,                     # Ordena Posição x
         0.96,                    # Ordena Posição y
         'ENSEMBLE $NPT$',      # Texto A ser colocado
          ha='center',            # Alinha texto horizontalmente
          va='center',            # Alinha texto verticalmente
          fontsize = 'xx-large')


fig.text(0.5,                      # Ordena Posição x
         0.03,                     # Ordena Posição y
         'Ciclos Monte Carlo',     # Texto A ser colocado
          ha='center',             # Alinha texto horizontalmente
          va='center',             # Alinha texto verticalmente
          fontsize = 'xx-large')

fig.text(0.029,
         0.5,
         'H$_{c}$/N (g/cm³)',
          ha='center',
          va='center',
          fontsize = 'xx-large',
          rotation='vertical')      # Rotaciona o nome do eixo



plt.savefig('d_nmove_NpT.png', dpi=300, orientation='portrait', transparent=True, format='png')
plt.show()
