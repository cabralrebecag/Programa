

    
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from INCERTEZA_EXT.txt_to_csv import path_lda
    

    #d1 = path_lda.result

d1=pd.read_csv('/Users/rebecacabral/Documents/CDTN/INCERTEZA_EXT/Final',sep=',',header=None, skiprows=[0])

#Campo Vetorial de Velocidades
#def campo_vetorial(path,path2):
#d1 = path_lda(path,path2)
M_1 = np.hypot(d1[3]/1.99, d1[4]/1.99)   # Cria vetor de módulo de velocidade (cores)
plt.style.use('classic')
ax1=plt.subplot(1,1,1)
q1=ax1.quiver(d1[2],d1[1],d1[3]/1.97,-d1[4]/1.97,M_1, scale=8, width=0.004, clim=[0.0,0.20], cmap='inferno_r')

ax1.set_aspect(1)    # fixa uma relação entre os eixos de 1:1
plt.grid(True)
#plt.colorbar(q1)


cb1 = plt.colorbar(q1, ax=[ax1], pad=0.03, ticks=[0.0, 0.1, 0.20], anchor=(2.0, 0.4), shrink=0.85, label=(r'$\overline{ V } \ / \langle \overline{ w } \rangle$'))
cb1.ax.tick_params(labelsize=9)


plt.subplots_adjust(left=0.1, right=0.915, bottom=0.1, top=0.9, wspace=0.2, hspace=0.0)

plt.text(-0.2, 0.0, r'$y/p$', ha='center', va='center', rotation='vertical')
plt.text(1.0, -0.7, r'$x/p$', ha='center', va='center', rotation='horizontal')

ax1.annotate("$Aletada$", xy=(1,0.6), xycoords="data", va="center", ha="center", bbox=dict(boxstyle="round", fc="w"), size=20)
    
plt.savefig('/Users/rebecacabral/Documents/CDTN/INCERTEZA_EXT/Vetores15mm.png', format='png', dpi=800)

plt.show()
    
#    return plt

