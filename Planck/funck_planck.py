import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as sc
import seaborn as sns

#plt.style.use('fivethirtyeight')
sns.set(style="ticks")
fig, ax = plt.subplots(figsize=(8, 6))

# Ajusta subplots.
fig.subplots_adjust(
                      left = 0.12,
                      right = 0.90,    # {Define as distâncias entre os extremos}
                      bottom = 0.12,
                      top = 0.93,
                      hspace = 0.24,   # Organiza espaçoes entre os subplots
                      wspace = 0.23    # Organiza espaçoes entre os subplots
                   )


def func_planck(nu, T):
    a = (2 * sc.h * nu ** 3)/(sc.c ** 2)
    b = (sc.h * nu) / (sc.k * T)
    return a * (1/(np.exp(b) - 1))


ini_freq = 0.01*10**14
fim_freq = 0.96*10**15
nu = np.linspace(ini_freq, fim_freq, 150)
T1 = 3000
T2 = 3500
T3 = 4000

fig1 = ax.plot(nu, func_planck(nu, T1), color='k', linewidth=2.8, label='3000K')
fig2 = ax.plot(nu, func_planck(nu, T2), color='r', linewidth=2.8, label='3500K')
fig3 = ax.plot(nu, func_planck(nu, T3), color='g', linewidth=2.8, label='4000K')
fig.legend(loc='upper right', shadow=False, fontsize='large', bbox_to_anchor=(0.88, 0.88), frameon=False)
plt.grid(False)


# Descritores dos eixos
fig.text(
          0.04,                      # Ordena posição x
          0.5,                       # Ordena posição y
          r'$I_\nu (W \cdot m^{-2} \cdot Hz^{-1})$',
          ha = 'center',
          va = 'center',
          fontsize = 'xx-large',
          rotation = 'vertical'
        )

fig.text(
          0.5,                      # Ordena posição x
          0.03,                     # Ordena posição y
          r'$\nu (Hz)$',
          ha = 'center',
          va = 'center',
          fontsize = 'xx-large'
        )

plt.savefig(
             'planck_fig.png',
             dpi=300,
             orientation = 'portrait',
             transparent = True,
             format='png'
            )

plt.show()
