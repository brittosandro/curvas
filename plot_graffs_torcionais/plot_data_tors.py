import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def todas_curvas_juntas(angulos, energia_total, energia_torcional, energia_nao_ligada, momento_de_dipolo):
    sns.set(style="ticks")
    fig, ax = plt.subplots(2, 2, figsize=(7.2, 6.2))
    fig.subplots_adjust(
                          left=0.085,
                          right=0.98,    # {Define as distâncias entre os extremos}
                          bottom=0.12,
                          top=0.97,
                          hspace=0.165,   # Organiza espaçoes entre os subplots
                          wspace=0.280)    # Organiza espaçoes entre os subplots

    # Energia Total em função do ângulo
    ax[0, 0].plot(angulos, energia_total, 'blue', alpha=0.55)
    ax[0, 0].set_xticks([-180,-120,-60,0,60,120,180])
    ax[0, 0].tick_params(labelcolor='k', labelsize='small', width=1.0)
    #ax[0, 0].set_xlabel(r'$\phi$ $^\circ$ (Dihedral)', )
    ax[0, 0].set_ylabel('Energia Potencial (kcal/mol)', )

    # Energia Torcional diedral em função do ângulo
    ax[0, 1].plot(angulos, energia_torcional, 'blue', alpha=0.55)
    ax[0, 1].set_xticks([-180,-120,-60,0,60,120,180])
    ax[0, 1].tick_params(labelcolor='k', labelsize='small', width=1.0)
    #ax[0, 1].set_xlabel(r'$\phi$ $^\circ$ (Dihedral)', )
    ax[0, 1].set_ylabel('Energia Total Diedral (kcal/mol)',)

    # Energia NÃO ligada em função do ângulo
    ax[1, 0].plot(angulos, energia_nao_ligada, 'blue', alpha=0.55)
    ax[1, 0].set_xticks([-180,-120,-60,0,60,120,180])
    ax[1, 0].tick_params(labelcolor='k', labelsize='small', width=1.0)
    #ax[1, 0].set_xlabel(r'$\phi$ $^\circ$ (Dihedral)', )
    ax[1, 0].set_ylabel('Energia Não-Ligada (kcal/mol)',)

    # Momento de Dipolo em função do ângulo
    ax[1, 1].plot(angulos, momento_de_dipolo, 'blue', alpha=0.55)
    ax[1, 1].set_xticks([-180,-120,-60,0,60,120,180])
    ax[1, 1].tick_params(labelcolor='k', labelsize='small', width=1.0)
    #ax[1, 1].set_xlabel(r'$\phi$ $^\circ$ (Dihedral)', )
    ax[1, 1].set_ylabel(r'$\mu$ (Debye)',)

    fig.text(
          0.5,                      # Ordena posição x
          0.03,                     # Ordena posição y
          r'$\phi$ $^\circ$ (Diedro)',
          ha = 'center',
          va = 'center',
          fontsize = 'x-large')

    plt.savefig(
             'figura.png',
             dpi=300,
             orientation = 'portrait',
             transparent = True,
             format='png')

    plt.show()

def energia_total(angulos, energia_total):
    sns.set(style="ticks")
    fig, ax = plt.subplots(figsize=(8, 6))

    # Ajusta subplots.
    fig.subplots_adjust(
                      left = 0.12,
                      right = 0.90,    # {Define as distâncias entre os extremos}
                      bottom = 0.12,
                      top = 0.93,
                      hspace = 0.24,   # Organiza espaçoes entre os subplots
                      wspace = 0.23)    # Organiza espaçoes entre os subplots

    fig1 = ax.plot(angulos, energia_total, color='k', linewidth=2)

    plt.show()


if __name__ == '__main__':

    dados = np.loadtxt('tors_7-4-1-8.out', comments='#')
    angulos = dados[:,0]
    energia_total = dados[:,1]
    energia_torcional = dados[:,2]
    energia_nao_ligada = dados[:,3]
    momento_de_dipolo = dados[:,4]

    todas_curvas_juntas(angulos, energia_total, energia_torcional, energia_nao_ligada, momento_de_dipolo)
