import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#plt.style.use('fivethirtyeight')
sns.set(style="ticks")
fig, ax = plt.subplots(figsize=(8, 6))
#handles, labels = ax.get_legend_handles_labels()


# Ajusta subplots.
fig.subplots_adjust(
                      left = 0.12,
                      right = 0.90,    # {Define as distâncias entre os extremos}
                      bottom = 0.12,
                      top = 0.93,
                      hspace = 0.24,   # Organiza espaçoes entre os subplots
                      wspace = 0.23    # Organiza espaçoes entre os subplots
                   )


dados_experimentais = np.loadtxt('experimental.txt')
x_exp = dados_experimentais[:, 0]
y_exp = dados_experimentais[:, 1]

dados_M06L = np.loadtxt('M06L.txt')
x_M06L = dados_M06L[:, 0]
y_M06L = dados_M06L[:, 1]

dados_M06 = np.loadtxt('M06.txt')
x_M06 = dados_M06[:, 0]
y_M06 = dados_M06[:, 1]

dados_M06HF = np.loadtxt('M06HF.txt')
x_M06HF = dados_M06HF[:, 0]
y_M06HF = dados_M06HF[:, 1]

dados_M062X = np.loadtxt('M062X.txt')
x_M062X = dados_M062X[:, 0]
y_M062X = dados_M062X[:, 1]

# Construindo segundo eixo
ax_M06L = ax.twinx()
ax_M06 = ax.twinx()
ax_M062X = ax.twinx()
ax_M06HF = ax.twinx()

fig1 = ax_M06L.vlines(x_M06L, 0, y_M06L, color='#FF9999', linewidth=2, label="M06L (0% ${E_{x}^{HF}}$)")
ax_M06L.yaxis.set_visible(False)

fig2 = ax_M06.vlines(x_M06, 0, y_M06, color='#6666FF', linewidth=2, label="M06 (27% ${E_{x}^{HF}}$)")
ax_M06.yaxis.set_visible(False)

fig3 = ax_M062X.vlines(x_M062X, 0, y_M062X, color='#00CC66', linewidth=2, label="M06-2X (54% ${E_{x}^{HF}}$)")
ax_M062X.yaxis.set_visible(False)

fig4 = ax_M06HF.vlines(x_M06HF, 0, y_M06HF, color='#999900', linewidth=2, label="M06HF (100% ${E_{x}^{HF}}$)")

fig5 = ax.plot(x_exp, y_exp, color='k', linewidth=2, label='Experimental')
fig.legend(loc='upper right', shadow=False, fontsize='large', bbox_to_anchor=(0.92, 0.93), frameon=False)
#plt.legend(handles=([fig1, fig2, fig3, fig4]), loc='upper right', shadow=False, fontsize='large')
plt.grid(False)


# Descritores dos eixos
fig.text(
          0.98,                      # Ordena posição x
          0.5,                     # Ordena posição y
          'Osc. Strength',
          ha = 'center',
          va = 'center',
          fontsize = 'xx-large',
          rotation = 'vertical'
        )

fig.text(
          0.5,                      # Ordena posição x
          0.04,                     # Ordena posição y
          'Wavelength (nm)',
          ha = 'center',
          va = 'center',
          fontsize = 'xx-large'
        )

fig.text(
          0.03,
          0.5,
          'Absorbance (AU)',
          ha = 'center',
          va = 'center',
          fontsize = 'xx-large',
          rotation = 'vertical'
        )

plt.savefig(
             'fig_Daniel5.png',
             dpi=300,
             orientation = 'portrait',
             transparent = True,
             format='png'
            )

plt.show()
