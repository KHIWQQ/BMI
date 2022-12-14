# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\bmi_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1004, 451)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 30, 419, 348))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.title = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.gridLayout_8.addWidget(self.title, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 2)
        self.gridLayout_8.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.no_in = QtWidgets.QLineEdit(self.layoutWidget)
        self.no_in.setObjectName("no_in")
        self.gridLayout_6.addWidget(self.no_in, 1, 0, 1, 1)
        self.name_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name_2.setFont(font)
        self.name_2.setObjectName("name_2")
        self.gridLayout_6.addWidget(self.name_2, 0, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.name = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.gridLayout_5.addWidget(self.name, 0, 0, 1, 1)
        self.lastname = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lastname.setFont(font)
        self.lastname.setObjectName("lastname")
        self.gridLayout_5.addWidget(self.lastname, 0, 1, 1, 1)
        self.name_in = QtWidgets.QLineEdit(self.layoutWidget)
        self.name_in.setObjectName("name_in")
        self.gridLayout_5.addWidget(self.name_in, 1, 0, 1, 1)
        self.lname_in = QtWidgets.QLineEdit(self.layoutWidget)
        self.lname_in.setObjectName("lname_in")
        self.gridLayout_5.addWidget(self.lname_in, 1, 1, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_5, 0, 1, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem1, 3, 0, 1, 1)
        self.button_insert_user = QtWidgets.QPushButton(self.layoutWidget)
        self.button_insert_user.setObjectName("button_insert_user")
        self.gridLayout_8.addWidget(self.button_insert_user, 4, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem2, 5, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.height_in = QtWidgets.QLineEdit(self.layoutWidget)
        self.height_in.setObjectName("height_in")
        self.gridLayout_2.addWidget(self.height_in, 1, 1, 1, 1)
        self.height = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.height.setFont(font)
        self.height.setObjectName("height")
        self.gridLayout_2.addWidget(self.height, 1, 0, 1, 1)
        self.weight_in = QtWidgets.QLineEdit(self.layoutWidget)
        self.weight_in.setObjectName("weight_in")
        self.gridLayout_2.addWidget(self.weight_in, 0, 1, 1, 1)
        self.weight = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.weight.setFont(font)
        self.weight.setObjectName("weight")
        self.gridLayout_2.addWidget(self.weight, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 2, 0, 1, 2)
        self.gridLayout_8.addLayout(self.gridLayout_2, 6, 0, 1, 1)
        self.button_calculate = QtWidgets.QPushButton(self.layoutWidget)
        self.button_calculate.setObjectName("button_calculate")
        self.gridLayout_8.addWidget(self.button_calculate, 7, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem4, 8, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(540, 110, 411, 263))
        self.widget.setObjectName("widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.No = QtWidgets.QLabel(self.widget)
        self.No.setObjectName("No")
        self.gridLayout_4.addWidget(self.No, 0, 0, 1, 1)
        self.Name = QtWidgets.QLabel(self.widget)
        self.Name.setObjectName("Name")
        self.gridLayout_4.addWidget(self.Name, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 2, 1, 1)
        self.no_show = QtWidgets.QLineEdit(self.widget)
        self.no_show.setObjectName("no_show")
        self.gridLayout_4.addWidget(self.no_show, 1, 0, 1, 1)
        self.name_show = QtWidgets.QLineEdit(self.widget)
        self.name_show.setObjectName("name_show")
        self.gridLayout_4.addWidget(self.name_show, 1, 1, 1, 1)
        self.lname_show = QtWidgets.QLineEdit(self.widget)
        self.lname_show.setObjectName("lname_show")
        self.gridLayout_4.addWidget(self.lname_show, 1, 2, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.result_show = QtWidgets.QTextEdit(self.widget)
        self.result_show.setObjectName("result_show")
        self.gridLayout_3.addWidget(self.result_show, 5, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 2, 0, 1, 2)
        self.bmi = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bmi.setFont(font)
        self.bmi.setObjectName("bmi")
        self.gridLayout_3.addWidget(self.bmi, 3, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 0, 0, 1, 2)
        self.result = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.result.setFont(font)
        self.result.setObjectName("result")
        self.gridLayout_3.addWidget(self.result, 5, 0, 1, 1)
        self.bmi_show = QtWidgets.QLineEdit(self.widget)
        self.bmi_show.setObjectName("bmi_show")
        self.gridLayout_3.addWidget(self.bmi_show, 3, 1, 1, 1)
        self.type = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.type.setFont(font)
        self.type.setObjectName("type")
        self.gridLayout_3.addWidget(self.type, 4, 0, 1, 1)
        self.type_show = QtWidgets.QLineEdit(self.widget)
        self.type_show.setObjectName("type_show")
        self.gridLayout_3.addWidget(self.type_show, 4, 1, 1, 1)
        self.button_show_bmi = QtWidgets.QPushButton(self.widget)
        self.button_show_bmi.setObjectName("button_show_bmi")
        self.gridLayout_3.addWidget(self.button_show_bmi, 1, 0, 1, 2)
        self.gridLayout_4.addLayout(self.gridLayout_3, 2, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1004, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "BMI CRMA [EP]"))
        self.name_2.setText(_translate("MainWindow", "No:          "))
        self.name.setText(_translate("MainWindow", "Name:          "))
        self.lastname.setText(_translate("MainWindow", "Lastname:          "))
        self.button_insert_user.setText(_translate("MainWindow", "Submit"))
        self.height.setText(_translate("MainWindow", "height (cm) :"))
        self.weight.setText(_translate("MainWindow", "weight  (Kg):          "))
        self.button_calculate.setText(_translate("MainWindow", "Calculate"))
        self.No.setText(_translate("MainWindow", "No :"))
        self.Name.setText(_translate("MainWindow", "Name :"))
        self.label_3.setText(_translate("MainWindow", "Lastname :"))
        self.bmi.setText(_translate("MainWindow", "BMI :          "))
        self.result.setText(_translate("MainWindow", "Suggestion :"))
        self.type.setText(_translate("MainWindow", "Type"))
        self.button_show_bmi.setText(_translate("MainWindow", "Show BMI"))

    # Button
        self.button_insert_user.clicked.connect(self.insert)
        self.button_calculate.clicked.connect(self.calbmi)
        self.button_show_bmi.clicked.connect(self.showbmi)
        
    # Function
    def insert(self):
        id = self.no_in.text()
        name = self.name_in.text()
        lname = self.lname_in.text()   
        print(id)
        print(name)
        print(lname) 
        insertuser(id,name,lname)
    
    def calbmi(self):
        id = self.no_in.text()
        weight = int(self.weight_in.text())
        height = int(self.height_in.text())
        bmiresult = weight/((height/100)*(height/100))
        print(bmiresult)
        if(bmiresult<18):
            bmiid = 1
        elif(bmiresult<23):
            bmiid = 2
        elif(bmiresult<25):
            bmiid = 3
        elif(bmiresult<30):
            bmiid = 4
        elif(bmiresult>=30):
            bmiid = 5
        bmi = bmiresult
        type = bmiid
        insertbmi(id,weight,height,bmi,type)
        # return bmiresult    
    
    def showbmi(self):
        id = self.no_show.text()

        self.name_show.setPlaceholderText(showname(id))
        self.lname_show.setPlaceholderText(showlname(id))
        self.bmi_show.setPlaceholderText(showbmi(id))
        self.type_show.setPlaceholderText(showtype(id))  
        self.result_show.setPlaceholderText(showsuggest(id))   
        

import mysql.connector

def ConnectorMysql():
    
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="bmi",
        # auth_plugin='mysql_native_password'
    )
    print("db is on the way")
    return mydb

def insertuser(id,name,lname):
    print("insert in")
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'INSERT INTO `bmii`(`id`, `name`, `lname`, `bmi`, `type`, `suggest`) VALUES ({id},"{name}","{lname}",0,0,0);'
    print(sql)
    print("Insert into success!!")
    cur.execute(sql)
    db.commit()
    db.close()

def insertbmi(id,weight,height,bmi,type):
    print("insert bmi")
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'UPDATE `bmii` SET `weight`={weight}, `height`={height}, `bmi`={bmi}, `type`={type} WHERE `id`={id};'
    print(sql)
    print("Insert bmi success!!")
    cur.execute(sql)
    db.commit()
    db.close()    
    
def showname(id):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = f'SELECT name FROM bmii WHERE id="{id}";'
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    name = str(myresult[0][0])
    print(name)
    return name 

def showlname(id):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = f'SELECT lname FROM bmii WHERE id="{id}";'
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    lname = str(myresult[0][0])
    print(lname)
    return lname   
    
def showtype(id):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = f'SELECT type FROM bmii WHERE id="{id}";'
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    type = str(myresult[0][0])
    print(type)
    sql = f'SELECT bmitype, bmicomment FROM bmicare WHERE bmiid="{type}";'
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    bmitype = str(myresult[0][0])
    suggest = str(myresult[0][1])
    print(bmitype)
    print(suggest)
    return bmitype

def showbmi(id):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = f'SELECT bmi FROM bmii WHERE id="{id}";'
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    bmi = str(myresult[0][0])
    print(bmi)
    return bmi

def showsuggest(id):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = f'SELECT type FROM bmii WHERE id="{id}";'
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    type = str(myresult[0][0])
    print(type)
    sql = f'SELECT bmitype, bmicomment FROM bmicare WHERE bmiid="{type}";'
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    bmitype = str(myresult[0][0])
    suggest = str(myresult[0][1])
    print(bmitype)
    print(suggest)
    return suggest


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
