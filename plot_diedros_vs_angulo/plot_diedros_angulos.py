import matplotlib.pyplot as plt
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

with open('diedros.dat') as f:
    diedros = f.readlines()

d = [float(diedro.replace('\n', '')) for diedro in diedros]

with open('dipolo.dat') as f:
    dipolos = f.readlines()

dip = [float(dipolo.replace('\n', '')) for dipolo in dipolos]

fig1 = ax.scatter(d, dip, s=2)
#plt.xlabel(r"$\phi$ $^\circ$")
#plt.ylabel(r"$\mu$")
plt.xticks([-180,-120,-60,0,60,120,180])

# Descritores dos eixos
fig.text(
          0.04,                      # Ordena posição x
          0.5,                       # Ordena posição y
          r'$\mu$ (Debye)',
          ha = 'center',
          va = 'center',
          fontsize = 'xx-large',
          rotation = 'vertical'
        )

fig.text(
          0.5,                      # Ordena posição x
          0.03,                     # Ordena posição y
          r'$\phi$ $^\circ$ (Dihedral)',
          ha = 'center',
          va = 'center',
          fontsize = 'xx-large'
        )

plt.savefig(
             'dipole_dihedral.png',
             dpi=300,
             orientation = 'portrait',
             transparent = True,
             format='png'
            )

plt.show()
