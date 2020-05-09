#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 08:01:25 2020

@author: rebecacabral
"""

import csv
import pandas as pd
import numpy as np
from os import listdir
from os.path import isfile, join

# def path_pd(path1):
#     save_path = path1
#     return save_path 

 #   save_path = r'/Users/rebecacabral/Documents/CDTN/TENSORES_DE_REYNOLDS'
def tensores(save_path):  
    onlyfiles = [f for f in listdir(save_path) if isfile(join(save_path, f))]
    
    linha = []
    lista= []
    
    for aux in range (0,len(onlyfiles)):    #delimitar a range de acordo com o numero dos testes analisados
        with open(save_path + '/' + onlyfiles[aux], encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile) 
            for linha in spamreader:
                aux1=str(linha[0]).split('\t')
                lista.append(aux1)
    
    u=[]
    v=[]
    Vx=[]
    Vy=[]
    VxVx=[]
    VyVy=[]
    VxVy=[]
    VxVxrms=[]
    VyVyrms=[]
    VxVyrms=[]
    
    for i in lista:
        u.append(i[3])
        v.append(i[4])   
        
    u=np.array(u,dtype=float)
    v=np.array(v,dtype=float)
        
    #umean=sum(u)/len(u)
    
    u_prime = (u - (sum(u)/len(u)))
    v_prime = (v - (sum(v)/len(v)))
    umod_prime = np.absolute(u - u.mean())
    vmod_prime = np.absolute(v - v.mean())
    uv = (u_prime) * (v_prime)
    uu = (u_prime) * (u_prime)
    vv = (v_prime) * (v_prime)
        
    uvmod = umod_prime*vmod_prime
        
        
    Vx.append(u_prime.mean())
    Vy.append(v_prime.mean())
    VxVy.append(uv.mean())
    VxVx.append((u_prime*u_prime).mean())
    VyVy.append((v_prime*v_prime).mean())
    VxVxrms.append(uu.mean()**0.5)
    VyVyrms.append(vv.mean()**0.5)
    VxVyrms.append(uvmod.mean()**0.5)
        
    das = {'u':Vx,'v':Vy,'uu':VxVx, 'vv':VyVy,'uv':VxVy,'uu_rms':VxVxrms, 'vv_rms':VyVyrms,'uv_rms':VxVyrms}
    resultado = pd.DataFrame(data=das)
    return resultado
#pd.DataFrame(resultado).to_csv("30mm_sub2_topo_t01TR.csv", sep='\t')