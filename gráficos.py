#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 10:40:52 2020

@author: rebecacabral
"""

import pandas as pd
import numpy as np
import glob
# from txt_to_csv import frame
# from txt_to_csv import R1
# from txt_to_csv import R2


    
def perfil_velocidade(path):
      
    all_files = glob.glob(path + '/15mm_campo_topo_t0*.csv')
    li = []
    for filename in all_files:
        df = pd.read_csv(filename, skiprows=6, index_col=None, header=0, sep='\t')
        li.append(df)
        frame = pd.concat(li, axis=1, ignore_index=True)


    frame=frame.iloc[:,[0,1,2,8,9,25,26,42,43,59,60,76,77]]
#frame = frame.convert_objects(convert_dates='coerce',convert_numeric=True)

    R1=frame.filter([8,25,42,59,76], axis=1)
    R2=frame.filter([9,26,43,60,77], axis=1)
    
    plot = ([frame[1],frame[2],R1,R2])
    plot = pd.concat(plot, axis=1, ignore_index=True)

    plot = np.array(round(plot,3))

    li=[]
    for i in range(len(plot)):
        if plot[i][0] == 1.50e-01:
            li.append(plot[i][:])
            
    li = np.array(li)
            
    x = []          
    for i in range(len(li)):
        x.append(li[i][1])
    x = np.divide(x,-14.3)
    
    
    y1 = []
    for i in li:
        y1.append(i[2])
    y1 = np.array(y1)
    
    y2 = []
    for i in li:
        y2.append(i[3])
    y2 = np.array(y2)
    
    y3 = []
    for i in li:
        y3.append(i[4])
    y3 = np.array(y3)

    y4 = []
    for i in li:
        y4.append(i[5])
    y4 = np.array(y4)
    
    y5 = []
    for i in li:
        y5.append(i[6])
    y5 = np.array(y5)
    
    y6 = []
    for i in li:
        y6.append(i[7])
    y6 = np.array(y6)
    
    y7 = []
    for i in li:
        y7.append(i[8])
    y7 = np.array(y7)

    y8 = []
    for i in li:
        y8.append(i[9])
    y8 = np.array(y8)
    
    y9 = []
    for i in li:
        y9.append(i[10])
    y9 = np.array(y9)
    
    y10 = []
    for i in li:
        y10.append(i[11])
    y10 = np.array(y10)
        
    y = [x,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10]
        
 #   y = pd.DataFrame(y, index = ['x', 'y1', 'y2','y3','y4','y5','y6','y7','y8','y9','y10'])
    
    return y
            
    # fig, (ax1,ax2)=plt.subplots(1,2, figsize=(12,7))
    # ax1.plot(x, np.divide(y1,W), 'ro', label = 'Teste 1')
    # ax1.plot(x, np.divide(y2,W), 'bo', label = 'Teste 2')
    # ax1.plot(x, np.divide(y3,W), 'go', label = 'Teste 3')
    # ax1.plot(x, np.divide(y4,W), 'mo', label = 'Teste 4')
    # ax1.plot(x, np.divide(y5,W), 'yo', label = 'Teste 5')
    # ax1.legend()
    # ax1.set_ylabel('$u/w$')
    # ax1.set_ylim(-0.1, 0.2)
    # ax1.set_xlabel('$x/passo$')
    # ax1.set_title('Perfil da velocidade $u$ no subcanal X' )
    # ax2.plot(x, np.divide(y6,W), 'ro', label = 'Teste 1')
    # ax2.plot(x, np.divide(y7,W), 'bo', label = 'Teste 2')
    # ax2.plot(x, np.divide(y8,W), 'go', label = 'Teste 3')
    # ax2.plot(x, np.divide(y9,W), 'mo', label = 'Teste 4')
    # ax2.plot(x, np.divide(y10,W), 'yo', label = 'Teste 5')
    # ax2.legend()
    # ax2.set_ylabel('$v/w$')
    # ax2.set_ylim(-0.1, 0.2)
    # ax2.set_xlabel('$x/passo$')
    # ax2.set_title('Perfil da velocidade $v$ no subcanal X' )
    # plt.savefig('/Users/rebecacabral/Documents/CDTN/INCERTEZA_EXT/Perfil_de_velocidade_U_e_V.png', format='png')
    # plt.show()    
 
        


        



        