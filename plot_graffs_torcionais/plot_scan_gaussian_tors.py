import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set(style="ticks")
fig = plt.gcf()
fig.subplots_adjust(top=0.94,
                    bottom=0.14,
                    left=0.14,
                    right=0.925,
                    hspace=0.2,
                    wspace=0.2)

dados = np.loadtxt('dados.gaussian.txt')

angulos = dados[:, 0]
energia = dados[:, 1]

energia_absoluta = np.abs(energia)
max_energia = max(energia_absoluta)
nova_lista_energia = [max_energia - energia for energia in energia_absoluta]

plt.plot(angulos, nova_lista_energia, color='#3399ff', linewidth=2.5)
plt.xlim([-180, 180])
plt.xticks([-180,-120,-60,0,60,120,180])
plt.xlabel(r'$\phi$ $^\circ$ (Diedro)', fontsize=17)
plt.ylabel(r'Energia Total Ab initio (kcal/mol)', fontsize=15)
plt.savefig(
            'estimando_energia.png',
             dpi=300,
             orientation = 'portrait',
             transparent = True,
             format='png')
plt.show()
