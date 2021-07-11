#QTableView组件的使用
from PyQt5.QtWidgets import QApplication,QTableView, QHeaderView, QFormLayout,   QVBoxLayout,QWidget,QApplication ,QHBoxLayout, QPushButton,QMainWindow,QGridLayout,QLabel,QMessageBox
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import QStandardItemModel,QStandardItem,QIcon

import mysql
import TCPserver

class WindowClass(QWidget):
    #如果集成QMainWindow 则self.setLayout(self.layout) 替换成
    """
        widget=QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)
    """
    num=0
    sock1=None
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
        self.itemArr=[]

    def keyPressEvent(self, event):
        # 这里event.key（）显示的是按键的编码
        print("按下：" + str(event.key()))
        # 举例，这里Qt.Key_A注意虽然字母大写，但按键事件对大小写不敏感
        if (event.key() == Qt.Key_Escape):
            exit(0)
        if (event.key()==Qt.Key_0):
            print("test")
        if (event.key()==Qt.Key_1):
            self.showData("111")
        if (event.key()==Qt.Key_2):
            self.submit()
        if (event.key()==Qt.Key_3):
            self.resetForm()
        if (event.key()==Qt.Key_4):
            self.listenData()
        if (event.key()==Qt.Key_5):
            print("listening...")
            self.sock1 = TCPserver.sock()
            print(self.sock1)
    # 获取用户的id
    def getUserid(self):
        return

    # 显示数据
    def showData(self,a):
        i = QStandardItem(a)
        self.model.setItem(self.num, 1, i)
        ret=self.mysql.select("SELECT * FROM `goods` WHERE `label`='"+a+"'")
        i = QStandardItem(ret[0][0])
        self.model.setItem(self.num, 0, i)
        i = QStandardItem(str(ret[0][2]))
        self.model.setItem(self.num, 2, i)
        self.num+=1
        self.itemArr.append(ret[0][1])

    # 监听数据
    def listenData(self):
        while True:
            scanFlag=QMessageBox.question(self,"确定扫描", "请将商品放在指定区域", QMessageBox.Yes |  QMessageBox.No, QMessageBox.Yes)
            if scanFlag==65536:
                # print(scanFlag)
                return
            if self.sock1==None:
                # print("no socket")
                return
            self.sock1.send("aaaa")
            itemStr=self.sock1.listen()
            print(itemStr)
            itemStr=itemStr.replace(" ", "")
            itemList=itemStr.split(',')
            for item in itemList:
                self.showData(item)
            self.submit()

    # 重置界面
    def resetForm(self):
        self.model = QStandardItemModel(100, 3)
        self.tableView.setModel(self.model)
        self.num=0

    # 商品结算
    def submit(self,userid="test00001"):
        totalPrice=0.0
        for item in self.itemArr:
            print(item)
            ret=self.mysql.select("SELECT * FROM `goods` WHERE `label`='"+item+"'")
            updateStr="UPDATE `goods` SET `last`="+str((ret[0][3]-1))+" WHERE `label`="+item
            self.mysql.update(updateStr)
            totalPrice+=ret[0][2]
        print("submit complete")
        strUser="用户"+userid
        messageStr="您本次消费"+str(totalPrice)+"元"
        if totalPrice!=0.0:
            affordFlag=QMessageBox.question(self, strUser, messageStr, QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            print(affordFlag)
            insertStr = "INSERT INTO `record`(`consumer`, `time`, `totalPrice`) VALUES ('" + userid + "',now()," + str(
                totalPrice) + ")"
            print(insertStr)
            self.mysql.insert(insertStr)
        self.resetForm()
        self.itemArr = []
        return

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=WindowClass()
    win.setWindowTitle('无人超市销售面板')
    win.show()
    sys.exit(app.exec_())