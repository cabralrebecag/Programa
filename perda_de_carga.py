#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 08:00:46 2020
@author: rebecacabral
"""

import numpy as np
import csv
#dados de entrada
H=76.2  #em mm
D=10.75  #em mm
At=H**2-25*((np.pi*D**2)/4)
P=(4*H)+(25*np.pi*D)
Dh=(4*At)/P
ed=0.000001  #rugosidade relativa
g=9,807
Incerteza_Dh=np.sqrt((((((((4*H)+(25*np.pi*D))*8*H)-((4*(H**2))-25*np.pi*(D**2))*4)/(((4*H)+(25*np.pi*D))**2))*H)**2)+((((((4*H)+25*np.pi*D)*50*np.pi*D)-(((4*(H**2))-(25*np.pi*(D**2)))*25*np.pi))/(((4*H)+(25*np.pi*D))**2))*D)**2)


from os import listdir
from os.path import isfile, join
import statistics

def perda_carga(save_path):
#codigo pra ler os arquivos e organiza-los em listas
    onlyfiles = [f for f in listdir(save_path) if isfile(join(save_path, f))]    
    lista=[]
    p=[]
    re=[]
    ro=[]
    vis=[]  
    for aux in range (len(onlyfiles)):   
        with open(save_path + "/" + onlyfiles[aux], newline='') as csvfile:      
            spamreader = csv.reader(csvfile) 
            for linha in spamreader:
                aux1=str(linha[0]).split()
                lista.append(aux1)               
            for i in lista:
                p.append(i[23])       
    p=np.array(p,dtype=float)
    
#contas média da perda de carga
    
    media_p=(sum(p)/len(p))*100  #em pascal
    
    std_media_p=statistics.stdev(p)   #em mbar
    print("DP = " +str(media_p) + " +/- " + str(std_media_p))
 
#contas média da densidade
    
    for i in lista:
        ro.append(i[9])
        
    ro=np.array(ro,dtype=float)    
    media_ro=(sum(ro)/len(ro))
    
#contas média viscosidade
    
    for i in lista:
        vis.append(i[11])
        
    vis=np.array(vis,dtype=float)    
    media_vis=(sum(vis)/len(vis))/1000

#contas média reynolds
    
    for i in lista:
        re.append(i[19])
        
    re=np.array(re,dtype=float)    
    media_re=(sum(re)/len(re))
    
    v=(media_re*media_vis)/media_ro*Dh
    
#colebrook
    
    fi=1
    f=fi
    r=1
    i=0
    while r>(10**(-4)):
        fv=f
        f=(-2*np.log((ed/3.7)+(2.51/media_re*fv**0.5)))**(-2)
        r=abs(f-fv)
        print("f = " + str(f))
        print("r = " + str(r))    
        i=i+1
        if i==2: 
            print("deu i max")
            break

#altura manométrica        
    hl = f*H*v**2/Dh*2
    
# calculo de perda localizada
    
    k = 2*hl/v**2
    k = ("k = " +str(k))
        
    return (("HL = "+ str(hl)), k)
