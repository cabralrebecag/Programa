#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 12:27:58 2020

@author: rebecacabral
"""
from w_combinada import w
from w_combinada import incert_ext_w
from txt_to_csv import path_lda
from gráficos import perfil_velocidade
from perda_de_carga import perda_carga
from tensores_de_reynolds import tensores
#from Campo_Vetorial_15mm_v1 import campo_vetorial
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

path2 = ('/Users/rebecacabral/Documents/CDTN/PROGRAMA/INCERTEZA_EXT')
path3 = ('/Users/rebecacabral/Documents/CDTN/PROGRAMA/PERDA_DE_CARGA')
path4 = ('/Users/rebecacabral/Documents/CDTN/PROGRAMA/TENSORES_DE_REYNOLDS')

# b = w(path3)
# print (b)

a = path_lda(path3, path2)
print (a)

d = incert_ext_w(path3)
print (d)

c = perda_carga(path3)
print (c)

e = tensores(path4)
print (e)

f = perfil_velocidade(path2)
print (f)

a = list(a)
r = []
s = []
t = []
u = []

a1=np.array(a[1],dtype=float)
for i in range (len(a1)):
    r.append(a1[i][0])
r = np.array(r, dtype=float)
    
for i in range (len(a1)):
    s.append(a1[i][1])
s = np.array(s, dtype=float)

for i in range (len(a1)):
    t.append(a1[i][2])
t = np.array(t, dtype=float)
tt = np.divide(t,1.99)
ttt = np.divide(t,1.97)
    
for i in range (len(a1)):
    u.append(a1[i][3])
u = np.array(u, dtype=float)
uu = np.divide(u,1.99)
uuu = np.divide(u,1.97)


M_1 = np.hypot(tt,uu)   # Cria vetor de módulo de velocidade (cores)
plt.style.use('classic')
ax1=plt.subplot(1,1,1)
q1=ax1.quiver(s, r, ttt, -uuu, M_1, scale=8, width=0.004, clim=[0.0,0.20], cmap='inferno_r')

ax1.set_aspect(1)    # fixa uma relação entre os eixos de 1:1
plt.grid(True)
#plt.colorbar(q1)


cb1 = plt.colorbar(q1, ax=[ax1], pad=0.03, ticks=[0.0, 0.1, 0.20], anchor=(2.0, 0.4), shrink=0.85, label=(r'$\overline{ V } \ / \langle \overline{ w } \rangle$'))
cb1.ax.tick_params(labelsize=9)


plt.subplots_adjust(left=0.1, right=0.915, bottom=0.1, top=0.9, wspace=0.2, hspace=0.0)

plt.text(-0.2, 0.0, r'$y/p$', ha='center', va='center', rotation='vertical')
plt.text(1.0, -0.7, r'$x/p$', ha='center', va='center', rotation='horizontal')

ax1.annotate("$Aletada$", xy=(1,0.6), xycoords="data", va="center", ha="center", bbox=dict(boxstyle="round", fc="w"), size=20)
    
plt.savefig('/Users/rebecacabral/Documents/CDTN/Programa/Vetores15mm.png', format='png', dpi=800)

plt.show()




fig, (ax1,ax2)=plt.subplots(1,2, figsize=(12,7))
ax1.plot(f[0], np.divide(f[1],d[0][0]), 'ro', label = 'Teste 1')
ax1.plot(f[0], np.divide(f[2],d[0][0]), 'bo', label = 'Teste 2')
ax1.plot(f[0], np.divide(f[3],d[0][0]), 'go', label = 'Teste 3')
ax1.plot(f[0], np.divide(f[4],d[0][0]), 'mo', label = 'Teste 4')
ax1.plot(f[0], np.divide(f[5],d[0][0]), 'yo', label = 'Teste 5')
ax1.legend()
ax1.set_ylabel('$u/w$')
ax1.set_ylim(-0.1, 0.2)
ax1.set_xlabel('$x/passo$')
ax1.set_title('Perfil da velocidade $u$ no subcanal X' )
ax2.plot(f[0], np.divide(f[6],d[0][0]), 'ro', label = 'Teste 1')
ax2.plot(f[0], np.divide(f[7],d[0][0]), 'bo', label = 'Teste 2')
ax2.plot(f[0], np.divide(f[8],d[0][0]), 'go', label = 'Teste 3')
ax2.plot(f[0], np.divide(f[9],d[0][0]), 'mo', label = 'Teste 4')
ax2.plot(f[0], np.divide(f[10],d[0][0]), 'yo', label = 'Teste 5')
ax2.legend()
ax2.set_ylabel('$v/w$')
ax2.set_ylim(-0.1, 0.2)
ax2.set_xlabel('$x/passo$')
ax2.set_title('Perfil da velocidade $v$ no subcanal X' )
plt.savefig('/Users/rebecacabral/Documents/CDTN/Programa/Perfil_de_velocidade_U_e_V.png', format='png')
plt.show() 