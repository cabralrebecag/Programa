# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'início.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic
import sys
from w_combinada import w
from w_combinada import incert_ext_w
from txt_to_csv import path_lda
from gráficos import perfil_velocidade
from perda_de_carga import perda_carga
from tensores_de_reynolds import tensores
# from TENSORES_DE_REYNOLDS import tensores_de_reynolds

Form, Window = uic.loadUiType('início.ui')

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Window()
        self.ui.form = Form()
        self.ui.form.setupUi(self)
        self.ui.form.toolButton_reynolds.clicked.connect(self.r_botao)
        self.ui.form.toolButton_lda.clicked.connect(self.lda_botao)
        self.ui.form.toolButton_pd.clicked.connect(self.pd_botao)
        self.ui.form.ok_button.clicked.connect(self.ok_botao)
        self.ui.form.ok_button.clicked.connect(lambda:self.check_box(self.ui.form.velocity_profile,self.ui.form.vector_field))
        
    def r_botao(self):
         path1 = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select a directory')
         if path1:
             self.ui.form.folder_reynolds.setText(path1)
         self.string_path1 = path1
        
    def lda_botao(self):
         path2 = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select a directory')
         if path2:
             self.ui.form.file_lda.setText(path2)
         self.string_path2 = path2        
         
    def pd_botao(self):
         path3 = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select a directory')
         if path3:
             self.ui.form.file_pd.setText(path3)
         self.string_path3 = path3 
 
                
    def ok_botao(self):
        
        # b = w(self.string_path3)
        # print (b)
        
        a = path_lda(self.string_path2, self.string_path2)
        print (a)

        d = incert_ext_w(self.string_path3)
        print (d)

        c = perda_carga(self.string_path3)
        print (c)
        
        e = tensores(self.string_path1)
        print (e)
        
    def check_box(self, velocity_profile, vector_field):
        if self.ui.form.velocity_profile.isChecked():
             perfil_velocidade.plot = (path_lda.frame + path_lda.R1 + path_lda.R2)
        if self.ui.form.vector_field.isChecked():
             campo_vetorial.d1 = path_lda.result
        
 
        # with concurrent.futures.ThreadPoolExecutor() as executer:
        #     f1 = executer.submit(thread_mmao, num_images2, dir, file_prefix, num_primeira)
        #     f2 = executer.submit(thread_bckg, num_images, dir, file_prefix, num_primeira)
        #     mao = f1.result()
        #     bck_ground = f2.result()  
        # x = threading.Thread(target = thread_processing, args = (num_images, dir, file_prefix, num_primeira, bck_ground, mao, met, w_size, ovl, n_iterations))
        # x.start()

        
        
app = QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())

