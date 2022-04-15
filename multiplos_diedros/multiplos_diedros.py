from distutils.spawn import find_executable
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.use('Agg')
import numpy as np
import seaborn as sns


sns.set(style="ticks")
fig, ax = plt.subplots(figsize=(8., 5.5))

# Ajusta subplots.
fig.subplots_adjust(left = 0.110,
                    right = 0.80,  # Define as distâncias entre os extremos
                    bottom = 0.12,
                    top = 0.865,
                    hspace = 0.24, # Organiza espaçoes entre os subplots
                    wspace = 0.23) # Organiza espaçoes entre os subplots
                   

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


fig1 = ax.scatter(nmove, diedros1, s=6.2, color='#FF9999', label='4-6-1-13')
fig2 = ax.scatter(nmove, diedros2, s=6.2, color='#6666FF', label='5-4-6-2')
fig3 = ax.scatter(nmove, diedros3, s=6.2, color='#00CC66', label='5-4-6-1')
fig4 = ax.scatter(nmove, diedros4, s=6.2, color='#999900', label='11-3-4-6')

fig.legend(loc='upper right', shadow=False, fontsize='large', 
           bbox_to_anchor=(1.00, 0.88), frameon=False, ncol=1)
           
fig.text(0.46,                     # Ordena Posição x
         0.03,                     # Ordena Posição y
         'Ciclos Monte Carlo',     # Texto A ser colocado
          ha='center',             # Alinha texto horizontalmente
          va='center',             # Alinha texto verticalmente
          fontsize = 'xx-large')

fig.text(0.029,
         0.5,
         'Diedro ($\phi$)',
          ha='center',
          va='center',
          fontsize = 'xx-large',
          rotation='vertical')      # Rotaciona o nome do eixo

plt.savefig('diedros_plot1.png',
             dpi=300,
             orientation = 'portrait',
             transparent = True,
             format='png')

plt.savefig('diedros_plot2.pdf',
             dpi=300,
             orientation = 'portrait',
             transparent = True,
             format='pdf')             

#plt.show()
