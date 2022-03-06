import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np


with open("imdz.in.out") as f:
    arq_inf = f.read()

separador1 = '*' * 52
separador2 = 'NMOVE'
separador3 = 'Density'
separador4 = 'Averages'

cabecalho = arq_inf.split(separador1)[1]
string_dados = arq_inf.split(separador3)[2].split(separador4)[0]

with open('arq_dados.txt', 'w') as f:
    f.write(string_dados)

dados = np.loadtxt('arq_dados.txt')
NMOVE = dados[:, 0]
Hc_N = dados[:, 2]
density = dados[:, 4]


mu = np.average(Hc_N)
sigma = np.std(Hc_N)

#num_bins = 20
#y = (1/(np.sqrt(2*np.pi*sigma**2)))*np.exp((-1/2)*((Hc_N-mu)/sigma)**2)

num_bins=60
fig, ax = plt.subplots()

n, bins, patches = ax.hist(Hc_N, num_bins, density=True, facecolor='blue', alpha=0.55)
y = norm.pdf(bins,mu,sigma)

ax.plot(bins, y, '--', linewidth=1, color='red')
ax.set_xlabel('Entalpia de Conformacao por Molecula')
ax.set_ylabel('Probabilidade')
ax.set_title('$\mu={}, \sigma={}$'.format(mu, sigma))
fig.tight_layout()
plt.show()

#y = mlab.normpdf(bins, mu, sigma)
#plt.plot(bins, y, 'r--')


#plt.hist(Hc_N, bins=y)
#plt.plot(NMOVE, density)
#plt.plot(NMOVE, Hc_N)
#plt.show()
