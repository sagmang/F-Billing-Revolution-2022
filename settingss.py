#from ast import pattern
from calendar import c
from cgitb import enable, reset, text
from distutils import command
from itertools import count
from pydoc import describe
from secrets import choice
from sqlite3 import enable_callback_tracebacks
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.font import BOLD
from urllib.parse import parse_qs
from PIL import ImageTk, Image, ImageFile
from matplotlib.font_manager import json_dump
from numpy import choose, empty, place
import pandas as pd
from tkinter.messagebox import showinfo
import tkinter.scrolledtext as scrolledtext
from tkinter.filedialog import askopenfilename
import os
import webbrowser
from pip import main
from tkcalendar import Calendar
from tkcalendar import DateEntry
from datetime import date
from tkinter import filedialog
import subprocess
import mysql.connector
import io
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import shutil
import csv
import json
from tkPDFViewer import tkPDFViewer as pdf
from tkinter import Tk, Canvas


fbilldb = mysql.connector.connect(
    host="localhost", user="root", password="", database="fbillingsintgrtd", port="3306"
)
fbcursor = fbilldb.cursor()

root=Tk()
root.geometry("1300x730")
root.resizable(False, False)
root.title("F-Billing Revolution 2022(FREE version) | Company database:fbillingdb | User:Administrator")
p1 = PhotoImage(file = 'images/fbicon.png')
root.iconphoto(False, p1)


s = ttk.Style()
s.theme_use('default')
s.configure('TNotebook.Tab', background="#999999", width=20, padding=10)
invoices= PhotoImage(file="images/invoice.png")
orders = PhotoImage(file="images/order.png")
estimates = PhotoImage(file="images/estimate.png")
recurring = PhotoImage(file="images/recurring.png")
purchase = PhotoImage(file="images/purchase.png")
expenses = PhotoImage(file="images/expense.png")
customer = PhotoImage(file="images/customer.png")
product = PhotoImage(file="images/package.png")
reports = PhotoImage(file="images/report.png")
setting = PhotoImage(file="images/setting.png")
tick = PhotoImage(file="images/check.png")
warnin = PhotoImage(file="images/sign_warning.png")
cancel = PhotoImage(file="images/close.png")
saves = PhotoImage(file="images/save.png")
folder = PhotoImage(file="images/folder-black.png")
photo11 = PhotoImage(file = "images/invoice-pvt.png")
customer = PhotoImage(file="images/customer.png")
smslog = PhotoImage(file = "images/smslog.png")
video = PhotoImage(file = "images/video.png")
mark1 = PhotoImage(file="images/mark.png")
mark2 = PhotoImage(file="images/mark2.png")
photo10 = PhotoImage(file = "images/text-message.png")
addnew = PhotoImage(file="images/plus.png")
delete = PhotoImage(file="images/delete_E.png")

tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3=  ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)
tab6=  ttk.Frame(tabControl)
tab7 = ttk.Frame(tabControl)
tab8 = ttk.Frame(tabControl)
tab9 =  ttk.Frame(tabControl)
tab10=  ttk.Frame(tabControl)
tabControl.add(tab1,image=invoices,compound = LEFT, text ='Invoices',)
tabControl.add(tab2,image=orders,compound = LEFT, text ='Orders')
tabControl.add(tab3,image=estimates,compound = LEFT, text ='Estimates')
tabControl.add(tab4,image=recurring,compound = LEFT, text ='Recurring')
tabControl.add(tab5,image=purchase,compound = LEFT, text ='Purchase Orders') 
tabControl.add(tab6,image=expenses,compound = LEFT, text ='Expenses')
tabControl.add(tab7,image=customer,compound = LEFT, text ='Customers')
tabControl.add(tab8,image=product,compound = LEFT, text ='Product/Services')
tabControl.add(tab9,image=reports,compound = LEFT, text ='Report')
tabControl.add(tab10,image=setting,compound = LEFT, text ='Settings')
tabControl.pack(expand = 1, fill ="both")


selectall = PhotoImage(file="images/table_select_all.png")
cut = PhotoImage(file="images/cut.png")
copy = PhotoImage(file="images/copy.png")
paste = PhotoImage(file="images/paste.png")

undo = PhotoImage(file="images/undo.png")
redo = PhotoImage(file="images/redo.png")
bold = PhotoImage(file="images/bold.png")

italics = PhotoImage(file="images/italics.png")
underline = PhotoImage(file="images/underline.png")
left = PhotoImage(file="images/left.png")

