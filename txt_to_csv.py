#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 08:03:37 2020

@author: rebecacabral
"""

import pandas as pd
import numpy as np
from os import listdir
from os.path import isfile, join

# df = pd.read_fwf('15mm_campo_topo_t01.txt')
# df.to_csv('15mm_campo_topo_t01.csv')
# df = pd.read_fwf('15mm_campo_topo_t02.txt')
# df.to_csv('15mm_campo_topo_t02.csv')
# df = pd.read_fwf('15mm_campo_topo_t03.txt')
# df.to_csv('15mm_campo_topo_t03.csv')
# df = pd.read_fwf('15mm_campo_topo_t04.txt')
# df.to_csv('15mm_campo_topo_t04.csv')
# df = pd.read_fwf('15mm_campo_topo_t05.txt')
# df.to_csv('15mm_campo_topo_t05.csv')

import glob
from w_combinada import w


def path_lda(path3,path):
#lendo os asquivos e organizando os dados importantes em um dataframe (frame)
    W = w(path3)
    
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    aux= []
    for aux in range(len(onlyfiles)):
        for files in onlyfiles:
            df = pd.read_fwf(path + '/' + onlyfiles[aux])
            df.to_csv(path + '/' + onlyfiles[aux] + '.csv')
                
    all_files= [f for f in listdir(path) if isfile(join(path, f))]
    files = []
    for i in range(len(all_files)):
        if all_files[i][-1] == 'v':
            files.append(all_files[i])
           
    li = []
    for filename in files:
        df = pd.read_csv(path + "/" + filename, skiprows=6, index_col=None, header=0, delim_whitespace=True)
        li.append(df)
        fr = pd.concat(li, axis=1, ignore_index=True)
    
    frame=fr.iloc[:,[0,1,2,8,9,25,26,42,43,59,60,76,77]] 
    
#filtrando os valores de velocidade
    R1=frame.filter([8,25,42,59,76], axis=1)
    R2=frame.filter([9,26,43,60,77], axis=1)

#média das velocidade em cada posição
    Mean1=R1.mean(axis=1)
    Mean2=R2.mean(axis=1)

#dados de entrada
    DLDA1=0.03902   #Em metros
    DLDA2=0.03878   #Em metros
    LâmbidaLDA1=0.000000561   #Em metros
    LâmbidaLDA2=0.000000532   #Em metros
    Dfocal=0.1596   #Em metros
    Incerteza_D=0.00002   #Em metros
    Incerteza_f=0.00002   #Em metros
    Hz=852190.7893
    TB1=0.007557497351   #Em radianos

#constanes angulares 
    gama1=np.arctan((DLDA1/2)/Dfocal)
    gama2=np.arctan((DLDA2/2)/Dfocal)

    CTE1=(LâmbidaLDA1/(2*np.sin(gama1)))  #aproximação diferente
    CTE2=(LâmbidaLDA2/(2*np.sin(gama2)))  #aproximação diferente

#media das velocidades(frequencia)
    Mean1F=(Mean1/CTE1)
    Mean2F=(Mean2/CTE2)

#desvio padra das velocidades em m/s e em "frequencia""
    STD1=((R1.std(axis=1))/np.sqrt(2))
    STD2=((R2.std(axis=1))/np.sqrt(2))

    STD1F=STD1/CTE1
    STD2F=STD2/CTE2
#parametros angulares
    Incerteza_ângulo1=np.sqrt(((Dfocal*2*Incerteza_D)/((4*(Dfocal)**2)+((DLDA1)**2)))**2+((-2*DLDA1*Incerteza_f)/((4*(Dfocal)**2)+(DLDA1**2)))**2)
    Incerteza_ângulo2=np.sqrt(((Dfocal*2*Incerteza_D)/((4*(Dfocal)**2)+((DLDA2)**2)))**2+((-2*DLDA2*Incerteza_f)/((4*(Dfocal)**2)+(DLDA2**2)))**2)

    Componente_ângulo1=(-np.cos(gama1)*Mean1*Incerteza_ângulo1/(2*np.sin(gama1)))
    Componente_ângulo2=(-np.cos(gama2)*Mean2*Incerteza_ângulo2/(2*np.sin(gama2)))

#um parametro da teoria do angulo de euler
    Tait_Bryan1=(((np.cos(TB1)**2)-((np.sin(TB1)**3)))-1)*Mean1F-(np.cos(TB1)*np.sin(TB1))*Mean2F+((np.cos(TB1)*np.sin(TB1))+(np.cos(TB1)*np.sin(TB1)**2))*Hz
    Tait_Bryan2=((np.cos(TB1)*np.sin(TB1))+(np.cos(TB1)*np.sin(TB1)**2))*Mean1F+((np.cos(TB1)**2)-1)*Mean2F+((np.sin(TB1)**2)-((np.cos(TB1)**2)*(np.sin(TB1))))*Hz

#incerteza da frequencia do laser e seu componente na incerteza
    Incerteza_Freq1=np.sqrt((STD1F)**2+(Tait_Bryan1)**2)
    Incerteza_Freq2=np.sqrt((STD2F)**2+(Tait_Bryan2)**2)

    Componente_Freq1=((LâmbidaLDA1)*Incerteza_Freq1)/(2*np.sin(gama1))
    Componente_Freq2=((LâmbidaLDA2)*Incerteza_Freq2)/(2*np.sin(gama2))

#incerteza extendida e normalizada
    Incerteza_Extendida1=2*(np.sqrt((Componente_ângulo1)**2+(Componente_Freq1)**2))
    Incerteza_Extendida2=2*(np.sqrt((Componente_ângulo2)**2+(Componente_Freq2)**2))

    Inc_Ext_Norm1=(((Incerteza_Extendida1/2)/(W))**2+((Mean1*W)/(W)**2)**2)**0.5
    Inc_Ext_Norm2=(((Incerteza_Extendida2/2)/(W))**2+((Mean2*W)/(W)**2)**2)**0.5

#componentes du, dv e dw  pra calcular a incerteza do vetor velocidade
    du=(Mean1/(W**2))*((Mean1/W)**2+(Mean2/W)**2)**0.5
    dv=(Mean2/(W**2))*((Mean1/W)**2+(Mean2/W)**2)**0.5
    dw=(((Mean1)**2+(Mean2)**2)/(W**3))*((Mean1/W)**2+(Mean2/W)**2)**0.5
    incerteza_v=2*((du*Incerteza_Extendida1/2)**2+(dv*Incerteza_Extendida2/2)**2+(dw*W)**2)**0.5

#calculo do fluxo secundário
    v_lateral=abs(np.sqrt(Mean1**2+Mean2**2))
    v_lateral_med=np.mean(v_lateral)
    sf=v_lateral_med/W
    sf=str(sf)

#organizando os resultados em um dataframe
    Result = ([frame.iloc[:,[1]], frame.iloc[:,[2]], Mean1, Mean2, Incerteza_Extendida1, Incerteza_Extendida2, Inc_Ext_Norm1, Inc_Ext_Norm2, du, dv, dw, incerteza_v ])
    Result_con= pd.concat(Result, axis=1, ignore_index=True)
    result = pd.DataFrame(Result_con.values, columns = ['X[mm]','Y[mm]','MédiaU','MédiaV','IncertezaExtendidaU','IncertezaExtendidaV', 'IncertezaExpandidaNormalizadaU', 'IncertezaExpandidaNormalizadaV', 'ComponenteDU', 'ComponenteDV', 'ComponenteDW', 'IncertezaVetorV'] )
    result.to_csv("/Users/rebecacabral/Documents/CDTN/Programa/Final")
    return(("Secondary Flow       " + sf), result)