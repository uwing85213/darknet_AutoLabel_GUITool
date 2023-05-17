# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 00:58:10 2021

@author: MH-Lin
"""



from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QMessageBox,QFileDialog
from PyQt5.QtGui import QIcon, QPixmap,QImage
from PyQt5.QtCore import QTimer,QThread,pyqtSignal

from AutolabelUI import Ui_MainWindow #UI檔案引入class
import sys
import os
import cv2
import numpy as np
import time


from YingRen_Yolov4API import Yolov4YingRen #有autolabel


import glob #autolabel用的lib
from reader import Reader #py檔
import shutil #複製name檔 到 資料夾內 改名成classes


def resource_path(relative_path):
    if getattr(sys, 'frozen', False): #是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
         super(MainWindow, self).__init__()
         self.ui = Ui_MainWindow()
         self.ui.setupUi(self)
         
         #UI設定
         self.ui.btnLoadModel_4K.clicked.connect(self.LoadModel_1)#
         self.ui.btnLoadModel_Hot.clicked.connect(self.LoadModel_2)#
         
         self.ui.btnAutoLabel.clicked.connect(self.AutoLabel_start)
         self.ui.btnAutoLabel_2.clicked.connect(self.OpenFileFolder)
         
         
         self.ui.rdn4K.setChecked(True)#
         self.ui.rdn4K.setEnabled(False)
         self.ui.rdnHot.setEnabled(False)
         self.ui.btnAutoLabel.setEnabled(False)
         
         ##變數相關
         
         self.timer_camera = QtCore.QTimer()  # 初始化定时器
         
         self.imgs_dir=""
         
         ##變數-AI相關
         self.config_file_Path_1=None 
         self.data_file_path_1=None 
         self.weights_Path_1=None 
         self.names_file_path_1=None
         self.detector_1=None         

         
         self.config_file_Path_2=None 
         self.data_file_path_2=None 
         self.weights_Path_2=None 
         self.names_file_path_2=None
         self.detector_2=None
         
         ##auto label
         self.num=0
         self.result=None
         self.txt_classes=None
    def LoadModel_1(self):     
         self.config_file_Path_1=resource_path(os.path.join("models/cocoWeight","yolov4.cfg"))
         self.data_file_path_1=resource_path(os.path.join("models/cocoWeight","coco.data"))
         self.weights_Path_1=resource_path(os.path.join("models/cocoWeight","yolov4.weights"))
         self.names_file_path_1=resource_path(os.path.join("models/cocoWeight","coco.names"))
         #
         f = open(self.data_file_path_1, 'w')
         namespath=self.names_file_path_1
         filepathname='classes=%d \n names='% 2 +namespath+'\n'
         #filepathname=str(filepathname)
         f.write(u'classes=%d \n names='% 2 +namespath+'\n')
         f.close()
         #
         self.detector_1 = Yolov4YingRen(self.config_file_Path_1,self.data_file_path_1,self.weights_Path_1,gpuid=0)#載入模型
         strLog='%s Load 4K Model Finish'%time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
         # print(strLog)
         self.ui.listLog.addItem(strLog)
         msg = QtWidgets.QMessageBox.about(self, u'提示',u'載入完成')
         self.ui.btnLoadModel_4K.setEnabled(False)
         self.ui.rdn4K.setEnabled(True)
         # self.ui.btnAutoLabel.setEnabled(True)
         if self.num>0:
             self.ui.btnAutoLabel.setEnabled(True)
         
    def LoadModel_2(self):        
         self.config_file_Path_2=resource_path(os.path.join("models/cocoWeight","yolov4.cfg"))
         self.data_file_path_2=resource_path(os.path.join("models/cocoWeight","coco.data"))
         self.weights_Path_2=resource_path(os.path.join("models/cocoWeight","yolov4.weights"))
         self.names_file_path_2=resource_path(os.path.join("models/cocoWeight","coco.names"))
         #
         f = open(self.data_file_path_2, 'w')
         namespath=self.names_file_path_2
         filepathname='classes=%d \n names='% 3 +namespath+'\n'
         #filepathname=str(filepathname)
         f.write(u'classes=%d \n names='% 3 +namespath+'\n')
         f.close()
         #
         self.detector_2 = Yolov4YingRen(self.config_file_Path_2,self.data_file_path_2,self.weights_Path_2,gpuid=0)#載入模型
         strLog='%s Hot Model Finish'%time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
         print(strLog)
         self.ui.listLog.addItem(strLog)
         msg = QtWidgets.QMessageBox.about(self, u'提示',u'載入完成')
         self.ui.btnLoadModel_Hot.setEnabled(False)
         self.ui.rdnHot.setEnabled(True)
         self.ui.rdnHot.setChecked(True)
         if self.num>0:
             self.ui.btnAutoLabel.setEnabled(True)
         

    def OpenFileFolder(self):
        self.ui.listImg.clear()
        self.ui.listTxt.clear()
        
        if self.timer_camera.isActive()==True:
            self.timer_camera.stop()
            return
        strLog='%s '%time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.imgs_dir=QFileDialog.getExistingDirectory(self,"Choose Images Folder",os.getcwd())#選取資料夾        
        if self.imgs_dir == "":
            self.ui.listLog.addItem(strLog+'Cancel choose')
            print("\nCancel choose")
            return                            
        self.ui.listLog.addItem(strLog+' Image Folder Path: '+self.imgs_dir)
        
        #產生檔案清單
        select= self.imgs_dir + r'/*.jpg'
        self.result=glob.glob(select)
        # print(self.result)
        self.file_num=len(self.result)
        
        if self.file_num==0:#無jpg就返回
            self.ui.listLog.addItem('No jpg,pleace re choose')
            print("\nNo jpg")
            return
        for i in range(self.file_num):#file_num
            imgname=self.result[i]
            imgname_array=imgname.split('/')
            self.ui.listImg.addItem(imgname_array[-1])
        
        if self.ui.btnLoadModel_4K.isEnabled()==False or self.ui.btnLoadModel_Hot.isEnabled()==False:
            self.ui.btnAutoLabel.setEnabled(True)
    
    def AutoLabel_start(self):
        self.ui.listTxt.clear()
        classfile=self.imgs_dir+r'/classes.txt'
        if os.path.isfile(classfile):#刪除檔案避免出問題
            os.remove(classfile)
                    
        objs=[]
        if self.ui.rdn4K.isChecked()==True:
            names_file_path=self.names_file_path_1
        else:
            names_file_path=self.names_file_path_2
         
            
        self.txt_classes=Reader.get_classes(names_file_path)
        #複製name檔 到 資料夾內 改名成classes
        shutil.copyfile(names_file_path, self.imgs_dir+r'/classes.txt')
        print('Copy nameFile finsh')
        
        if self.ui.rdn4K.isChecked()==True:
                self.rdnBool = True
        else:
                self.rdnBool = False   
        
        
        #用timer去跑偵測
        # self.timer_camera.timeout.connect(self.AutoLabel_Timer)
        # self.timer_camera.start(100)
        self.AutoLabel_Timer()
        
    def AutoLabel_Timer(self):
        # self.timer_camera.stop()
        self.ui.btnAutoLabel.setEnabled(False)
        for i in range(self.file_num):#file_num
            print(self.result[i])
            #創檔案
            txtname=self.result[i][:-4] + '.txt'
            f = open(txtname, 'w')
            #read img
            img = cv2.imread(self.result[i])
            #prediect
            if self.rdnBool==True:
                obj = self.detector_1.Autolabel_YingRen(img, 0.25)  # 物件偵測器
            else:
                obj = self.detector_2.Autolabel_YingRen(img, 0.25)  # 物件偵測器
            #write txt
            obj_num=len(obj)
            for j in range(obj_num):
                f.write("%d %.6f %.6f %.6f %.6f\n" % (self.txt_classes[obj[j][0]],obj[j][1],obj[j][2],obj[j][3],obj[j][4]) )
                
            f.close()
                # print('txt finsh')   
            # print('OK')
            txtname_array=txtname.split('/')
            self.ui.listTxt.addItem(txtname_array[-1])
            QtWidgets.QApplication.processEvents()
        # self.timer_camera.stop()
        strLog='%s '%time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.ui.listLog.addItem(strLog+'AutoLabel finished')
        self.ui.btnAutoLabel.setEnabled(True)
        msg = QtWidgets.QMessageBox.about(self, u'提示',u'標記完成')             
        
if __name__ == '__main__':
     app = QtWidgets.QApplication([])
     window = MainWindow()
     window.show()
     sys.exit(app.exec_())