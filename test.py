#QTableView组件的使用
from PyQt5.QtWidgets import QTableView, QHeaderView, QFormLayout,   QVBoxLayout,QWidget,QApplication ,QHBoxLayout, QPushButton,QMainWindow,QGridLayout,QLabel
import sys
from PyQt5.QtCore import  *
from PyQt5.QtGui import  QStandardItemModel,QStandardItem

import mysql


class WindowClass(QWidget):
    #如果集成QMainWindow 则self.setLayout(self.layout) 替换成
    """
        widget=QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)
    """
    num=0
    #即可， 注意集成QWidget和集成QMainWindow时候区别
    def __init__(self,parent=None):
        self.mysql=mysql.SqlFunc()
        super(WindowClass, self).__init__(parent)
        self.layout=QVBoxLayout()
        self.model=QStandardItemModel(100,3)#存储任意结构数据
        self.model.setHorizontalHeaderLabels(['商品','标签','价格'])
        # for row in range(4):
        #     for column in range(4):
        #         i=QStandardItem("row %s,column %s"%(row,column))
        #         self.model.setItem(row,column,i)
        self.tableView=QTableView()
        self.tableView.setModel(self.model)
        self.layout.addWidget(self.tableView)
        #继承QMainWidow使用下面三行代码
        # widget=QWidget()
        # widget.setLayout(self.layout)
        # self.setCentralWidget(widget)
        #继承QWidget则使用下面这样代码
        self.setLayout(self.layout)
        #设置表格充满这个布局QHeaderView
        #self.tableView.horizontalHeader().setStretchLastSection(True)#最后一列决定充满剩下的界面
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)#所有列自动拉伸，充满界面

    def keyPressEvent(self, event):
        # 这里event.key（）显示的是按键的编码
        print("按下：" + str(event.key()))
        # 举例，这里Qt.Key_A注意虽然字母大写，但按键事件对大小写不敏感
        if (event.key() == Qt.Key_Escape):
            exit(0)
        if (event.key()==Qt.Key_0):
            print("test")
        if (event.key()==Qt.Key_1):
            self.showData("水")
        if (event.key()==Qt.Key_2):
            self.submit()
        if (event.key()==Qt.Key_3):
            self.resetForm()

    # 显示数据
    def showData(self,a):
        i = QStandardItem(a)
        self.model.setItem(self.num, 0, i)
        ret=self.mysql.select("SELECT * FROM `goods` WHERE `name`='"+a+"'")
        i = QStandardItem(ret[0][1])
        self.model.setItem(self.num, 1, i)
        i = QStandardItem(str(ret[0][2]))
        self.model.setItem(self.num, 2, i)
        self.num+=1

    # 监听数据
    def listenData(self):
        return

    def resetForm(self):
        self.model = QStandardItemModel(8, 4)
        self.tableView.setModel(self.model)
        self.num=0

    def submit(self):

        return

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=WindowClass()
    win.show()
    sys.exit(app.exec_())