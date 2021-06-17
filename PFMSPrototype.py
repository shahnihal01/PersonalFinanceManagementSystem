from fpdf import FPDF
import os
import sys
import smtplib
from email.message import EmailMessage
from Credentials import *
import sqlite3
import matplotlib.pyplot as plt



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
pdf.cell(40,10,'Your annual income is: '+''.join([str(item) for item in inc ]),ln=1)
pdf.cell(40,5,'According to xyz survey conducted by xyz organization your current annual income puts you in this',ln=1)
pdf.cell(40,5,'bracket 1.5 to 3 lakh rupees per annum which qualifies as upper middle class in India.', ln=1)
pdf.cell(40,5,'Your expenditure is represented graphically below to give you a better idea of how you spend your',ln=1)
pdf.cell(40,5,'income: ',ln=1)
pdf.image('plot.png', x = -5, y = None, w = 0, h = 0, type = 'PNG', link = '')
pdf.cell(40,10,'Monthly your savings are: ',ln=1)
pdf.cell(40,5,'Investing money is very important to ensure that your savings dont lose value because of inflation.',ln=1)
pdf.cell(40,5,'Thus according to your income bracket we suggest you follow this investment plan for best results',ln=1)
pdf.cell(40,5,'in terms of long term wealth creation:',ln=1)
pdf.cell(40,5,'1. 20 percent must be in high risk investments',ln=1)
pdf.cell(40,5,'2. 60 percent in low risk investments',ln=1)
pdf.cell(40,5,'3. And 10 percent must be reserved in cash for emergencies',ln=1)

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