right = PhotoImage(file="images/right.png")
center = PhotoImage(file="images/center.png")
hyperlink = PhotoImage(file="images/hyperlink.png")
remove = PhotoImage(file="images/eraser.png")


photo = PhotoImage(file = "images/plus.png")
photo1 = PhotoImage(file = "images/edit.png")
photo2 = PhotoImage(file = "images/delete_E.png")
photo3 = PhotoImage(file = "images/export-file.png")
photo4 = PhotoImage(file = "images/seo.png")
photo5 = PhotoImage(file = "images/printer.png")
photo6 = PhotoImage(file = "images/gmail.png")
photo7 = PhotoImage(file = "images/priewok.png")
photo8 = PhotoImage(file = "images/refresh_E.png")
photo9 = PhotoImage(file = "images/sum.png")
photo10 = PhotoImage(file = "images/text-message.png")

settingsframe=Frame(tab10, relief=GROOVE, bg="#f8f8f2")
settingsframe.pack(side="top", fill=BOTH)
  
settframe=Frame(settingsframe, bg="#f5f3f2", height=60)
settframe.pack(side="top", fill=X)

pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=(5, 2))
pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=(0, 5))

    
addcustomerIcon = ImageTk.PhotoImage(Image.open("images/user_add.png"))
addcustomerLabel = Button(settframe,compound="top", text="Save\nSettings",relief=RAISED,    command="",image=saves, font=("arial", 8),bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
addcustomerLabel.pack(side="left", pady=3, ipadx=4)
pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=(0, 5))

editcustomerIcon = ImageTk.PhotoImage(Image.open("images/user_edit.png"))
editcustomerLabel = Button(settframe,compound="top", text="Quick\nStart Wizard",relief=RAISED,command="",  image=editcustomerIcon,  font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
editcustomerLabel.pack(side="left")

deletecustomerIcon = ImageTk.PhotoImage(Image.open("images/user_delete.png"))
deletecustomerLabel = Button(settframe,compound="top", text="Company\nManager",relief=RAISED, command="", image=deletecustomerIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
deletecustomerLabel.pack(side="left")

pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=5)

previewinvoiceIcon = ImageTk.PhotoImage(Image.open("images/priewok.png"))
previewinvoiceLabel = Button(settframe,compound="top",command="", text="Optimize\nData tables", relief=RAISED,               image=previewinvoiceIcon, font=("arial", 8),bg="#f8f8f2", fg="black",  height=55, bd=1, width=55)
previewinvoiceLabel.pack(side="left")

printinvoiceIcon = ImageTk.PhotoImage(Image.open("images/printer.png"))
printinvoiceLabel = Button(settframe,compound="top", text="Repair\nDatabase",relief=RAISED,  command="",  image=printinvoiceIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
printinvoiceLabel.pack(side="left")

pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=5)

emailinviceIcon = ImageTk.PhotoImage(Image.open("images/gmail.png"))
emailinviceLabel = Button(settframe,compound="top",command="", text="Backup\nDatabase", relief=RAISED,               image=emailinviceIcon, font=("arial", 8),bg="#f8f8f2", fg="black",height=55,   bd=1, width=55)
emailinviceLabel.pack(side="left")

refreshcustomerIcon = ImageTk.PhotoImage(Image.open("images/refresh.png"))
refreshcustomerLabel = Button(settframe,compound="top", command="",text="Restore\nDatabase", relief=RAISED,               image=refreshcustomerIcon, font=("arial", 8),bg="#f8f8f2", fg="black",  height=55, bd=1, width=55)
refreshcustomerLabel.pack(side="left")

pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=5)

smsIcon = ImageTk.PhotoImage(Image.open("images/text-message.png"))
smsLabel = Button(settframe,compound="top", text="Serach\nfor Updates",command="", relief=RAISED,  image=smsIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
smsLabel.pack(side="left")

pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=5)

importcustomerIcon = ImageTk.PhotoImage(Image.open("images/import.png"))
importcustomerLabel = Button(settframe,compound="top", text="Enter licence\nKey Code",command="", relief=RAISED, image=importcustomerIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1,  width=55)
importcustomerLabel.pack(side="left")

pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=5)

exportcustomerIcon = ImageTk.PhotoImage(Image.open("images/export.png"))
exportcustomerLabel = Button(settframe,compound="top", text="Online\nUser Manual",command="",relief=RAISED,   image=exportcustomerIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1,width=55)
exportcustomerLabel.pack(side="left")

pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=5)

