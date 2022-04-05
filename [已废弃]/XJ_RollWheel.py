import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt,QRect
from PyQt5.QtGui import QPainter,QPen,QColor,QImage,QFont
from PyQt5.QtWidgets import *
import os
from types import MethodType


class XJ_RollWheel(QWidget):
    class WheelPicts:
        def __init__(self,path):
            self.__pict=[]
            for name in os.listdir(path):
                file=os.path.join(path,name)
                if(os.path.isfile(file)):
                    self.__pict.append(QImage(file))
            self.__len=len(self.__pict)
            if(self.__len==0):
                self.__pict.append(QImage())
                self.__len=1
            self.__curr=0

        def Next(self):
            self.__curr=self.__curr+1
            if(self.__curr>=self.__len):
                self.__curr=self.__curr-self.__len

        def Back(self):
            self.__curr=self.__curr-1
            if(self.__curr<0):
                self.__curr=self.__curr+self.__len

        def Current(self):
            return self.__pict[self.__curr]

    def __init__(self,parent=None,hint='',width=100,height=300):
        super(XJ_RollWheel, self).__init__(parent)
        self.__val_min=0#最小值
        self.__val_max=100#最大值
        self.__picts=XJ_RollWheel.WheelPicts('./滚轮图片')
        self.__widget_hint=QLabel(hint,self)
        self.__widget_pict=QWidget(self)
        self.__widget_input=QLineEdit('30',self)

        grid = QGridLayout()#盒布局对不同类型的控件所分配的空间很不合理，用多了真的血压会上来，得用其他布局
        grid.addWidget(self.__widget_hint, 1, 0)
        grid.addWidget(self.__widget_pict, 2, 0 , 20 , 1)# 占据20行1列
        grid.addWidget(self.__widget_input, 22 , 0)
        self.setLayout(grid)
        self.resize(width,height)
        
        font=QFont()
        font.setBold(True)
        font.setPixelSize(20)
        self.__widget_hint.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)#设置靠底居中
        self.__widget_hint.setFont(font)#设置字体
        self.__widget_hint.setStyleSheet("QLabel{color:rgb(255,50,50);}")#设置颜色
        
        def paintEvent(self,event):
            painter=QPainter(self)
            painter.drawImage(QRect(0,0,self.size().width(),self.size().height()),self.__pict)
        def mouseMoveEvent(self,event):
            self.setCursor(Qt.PointingHandCursor)#手型光标
        self.__widget_pict.paintEvent=MethodType(paintEvent,self.__widget_pict)
        self.__widget_pict.mouseMoveEvent=MethodType(mouseMoveEvent,self.__widget_pict)
        self.__widget_pict.__pict=self.__picts.Current()
        self.__widget_pict.setFocusPolicy(Qt.ClickFocus|Qt.WheelFocus)#让控件可以获取焦点
        self.__widget_pict.setMouseTracking(True)#时刻捕捉鼠标移动
        
        def focusOutEvent(self,event):
            min,max=self.__parent.Get_ValueRange()
            curr=''.join(list(filter(lambda c:c.isdigit(),self.text())))
            curr=int(curr) if len(curr) else 0
            if(curr<min):
                curr=min
            elif(curr>max):
                curr=max
            self.setText(str(curr))
            self.setReadOnly(True)
            event.accept()
        def mouseDoubleClickEvent(self,event):
            event.ignore()
        def mouseMoveEvent(self,event):
            self.setCursor(Qt.PointingHandCursor)#手型光标
        self.__widget_input.focusOutEvent=MethodType(focusOutEvent,self.__widget_input)
        self.__widget_input.mouseDoubleClickEvent=MethodType(mouseDoubleClickEvent,self.__widget_input)
        self.__widget_input.mouseMoveEvent=MethodType(mouseMoveEvent,self.__widget_input)
        self.__widget_input.__parent=self
        self.__widget_input.setReadOnly(True)
        self.__widget_input.setAlignment(Qt.AlignCenter)#设置居中
        self.__widget_input.setFont(font)#设置字体
        self.setFocusPolicy(Qt.ClickFocus|Qt.WheelFocus)#让控件背景可以获取焦点
    
        self.HideWheel()#因为太丑了，默认隐藏

    def Set_ValueRange(self,valMin,valMax):
        self.__val_min=valMin
        self.__val_max=valMax
        if(self.__val_max<self.__val_min):
            self.__val_max,self.__val_min=self.__val_min,self.__val_max

        curr=int(self.__widget_input.text())
        if(curr<self.__val_min):
            self.__widget_input.setText(str(self.__val_min))
        if(curr>self.__val_max):
            self.__widget_input.setText(str(self.__val_max))
        
    def Get_ValueRange(self):#返回取值范围
        return (self.__val_min,self.__val_max)
    
    def ShowHint(self):
        self.__widget_hint.show()
        
    def HideHint(self):
        self.__widget_hint.hide()
    
    def SetHint(self,tx):
        self.__widget_hint.setText(tx)

    def HideWheel(self):
        self.__widget_pict.hide()
        self.layout().addWidget(self.__widget_input, 2 , 0)

    def ShowWheel(self):
        self.__widget_pict.show()
        self.layout().addWidget(self.__widget_input, 22 , 0)

    def mouseDoubleClickEvent(self,event):
        self.__widget_input.setReadOnly(False)
        self.__widget_input.setFocus()
        event.accept()
        
    def wheelEvent(self,event):
        delta=event.angleDelta()
        curr=''.join(list(filter(lambda c:c.isdigit(),self.__widget_input.text())))
        curr=int(curr) if len(curr) else 0
        if(delta.y()>0):#滚轮向上滚动，增加
            if(curr<self.__val_max):
                curr=curr+1
                self.__picts.Next()
        elif(delta.y()<0):#向下滚动，减少
            if(curr>self.__val_min):
                curr=curr-1
                self.__picts.Back()
        self.__widget_input.setText(str(curr))
        self.__widget_pict.__pict=self.__picts.Current()
        self.update()
        event.accept()

    


if __name__=='__main__':
    app = QApplication(sys.argv)
    
    lst=[]
    hbox=QHBoxLayout()
    for i in range(3):
        lst.append(XJ_RollWheel(None,'滚轮'+str(i+1),100,300))
        hbox.addWidget(lst[i])
    lst[0].ShowWheel()
    lst[0].HideHint()
    lst[2].HideWheel()
#    lst[2].show()

    test=QWidget()
    test.setLayout(hbox)
    test.resize(500,500)
    test.show()

    sys.exit(app.exec())



