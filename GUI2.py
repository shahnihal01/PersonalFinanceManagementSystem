from PyQt5 import QtCore, QtGui, QtWidgets
from GUI3 import Ui_MainWindow1
import sqlite3
from fpdf import FPDF
import os
import sys
import smtplib
from email.message import EmailMessage
from Credentials import *
import matplotlib.pyplot as plt


class Ui_OtherWindow(object):
    conn=sqlite3.connect('PFMSDB.db')
    c=conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS PFMSDB(NAME TEXT,EMAIL TEXT,INC DOUBLE,RENT DOUBLE,GROCER DOUBLE,TRANS DOUBLE,ENT DOUBLE,MISC DOUBLE)""")
    conn.commit()
    conn.close()
    def insert(self):
        s1=self.lineEdit.text()
        s2=self.lineEdit_10.text()
        s3=self.lineEdit_4.text()
        s4=self.lineEdit_5.text()
        s5=self.lineEdit_6.text()
        s6=self.lineEdit_7.text()
        s7=self.lineEdit_8.text()
        s8=self.lineEdit_9.text()
        conn=sqlite3.connect('PFMSDB.db')
        c=conn.cursor()
        sql= '''INSERT INTO PFMSDB (NAME,EMAIL,INC,RENT,GROCER,TRANS,ENT,MISC) VALUES (?,?,?,?,?,?,?,?)'''
        val=(s1,s2,s3,s4,s5,s6,s7,s8)
        c.execute(sql,val)
        conn.commit()
        conn.close()

    def view(self): 
        conn=sqlite3.connect('PFMSDB.db')
        c=conn.cursor()
        c.execute("""SELECT * FROM PFMSDB""")
        s=c.fetchall()
        print("records in db are", s)
        conn.commit()
        conn.close()
    
    def open3(self):
        self.Win = QtWidgets.QMainWindow()
        self.ui1 = Ui_MainWindow1()
        self.ui1.setupUi(self.Win)
        self.Win.show()

    def setupUi(self, OtherWindow):
        OtherWindow.setObjectName("PERSONAL FINANCIAL MANAGEMENT SYSTEM")
        OtherWindow.resize(640, 480)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 116, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 116, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 116, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 116, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        OtherWindow.setPalette(palette)
        self.label = QtWidgets.QLabel(OtherWindow)
        self.label.setGeometry(QtCore.QRect(20, 10, 461, 111))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(OtherWindow)
        self.label_2.setGeometry(QtCore.QRect(506, 10, 101, 111))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("D:/Nihal/COLLEGE/Mini Project/SEM4 MINI/IMG_20210423_194547.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(OtherWindow)
        self.label_3.setGeometry(QtCore.QRect(50, 160, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(OtherWindow)
        self.label_4.setGeometry(QtCore.QRect(50, 200, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(OtherWindow)
        self.label_5.setGeometry(QtCore.QRect(10, 240, 150, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(OtherWindow)
        self.lineEdit.setGeometry(QtCore.QRect(130, 160, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(OtherWindow)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 200, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(OtherWindow)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 240, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_6 = QtWidgets.QLabel(OtherWindow)
        self.label_6.setGeometry(QtCore.QRect(320, 160, 150, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(OtherWindow)
        self.label_7.setGeometry(QtCore.QRect(320, 200, 250, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(OtherWindow)
        self.label_8.setGeometry(QtCore.QRect(320, 230, 151, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(OtherWindow)
        self.label_9.setGeometry(QtCore.QRect(320, 260, 151, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(OtherWindow)
        self.label_10.setGeometry(QtCore.QRect(320, 290, 151, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(OtherWindow)
        self.label_11.setGeometry(QtCore.QRect(320, 320, 141, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(OtherWindow)
        self.label_12.setGeometry(QtCore.QRect(320, 350, 151, 16))
        self.label_12.setObjectName("label_12")
        self.lineEdit_4 = QtWidgets.QLineEdit(OtherWindow)
        self.lineEdit_4.setGeometry(QtCore.QRect(470, 160, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(OtherWindow)
        self.lineEdit_5.setGeometry(QtCore.QRect(470, 230, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(OtherWindow)
        self.lineEdit_6.setGeometry(QtCore.QRect(470, 260, 113, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(OtherWindow)
        self.lineEdit_7.setGeometry(QtCore.QRect(470, 290, 113, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(OtherWindow)
        self.lineEdit_8.setGeometry(QtCore.QRect(470, 320, 113, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(OtherWindow)
        self.lineEdit_9.setGeometry(QtCore.QRect(470, 350, 113, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_13 = QtWidgets.QLabel(OtherWindow)
        self.label_13.setGeometry(QtCore.QRect(50, 280, 71, 16))
        self.label_13.setObjectName("label_13")
        self.lineEdit_10 = QtWidgets.QLineEdit(OtherWindow)
        self.lineEdit_10.setGeometry(QtCore.QRect(130, 280, 113, 20))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.pushButton = QtWidgets.QPushButton(OtherWindow)
        self.pushButton.setGeometry(QtCore.QRect(250, 412, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.insert())
        self.pushButton.clicked.connect(lambda: self.addpdfemail())
        self.pushButton.clicked.connect(lambda: self.open3())


        self.retranslateUi(OtherWindow)
        QtCore.QMetaObject.connectSlotsByName(OtherWindow)

    def retranslateUi(self, OtherWindow):
        _translate = QtCore.QCoreApplication.translate
        OtherWindow.setWindowTitle(_translate("OtherWindow", "PERSONAL FINANCIAL MANAGEMENT SYSTEM"))
        self.label.setText(_translate("OtherWindow", "PERSONAL FINANCE MANAGEMENT SYSTEM"))
        self.label_3.setText(_translate("OtherWindow", "NAME :"))
        self.label_4.setText(_translate("OtherWindow", "AGE :"))
        self.label_5.setText(_translate("OtherWindow", "OCCUPATION:"))
        self.label_13.setText(_translate("OtherWindow", "E-MAIL :"))
        self.label_6.setText(_translate("OtherWindow", "MONTHLY INCOME:"))
        self.label_7.setText(_translate("OtherWindow", "MONTHY EXPENDIYTURE ON :"))
        self.label_8.setText(_translate("OtherWindow", "1. Rent/House EMI : "))
        self.label_9.setText(_translate("OtherWindow", "2. Groceries :"))
        self.label_10.setText(_translate("OtherWindow", "3. Transportation:"))
        self.label_11.setText(_translate("OtherWindow", "4. Entertainment : "))
        self.label_12.setText(_translate("OtherWindow", "5. Misc. :"))
        self.pushButton.setText(_translate("OtherWindow", "GO"))

    def addpdfemail(self):
        conn=sqlite3.connect('PFMSDB.db')
        cur = conn.cursor()
        email = cur.execute('SELECT EMAIL FROM PFMSDB').fetchall()[-1]
        inc = cur.execute('SELECT INC FROM PFMSDB').fetchall()[-1]
        rent = cur.execute('SELECT RENT FROM PFMSDB').fetchall()[-1]
        grocer = cur.execute('SELECT GROCER FROM PFMSDB').fetchall()[-1]
        trans = cur.execute('SELECT TRANS FROM PFMSDB').fetchall()[-1]
        ent = cur.execute('SELECT ENT FROM PFMSDB').fetchall()[-1]         
        misc = cur.execute('SELECT MISC FROM PFMSDB').fetchall()[-1]
        conn.commit()
        conn.close()

        sav = inc[0]-rent[0]-grocer[0]-trans[0]-ent[0]-misc[0]
        labels = 'Rent', 'Groceries', 'Transportation','Entertainment','Miscellaneous','savings'
        fig = [rent[0], grocer[0], trans[0], ent[0], misc[0], sav]
        explode = (0, 0.1, 0, 0, 0, 0)
        fig1, ax1 = plt.subplots()
        print(fig)
        ax1.pie(fig, explode=None, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax1.axis('equal')
        plt.savefig("plot.png")

        pdf = FPDF()
        title = 'YOUR PERSONAL FINANCIAL ANALYSIS AND CUSTOM INVESTMENT PLAN BASED ON YOUR INPUT'

        pdf = FPDF('P','mm','A4')

        pdf.add_page()
        pdf.set_font('helvetica','B',11)
        pdf.cell(40,10,'YOUR PERSONAL FINANCIAL ANALYSIS AND CUSTOM INVESTMENT PLAN BASED ON YOUR INPUT', ln=1)
        pdf.set_font('helvetica','',11) 
        pdf.cell(40,10,'Your annual income is: '+''.join([str(12*item) for item in inc ]),ln=1)
        pdf.cell(40,5,'According to NCAER-CMCR 2017 annual income data survey conducted by National Council of Applied ',ln=1) 
        pdf.cell(40,5,'Economic Research, your current annual income puts you in the bracket of',ln=1)
        if (12*inc[0] < 150000): 
            pdf.cell(40,5,'Below 1.5 lakh rupees per annum which qualifies as deprived class in India.', ln=1)
        elif (150000 < 12*inc[0]< 350000):
            pdf.cell(40,5,'1.5 to 3 lakh rupees per annum which qualifies as aspiring middle class in India.', ln=1)
        elif (350000 < 12*inc[0] <1700000):
            pdf.cell(40,5,'3.5 lakh rupees to 17 lakh per annum which qualifies as upper middle class in India.', ln=1)
        else:
            pdf.cell(40,5,'17 lakh rupees and above per annum which qualifies as rich in India.', ln=1)
        pdf.cell(40,5,'Your expenditure is represented graphically below to give you a better idea of how you spend your',ln=1)
        pdf.cell(40,5,'income: ',ln=1)
        pdf.image('plot.png', x = -5, y = None, w = 0, h = 0, type = 'PNG', link = '')
        pdf.cell(40,5,'Monthly your savings are: ' + str(sav),ln=1)
        pdf.cell(40,5,'Investing money is very important to ensure that your savings dont lose value because of inflation.',ln=1)
        pdf.cell(40,5,'Thus according to your income bracket we suggest you follow this investment plan for best results',ln=1)
        pdf.cell(40,5,'in terms of long term wealth creation:',ln=1)
        if inc[0] < 150000:
            pdf.cell(40,5,'1. 30 percent must be your savings',ln=1)
            pdf.cell(40,5,'2. 50 percent in low risk investments',ln=1)
            pdf.cell(40,5,'3. And 20 percent must be reserved in cash for emergencies',ln=1)
        elif 150000< inc[0] <350000:
            pdf.cell(40,5,'1. 20 percent must be in high risk investments',ln=1)
            pdf.cell(40,5,'2. 60 percent in low risk investments',ln=1)
            pdf.cell(40,5,'3. And 20 percent must be reserved in cash for emergencies',ln=1) 
        elif 350000< inc[0]< 1700000:
            pdf.cell(40,5,'1. 30 percent must be in high risk investments',ln=1)
            pdf.cell(40,5,'2. 60 percent in low risk investments',ln=1)
            pdf.cell(40,5,'3. And 10 percent must be reserved in cash for emergencies',ln=1)
        else :
            pdf.cell(40,5,'1. 55 percent must be in high risk investments',ln=1)
            pdf.cell(40,5,'2. 40 percent in low risk investments',ln=1)
            pdf.cell(40,5,'3. And 5 percent must be reserved in cash for emergencies',ln=1)

        pdf.cell(40,10,'Low Risk Investments: Savings account, Fixed Deposits, Blue chip Stocks, PPF',ln=1)
        pdf.cell(40,5,'High Risk Investments: General Stock Trading, Crypto, Real Estate, Commodities.',ln=1)
        

        pdf.set_auto_page_break(auto = True, margin=15)

        pdf.output('Report.pdf', 'F')

        contacts = ['nihalshah07@gmail.com', 'test@example.com']

        msg = EmailMessage()
        msg['Subject'] = 'Personal Finance Management System Report'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = email

        files = ['Report.pdf']

        for file in files:
            with open(file, 'rb') as f:
                file_data = f.read()
                file_name = f.name

            msg.add_attachment(file_data, maintype = 'application', subtype = 'octet-stream', filename = file_name)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OtherWindow = QtWidgets.QWidget()
    ui = Ui_OtherWindow()
    ui.setupUi(OtherWindow)
    OtherWindow.show()
    ui.view()
    
    sys.exit(app.exec_())