customersearchIcon = ImageTk.PhotoImage(Image.open("images/search-icon.png"))
customersearchLabel = Button(settframe,compound="top",command="", text="Upgrade to\nPro Now!", relief=RAISED,               image=customersearchIcon, font=("arial", 8),bg="#f8f8f2", fg="black",  height=55, bd=1, width=55)
customersearchLabel.pack(side="left")


invoi1label = Label(settingsframe, text="Settings", font=("arial", 18), bg="#f8f8f2")
invoi1label.pack(side="left", padx=(20,0))

m = ttk.Style()
m.theme_use('default')
m.configure('one.TNotebook.Tab', background="white", width=20, padding=10)
tabControl = ttk.Notebook(tab10,style='one.TNotebook.Tab')
tab01 = ttk.Frame(tabControl)
tab02 = ttk.Frame(tabControl)
tab03=  ttk.Frame(tabControl)
tab04 = ttk.Frame(tabControl)
tab05 = ttk.Frame(tabControl)
tab06=  ttk.Frame(tabControl)
tab07 = ttk.Frame(tabControl)
tab08 = ttk.Frame(tabControl)
tab09 =  ttk.Frame(tabControl)
tab010=  ttk.Frame(tabControl)
tabControl.add(tab01,image=invoices,compound = LEFT, text ='Miscellaneous',)
tabControl.add(tab02,image=orders,compound = LEFT, text ='Company settings')
tabControl.add(tab03,image=estimates,compound = LEFT, text ='Invoiced settings')
tabControl.add(tab04,image=recurring,compound = LEFT, text ='Order settings')
tabControl.add(tab05,image=purchase,compound = LEFT, text ='Estimate settings') 
tabControl.add(tab06,image=expenses,compound = LEFT, text ='Administrator panel')
tabControl.add(tab07,image=customer,compound = LEFT, text ='Advanced settings')
tabControl.add(tab08,image=product,compound = LEFT, text ='Email templates')
tabControl.add(tab09,image=reports,compound = LEFT, text ='Payments')
tabControl.add(tab010,image=setting,compound = LEFT, text ='Purchase Order')
tabControl.pack(expand = 1, fill ="both")


################### tab05 ###################################
firsttab1=Frame(tab05, relief=GROOVE, bg="#f8f8f2")
firsttab1.pack(side="top", fill=BOTH)

firsttab=Frame(firsttab1, bg="#f5f3f2", height=700)
firsttab.pack(side="top", fill=BOTH)

ver = Label(firsttab,text="Estimate# prefix")
ver.place(x=5,y=40)

lbx = Listbox(firsttab1, height=1)
lbx.insert(END, "EST")
lbx.place(x=100,y=40)

ver = Label(firsttab,text="Starting estimate number")
ver.place(x=25,y=80)

spin1 = Spinbox(firsttab,from_=1,to=1000000,width=15)
spin1.place(x=50,y=100)

ver = Label(firsttab,text="Header box background color")
ver.place(x=5,y=140)

win_menu = StringVar()
winstyle = ttk.Combobox(firsttab,textvariable=win_menu)
winstyle.place(x=6 ,y=160)
winstyle['values'] = ('Default','Black','Maroon','Green','Olive','Navy','Purple','Teal','Gray','Silver','Red','Lime','Yellow','Blue','Fuchsia','Aqua','White','ScrollBar','Background','ActiveCaption','InactiveCaption','Menu','Window','WindowFrame','MenuText','WindowText','CaptionText','ActiveBorder','InactiveBorder','AppWorkSpace','Highlight','HighlightText','BtnFace','InactiveCaptionText','BtnHighlight','3DDkShadow','3DLight','InfoText','InfoBk','Custom')
winstyle.current(0)

ver = Label(firsttab,text="Customize Estimate text labels")
ver.place(x=5,y=190)

lbx = Listbox(firsttab1, height=8, width=25)
lbx.insert(END, "Estimate")
lbx.insert(END, "Estimate#")
lbx.insert(END, "Estimate date")
lbx.insert(END, "Due date")
lbx.insert(END, "Estimate to")
lbx.insert(END, "Estimate total")
lbx.place(x=5,y=220)

ver = Label(firsttab,text="Default Estimate template(example,click on preview for mouse scrolling)")
ver.place(x=248,y=55 )

ver = Label(firsttab,text="Default Estimate template")
ver.place(x=619,y=40)

