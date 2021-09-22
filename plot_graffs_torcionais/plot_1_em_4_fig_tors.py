import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="ticks")


if __name__ == '__main__':

    dados = np.loadtxt('tors_7-4-1-8.out', comments='#')
    angulos = dados[:,0]
    energia_total = dados[:,1]
    energia_torcional = dados[:,2]
    energia_nao_ligada = dados[:,3]
    momento_de_dipolo = dados[:,4]

    plt.plot(angulos, energia_total, color='#3399ff', linewidth=2.5)
    plt.xlim([-180, 180])
    plt.xticks([-180,-120,-60,0,60,120,180])
    plt.xlabel(r'$\phi$ $^\circ$ (Diedro)', fontsize=15)
    plt.ylabel(r'Energia Total (kcal/mol)', fontsize=15)
    plt.savefig(
             'energia_total.png',
             dpi=300,
             orientation = 'portrait',
             transparent = True,
             format='png')
    plt.gcf().clear()

    plt.plot(angulos, energia_torcional, color='#3399ff', linewidth=2.5)
    plt.xlim([-180, 180])
    plt.xticks([-180,-120,-60,0,60,120,180])
    plt.xlabel(r'$\phi$ $^\circ$ (Diedro)', fontsize=15)
    plt.ylabel(r'Energia Torcional Diedral (kcal/mol)', fontsize=15)
    plt.savefig(
             'energia_torcional.png',
             dpi=300,
             orientation = 'portrait',
             transparent = True,
             format='png')
    plt.gcf().clear()

    plt.plot(angulos, energia_nao_ligada, color='#3399ff', linewidth=2.5)
    plt.xlim([-180, 180])
    plt.xticks([-180,-120,-60,0,60,120,180])
    plt.xlabel(r'$\phi$ $^\circ$ (Diedro)', fontsize=15)
    plt.ylabel(r'Energia Não Ligada (kcal/mol)', fontsize=15)
    plt.savefig(
             'energia_nao_ligada.png',
             dpi=300,
             orientation = 'portrait',
             transparent = True,
             format='png')
    plt.gcf().clear()

    plt.plot(angulos, momento_de_dipolo, color='#3399ff', linewidth=2.5)
    plt.xlim([-180, 180])
    plt.xticks([-180,-120,-60,0,60,120,180])
    plt.xlabel(r'$\phi$ $^\circ$ (Diedro)', fontsize=15)
    plt.ylabel(r'Momento de Dipolo (kcal/mol)', fontsize=15)
    plt.savefig(
             'momento_de_dipolo.png',
             dpi=300,
             orientation = 'portrait',
             transparent = True,
             format='png')
    plt.gcf().clear()