win_menu = StringVar()
winstyle = ttk.Combobox(firsttab,textvariable=win_menu)
winstyle.place(x=770 ,y=40, width=220)
winstyle['values'] = ('Professional 1 (logo on left side)','Professional 2 (logo on right side)','Simplified 1 (logo on left side)','Simplified 2 (logo on right side)','Business Classic')
winstyle.current(0)

messagelbframe=LabelFrame(firsttab,text="Predefined terms and conditions text for estimates", height=100, width=980)
messagelbframe.place(x=248, y=400)

txt = scrolledtext.ScrolledText(firsttab, undo=True,width=115,height=4)
txt.place(x=260,y=425)

bttermadd = Button(firsttab,text="Restore defaults")
bttermadd.place(x=32,y=450)


frame = Frame(
    firsttab,
    width=953,
    height=300
    )
frame.pack(expand=True, fill=BOTH)
frame.place(x=247,y=90)
canvas=Canvas(
    frame,
    bg='grey',
    width=953,
    height=300,
    scrollregion=(0,0,700,700)
    )

vertibar=Scrollbar(
    frame,
    orient=VERTICAL
    )
vertibar.pack(side=RIGHT,fill=Y)
vertibar.config(command=canvas.yview)
canvas.config(width=953,height=300)

canvas.config(
    yscrollcommand=vertibar.set
    )
canvas.pack(expand=True,side=LEFT,fill=BOTH)
canvas.create_rectangle(100, 20, 850, 675 , outline='yellow',fill='white')


ver = Label(firsttab,text="Title text goes here..." ,background="white")
ver.place(x=655,y=175)
ver = Label(firsttab,text="Your Company Logo" ,background="white" ,font=30)
ver.place(x=475,y=235)
ver = Label(firsttab,text="Estimate#" ,background="white")
ver.place(x=445,y=295)
ver = Label(firsttab,text="Estimate date" ,background="white")
ver.place(x=445,y=315)
ver = Label(firsttab,text="Due date" ,background="white")
ver.place(x=445,y=335)
ver = Label(firsttab,text="Terms" ,background="white")
ver.place(x=445,y=355)



################### tab07 ###################################
firsttab1=Frame(tab07, relief=GROOVE, bg="#f8f8f2")
firsttab1.pack(side="top", fill=BOTH)

firsttab=Frame(firsttab1, bg="#f5f3f2", height=700)
firsttab.pack(side="top", fill=BOTH)

messagelbframe=LabelFrame(firsttab,text="Template advanced settings", height=250, width=1150)
messagelbframe.place(x=2, y=10)

fbill = Label(firsttab,text="Template",font="arial 10 bold").place(x=20,y=30)

ver = Label(firsttab,text="Professional 1 (logo on left side)")
ver.place(x=20,y=60)

ver = Label(firsttab,text="Professional 2 (logo on right side)")
ver.place(x=20,y=90)

ver = Label(firsttab,text="Simplified 1 (logo on left side)")
ver.place(x=20,y=120)

ver = Label(firsttab,text="Simplified 2 (logo on right side)")
ver.place(x=20,y=150)

ver = Label(firsttab,text="Business Classic")
ver.place(x=20,y=180)

fbill = Label(firsttab,text="Page size",font="arial 10 bold").place(x=255,y=30)

win_menu = StringVar()
winstyle = ttk.Combobox(firsttab,textvariable=win_menu)
winstyle.place(x=225 ,y=60)
winstyle['values'] = ('Letter','A4')
winstyle.current(0)

win_menu = StringVar()
winstyle = ttk.Combobox(firsttab,textvariable=win_menu)
winstyle.place(x=225,y=90)
winstyle['values'] = ('Letter','A4')
winstyle.current(0)

win_menu = StringVar()
winstyle = ttk.Combobox(firsttab,textvariable=win_menu)
winstyle.place(x=225,y=120)
winstyle['values'] = ('Letter','A4')
winstyle.current(0)

win_menu = StringVar()
winstyle = ttk.Combobox(firsttab,textvariable=win_menu)
winstyle.place(x=225,y=150)
winstyle['values'] = ('Letter','A4')
winstyle.current(0)

win_menu = StringVar()
winstyle = ttk.Combobox(firsttab,textvariable=win_menu)
winstyle.place(x=225,y=180)
winstyle['values'] = ('Letter','A4')
winstyle.current(0)

fbill = Label(firsttab,text="Right Margin(mm)",font="arial 10 bold").place(x=450,y=30)

spin1 = Spinbox(firsttab,from_=5,to=20,width=10)
spin1.place(x=465,y=60)

spin1 = Spinbox(firsttab,from_=5,to=20,width=10)
spin1.place(x=465,y=90)

spin1 = Spinbox(firsttab,from_=5,to=20,width=10)
spin1.place(x=465,y=120)

spin1 = Spinbox(firsttab,from_=5,to=20,width=10)
spin1.place(x=465,y=150)

spin1 = Spinbox(firsttab,from_=5,to=20,width=10)
spin1.place(x=465,y=180)


fbill = Label(firsttab,text="'Invoice to'block position shift(mm)",font="arial 10 bold").place(x=650,y=30)

lbl1 = Label(firsttab, text="Left : ").place(x=651,y=60)
lbl1 = Label(firsttab, text="Left : ").place(x=651,y=90)
lbl1 = Label(firsttab, text="Left : ").place(x=651,y=120)
lbl1 = Label(firsttab, text="Left : ").place(x=651,y=150)

spin1 = Spinbox(firsttab,from_=-10,to=100,width=10)
spin1.place(x=685,y=60)

spin1 = Spinbox(firsttab,from_=-10,to=100,width=10)
spin1.place(x=685,y=90)

spin1 = Spinbox(firsttab,from_=-10,to=100,width=10)
spin1.place(x=685,y=120)

spin1 = Spinbox(firsttab,from_=-10,to=100,width=10)
spin1.place(x=685,y=150)

lbl1 = Label(firsttab, text="Top : ").place(x=785,y=60)
lbl1 = Label(firsttab, text="Top : ").place(x=785,y=90)
lbl1 = Label(firsttab, text="Top : ").place(x=785,y=120)
lbl1 = Label(firsttab, text="Top : ").place(x=785,y=150)

spin1 = Spinbox(firsttab,from_=0,to=100,width=10)
spin1.place(x=820,y=60)

spin1 = Spinbox(firsttab,from_=0,to=100,width=10)
spin1.place(x=820,y=90)

spin1 = Spinbox(firsttab,from_=0,to=100,width=10)
spin1.place(x=820,y=120)

spin1 = Spinbox(firsttab,from_=0,to=100,width=10)
spin1.place(x=820,y=150)

bttermadd = Button(firsttab,image=photo8,compound = LEFT,text="Refresh preview",width=115)
bttermadd.place(x=1000,y=50)

bttermadd = Button(firsttab,image=saves,compound = LEFT,text="Save Settings",width=115)
bttermadd.place(x=1000,y=140)

bttermadd = Button(firsttab,text="Restore defaults",width=16)
bttermadd.place(x=1000,y=180)

ver = Label(firsttab,text="By positioning 'Invoice to'block,the customer name/address can be displayed in right place in the windowed envelope. If you networking, you need to setup this on all computer.\nExample:(Left:20 and Top:10 means that shift 'Invoice to'block to right 20mm and shift down 10mm) Original position Left:0 Top:0")
ver.place(x=50,y=210)


win_menu = StringVar()
winstyle = ttk.Combobox(firsttab,textvariable=win_menu)
winstyle.place(x=2 ,y=270, width=220)
winstyle['values'] = ('Professional 1 (logo on left side)','Professional 2 (logo on right side)','Simplified 1 (logo on left side)','Simplified 2 (logo on right side)','Business Classic')
winstyle.current(0)

ver = Label(firsttab,text="Selected template preview (example, click on preview for mouse scrolling)")
ver.place(x=230,y=270)
 

#lbx = Listbox(firsttab, height=11, width=201, bg="grey")
#lbx.place(x=2,y=309)
#v1 = pdf.ShowPdf()
#v2 = v1.pdf_view(firsttab1,width = 151, height = 10)
#v2.place(x=2,y=309)

frame = Frame(
    firsttab,
    width=1200,
    height=155
    )
frame.pack(expand=True, fill=BOTH)
frame.place(x=2,y=309)
canvas=Canvas(
    frame,
    bg='grey',
    width=1200,
    height=155,
    scrollregion=(0,0,700,700)
    )

vertibar=Scrollbar(
    frame,
    orient=VERTICAL
    )
vertibar.pack(side=RIGHT,fill=Y)
vertibar.config(command=canvas.yview)
canvas.config(width=1200,height=155)

canvas.config(
    yscrollcommand=vertibar.set
    )
canvas.pack(expand=True,side=LEFT,fill=BOTH)
canvas.create_rectangle(20, 20, 1175, 680 , outline='yellow',fill='white')



root.mainloop()