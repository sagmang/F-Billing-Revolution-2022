#from ast import pattern
from calendar import c
from cgitb import enable, text
from distutils import command
from itertools import count
from pydoc import describe
from secrets import choice
from sqlite3 import enable_callback_tracebacks
import string
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.font import BOLD
from urllib.parse import parse_qs
from xml.dom.minidom import Comment, Entity
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


fbilldb = mysql.connector.connect(
    host="localhost", user="root", password="", database="fbillingsintgrtd", port="3306"
)
fbcursor = fbilldb.cursor()

ImageFile.LOAD_TRUNCATED_IMAGES = True

def reset():
  global root
  root.destroy()


# root.title("F-Billing Revolution 2022(FREE version) | Company database:fbillingdb | User:Administrator")
def log():
    global user_name1
    user_name1=username1.get()
    passwd1=password1.get()
    if user_name1=="" or passwd1=="":
        Label(text='Plz enter both username and password',fg='red').place(x=85,y=260)
    else:
        sql='SELECT * FROM users WHERE username=%s AND password=%s'
        val=(user_name1,passwd1,)
        fbcursor.execute(sql,val)
        if fbcursor.fetchone()is not None:
            mainpage()
            if user_name1 != "adminstator":
              tab06.destroy()
            else:
              pass
            root.iconify()
        else:
            messagebox.showinfo('Acess denied','Username Or Password Wrong')

  
sql = "select * from users"
fbcursor.execute(sql)
user_log = fbcursor.fetchall()
if not user_log:
  def lo():
    mainpage()
  root=Tk()
  root.geometry("500x250")
  root.resizable(False, False)
  root.eval('tk::PlaceWindow . center')
  Label(text='Wellocome to F-Billing Revolution 2022',font='arial 13 bold').place(x=100,y=40)
  submitbtn1=Button(text='OPEN NOW', width=20,height=2,command=lo,activeforeground="white",activebackground="black",font='arial 8 bold').place(x=165,y=100)             
else:
    root=Tk()
    root.geometry("1360x768")
    root.resizable(False, False)
    root.eval('tk::PlaceWindow . center')
    root.title("F-Billing Revolution 2022")
    p1 = PhotoImage(file = 'images/fbicon.png')
    root.iconphoto(False,p1)
    username1=StringVar()
    password1=StringVar()

    Label(text='Login F-Billing Revolution 2022',font='arial 13 bold').place(x=120,y=15)
    
  
    sql = "select username from users"
    fbcursor.execute(sql)
    user_log_name = fbcursor.fetchall()
    uss1=Label(text='Username').place(x=120,y=65)
    ee1 = ttk.Combobox(textvariable=username1)
    ee1.place(x=220,y=65)
    ee1["values"] = user_log_name

    pss1=Label(text='Password').place(x=120,y=105)
    ee2=Entry(textvariable=password1,show='*',width=23).place(x=220,y=105)
    
    submitbtn1=Button(text='Login', width=15,command=log,activeforeground="white",
                   activebackground="black").place(x=250,y=150)
    
  
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

est_logo = PhotoImage(file = "images/company_logo.png")

def mainpage():
  root.iconify()
  main = Toplevel()
  main.geometry("1360x730")
  p1 = PhotoImage(file = 'images/fbicon.png')
  main.iconphoto(False, p1)
  main.title("F-Billing Revolution 2022(FREE version) | Company database:fbillingdb | User:Administrator")
  s = ttk.Style()
  s.theme_use('default')
  s.configure('TNotebook.Tab', background="#999999", width=20, padding=10)
  tabControl = ttk.Notebook(main)
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

  
  

  ######################Estimate Section#####################

  # #create new order

  def estimate_create():
    estimate_pop=Toplevel(estimate_midFrame)
    estimate_pop.title("Estimate")
    estimate_pop.geometry("950x690+150+0")

    def add_new_estimate():
      estimate_number = estimate_number_entry.get()
      estdate = estimate_date_entry.get_date()
      duedate = estimate_duedate_entry.get_date()
      status = estimates_draft.cget("text")
      emailon = estimates_nev1.cget("text")
      printon = estimates_nev2.cget("text")
      #smson = 
      esttot =  estimate_total1.cget("text")
      totpaid = estimate_totalpaid1.cget("text")
      balance = estimate_balancee1.cget("text")
      extracostname = estimates_costname1.get()
      extracost = estimates_cost3.get()
      template = estimates_etemplate.get()
      salesper =  estimates_sales6.get()
      discourate = estimates_discount2.get()
      tax1 =  estimates_tax4.get()
      category = estimates_category7.get()
      businessname = estimate_combo_name1.get()
      businessaddress = estimate_addresstext2.get("1.0",END)
      shipname = estimate_shipto3.get()
      shipaddress =  estimate_ship_address4.get("1.0",END)
      cpemail = estimate_email5.get()
      cpmobileforsms = estimate_sms6.get()
      title_text = estimates_etitletext.get()
      header_text = estimates_eheader_text.get()
      footer_text = estimates_efooter_text.get()
      #comments = estimates_ecomments.get("1.0",END)
      term_of_payment = estimate_eterms.get()
      terms = estimates_eterm_text.get("1.0",END)
      # private_notes = estimates_pvt_notes.get("1.0",END)

      # private_sql = "INSERT INTO invoice_private_notes(private_notes) VALUES(%s)"
      # private_val = (private_notes,)
      # fbcursor.execute(private_sql,private_val)
      # fbilldb.commit()

      # private_get_sql = "SELECT invoicepvtnoteid FROM invoice_private_notes WHERE private_notes=%s"
      # private_get_val = (private_notes,)
      # fbcursor.execute(private_get_sql,private_get_val)
      # private_data = fbcursor.fetchone()
      # privatenoteid = 0
      # for p in private_data:
      #   pass
      # privatenoteid += p

      

      estimate_sql="INSERT INTO estimate (estimate_number,estdate,duedate,status,emailon,printon,esttot,totpaid,balance,extracostname,extracost,template, salesper,discourate,tax1, category,businessname,businessaddress,shipname, shipaddress,cpemail,cpmobileforsms,title_text, header_text,footer_text,term_of_payment,terms) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" #adding values into db
      estimate_val=(estimate_number,estdate,duedate,status,emailon,printon,esttot,totpaid,balance,extracostname,extracost,template, salesper,discourate,tax1, category,businessname,businessaddress,shipname, shipaddress,cpemail,cpmobileforsms,title_text, header_text, footer_text,term_of_payment,terms,)
      fbcursor.execute(estimate_sql,estimate_val)
      fbilldb.commit()
      messagebox.showinfo("F-Billing Revolution","Estimate saved")


    #select customer
    def estimate_custom():
      estimate_cuselection=Toplevel()
      estimate_cuselection.title("Select Customer")
      estimate_cuselection.geometry("930x650+240+10")
      estimate_cuselection.resizable(False, False)


      #add new customer
      def estimate_create1():
        estimate_ven=Toplevel(estimate_midFrame)
        estimate_ven.title("Add new vendor")
        estimate_ven.geometry("930x650+240+10")
        estimate_checkvar1=IntVar()
        estimate_checkvar2=IntVar()
        estimate_radio=IntVar()
        estimate_createFrame=Frame(estimate_ven, bg="#f5f3f2", height=650)
        estimate_createFrame.pack(side="top", fill="both")
        estimate_labelframe1 = LabelFrame(estimate_createFrame,text="Customer",bg="#f5f3f2",font=("arial",15))
        estimate_labelframe1.place(x=10,y=5,width=910,height=600)

        fbcursor.execute("SELECT * FROM Customer ORDER BY customerid DESC LIMIT 1")
        est_qury = fbcursor.fetchone()

        estimate_text1=Label(estimate_labelframe1, text="Customer ID:",bg="#f5f3f2",fg="blue").place(x=5 ,y=10)
        estimate_eid=Entry(estimate_labelframe1,width=25)
        estimate_eid.place(x=150,y=10)
        if not est_qury== None:
          id00=est_qury[0]+1
        else:
          id00=1
        estimate_eid.insert(0, id00)

        estimate_text2=Label(estimate_labelframe1, text="Category:",bg="#f5f3f2").place(x=390 ,y=10)
        estimate_e2=ttk.Combobox(estimate_labelframe1,width=25,value="Default")
        estimate_e2.place(x=460 ,y=10)
        estimate_text3=Label(estimate_labelframe1, text="Status:",bg="#f5f3f2").place(x=710 ,y=10)
        estimate_checkbtn1=Checkbutton(estimate_labelframe1,text="Active",variable=estimate_checkvar1,onvalue=1,offvalue=0,bg="#f5f3f2")
        estimate_checkbtn1.place(x=760 ,y=10)
        
        estimate_labelframe2 = LabelFrame(estimate_labelframe1,text="Invoice to (appears on invoices)",bg="#f5f3f2")
        estimate_labelframe2.place(x=5,y=40,width=420,height=150)
        estimate_name = Label(estimate_labelframe2, text="Ship to name:",bg="#f5f3f2",fg="blue").place(x=5,y=5)
        estimate_eshipto = Entry(estimate_labelframe2,width=28)
        estimate_eshipto.place(x=130,y=5)

        estimate_addr = Label(estimate_labelframe2, text="Address:",bg="#f5f3f2",fg="blue")
        estimate_addr.place(x=5,y=40)

        estimate_eshipaddr = Entry(estimate_labelframe2,width=28)
        estimate_eshipaddr.place(x=130,y=40,height=80)

        def est_btn5cpy():
          tosp=estimate_eshipto.get()
          saddres=estimate_eshipaddr.get()
          estimate_businessname1.delete(0, 'end')
          estimate_businessname1.insert(0, tosp)
          estimate_businessaddress1.delete(0,'end')
          estimate_businessaddress1.insert(0, saddres)
      
        
        estimate_btn1=Button(estimate_labelframe1,width=3,height=2,compound = LEFT,text=">>", command=est_btn5cpy)
        estimate_btn1.place(x=440, y=90)

        estimate_labelframe3 = LabelFrame(estimate_labelframe1,text="Ship to (appears on invoices)",bg="#f5f3f2")
        estimate_labelframe3.place(x=480,y=40,width=420,height=150)
        estimate_name1 = Label(estimate_labelframe3, text="Business name:",bg="#f5f3f2").place(x=5,y=5)
        estimate_businessname1 = Entry(estimate_labelframe3,width=28)
        estimate_businessname1.place(x=130,y=5)
        estimate_addr01 = Label(estimate_labelframe3, text="Address:",bg="#f5f3f2").place(x=5,y=40)
        estimate_businessaddress1 = Entry(estimate_labelframe3,width=28)
        estimate_businessaddress1.place(x=130,y=40,height=80)
        
        estimate_labelframe4 = LabelFrame(estimate_labelframe1,text="Contact",bg="#f5f3f2")
        estimate_labelframe4.place(x=5,y=195,width=420,height=150)
        estimate_name11 = Label(estimate_labelframe4, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
        estimate_ecp = Entry(estimate_labelframe4,width=28)
        estimate_ecp.place(x=130,y=5)
        estimate_email1 = Label(estimate_labelframe4, text="E-mail address:",bg="#f5f3f2",fg="blue").place(x=5,y=35)
        estimate_eemail = Entry(estimate_labelframe4,width=28)
        estimate_eemail.place(x=130,y=35)
        estimate_tel1 = Label(estimate_labelframe4, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
        estimate_etel = Entry(estimate_labelframe4,width=11)
        estimate_etel.place(x=130,y=65)
        estimate_fax1 = Label(estimate_labelframe4, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
        estimate_efax = Entry(estimate_labelframe4,width=11)
        estimate_efax.place(x=280,y=65)
        estimate_sms1 = Label(estimate_labelframe4, text="Mobile number for SMS notifications:",bg="#f5f3f2").place(x=5,y=95)
        estimate_esms = Entry(estimate_labelframe4,width=15)
        estimate_esms.place(x=248,y=95)

        def est_btncpy1():
          ecprsn1=estimate_ecp.get()
          ecemail1=estimate_eemail.get()
          eno=estimate_etel.get()
          efx=estimate_efax.get()
          estimate_ecp2.insert(0, ecprsn1)
          estimate_eemail2.insert(0, ecemail1)
          estimate_etel2.insert(0, eno)
          estimate_efax2.insert(0, efx)      

        estimate_btn11=Button(estimate_labelframe1,width=3,height=2,compound = LEFT,text=">>", command=est_btncpy1)
        estimate_btn11.place(x=440, y=250)

        
        estimate_labelframe5 = LabelFrame(estimate_labelframe1,text="Ship to contact",bg="#f5f3f2")
        estimate_labelframe5.place(x=480,y=195,width=420,height=125)
        estimate_name2 = Label(estimate_labelframe5, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
        estimate_ecp2 = Entry(estimate_labelframe5,width=28)
        estimate_ecp2.place(x=130,y=5)

        estimate_email2 = Label(estimate_labelframe5, text="E-mail address:",bg="#f5f3f2").place(x=5,y=35)
        estimate_eemail2 = Entry(estimate_labelframe5,width=28)
        estimate_eemail2.place(x=130,y=35)

        estimate_tel2 = Label(estimate_labelframe5, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
        estimate_etel2 = Entry(estimate_labelframe5,width=11)
        estimate_etel2.place(x=130,y=65)

        estimate_fax2 = Label(estimate_labelframe5, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
        estimate_efax2 = Entry(estimate_labelframe5,width=11)
        estimate_efax2.place(x=280,y=65)

        estimate_labelframe6 = LabelFrame(estimate_labelframe1,text="Contact",bg="#f5f3f2")
        estimate_labelframe6.place(x=5,y=350,width=420,height=100)
        estimate_checkbtn2=Checkbutton(estimate_labelframe6,text="Tax Exempt",variable=estimate_checkvar2,onvalue=1,offvalue=0,bg="#f5f3f2")
        estimate_checkbtn2.place(x=5 ,y=5)

        estimate_tax3 = Label(estimate_labelframe6, text="Specific Tax1 %:",bg="#f5f3f2").place(x=180,y=5)
        estimate_estax = Entry(estimate_labelframe6,width=10)
        estimate_estax.place(x=290,y=5)

        estimate_discount = Label(estimate_labelframe6, text="Discount%:",bg="#f5f3f2").place(x=5,y=35)
        estimate_edis = Entry(estimate_labelframe6,width=10)
        estimate_edis.place(x=100,y=35)

        estimate_labelframe7 = LabelFrame(estimate_labelframe1,text="Contact",bg="#f5f3f2")
        estimate_labelframe7.place(x=480,y=330,width=420,height=100)
        estimate_country4 = Label(estimate_labelframe7, text="country:",bg="#f5f3f2").place(x=5,y=5)
        estimate_ecou2 = Entry(estimate_labelframe7,width=28)
        estimate_ecou2.place(x=130,y=5)

        estimate_city4 = Label(estimate_labelframe7, text="City:",bg="#f5f3f2").place(x=5,y=35)
        estimate_ecity2 = Entry(estimate_labelframe7,width=28)
        estimate_ecity2.place(x=130,y=35)

        estimate_labelframe8 = LabelFrame(estimate_labelframe1,text="Customer Type",bg="#f5f3f2")
        estimate_labelframe8.place(x=5,y=460,width=420,height=100)
        estimate_R1=Radiobutton(estimate_labelframe8,text=" Client ",variable=estimate_radio,value=1,bg="#f5f3f2")
        estimate_R1.place(x=5,y=15)
        estimate_R2=Radiobutton(estimate_labelframe8,text=" Vendor ",variable=estimate_radio,value=2,bg="#f5f3f2")
        estimate_R2.place(x=150,y=15)
        estimate_R3=Radiobutton(estimate_labelframe8,text=" Both(client/vendor)",variable=estimate_radio,value=3,bg="#f5f3f2")
        estimate_R3.place(x=250,y=15)
        

        estimate_labelframe9 = LabelFrame(estimate_labelframe1,text="Notes",bg="#f5f3f2")
        estimate_labelframe9.place(x=480,y=430,width=420,height=150)
        estimate_enotes = scrolledtext.ScrolledText(estimate_labelframe9, undo=True,width=47,height=7)
        estimate_enotes.place(x=10,y=10)

        estimate_btn51=Button(estimate_ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=tick ,text="OK").place(x=20, y=615)
        estimate_btn52=Button(estimate_ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=cancel,text="Cancel").place(x=800, y=615)
          
                

      estimate_enter=Label(estimate_cuselection, text="Enter filter text").place(x=5, y=10)
      estimate_e61=Entry(estimate_cuselection, width=20).place(x=110, y=10)
      estimate_text6=Label(estimate_cuselection, text="Filtered column").place(x=340, y=10)
      estimate_e26=Entry(estimate_cuselection, width=20).place(x=450, y=10)

      estimate_cusventtree=ttk.Treeview(estimate_cuselection, height=27)
      estimate_cusventtree["columns"]=["1","2","3", "4"]
      estimate_cusventtree.column("#0", width=35)
      estimate_cusventtree.column("1", width=160)
      estimate_cusventtree.column("2", width=160)
      estimate_cusventtree.column("3", width=140)
      estimate_cusventtree.column("4", width=140)
      estimate_cusventtree.heading("#0",text="")
      estimate_cusventtree.heading("1",text="Customer/Ventor ID")
      estimate_cusventtree.heading("2",text="Customer/Ventor Name")
      estimate_cusventtree.heading("3",text="Tel.")
      estimate_cusventtree.heading("4",text="Contact Person")
      estimate_cusventtree.place(x=5, y=45)

      sql_sel_est_cust = "SELECT * FROM Customer"
      fbcursor.execute(sql_sel_est_cust)
      est_customer_details = fbcursor.fetchall()

      count=0
      for i in est_customer_details:
        if True:
          estimate_cusventtree.insert(parent='',index='end',iid=i,text='',values=(i[0],i[4],i[10],i[8]))
        else:
          pass
      count += 1



      estimate_ctegorytree=ttk.Treeview(estimate_cuselection, height=27)
      estimate_ctegorytree["columns"]=["1"]
      estimate_ctegorytree.column("#0", width=35, minwidth=20)
      estimate_ctegorytree.column("1", width=205, minwidth=25, anchor=CENTER)    
      estimate_ctegorytree.heading("#0",text="", anchor=W)
      estimate_ctegorytree.heading("1",text="View filter by category", anchor=CENTER)
      estimate_ctegorytree.place(x=660, y=45)

      est_cust_fil_cat_list = Listbox(estimate_cuselection,height=34,width=40,bg="white",activestyle="dotbox",fg="black",highlightbackground="white")
      est_cust_fil_cat_list.insert(0,"               View all records")
      est_cust_fil_cat_list.insert(1,"               View only Client/Vendor")
      est_cust_fil_cat_list.insert(2,"               View only Client type")
      est_cust_fil_cat_list.insert(3,"               View only Vendor type")
      est_cust_fil_cat_list.insert(4,"               Default")
      est_cust_fil_cat_list.place(x=660,y=63)
      est_cust_fil_cat_list.bind('<<ListboxSelect>>')


      estimate_scrollbar = Scrollbar(estimate_cuselection)
      estimate_scrollbar.place(x=640, y=45, height=560)
      estimate_scrollbar.config( command=tree.yview )

      estimate_btn71=Button(estimate_cuselection,compound = LEFT,image=tick ,text="ok", width=60).place(x=15, y=610)
      estimate_btn72=Button(estimate_cuselection,compound = LEFT,image=tick,text="Edit selected customer", width=150,command=estimate_create1).place(x=250, y=610)
      estimate_btn73=Button(estimate_cuselection,compound = LEFT,image=tick, text="Add new customer", width=150,command=estimate_create1).place(x=435, y=610)
      estimate_btn74=Button(estimate_cuselection,compound = LEFT,image=cancel ,text="Cancel", width=60).place(x=740, y=610)   



      

    #add new line item
    def estimate_newline():
      estimate_newselection=Toplevel()
      estimate_newselection.title("Select Customer")
      estimate_newselection.geometry("930x650+240+10")
      estimate_newselection.resizable(False, False)


      #add new product
      def estimate_product():  
        estimate_top = Toplevel()  
        estimate_top.title("Add a new Product/Service")
        estimate_p2 = PhotoImage(file = 'images/fbicon.png')
        estimate_top.iconphoto(False, estimate_p2)
      
        estimate_top.geometry("700x550+390+15")
        estimate_tabControl = ttk.Notebook(estimate_top)
        estimate_s = ttk.Style()
        estimate_s.theme_use('default')
        estimate_s.configure('TNotebook.Tab', background="#999999",padding=10,bd=0)


        estimate_tab1 = ttk.Frame(estimate_tabControl)
        estimate_tab2 = ttk.Frame(estimate_tabControl)
      
        estimate_tabControl.add(estimate_tab1,compound = LEFT, text ='Product/Service')
        estimate_tabControl.add(estimate_tab2,compound = LEFT, text ='Product Image')
      
        estimate_tabControl.pack(expand = 1, fill ="both")
      
        estimate_innerFrame = Frame(estimate_tab1,bg="#f5f3f2", relief=GROOVE)
        estimate_innerFrame.pack(side="top",fill=BOTH)

        estimate_Customerlabelframe = LabelFrame(estimate_innerFrame,text="Product/Service",width=580,height=485)
        estimate_Customerlabelframe.pack(side="top",fill=BOTH,padx=10)

        estimate_code1=Label(estimate_Customerlabelframe,text="Code or SKU:",fg="blue",pady=10,padx=10)
        estimate_code1.place(x=20,y=0)
        estimate_codeentry = Entry(estimate_Customerlabelframe,width=35)
        estimate_codeentry.place(x=120,y=8)

        estimate_checkvarStatus=IntVar()
        estimate_status1=Label(estimate_Customerlabelframe,text="Status:")
        estimate_status1.place(x=500,y=8)
        estimate_Button1 = Checkbutton(estimate_Customerlabelframe,
                          variable = estimate_checkvarStatus,text="Active",compound="right",
                          onvalue =0 ,
                          offvalue = 1,
                        
                          width = 10)

        estimate_Button1.place(x=550,y=5)

        estimate_category1=Label(estimate_Customerlabelframe,text="Category:",pady=5,padx=10)
        estimate_category1.place(x=20,y=40)
        estimate_n = StringVar()
        estimate_country0 = ttk.Combobox(estimate_Customerlabelframe, width = 40, textvariable = estimate_n )
        
        estimate_country0['values'] = ('Default',' India',' China',' Australia',' Nigeria',' Malaysia',' Italy',' Turkey',)
        
        estimate_country0.place(x=120,y=45)
        estimate_country0.current(0)


        estimate_name81=Label(estimate_Customerlabelframe,text="Name :",fg="blue",pady=5,padx=10)
        estimate_name81.place(x=20,y=70)
        estimate_nameentry = Entry(estimate_Customerlabelframe,width=60)
        estimate_nameentry.place(x=120,y=75)

        estimate_des1=Label(estimate_Customerlabelframe,text="Description :",pady=5,padx=10)
        estimate_des1.place(x=20,y=100)
        estimate_desentry = Entry(estimate_Customerlabelframe,width=60)
        estimate_desentry.place(x=120,y=105)

        estimate_uval = IntVar(estimate_Customerlabelframe, value='$0.00')
        estimate_unit1=Label(estimate_Customerlabelframe,text="Unit Price:",fg="blue",pady=5,padx=10)
        estimate_unit1.place(x=20,y=130)
        estimate_unitentry = Entry(estimate_Customerlabelframe,width=20,textvariable=estimate_uval)
        estimate_unitentry.place(x=120,y=135)

        estimate_pcsval = IntVar(estimate_Customerlabelframe, value='$0.00')
        estimate_pcs1=Label(estimate_Customerlabelframe,text="Pcs/Weight:",fg="blue",pady=5,padx=10)
        estimate_pcs1.place(x=320,y=140)
        estimate_pcsentry = Entry(estimate_Customerlabelframe,width=20,textvariable=estimate_pcsval)
        estimate_pcsentry.place(x=410,y=140)

        estimate_costval = IntVar(estimate_Customerlabelframe, value='$0.00')
        estimate_cost1=Label(estimate_Customerlabelframe,text="Cost:",pady=5,padx=10)
        estimate_cost1.place(x=20,y=160)
        estimate_costentry = Entry(estimate_Customerlabelframe,width=20,textvariable=estimate_costval)
        estimate_costentry.place(x=120,y=165)

        estimate_priceval = IntVar(estimate_Customerlabelframe, value='$0.00')
        estimate_price1=Label(estimate_Customerlabelframe,text="(Price Cost):",pady=5,padx=10)
        estimate_price1.place(x=20,y=190)
        estimate_priceentry = Entry(estimate_Customerlabelframe,width=20,textvariable=estimate_priceval)
        estimate_priceentry.place(x=120,y=195)

        estimate_checkvarStatus2=IntVar()
      
        estimate_Button92 = Checkbutton(estimate_Customerlabelframe,variable = estimate_checkvarStatus2,
                          text="Taxable Tax1rate",compound="right",
                          onvalue =0 ,
                          offvalue = 1,
                          height=2,
                          width = 12)

        estimate_Button92.place(x=415,y=170)


        estimate_checkvarStatus3=IntVar()
      
        estimate_Button93 = Checkbutton(estimate_Customerlabelframe,variable = estimate_checkvarStatus3,
                          text="No stock Control",
                          onvalue =1 ,
                          offvalue = 0,
                          height=3,
                          width = 15)

        estimate_Button93.place(x=40,y=220)


        estimate_stockval = IntVar(estimate_Customerlabelframe, value='0')
        estimate_stock1=Label(estimate_Customerlabelframe,text="Stock:",pady=5,padx=10)
        estimate_stock1.place(x=90,y=260)
        estimate_stockentry = Entry(estimate_Customerlabelframe,width=15,textvariable=estimate_stockval)
        estimate_stockentry.place(x=150,y=265)

        estimate_lowval = IntVar(estimate_Customerlabelframe, value='0')
        estimate_low1=Label(estimate_Customerlabelframe,text="Low Stock Warning Limit:",pady=5,padx=10)
        estimate_low1.place(x=300,y=260)
        estimate_lowentry = Entry(estimate_Customerlabelframe,width=10,textvariable=estimate_lowval)
        estimate_lowentry.place(x=495,y=265)

      
        estimate_ware1=Label(estimate_Customerlabelframe,text="Warehouse:",pady=5,padx=10)
        estimate_ware1.place(x=60,y=290)
        estimate_wareentry = Entry(estimate_Customerlabelframe,width=50)
        estimate_wareentry.place(x=150,y=295)

        estimate_text10=Label(estimate_Customerlabelframe,text="Private notes(not appears on invoice):",pady=5,padx=10)
        estimate_text10.place(x=20,y=330)

        estimate_txt = scrolledtext.ScrolledText(estimate_Customerlabelframe, undo=True,width=62,height=4)
        estimate_txt.place(x=32,y=358)




        estimate_okButton = Button(estimate_innerFrame,compound = LEFT,image=tick , text ="Ok",width=60)
        estimate_okButton.pack(side=LEFT)

        estimate_cancelButton = Button(estimate_innerFrame,compound = LEFT,image=cancel ,text="Cancel",width=60)
        estimate_cancelButton.pack(side=RIGHT)

        estimate_imageFrame = Frame(estimate_tab2, relief=GROOVE,height=580)
        estimate_imageFrame.pack(side="top",fill=BOTH)

        estimate_browseimg=Label(estimate_imageFrame,text=" Browse for product image file(recommended image type:JPG,size 480x320 pixels) ",bg='#f5f3f2')
        estimate_browseimg.place(x=15,y=35)

        estimate_browsebutton=Button(estimate_imageFrame,text = 'Browse')
        estimate_browsebutton.place(x=580,y=30,height=30,width=50)
        
        estimate_removeButton = Button(estimate_imageFrame,compound = LEFT,image=cancel, text ="Remove Product Image",width=150)
        estimate_removeButton.place(x=400,y=450)



      
                      
      estimate_enter10=Label(estimate_newselection, text="Enter filter text").place(x=5, y=10)
      estimate_e10=Entry(estimate_newselection, width=20).place(x=110, y=10)
      estimate_text10=Label(estimate_newselection, text="Filtered column").place(x=340, y=10)
      estimate_e20=Entry(estimate_newselection, width=20).place(x=450, y=10)

      estimate_cusventtree1=ttk.Treeview(estimate_newselection, height=27)
      estimate_cusventtree1["columns"]=["1","2","3", "4","5"]
      estimate_cusventtree1.column("#0", width=35)
      estimate_cusventtree1.column("1", width=160)
      estimate_cusventtree1.column("2", width=160)
      estimate_cusventtree1.column("3", width=140)
      estimate_cusventtree1.column("4", width=70)
      estimate_cusventtree1.column("5", width=70)
      estimate_cusventtree1.heading("#0",text="")
      estimate_cusventtree1.heading("1",text="ID/SKU")
      estimate_cusventtree1.heading("2",text="Product/Service Name")
      estimate_cusventtree1.heading("3",text="Unit price")
      estimate_cusventtree1.heading("4",text="Service")
      estimate_cusventtree1.heading("5",text="Stock")
      estimate_cusventtree1.place(x=5, y=45)

      estimate_sql = "SELECT * FROM Productservice"
      fbcursor.execute(estimate_sql)
      est_product_details = fbcursor.fetchall()

      count = 0
      for p in est_product_details:
        if True:
          estimate_cusventtree1.insert(parent='',index='end',iid=p,text='',values=(p[0],p[4],p[7],p[12],p[13]))
        else:
          pass
      count += 1


      estimate_ctegorytree1=ttk.Treeview(estimate_newselection, height=27)
      estimate_ctegorytree1["columns"]=["1"]
      estimate_ctegorytree1.column("#0", width=35, minwidth=20)
      estimate_ctegorytree1.column("1", width=205, minwidth=25, anchor=CENTER)    
      estimate_ctegorytree1.heading("#0",text="", anchor=W)
      estimate_ctegorytree1.heading("1",text="View filter by category", anchor=CENTER)
      estimate_ctegorytree1.place(x=660, y=45)

      est_fil_cat_list = Listbox(estimate_newselection,height=34,width=40,bg="white",activestyle="dotbox",fg="black",highlightbackground="white")
      est_fil_cat_list.insert(0,"               View all Products/Services")
      est_fil_cat_list.insert(1,"               View all Products")
      est_fil_cat_list.insert(2,"               View all Services")
      est_fil_cat_list.insert(3,"               Default")
      est_fil_cat_list.place(x=660,y=63)
      est_fil_cat_list.bind('<<ListboxSelect>>')


      estimate_scrollbar10 = Scrollbar(estimate_newselection)
      estimate_scrollbar10.place(x=640, y=45, height=560)
      estimate_scrollbar10.config( command=tree.yview )
    

      estimate_btn11=Button(estimate_newselection,compound = LEFT,image=tick ,text="ok", width=60).place(x=15, y=610)
      estimate_btn11=Button(estimate_newselection,compound = LEFT,image=tick , text="Edit product/Service", width=150,command=product).place(x=250, y=610)
      estimate_btn11=Button(estimate_newselection,compound = LEFT,image=tick , text="Add product/Service", width=150,command=product).place(x=435, y=610)
      estimate_btn11=Button(estimate_newselection,compound = LEFT,image=cancel ,text="Cancel", width=60).place(x=740, y=610)



    #preview new line
    def estimate_previewline():
      messagebox.showerror("F-Billing Revolution","line is required,please select customer for this order before printing.")


    
    #sms notification
    def estimate_sms1():
      estimate_send_SMS=Toplevel()
      estimate_send_SMS.geometry("700x480+240+150")
      estimate_send_SMS.title("Send SMS notification")

      estimate_style = ttk.Style()
      estimate_style.theme_use('default')
      estimate_style.configure('TNotebook.Tab', background="#999999", padding=5)
      estimate_sms_Notebook = ttk.Notebook(estimate_send_SMS)
      estimate_SMS_Notification = Frame(estimate_sms_Notebook, height=470, width=700)
      estimate_SMS_Service_Account = Frame(estimate_sms_Notebook, height=470, width=700)
      estimate_sms_Notebook.add(estimate_SMS_Notification, text="SMS Notification")
      estimate_sms_Notebook.add(estimate_SMS_Service_Account, text="SMS Service Account")
      estimate_sms_Notebook.place(x=0, y=0)

      estimate_numlbel=Label(estimate_SMS_Notification, text="SMS number or comma seperated SMS number list(Please start each SMS number with the country code)")
      estimate_numlbel.place(x=10, y=10)
      estimate_numentry=Entry(estimate_SMS_Notification, width=92).place(x=10, y=30)
      estimate_stexbel=Label(estimate_SMS_Notification, text="SMS Text").place(x=10, y=60)
      estimate_stex=Entry(estimate_SMS_Notification, width=40).place(x=10, y=85,height=120)
      
      estimate_dclbel=Label(estimate_SMS_Notification, text="Double click to insert into text")
      estimate_dclbel.place(x=410, y=60)
      estimate_dcl=Entry(estimate_SMS_Notification, width=30)
      estimate_dcl.place(x=400, y=85,height=200)
      
      estimate_smstype=LabelFrame(estimate_SMS_Notification, text="SMS message type", width=377, height=60)
      estimate_smstype.place(x=10, y=223)
      estimate_snuvar=IntVar()
      estimate_normal_rbtn=Radiobutton(estimate_smstype, text="Normal SMS(160 chars)", variable=estimate_snuvar, value=1)
      estimate_normal_rbtn.place(x=5, y=5)
      estimate_unicode_rbtn=Radiobutton(estimate_smstype, text="Unicode SMS(70 chars)", variable=estimate_snuvar, value=2)
      estimate_unicode_rbtn.place(x=190, y=5)
      estimate_tiplbf=LabelFrame(estimate_SMS_Notification, text="Tips", width=680, height=120)
      estimate_tiplbf.place(x=10, y=290)
      estimate_tiplabl=Label(estimate_tiplbf,justify=LEFT,fg="red",  text="Always start the SMS nymber with the country code. Do not use the + sign at the beginning(example\nUS number:8455807546). Do not use any special characters in your normal SMS text. Please use the\nstndard SMS characters or the English alphabet and numbers only. Otherwise the SMS will be\nunreadable or undeliverable. If you need to enter international characters, accents,email address, or\nspecial characters to the SMS text field then choose the Unicode SMS format.")
      estimate_tiplabl.place(x=5, y=5)

      estimate_btnn1=Button(estimate_SMS_Notification, width=20, text="Send SMS notification").place(x=10, y=420)
      estimate_btnn2=Button(estimate_SMS_Notification, width=25, text="Confirm SMS cost before sending").place(x=280, y=420)
      estimate_btnn3=Button(estimate_SMS_Notification, width=15, text="Cancel").place(x=550, y=420)
      

      estimate_smstypee=LabelFrame(estimate_SMS_Service_Account, text="Select the notification service provider", width=670, height=65)
      estimate_smstypee.place(x=10, y=5)
      estimate_snumvarr=IntVar()
      estimate_normal_rbtn=Radiobutton(estimate_smstypee,text="BULKSMS(www.bulksms.com)",variable=estimate_snumvarr,value=1,)
      estimate_normal_rbtn.place(x=5, y=5)
      estimate_unicode_rbtn=Radiobutton(estimate_smstypee, text="Unicode SMS(70 chars)-Recommended", variable=estimate_snumvarr, value=2)
      estimate_unicode_rbtn.place(x=290, y=5)

      estimate_sms1type=LabelFrame(estimate_SMS_Service_Account, text="Your BULKSMS.COM Account", width=670, height=100)
      estimate_sms1type.place(x=10, y=80)
      estimate_namee=Label(estimate_sms1type, text="Username").place(x=10, y=5)
      estimate_na=Entry(estimate_sms1type, width=20).place(x=100, y=5)
      estimate_password=Label(estimate_sms1type, text="Password").place(x=10, y=45)
      estimate_pas=Entry(estimate_sms1type, width=20).place(x=100, y=45)
      estimate_combo=Label(estimate_sms1type, text="Route").place(x=400, y=5)
      estimate_nn = StringVar()
      estimate_combo1 = ttk.Combobox(estimate_sms1type, width = 20, textvariable = estimate_nn ).place(x=450,y=5)
      estimate_btnnn1=Button(estimate_sms1type, width=10, text="Save settings").place(x=550, y=45)

      
      estimate_tiplbf=LabelFrame(estimate_SMS_Service_Account, text="Terms of service", width=680, height=250)
      estimate_tiplbf.place(x=10, y=190)
      estimate_tiplabl=Label(estimate_tiplbf,justify=LEFT,fg="red",  text="The SMS notification service is not free.This service costs you creadit.You must have your own account\nat BULKSMS.COM and you need to have sufficient creadit and an active internet connection to use\nthis feature.Please review all fields in this form for accuracy")
      estimate_tiplabl.place(x=0, y=5)
      estimate_tiplabl1=Label(estimate_tiplbf,justify=LEFT,fg="black",  text="visit www.bulksms.com website to create your own account.please make sure the BULKSMS .COM\n service works well in your country before you busy creadit")
      estimate_tiplabl1.place(x=0, y=60)
      estimate_tiplabl2=Label(estimate_tiplbf,justify=LEFT,fg="black",  text="Our SMS notification tool comes without any warranty.our software only forwards your SMS message\nthe BULKSMS API server .The BULKSMS API server will try to sent SMS message your recipient")
      estimate_tiplabl2.place(x=0, y=100)
      estimate_tiplabl3=Label(estimate_tiplbf,justify=LEFT,fg="red",  text="Please note that you access and use the SMS notification tool your own risk.F-Billing software is not\nresponsible for any type of loss or damage or undelivered SMS massage which you may as a result\nof accessing and using the SMS notification service.")
      estimate_tiplabl3.place(x=0, y=140)
      estimate_checkvarr1=IntVar()
      estimate_chkbtnn1=Checkbutton(estimate_tiplbf,text="I have read and agree to the terms of service above",variable=estimate_checkvarr1,onvalue=1,offvalue=0).place(x=70, y=200) 



    
    #delete line item  
    def estimate_delete1():
      messagebox.showerror("F-Billing Revolution","Customer is required,please select customer before deleting line item .")
      
      

    estimate_firFrame=Frame(estimate_pop, bg="#f5f3f2", height=60)
    estimate_firFrame.pack(side="top", fill=X)

    estimate_w = Canvas(estimate_firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
    estimate_w.pack(side="left", padx=5)

    estimate_create = Button(estimate_firFrame,compound="top", text="Select\nCustomer",relief=RAISED, image=customer,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=estimate_custom)
    estimate_create.pack(side="left", pady=3, ipadx=4)


    estimate_w1 = Canvas(estimate_firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
    estimate_w1.pack(side="left", padx=5)

    estimate_addd= Button(estimate_firFrame,compound="top", text="Add new\nline item",relief=RAISED, image=photo,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=estimate_newline)
    estimate_addd.pack(side="left", pady=3, ipadx=4)

    estimate_dele= Button(estimate_firFrame,compound="top", text="Delete line\nitem",relief=RAISED, image=photo2,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=estimate_delete1)
    estimate_dele.pack(side="left", pady=3, ipadx=4)

    estimate_w2 = Canvas(estimate_firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
    estimate_w2.pack(side="left", padx=5)

    estimate_prev= Button(estimate_firFrame,compound="top", text="Preview\nEstimate",relief=RAISED, image=photo4,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=estimate_previewline)
    estimate_prev.pack(side="left", pady=3, ipadx=4)

    estimate_prin= Button(estimate_firFrame,compound="top", text="Print \nEstimate",relief=RAISED, image=photo5,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=estimate_printsele)
    estimate_prin.pack(side="left", pady=3, ipadx=4)

    estimate_w3 = Canvas(estimate_firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
    estimate_w3.pack(side="left", padx=5)

    estimate_mail= Button(estimate_firFrame,compound="top", text="Email\nEstimate",relief=RAISED, image=photo6,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=estimate_emailord)
    estimate_mail.pack(side="left", pady=3, ipadx=4)

    estimate_smss1= Button(estimate_firFrame,compound="top", text="Send SMS\nnotification",relief=RAISED, image=photo10,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=estimate_sms1)
    estimate_smss1.pack(side="left", pady=3, ipadx=4)

    estimate_w4 = Canvas(estimate_firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
    estimate_w4.pack(side="left", padx=5)

    estimate_smss1= Button(estimate_firFrame,compound="top", text="Set Status\nto Accepted",relief=RAISED, image=mark1,bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
    estimate_smss1.pack(side="left", pady=3, ipadx=4)

    estimate_smss1= Button(estimate_firFrame,compound="top", text="Set Status\nto Declined",relief=RAISED, image=mark1,bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
    estimate_smss1.pack(side="left", pady=3, ipadx=4)

    def estimate_calcu():
      subprocess.Popen('C:\\Windows\\System32\\calc.exe')

    estimate_calc= Button(estimate_firFrame,compound="top", text="Open\nCalculator",relief=RAISED, image=photo9,bg="#f5f3f2", fg="black", height=55, bd=1, width=55, command=estimate_calcu)
    estimate_calc.pack(side="left", pady=3, ipadx=4)

    estimate_save= Button(estimate_firFrame,compound="top", text="Save",relief=RAISED, image=tick,bg="#f5f3f2", fg="black", height=55, bd=1, width=55, command=add_new_estimate)
    estimate_save.pack(side="right", pady=3, ipadx=4)


    estimate_fir1Frame=Frame(estimate_pop, height=180,bg="#f5f3f2")
    estimate_fir1Frame.pack(side="top", fill=X)

    estimate_labelframee1 = LabelFrame(estimate_fir1Frame,text="Customers",font=("arial",15))
    estimate_labelframee1.place(x=10,y=5,width=640,height=160)

    def est_to_combo(event):
      global est_sel_combo
      est_to_str = est_to.get()
      sql = "SELECT * FROM Customer WHERE businessname=%s"
      val = (est_to_str,)
      fbcursor.execute(sql,val)
      est_sel_combo = fbcursor.fetchone()
      estimate_addresstext2.delete('1.0',END)
      estimate_addresstext2.insert('1.0',est_sel_combo[5])
      estimate_shipto3.delete(0, END)
      estimate_shipto3.insert(0, est_sel_combo[6])
      estimate_ship_address4.delete('1.0',END)
      estimate_ship_address4.insert('1.0',est_sel_combo[7])
      estimate_email5.delete(0,END)
      estimate_email5.insert(0,est_sel_combo[9])
      estimate_sms6.delete(0,END)
      estimate_sms6.insert(0,est_sel_combo[12])

    def est_copy_cust_details():
        estimate_shipto3.delete(0, END)
        estimate_shipto3.insert(0, est_sel_combo[4])
        estimate_ship_address4.delete('1.0',END)
        estimate_ship_address4.insert('1.0',est_sel_combo[5])


    est_sql2 = "select businessname from Customer"
    fbcursor.execute(est_sql2,)
    estodata = fbcursor.fetchall()

    estimate_orderr1 = Label(estimate_labelframee1, text="Estimate to").place(x=10,y=5)
    est_to = StringVar()
    estimate_combo_name1 = ttk.Combobox(estimate_labelframee1, width=28,textvariable=est_to)
    estimate_combo_name1.place(x=80,y=5)
    estimate_combo_name1['values'] = estodata
    estimate_combo_name1.bind("<<ComboboxSelected>>", est_to_combo)

    estimate_addresss=Label(estimate_labelframee1,text="Address").place(x=10,y=30)
    estimate_addresstext2=Text(estimate_labelframee1,width=23)
    estimate_addresstext2.place(x=80,y=30,height=70)
    estimate_shipp=Label(estimate_labelframee1,text="Ship to")
    estimate_shipp.place(x=342,y=5)
    estimate_shipto3=Entry(estimate_labelframee1,width=30)
    estimate_shipto3.place(x=402,y=3)
    estimate_addresss1=Label(estimate_labelframee1,text="Address").place(x=340,y=30)
    estimate_ship_address4=Text(estimate_labelframee1,width=23)
    estimate_ship_address4.place(x=402,y=30,height=70)

    estimate_bttn1=Button(estimate_labelframee1,width=3,height=2,compound = LEFT,text=">>",command=est_copy_cust_details)
    estimate_bttn1.place(x=280, y=50)
    
    estimate_labelframee2 = LabelFrame(estimate_fir1Frame,text="")
    estimate_labelframee2.place(x=10,y=130,width=640,height=42)
    estimate_emaill=Label(estimate_labelframee2,text="Email").place(x=10,y=5)
    estimate_email5=Entry(estimate_labelframee2,width=30)
    estimate_email5.place(x=80,y=5)
    estimate_smms=Label(estimate_labelframee2,text="SMS Number").place(x=328,y=5)
    estimate_sms6=Entry(estimate_labelframee2,width=30)
    estimate_sms6.place(x=402,y=5)
      
    estimate_labelframe = LabelFrame(estimate_fir1Frame,text="Estimate",font=("arial",15))
    estimate_labelframe.place(x=652,y=5,width=290,height=170)

    

    estimate_order0=Label(estimate_labelframe,text="Estimate#").place(x=5,y=5)
    estimate_number_entry=Entry(estimate_labelframe,width=25)
    estimate_number_entry.place(x=100,y=5,)
    estimate_number_entry.delete(0,'end')

    def est_num_increment(inum):
      result = ""
      numberStr = ""
      i = len(inum) - 1
      while i > 0:
        c = inum[i]
        if not c.isdigit():
          break
        numberStr = c + numberStr
        i -= 1
      number = int(numberStr)
      number += 1
      result += inum[0 : i + 1]
      result += "0" if number < 10 else ""
      result += str(number)
      return result
    
    fbcursor.execute("SELECT * FROM estimate ORDER BY estimateid DESC LIMIT 1")
    est_number_data = fbcursor.fetchone()
    
    if not est_number_data == None:
      a = est_number_data[1]
      est_no = est_num_increment(a)
    else:
      est_no = 1
    estimate_number_entry.insert(0,est_no)

    
    est_term_sql = "SELECT terms_of_payment FROM terms_of_payment"
    fbcursor.execute(est_term_sql,)
    est_term_data = fbcursor.fetchall()
    tdata = []
    for i in est_term_data:
      tdata.append(i[0])

    
    estimate_orderdate=Label(estimate_labelframe,text="Estimate date").place(x=5,y=33)
    estimate_date_entry=DateEntry(estimate_labelframe,width=20)
    estimate_date_entry.place(x=150,y=33)
    estimate_checkvarStatus5=IntVar()
    estimate_duedate=Checkbutton(estimate_labelframe,variable = estimate_checkvarStatus5,text="Due date",onvalue =0 ,offvalue = 1).place(x=5,y=62)
    estimate_duedate_entry=DateEntry(estimate_labelframe,width=20)
    estimate_duedate_entry.place(x=150,y=62)
    estimate_termss=Label(estimate_labelframe,text="Terms").place(x=5,y=92)
    estimate_eterms=ttk.Combobox(estimate_labelframe, value="",width=25)
    estimate_eterms.place(x=100,y=92)
    estimate_eterms['values'] = tdata
    estimate_eterms.bind("<<ComboboxSelected>>")
    estimate_reff=Label(estimate_labelframe,text="Order ref#").place(x=5,y=118)
    estimate_ee11=Entry(estimate_labelframe,width=27).place(x=100,y=118)

    estimate_fir2Frame=Frame(estimate_pop, height=150,width=100,bg="#f5f3f2")
    estimate_fir2Frame.pack(side="top", fill=X)
    estimate_listFrame = Frame(estimate_fir2Frame, bg="white", height=140,borderwidth=5,  relief=RIDGE)
    
    estimate_tree=ttk.Treeview(estimate_listFrame)
    estimate_tree["columns"]=["1","2","3","4","5","6","7","8"]

    estimate_tree.column("#0", width=40)
    estimate_tree.column("1", width=80)
    estimate_tree.column("2", width=190)
    estimate_tree.column("3", width=190)
    estimate_tree.column("4", width=80)
    estimate_tree.column("5", width=60)
    estimate_tree.column("6", width=60)
    estimate_tree.column("7", width=60)
    estimate_tree.column("8", width=80)
    
    estimate_tree.heading("#0")
    estimate_tree.heading("1",text="ID/SKU")
    estimate_tree.heading("2",text="Product/Service")
    estimate_tree.heading("3",text="Description")
    estimate_tree.heading("4",text="Unit Price")
    estimate_tree.heading("5",text="Quality")
    estimate_tree.heading("6",text="Pcs/Weight")
    estimate_tree.heading("7",text="Tax1")
    estimate_tree.heading("8",text="Price")
    
    estimate_tree.pack(fill="both", expand=1)
    estimate_listFrame.pack(side="top", fill="both", padx=5, pady=3, expand=1)

    estimate_fir3Frame=Frame(estimate_pop,height=200,width=700,bg="#f5f3f2")
    estimate_fir3Frame.place(x=0,y=490)

    estimate_tabStyle = ttk.Style()
    estimate_tabStyle.theme_use('default')
    estimate_tabStyle.configure('TNotebook.Tab', background="#999999", width=12, padding=5)
    estimate_myNotebookk=ttk.Notebook(estimate_fir3Frame)
    estimate_orderFrame = Frame(estimate_myNotebookk, height=200, width=800)
    estimate_headerFrame = Frame(estimate_myNotebookk, height=200, width=800)
    estimate_commentFrame = Frame(estimate_myNotebookk, height=200, width=800)
    estimate_termsFrame = Frame(estimate_myNotebookk, height=200, width=800)
    estimate_noteFrame = Frame(estimate_myNotebookk, height=200, width=800)
    estimate_documentFrame = Frame(estimate_myNotebookk, height=200, width=800)
    
    estimate_myNotebookk.add(estimate_orderFrame,compound="left", text="Estimate")
    estimate_myNotebookk.add(estimate_headerFrame,compound="left",  text="Header/Footer")
    estimate_myNotebookk.add(estimate_commentFrame,compound="left",  text="Comments")
    estimate_myNotebookk.add(estimate_termsFrame,compound="left", text="Terms")
    estimate_myNotebookk.add(estimate_noteFrame,compound="left",  text="Private notes")
    estimate_myNotebookk.add(estimate_documentFrame,compound="left",  text="Documents")
    estimate_myNotebookk.pack(expand = 1, fill ="both")  

    estimate_labelfram1 = LabelFrame(estimate_orderFrame,text="",font=("arial",15))
    estimate_labelfram1.place(x=1,y=1,width=800,height=170)

    est_extracost_sql = "SELECT extra_cost_name	FROM extra_cost_name"
    fbcursor.execute(est_extracost_sql,)
    est_extracost_data = fbcursor.fetchall()
    exdata = []
    for i in est_extracost_data:
      exdata.append(i[0])

    estimates_cost1=Label(estimate_labelfram1,text="Extra cost name").place(x=2,y=5)
    estimates_costname1=ttk.Combobox(estimate_labelfram1, value=exdata,width=20)
    estimates_costname1.place(x=115,y=5)

    estimates_rate=Label(estimate_labelfram1,text="Discount rate").place(x=370,y=5)
    estimates_discount2=Spinbox(estimate_labelfram1,width=6,from_=0,to=10,justify=RIGHT)
    estimates_discount2.place(x=460,y=5)

    estimates_cost2=Label(estimate_labelfram1,text="Extra cost").place(x=35,y=35)
    estimates_cost3=Entry(estimate_labelfram1,width=10)
    estimates_cost3.place(x=115,y=35)
    estimates_tax=Label(estimate_labelfram1,text="Tax1").place(x=420,y=35)
    estimates_tax4=Entry(estimate_labelfram1,width=7)
    estimates_tax4.place(x=460,y=35)
    estimates_template=Label(estimate_labelfram1,text="Template").place(x=37,y=70)

    est_temp_sql1 = "SELECT Defaultestimatetemplate FROM company "
    fbcursor.execute(est_temp_sql1,)
    est_temp_data1 = fbcursor.fetchall()
    tempdata = []
    for i in est_temp_data1:
      tempdata.append(i[0])

    # sql = "select * from estimate"
    # fbcursor.execute(sql)
    # est_sdata = fbcursor.fetchone()
    

    estimates_etemplate=ttk.Combobox(estimate_labelfram1, value=tempdata,width=25)
    estimates_etemplate.place(x=115,y=70)
    # if not est_sdata:
    #   pass
    # else:
    #   estimates_etemplate.insert(0, est_sdata[13])


    estimates_sales=Label(estimate_labelfram1,text="Sales Person").place(x=25,y=100)
    estimates_sales6=Entry(estimate_labelfram1,width=18)
    estimates_sales6.place(x=115,y=100)
    # if not est_sdata:
    #   pass
    # else:
    #   estimates_sales6.insert(0, est_sdata[14])

    estimates_category=Label(estimate_labelfram1,text="Category").place(x=300,y=100)
    estimates_category7=Entry(estimate_labelfram1,width=22)
    estimates_category7.place(x=370,y=100)
    
    estimate_statusfrme = LabelFrame(estimate_labelfram1,text="Status",font=("arial",15))
    estimate_statusfrme.place(x=540,y=0,width=160,height=160)
    estimates_draft=Label(estimate_statusfrme, text="Draft",font=("arial", 15, "bold"), fg="grey")
    estimates_draft.place(x=50, y=3)
    estimates_on1=Label(estimate_statusfrme, text="Emailed on:").place( y=50)
    estimates_nev1=Label(estimate_statusfrme, text="Never")
    estimates_nev1.place(x=100,y=50)
    estimates_on2=Label(estimate_statusfrme, text="Printed on:").place( y=90)
    estimates_nev2=Label(estimate_statusfrme, text="Never")
    estimates_nev2.place(x=100,y=90)

    est_header_sql = "SELECT headerandfooter FROM header_and_footer"
    fbcursor.execute(est_header_sql,)
    est_header_data = fbcursor.fetchall()
    hfdata = []
    for i in est_header_data:
      hfdata.append(i[0])

    estimates_text01=Label(estimate_headerFrame,text="Title text").place(x=50,y=5)
    estimates_etitletext=ttk.Combobox(estimate_headerFrame, value=hfdata,width=60)
    estimates_etitletext.place(x=125,y=5)
    estimates_etitletext.bind("<<ComboboxSelected>>")

    estimates_text02=Label(estimate_headerFrame,text="Page header text").place(x=2,y=45)
    estimates_eheader_text=ttk.Combobox(estimate_headerFrame, value=hfdata,width=60)
    estimates_eheader_text.place(x=125,y=45)
    estimates_eheader_text.bind("<<ComboboxSelected>>")

    estimates_text03=Label(estimate_headerFrame,text="Footer text").place(x=35,y=85)
    estimates_efooter_text=ttk.Combobox(estimate_headerFrame, value=hfdata,width=60)
    estimates_efooter_text.place(x=125,y=85)
    estimates_efooter_text.bind("<<ComboboxSelected>>")

    estimates_texttt=Label(estimate_noteFrame,text="Private notes(not shown on invoice/order/estemates)").place(x=10,y=10)
    estimates_pvt_notes=Text(estimate_noteFrame,width=85,height=7)
    estimates_pvt_notes.place(x=10,y=32)

    # est_term_sql = "SELECT Predefinedtextforestimates FROM company"
    # fbcursor.execute(est_term_sql,)
    # est_term_data = fbcursor.fetchall()
    # trdata = []
    # for i in est_term_data:
    #   trdata.append(i[0])
 
    estimates_eterm_text=scrolledtext.ScrolledText(estimate_termsFrame, undo=True,width=85,height=7)
    estimates_eterm_text.place(x=10,y=10)

    estimates_ecomments=Text(estimate_commentFrame,width=85,height=7)
    estimates_ecomments.place(x=10,y=10)

    estimates_btn1=Button(estimate_documentFrame,height=2,width=3,text="+").place(x=5,y=10)
    estimates_btn2=Button(estimate_documentFrame,height=2,width=3,text="-").place(x=5,y=50)
    estimates_texttt1=Label(estimate_documentFrame,text="Attached documents or image files.If you attach large email then email taken long time to send").place(x=50,y=10)
    estimates_cusventtree=ttk.Treeview(estimate_documentFrame, height=5)
    estimates_cusventtree["columns"]=["1","2","3"]
    estimates_cusventtree.column("#0", width=20)
    estimates_cusventtree.column("1", width=250)
    estimates_cusventtree.column("2", width=250)
    estimates_cusventtree.column("2", width=200)
    estimates_cusventtree.heading("#0",text="", anchor=W)
    estimates_cusventtree.heading("1",text="Attach to Email")
    estimates_cusventtree.heading("2",text="Filename")
    estimates_cusventtree.heading("3",text="Filesize")  
    estimates_cusventtree.place(x=50, y=45)
    

    estimate_fir4Frame1=Frame(estimate_pop,height=190,width=210,bg="#f5f3f2")
    estimate_fir4Frame1.place(x=740,y=520)
    estimate_summaryfrme = LabelFrame(estimate_fir4Frame1,text="Summary",font=("arial",15))
    estimate_summaryfrme.place(x=0,y=0,width=200,height=170)
    estimate_discounttt=Label(estimate_summaryfrme, text="Discount").place(x=0 ,y=0)
    estimate_discounttt1=Label(estimate_summaryfrme, text="$0.00").place(x=130 ,y=0)
    estimate_subbb=Label(estimate_summaryfrme, text="Subtotal").place(x=0 ,y=21)
    estimate_subbb1=Label(estimate_summaryfrme, text="$0.00").place(x=130 ,y=21)
    estimate_ttaax=Label(estimate_summaryfrme, text="Tax1").place(x=0 ,y=42)
    estimate_ttax1=Label(estimate_summaryfrme, text="$0.00").place(x=130 ,y=42)
    estimate_costt=Label(estimate_summaryfrme, text="Extra cost").place(x=0 ,y=63)
    estimate_costtt=Label(estimate_summaryfrme, text="$0.00").place(x=130 ,y=63)
    estimate_total=Label(estimate_summaryfrme, text="Estimate total").place(x=0 ,y=84)
    estimate_total1=Label(estimate_summaryfrme, text="$0.00")
    estimate_total1.place(x=130 ,y=84)
    estimate_totalll=Label(estimate_summaryfrme, text="Total paid").place(x=0 ,y=105)
    estimate_totalpaid1=Label(estimate_summaryfrme, text="$0.00")
    estimate_totalpaid1.place(x=130 ,y=105)
    estimate_balancee=Label(estimate_summaryfrme, text="Balance").place(x=0 ,y=126)
    estimate_balancee1=Label(estimate_summaryfrme, text="$0.00")
    estimate_balancee1.place(x=130 ,y=126)

    estimate_fir5Frame1=Frame(estimate_pop,height=38,width=210)
    estimate_fir5Frame1.place(x=735,y=485)
    estimate_btndown=Button(estimate_fir5Frame1, compound="left", text="Line Down").place(x=75, y=0)
    estimate_btnup=Button(estimate_fir5Frame1, compound="left", text="Line Up").place(x=150, y=0)
  ############################ End create new estimate #########################
  def edit_estimates_create():
    edit_estimate_pop=Toplevel(estimate_midFrame)
    edit_estimate_pop.title("Estimate")
    edit_estimate_pop.geometry("950x690+150+0")
    # edit_est_fetch = tree.item(tree.focus())["values"][1]
    sql_edit = "SELECT * FROM estimate WHERE estimate_number"
    # val_edit = (edit_est_fetch,)
    fbcursor.execute(sql_edit)
    global edit_est_data
    edit_est_data = fbcursor.fetchone()
    

    #select customer
    def edit_estimate_custom():
      edit_estimate_cuselection=Toplevel()
      edit_estimate_cuselection.title("Select Customer")
      edit_estimate_cuselection.geometry("930x650+240+10")
      edit_estimate_cuselection.resizable(False, False)


      #add new customer
      def edit_estimate_create1():
        edit_estimate_ven=Toplevel(estimate_midFrame)
        edit_estimate_ven.title("Add new vendor")
        edit_estimate_ven.geometry("930x650+240+10")
        edit_estimate_checkvar1=IntVar()
        edit_estimate_checkvar2=IntVar()
        edit_estimate_radio=IntVar()
        edit_estimate_createFrame=Frame(edit_estimate_ven, bg="#f5f3f2", height=650)
        edit_estimate_createFrame.pack(side="top", fill="both")
        edit_estimate_labelframe1 = LabelFrame(edit_estimate_createFrame,text="Customer",bg="#f5f3f2",font=("arial",15))
        edit_estimate_labelframe1.place(x=10,y=5,width=910,height=600)
        edit_estimate_text1=Label(edit_estimate_labelframe1, text="Customer ID:",bg="#f5f3f2",fg="blue").place(x=5 ,y=10)
        edit_estimate_e1=Entry(edit_estimate_labelframe1,width=25).place(x=150,y=10)
        edit_estimate_text2=Label(edit_estimate_labelframe1, text="Category:",bg="#f5f3f2").place(x=390 ,y=10)
        edit_estimate_e2=ttk.Combobox(edit_estimate_labelframe1,width=25,value="Default").place(x=460 ,y=10)
        edit_estimate_text3=Label(edit_estimate_labelframe1, text="Status:",bg="#f5f3f2").place(x=710 ,y=10)
        edit_estimate_checkbtn1=Checkbutton(edit_estimate_labelframe1,text="Active",variable=edit_estimate_checkvar1,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=760 ,y=10)
        
        edit_estimate_labelframe2 = LabelFrame(edit_estimate_labelframe1,text="Invoice to (appears on invoices)",bg="#f5f3f2")
        edit_estimate_labelframe2.place(x=5,y=40,width=420,height=150)
        edit_estimate_name = Label(edit_estimate_labelframe2, text="Ship to name:",bg="#f5f3f2",fg="blue").place(x=5,y=5)
        edit_estimate_e1 = Entry(edit_estimate_labelframe2,width=28).place(x=130,y=5)
        edit_estimate_addr = Label(edit_estimate_labelframe2, text="Address:",bg="#f5f3f2",fg="blue").place(x=5,y=40)
        edit_estimate_e2 = Entry(edit_estimate_labelframe2,width=28).place(x=130,y=40,height=80)
        
        edit_estimate_btn1=Button(edit_estimate_labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=440, y=90)

        edit_estimate_labelframe3 = LabelFrame(edit_estimate_labelframe1,text="Ship to (appears on invoices)",bg="#f5f3f2")
        edit_estimate_labelframe3.place(x=480,y=40,width=420,height=150)
        edit_estimate_name1 = Label(edit_estimate_labelframe3, text="Business name:",bg="#f5f3f2").place(x=5,y=5)
        edit_estimate_e01 = Entry(edit_estimate_labelframe3,width=28).place(x=130,y=5)
        edit_estimate_addr01 = Label(edit_estimate_labelframe3, text="Address:",bg="#f5f3f2").place(x=5,y=40)
        edit_estimate_e02 = Entry(edit_estimate_labelframe3,width=28).place(x=130,y=40,height=80)
        
        edit_estimate_labelframe4 = LabelFrame(edit_estimate_labelframe1,text="Contact",bg="#f5f3f2")
        edit_estimate_labelframe4.place(x=5,y=195,width=420,height=150)
        edit_estimate_name11 = Label(edit_estimate_labelframe4, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
        edit_estimate_e11 = Entry(edit_estimate_labelframe4,width=28).place(x=130,y=5)
        edit_estimate_email1 = Label(edit_estimate_labelframe4, text="E-mail address:",bg="#f5f3f2",fg="blue").place(x=5,y=35)
        edit_estimate_e21 = Entry(edit_estimate_labelframe4,width=28).place(x=130,y=35)
        edit_estimate_tel1 = Label(edit_estimate_labelframe4, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
        edit_estimate_e31 = Entry(edit_estimate_labelframe4,width=11).place(x=130,y=65)
        edit_estimate_fax1 = Label(edit_estimate_labelframe4, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
        edit_estimate_e41 = Entry(edit_estimate_labelframe4,width=11).place(x=280,y=65)
        edit_estimate_sms1 = Label(edit_estimate_labelframe4, text="Mobile number for SMS notifications:",bg="#f5f3f2").place(x=5,y=95)
        edit_estimate_e51 = Entry(edit_estimate_labelframe4,width=15).place(x=248,y=95)      

        edit_estimate_btn11=Button(edit_estimate_labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=440, y=250)

        
        edit_estimate_labelframe5 = LabelFrame(edit_estimate_labelframe1,text="Ship to contact",bg="#f5f3f2")
        edit_estimate_labelframe5.place(x=480,y=195,width=420,height=125)
        edit_estimate_name2 = Label(edit_estimate_labelframe5, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
        edit_estimate_e21 = Entry(edit_estimate_labelframe5,width=28).place(x=130,y=5)
        edit_estimate_email2 = Label(edit_estimate_labelframe5, text="E-mail address:",bg="#f5f3f2").place(x=5,y=35)
        edit_estimate_e22 = Entry(edit_estimate_labelframe5,width=28).place(x=130,y=35)
        edit_estimate_tel2 = Label(edit_estimate_labelframe5, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
        edit_estimate_e32 = Entry(edit_estimate_labelframe5,width=11).place(x=130,y=65)
        edit_estimate_fax2 = Label(edit_estimate_labelframe5, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
        edit_estimate_e42 = Entry(edit_estimate_labelframe5,width=11).place(x=280,y=65)

        edit_estimate_labelframe6 = LabelFrame(edit_estimate_labelframe1,text="Contact",bg="#f5f3f2")
        edit_estimate_labelframe6.place(x=5,y=350,width=420,height=100)
        edit_estimate_checkbtn2=Checkbutton(edit_estimate_labelframe6,text="Tax Exempt",variable=edit_estimate_checkvar2,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=5 ,y=5)
        edit_estimate_tax3 = Label(edit_estimate_labelframe6, text="Specific Tax1 %:",bg="#f5f3f2").place(x=180,y=5)
        edit_estimate_e31 = Entry(edit_estimate_labelframe6,width=10).place(x=290,y=5)
        edit_estimate_discount = Label(edit_estimate_labelframe6, text="Discount%:",bg="#f5f3f2").place(x=5,y=35)
        edit_estimate_e32 = Entry(edit_estimate_labelframe6,width=10).place(x=100,y=35)

        edit_estimate_labelframe7 = LabelFrame(edit_estimate_labelframe1,text="Contact",bg="#f5f3f2")
        edit_estimate_labelframe7.place(x=480,y=330,width=420,height=100)
        edit_estimate_country4 = Label(edit_estimate_labelframe7, text="country:",bg="#f5f3f2").place(x=5,y=5)
        edit_estimate_e41 = Entry(edit_estimate_labelframe7,width=28).place(x=130,y=5)
        edit_estimate_city4 = Label(edit_estimate_labelframe7, text="City:",bg="#f5f3f2").place(x=5,y=35)
        edit_estimate_e24 = Entry(edit_estimate_labelframe7,width=28).place(x=130,y=35)

        edit_estimate_labelframe8 = LabelFrame(edit_estimate_labelframe1,text="Customer Type",bg="#f5f3f2")
        edit_estimate_labelframe8.place(x=5,y=460,width=420,height=100)
        edit_estimate_R1=Radiobutton(edit_estimate_labelframe8,text=" Client ",variable=edit_estimate_radio,value=1,bg="#f5f3f2").place(x=5,y=15)
        edit_estimate_R2=Radiobutton(edit_estimate_labelframe8,text=" Vendor ",variable=edit_estimate_radio,value=2,bg="#f5f3f2").place(x=150,y=15)
        edit_estimate_R3=Radiobutton(edit_estimate_labelframe8,text=" Both(client/vendor)",variable=edit_estimate_radio,value=3,bg="#f5f3f2").place(x=250,y=15)
        

        edit_estimate_labelframe9 = LabelFrame(edit_estimate_labelframe1,text="Notes",bg="#f5f3f2")
        edit_estimate_labelframe9.place(x=480,y=430,width=420,height=150)
        edit_estimate_e51 = Entry(edit_estimate_labelframe9).place(x=10,y=10,height=100,width=390)

        edit_estimate_btn51=Button(edit_estimate_ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=tick ,text="OK").place(x=20, y=615)
        edit_estimate_btn52=Button(edit_estimate_ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=cancel,text="Cancel").place(x=800, y=615)
          
                

      edit_estimate_enter=Label(edit_estimate_cuselection, text="Enter filter text").place(x=5, y=10)
      edit_estimate_e61=Entry(edit_estimate_cuselection, width=20).place(x=110, y=10)
      edit_estimate_text6=Label(edit_estimate_cuselection, text="Filtered column").place(x=340, y=10)
      edit_estimate_e26=Entry(edit_estimate_cuselection, width=20).place(x=450, y=10)

      edit_estimate_cusventtree=ttk.Treeview(edit_estimate_cuselection, height=27)
      edit_estimate_cusventtree["columns"]=["1","2","3", "4"]
      edit_estimate_cusventtree.column("#0", width=35)
      edit_estimate_cusventtree.column("1", width=160)
      edit_estimate_cusventtree.column("2", width=160)
      edit_estimate_cusventtree.column("3", width=140)
      edit_estimate_cusventtree.column("4", width=140)
      edit_estimate_cusventtree.heading("#0",text="")
      edit_estimate_cusventtree.heading("1",text="Customer/Ventor ID")
      edit_estimate_cusventtree.heading("2",text="Customer/Ventor Name")
      edit_estimate_cusventtree.heading("3",text="Tel.")
      edit_estimate_cusventtree.heading("4",text="Contact Person")
      edit_estimate_cusventtree.place(x=5, y=45)

      sql = "SELECT * FROM Customer"
      fbcursor.execute(sql)
      edit_customer_details = fbcursor.fetchall()

      count=0
      for i in edit_customer_details:
        if True:
          edit_estimate_cusventtree.insert(parent='',index='end',iid=i,text='',values=(i[0],i[4],i[10],i[8]))
        else:
          pass
      count += 1

      def edit_cust_tree_fetch_1():
        edit_cust_tree_item_1 = edit_estimate_cusventtree.item(edit_estimate_cusventtree.focus())["values"][0]
        sql = "SELECT * FROM Customer WHERE customerid=%s"
        val = (edit_cust_tree_item_1,)
        fbcursor.execute(sql,val)
        edit_sel_cust_str_1 = fbcursor.fetchone()
        edit_estimate_ee1.delete(0, END)
        edit_estimate_ee1.insert(0,edit_sel_cust_str_1[4])
        edit_estimate_ee2.delete('1.0',END)
        edit_estimate_ee2.insert('1.0',edit_sel_cust_str_1[5])
        edit_estimate_ee3.delete(0, END)
        edit_estimate_ee3.insert(0, edit_sel_cust_str_1[6])
        edit_estimate_ee4.delete('1.0',END)
        edit_estimate_ee4.insert('1.0',edit_sel_cust_str_1[7])
        edit_estimate_ee5.delete(0,END)
        edit_estimate_ee5.insert(0,edit_sel_cust_str_1[9])
        edit_estimate_ee6.delete(0,END)
        edit_estimate_ee6.insert(0,edit_sel_cust_str_1[12])

        edit_estimate_cuselection.destroy()




      edit_estimate_ctegorytree=ttk.Treeview(edit_estimate_cuselection, height=27)
      edit_estimate_ctegorytree["columns"]=["1"]
      edit_estimate_ctegorytree.column("#0", width=35, minwidth=20)
      edit_estimate_ctegorytree.column("1", width=205, minwidth=25, anchor=CENTER)    
      edit_estimate_ctegorytree.heading("#0",text="", anchor=W)
      edit_estimate_ctegorytree.heading("1",text="View filter by category", anchor=CENTER)
      edit_estimate_ctegorytree.place(x=660, y=45)

      edit_fil_cat_list_1 = Listbox(edit_estimate_cuselection,height=34,width=40,bg="white",activestyle="dotbox",fg="black",highlightbackground="white")
      edit_fil_cat_list_1.insert(0,"               View all records")
      edit_fil_cat_list_1.insert(1,"               View only Client/Vendor")
      edit_fil_cat_list_1.insert(2,"               View only Client type")
      edit_fil_cat_list_1.insert(3,"               View only Vendor type")
      edit_fil_cat_list_1.insert(4,"               Default")
      edit_fil_cat_list_1.place(x=660,y=63)
      edit_fil_cat_list_1.bind('<<ListboxSelect>>')

      edit_estimate_scrollbar = Scrollbar(edit_estimate_cuselection)
      edit_estimate_scrollbar.place(x=640, y=45, height=560)
      edit_estimate_scrollbar.config( command=tree.yview )

      edit_estimate_btn71=Button(edit_estimate_cuselection,compound = LEFT,image=tick ,text="ok", width=60, command=edit_cust_tree_fetch_1)
      edit_estimate_btn71.place(x=15, y=610)
      edit_estimate_btn72=Button(edit_estimate_cuselection,compound = LEFT,image=tick,text="Edit selected customer", width=150,command=edit_estimate_create1).place(x=250, y=610)
      edit_estimate_btn73=Button(edit_estimate_cuselection,compound = LEFT,image=tick, text="Add new customer", width=150,command=edit_estimate_create1).place(x=435, y=610)
      edit_estimate_btn74=Button(edit_estimate_cuselection,compound = LEFT,image=cancel ,text="Cancel", width=60).place(x=740, y=610)   


    #add new line item
    def edit_estimate_newline():
      edit_estimate_newselection=Toplevel()
      edit_estimate_newselection.title("Select Customer")
      edit_estimate_newselection.geometry("930x650+240+10")
      edit_estimate_newselection.resizable(False, False)


      #add new product
      def edit_estimate_product():  
        edit_estimate_top = Toplevel()  
        edit_estimate_top.title("Add a new Product/Service")
        edit_estimate_p2 = PhotoImage(file = 'images/fbicon.png')
        edit_estimate_top.iconphoto(False, edit_estimate_p2)
      
        edit_estimate_top.geometry("700x550+390+15")
        edit_estimate_tabControl = ttk.Notebook(edit_estimate_top)
        edit_estimate_s = ttk.Style()
        edit_estimate_s.theme_use('default')
        edit_estimate_s.configure('TNotebook.Tab', background="#999999",padding=10,bd=0)


        edit_estimate_tab1 = ttk.Frame(edit_estimate_tabControl)
        edit_estimate_tab2 = ttk.Frame(edit_estimate_tabControl)
      
        edit_estimate_tabControl.add(edit_estimate_tab1,compound = LEFT, text ='Product/Service')
        edit_estimate_tabControl.add(edit_estimate_tab2,compound = LEFT, text ='Product Image')
      
        edit_estimate_tabControl.pack(expand = 1, fill ="both")
      
        edit_estimate_innerFrame = Frame(edit_estimate_tab1,bg="#f5f3f2", relief=GROOVE)
        edit_estimate_innerFrame.pack(side="top",fill=BOTH)

        edit_estimate_Customerlabelframe = LabelFrame(edit_estimate_innerFrame,text="Product/Service",width=580,height=485)
        edit_estimate_Customerlabelframe.pack(side="top",fill=BOTH,padx=10)

        edit_estimate_code1=Label(edit_estimate_Customerlabelframe,text="Code or SKU:",fg="blue",pady=10,padx=10)
        edit_estimate_code1.place(x=20,y=0)
        edit_estimate_codeentry = Entry(edit_estimate_Customerlabelframe,width=35)
        edit_estimate_codeentry.place(x=120,y=8)

        edit_estimate_checkvarStatus=IntVar()
        edit_estimate_status1=Label(edit_estimate_Customerlabelframe,text="Status:")
        edit_estimate_status1.place(x=500,y=8)
        edit_estimate_Button1 = Checkbutton(edit_estimate_Customerlabelframe,
                          variable = edit_estimate_checkvarStatus,text="Active",compound="right",
                          onvalue =0 ,
                          offvalue = 1,
                        
                          width = 10)

        edit_estimate_Button1.place(x=550,y=5)

        edit_estimate_category1=Label(edit_estimate_Customerlabelframe,text="Category:",pady=5,padx=10)
        edit_estimate_category1.place(x=20,y=40)
        edit_estimate_n = StringVar()
        edit_estimate_country0 = ttk.Combobox(edit_estimate_Customerlabelframe, width = 40, textvariable = edit_estimate_n )
        
        edit_estimate_country0['values'] = ('Default',' India',' China',' Australia',' Nigeria',' Malaysia',' Italy',' Turkey',)
        
        edit_estimate_country0.place(x=120,y=45)
        edit_estimate_country0.current(0)


        edit_estimate_name81=Label(edit_estimate_Customerlabelframe,text="Name :",fg="blue",pady=5,padx=10)
        edit_estimate_name81.place(x=20,y=70)
        edit_estimate_nameentry = Entry(edit_estimate_Customerlabelframe,width=60)
        edit_estimate_nameentry.place(x=120,y=75)

        edit_estimate_des1=Label(edit_estimate_Customerlabelframe,text="Description :",pady=5,padx=10)
        edit_estimate_des1.place(x=20,y=100)
        edit_estimate_desentry = Entry(edit_estimate_Customerlabelframe,width=60)
        edit_estimate_desentry.place(x=120,y=105)

        edit_estimate_uval = IntVar(edit_estimate_Customerlabelframe, value='$0.00')
        edit_estimate_unit1=Label(edit_estimate_Customerlabelframe,text="Unit Price:",fg="blue",pady=5,padx=10)
        edit_estimate_unit1.place(x=20,y=130)
        edit_estimate_unitentry = Entry(edit_estimate_Customerlabelframe,width=20,textvariable=edit_estimate_uval)
        edit_estimate_unitentry.place(x=120,y=135)

        edit_estimate_pcsval = IntVar(edit_estimate_Customerlabelframe, value='$0.00')
        edit_estimate_pcs1=Label(edit_estimate_Customerlabelframe,text="Pcs/Weight:",fg="blue",pady=5,padx=10)
        edit_estimate_pcs1.place(x=320,y=140)
        edit_estimate_pcsentry = Entry(edit_estimate_Customerlabelframe,width=20,textvariable=edit_estimate_pcsval)
        edit_estimate_pcsentry.place(x=410,y=140)

        edit_estimate_costval = IntVar(edit_estimate_Customerlabelframe, value='$0.00')
        edit_estimate_cost1=Label(edit_estimate_Customerlabelframe,text="Cost:",pady=5,padx=10)
        edit_estimate_cost1.place(x=20,y=160)
        edit_estimate_costentry = Entry(edit_estimate_Customerlabelframe,width=20,textvariable=edit_estimate_costval)
        edit_estimate_costentry.place(x=120,y=165)

        edit_estimate_priceval = IntVar(edit_estimate_Customerlabelframe, value='$0.00')
        edit_estimate_price1=Label(edit_estimate_Customerlabelframe,text="(Price Cost):",pady=5,padx=10)
        edit_estimate_price1.place(x=20,y=190)
        edit_estimate_priceentry = Entry(edit_estimate_Customerlabelframe,width=20,textvariable=edit_estimate_priceval)
        edit_estimate_priceentry.place(x=120,y=195)

        edit_estimate_checkvarStatus2=IntVar()
      
        edit_estimate_Button92 = Checkbutton(edit_estimate_Customerlabelframe,variable = edit_estimate_checkvarStatus2,
                          text="Taxable Tax1rate",compound="right",
                          onvalue =0 ,
                          offvalue = 1,
                          height=2,
                          width = 12)

        edit_estimate_Button92.place(x=415,y=170)


        edit_estimate_checkvarStatus3=IntVar()
      
        edit_estimate_Button93 = Checkbutton(edit_estimate_Customerlabelframe,variable = edit_estimate_checkvarStatus3,
                          text="No stock Control",
                          onvalue =1 ,
                          offvalue = 0,
                          height=3,
                          width = 15)

        edit_estimate_Button93.place(x=40,y=220)


        edit_estimate_stockval = IntVar(edit_estimate_Customerlabelframe, value='0')
        edit_estimate_stock1=Label(edit_estimate_Customerlabelframe,text="Stock:",pady=5,padx=10)
        edit_estimate_stock1.place(x=90,y=260)
        edit_estimate_stockentry = Entry(edit_estimate_Customerlabelframe,width=15,textvariable=edit_estimate_stockval)
        edit_estimate_stockentry.place(x=150,y=265)

        edit_estimate_lowval = IntVar(edit_estimate_Customerlabelframe, value='0')
        edit_estimate_low1=Label(edit_estimate_Customerlabelframe,text="Low Stock Warning Limit:",pady=5,padx=10)
        edit_estimate_low1.place(x=300,y=260)
        edit_estimate_lowentry = Entry(edit_estimate_Customerlabelframe,width=10,textvariable=edit_estimate_lowval)
        edit_estimate_lowentry.place(x=495,y=265)

      
        edit_estimate_ware1=Label(edit_estimate_Customerlabelframe,text="Warehouse:",pady=5,padx=10)
        edit_estimate_ware1.place(x=60,y=290)
        edit_estimate_wareentry = Entry(edit_estimate_Customerlabelframe,width=50)
        edit_estimate_wareentry.place(x=150,y=295)

        edit_estimate_text10=Label(edit_estimate_Customerlabelframe,text="Private notes(not appears on invoice):",pady=5,padx=10)
        edit_estimate_text10.place(x=20,y=330)

        edit_estimate_txt = scrolledtext.ScrolledText(edit_estimate_Customerlabelframe, undo=True,width=62,height=4)
        edit_estimate_txt.place(x=32,y=358)


        edit_estimate_okButton = Button(edit_estimate_innerFrame,compound = LEFT,image=tick , text ="Ok",width=60)
        edit_estimate_okButton.pack(side=LEFT)

        edit_estimate_cancelButton = Button(edit_estimate_innerFrame,compound = LEFT,image=cancel ,text="Cancel",width=60)
        edit_estimate_cancelButton.pack(side=RIGHT)

        edit_estimate_imageFrame = Frame(edit_estimate_tab2, relief=GROOVE,height=580)
        edit_estimate_imageFrame.pack(side="top",fill=BOTH)

        edit_estimate_browseimg=Label(edit_estimate_imageFrame,text=" Browse for product image file(recommended image type:JPG,size 480x320 pixels) ",bg='#f5f3f2')
        edit_estimate_browseimg.place(x=15,y=35)

        edit_estimate_browsebutton=Button(edit_estimate_imageFrame,text = 'Browse')
        edit_estimate_browsebutton.place(x=580,y=30,height=30,width=50)
        
        edit_estimate_removeButton = Button(edit_estimate_imageFrame,compound = LEFT,image=cancel, text ="Remove Product Image",width=150)
        edit_estimate_removeButton.place(x=400,y=450)

                      
      edit_estimate_enter10=Label(edit_estimate_newselection, text="Enter filter text").place(x=5, y=10)
      edit_estimate_e10=Entry(edit_estimate_newselection, width=20).place(x=110, y=10)
      edit_estimate_text10=Label(edit_estimate_newselection, text="Filtered column").place(x=340, y=10)
      edit_estimate_e20=Entry(edit_estimate_newselection, width=20).place(x=450, y=10)

      edit_estimate_cusventtree1=ttk.Treeview(edit_estimate_newselection, height=27)
      edit_estimate_cusventtree1["columns"]=["1","2","3", "4","5"]
      edit_estimate_cusventtree1.column("#0", width=35)
      edit_estimate_cusventtree1.column("1", width=160)
      edit_estimate_cusventtree1.column("2", width=160)
      edit_estimate_cusventtree1.column("3", width=140)
      edit_estimate_cusventtree1.column("4", width=70)
      edit_estimate_cusventtree1.column("5", width=70)
      edit_estimate_cusventtree1.heading("#0",text="")
      edit_estimate_cusventtree1.heading("1",text="ID/SKU")
      edit_estimate_cusventtree1.heading("2",text="Product/Service Name")
      edit_estimate_cusventtree1.heading("3",text="Unit price")
      edit_estimate_cusventtree1.heading("4",text="Service")
      edit_estimate_cusventtree1.heading("5",text="Stock")
      edit_estimate_cusventtree1.place(x=5, y=45)

      sql = "SELECT * FROM Productservice"
      fbcursor.execute(sql)
      edit_product_detail = fbcursor.fetchall()

      count = 0
      for p in edit_product_detail:
        if True:
          edit_estimate_cusventtree1.insert(parent='',index='end',iid=p,text='',values=(p[0],p[4],p[7],p[12],p[13]))
        else:
          pass
      count += 1



      edit_estimate_ctegorytree1=ttk.Treeview(edit_estimate_newselection, height=27)
      edit_estimate_ctegorytree1["columns"]=["1"]
      edit_estimate_ctegorytree1.column("#0", width=35, minwidth=20)
      edit_estimate_ctegorytree1.column("1", width=205, minwidth=25, anchor=CENTER)    
      edit_estimate_ctegorytree1.heading("#0",text="", anchor=W)
      edit_estimate_ctegorytree1.heading("1",text="View filter by category", anchor=CENTER)
      edit_estimate_ctegorytree1.place(x=660, y=45)

      edit_cust_fil_cat_list_1 = Listbox(edit_estimate_newselection,height=34,width=40,bg="white",activestyle="dotbox",fg="black",highlightbackground="white")
      edit_cust_fil_cat_list_1.insert(0,"               View all records")
      edit_cust_fil_cat_list_1.insert(1,"               View only Client/Vendor")
      edit_cust_fil_cat_list_1.insert(2,"               View only Client type")
      edit_cust_fil_cat_list_1.insert(3,"               View only Vendor type")
      edit_cust_fil_cat_list_1.insert(4,"               Default")
      edit_cust_fil_cat_list_1.place(x=660,y=63)
      edit_cust_fil_cat_list_1.bind('<<ListboxSelect>>')

      edit_estimate_scrollbar10 = Scrollbar(edit_estimate_newselection)
      edit_estimate_scrollbar10.place(x=640, y=45, height=560)
      edit_estimate_scrollbar10.config( command=tree.yview )
    

      edit_estimate_btn11=Button(edit_estimate_newselection,compound = LEFT,image=tick ,text="ok", width=60).place(x=15, y=610)
      edit_estimate_btn11=Button(edit_estimate_newselection,compound = LEFT,image=tick , text="Edit product/Service", width=150,command=product).place(x=250, y=610)
      edit_estimate_btn11=Button(edit_estimate_newselection,compound = LEFT,image=tick , text="Add product/Service", width=150,command=product).place(x=435, y=610)
      edit_estimate_btn11=Button(edit_estimate_newselection,compound = LEFT,image=cancel ,text="Cancel", width=60).place(x=740, y=610)



    #preview new line
    def edit_estimate_previewline():
      messagebox.showerror("F-Billing Revolution","line is required,please select customer for this order before printing.")


    
    #sms notification
    def edit_estimate_sms1():
      edit_estimate_send_SMS=Toplevel()
      edit_estimate_send_SMS.geometry("700x480+240+150")
      edit_estimate_send_SMS.title("Send SMS notification")

      edit_estimate_style = ttk.Style()
      edit_estimate_style.theme_use('default')
      edit_estimate_style.configure('TNotebook.Tab', background="#999999", padding=5)
      edit_estimate_sms_Notebook = ttk.Notebook(edit_estimate_send_SMS)
      edit_estimate_SMS_Notification = Frame(edit_estimate_sms_Notebook, height=470, width=700)
      edit_estimate_SMS_Service_Account = Frame(edit_estimate_sms_Notebook, height=470, width=700)
      edit_estimate_sms_Notebook.add(edit_estimate_SMS_Notification, text="SMS Notification")
      edit_estimate_sms_Notebook.add(edit_estimate_SMS_Service_Account, text="SMS Service Account")
      edit_estimate_sms_Notebook.place(x=0, y=0)

      edit_estimate_numlbel=Label(edit_estimate_SMS_Notification, text="SMS number or comma seperated SMS number list(Please start each SMS number with the country code)")
      edit_estimate_numlbel.place(x=10, y=10)
      edit_estimate_numentry=Entry(edit_estimate_SMS_Notification, width=92).place(x=10, y=30)
      edit_estimate_stexbel=Label(edit_estimate_SMS_Notification, text="SMS Text").place(x=10, y=60)
      edit_estimate_stex=Entry(edit_estimate_SMS_Notification, width=40).place(x=10, y=85,height=120)
      
      edit_estimate_dclbel=Label(edit_estimate_SMS_Notification, text="Double click to insert into text")
      edit_estimate_dclbel.place(x=410, y=60)
      edit_estimate_dcl=Entry(edit_estimate_SMS_Notification, width=30)
      edit_estimate_dcl.place(x=400, y=85,height=200)
      
      edit_estimate_smstype=LabelFrame(edit_estimate_SMS_Notification, text="SMS message type", width=377, height=60)
      edit_estimate_smstype.place(x=10, y=223)
      edit_estimate_snuvar=IntVar()
      edit_estimate_normal_rbtn=Radiobutton(edit_estimate_smstype, text="Normal SMS(160 chars)", variable=edit_estimate_snuvar, value=1)
      edit_estimate_normal_rbtn.place(x=5, y=5)
      edit_estimate_unicode_rbtn=Radiobutton(edit_estimate_smstype, text="Unicode SMS(70 chars)", variable=edit_estimate_snuvar, value=2)
      edit_estimate_unicode_rbtn.place(x=190, y=5)
      edit_estimate_tiplbf=LabelFrame(edit_estimate_SMS_Notification, text="Tips", width=680, height=120)
      edit_estimate_tiplbf.place(x=10, y=290)
      edit_estimate_tiplabl=Label(edit_estimate_tiplbf,justify=LEFT,fg="red",  text="Always start the SMS nymber with the country code. Do not use the + sign at the beginning(example\nUS number:8455807546). Do not use any special characters in your normal SMS text. Please use the\nstndard SMS characters or the English alphabet and numbers only. Otherwise the SMS will be\nunreadable or undeliverable. If you need to enter international characters, accents,email address, or\nspecial characters to the SMS text field then choose the Unicode SMS format.")
      edit_estimate_tiplabl.place(x=5, y=5)

      edit_estimate_btnn1=Button(edit_estimate_SMS_Notification, width=20, text="Send SMS notification").place(x=10, y=420)
      edit_estimate_btnn2=Button(edit_estimate_SMS_Notification, width=25, text="Confirm SMS cost before sending").place(x=280, y=420)
      edit_estimate_btnn3=Button(edit_estimate_SMS_Notification, width=15, text="Cancel").place(x=550, y=420)
      

      edit_estimate_smstypee=LabelFrame(edit_estimate_SMS_Service_Account, text="Select the notification service provider", width=670, height=65)
      edit_estimate_smstypee.place(x=10, y=5)
      edit_estimate_snumvarr=IntVar()
      edit_estimate_normal_rbtn=Radiobutton(edit_estimate_smstypee,text="BULKSMS(www.bulksms.com)",variable=edit_estimate_snumvarr,value=1,)
      edit_estimate_normal_rbtn.place(x=5, y=5)
      edit_estimate_unicode_rbtn=Radiobutton(edit_estimate_smstypee, text="Unicode SMS(70 chars)-Recommended", variable=edit_estimate_snumvarr, value=2)
      edit_estimate_unicode_rbtn.place(x=290, y=5)

      edit_estimate_sms1type=LabelFrame(edit_estimate_SMS_Service_Account, text="Your BULKSMS.COM Account", width=670, height=100)
      edit_estimate_sms1type.place(x=10, y=80)
      edit_estimate_namee=Label(edit_estimate_sms1type, text="Username").place(x=10, y=5)
      edit_estimate_na=Entry(edit_estimate_sms1type, width=20).place(x=100, y=5)
      edit_estimate_password=Label(edit_estimate_sms1type, text="Password").place(x=10, y=45)
      edit_estimate_pas=Entry(edit_estimate_sms1type, width=20).place(x=100, y=45)
      edit_estimate_combo=Label(edit_estimate_sms1type, text="Route").place(x=400, y=5)
      edit_estimate_nn = StringVar()
      edit_estimate_combo1 = ttk.Combobox(edit_estimate_sms1type, width = 20, textvariable = edit_estimate_nn ).place(x=450,y=5)
      edit_estimate_btnnn1=Button(edit_estimate_sms1type, width=10, text="Save settings").place(x=550, y=45)

      
      edit_estimate_tiplbf=LabelFrame(edit_estimate_SMS_Service_Account, text="Terms of service", width=680, height=250)
      edit_estimate_tiplbf.place(x=10, y=190)
      edit_estimate_tiplabl=Label(edit_estimate_tiplbf,justify=LEFT,fg="red",  text="The SMS notification service is not free.This service costs you creadit.You must have your own account\nat BULKSMS.COM and you need to have sufficient creadit and an active internet connection to use\nthis feature.Please review all fields in this form for accuracy")
      edit_estimate_tiplabl.place(x=0, y=5)
      edit_estimate_tiplabl1=Label(edit_estimate_tiplbf,justify=LEFT,fg="black",  text="visit www.bulksms.com website to create your own account.please make sure the BULKSMS .COM\n service works well in your country before you busy creadit")
      edit_estimate_tiplabl1.place(x=0, y=60)
      edit_estimate_tiplabl2=Label(edit_estimate_tiplbf,justify=LEFT,fg="black",  text="Our SMS notification tool comes without any warranty.our software only forwards your SMS message\nthe BULKSMS API server .The BULKSMS API server will try to sent SMS message your recipient")
      edit_estimate_tiplabl2.place(x=0, y=100)
      edit_estimate_tiplabl3=Label(edit_estimate_tiplbf,justify=LEFT,fg="red",  text="Please note that you access and use the SMS notification tool your own risk.F-Billing software is not\nresponsible for any type of loss or damage or undelivered SMS massage which you may as a result\nof accessing and using the SMS notification service.")
      edit_estimate_tiplabl3.place(x=0, y=140)
      edit_estimate_checkvarr1=IntVar()
      edit_estimate_chkbtnn1=Checkbutton(edit_estimate_tiplbf,text="I have read and agree to the terms of service above",variable=estimate_checkvarr1,onvalue=1,offvalue=0).place(x=70, y=200) 

    
    #delete line item  
    def edit_estimate_delete1():
      messagebox.showerror("F-Billing Revolution","Customer is required,please select customer before deleting line item .")
      
      

    edit_estimate_firFrame=Frame(edit_estimate_pop, bg="#f5f3f2", height=60)
    edit_estimate_firFrame.pack(side="top", fill=X)

    edit_estimate_w = Canvas(edit_estimate_firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
    edit_estimate_w.pack(side="left", padx=5)

    edit_estimate_create = Button(edit_estimate_firFrame,compound="top", text="Select\nCustomer",relief=RAISED, image=customer,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=edit_estimate_custom)
    edit_estimate_create.pack(side="left", pady=3, ipadx=4)


    edit_estimate_w1 = Canvas(edit_estimate_firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
    edit_estimate_w1.pack(side="left", padx=5)

    edit_estimate_addd= Button(edit_estimate_firFrame,compound="top", text="Add new\nline item",relief=RAISED, image=photo,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=edit_estimate_newline)
    edit_estimate_addd.pack(side="left", pady=3, ipadx=4)

    edit_estimate_dele= Button(edit_estimate_firFrame,compound="top", text="Delete line\nitem",relief=RAISED, image=photo2,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=edit_estimate_delete1)
    edit_estimate_dele.pack(side="left", pady=3, ipadx=4)

    edit_estimate_w2 = Canvas(edit_estimate_firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
    edit_estimate_w2.pack(side="left", padx=5)

    edit_estimate_prev= Button(edit_estimate_firFrame,compound="top", text="Preview\nEstimate",relief=RAISED, image=photo4,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=edit_estimate_previewline)
    edit_estimate_prev.pack(side="left", pady=3, ipadx=4)

    edit_estimate_prin= Button(edit_estimate_firFrame,compound="top", text="Print \nEstimate",relief=RAISED, image=photo5,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=estimate_printsele)
    edit_estimate_prin.pack(side="left", pady=3, ipadx=4)

    edit_estimate_w3 = Canvas(edit_estimate_firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
    edit_estimate_w3.pack(side="left", padx=5)

    edit_estimate_mail= Button(edit_estimate_firFrame,compound="top", text="Email\nEstimate",relief=RAISED, image=photo6,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=estimate_emailord)
    edit_estimate_mail.pack(side="left", pady=3, ipadx=4)

    edit_estimate_smss1= Button(edit_estimate_firFrame,compound="top", text="Send SMS\nnotification",relief=RAISED, image=photo10,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=edit_estimate_sms1)
    edit_estimate_smss1.pack(side="left", pady=3, ipadx=4)

    edit_estimate_w4 = Canvas(edit_estimate_firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
    edit_estimate_w4.pack(side="left", padx=5)

    edit_estimate_smss1= Button(edit_estimate_firFrame,compound="top", text="Set Status\nto Accepted",relief=RAISED, image=mark1,bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
    edit_estimate_smss1.pack(side="left", pady=3, ipadx=4)

    edit_estimate_smss1= Button(edit_estimate_firFrame,compound="top", text="Set Status\nto Declined",relief=RAISED, image=mark1,bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
    edit_estimate_smss1.pack(side="left", pady=3, ipadx=4)

    def edit_calcu():
      subprocess.Popen('C:\\Windows\\System32\\calc.exe')

    edit_estimate_calc= Button(edit_estimate_firFrame,compound="top", text="Open\nCalculator",relief=RAISED, image=photo9,bg="#f5f3f2", fg="black", height=55, bd=1, width=55, command=edit_calcu)
    edit_estimate_calc.pack(side="left", pady=3, ipadx=4)

    edit_estimate_save= Button(edit_estimate_firFrame,compound="top", text="Save",relief=RAISED, image=tick,bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
    edit_estimate_save.pack(side="right", pady=3, ipadx=4)


    edit_estimate_fir1Frame=Frame(edit_estimate_pop, height=180,bg="#f5f3f2")
    edit_estimate_fir1Frame.pack(side="top", fill=X)

    edit_estimate_labelframee1 = LabelFrame(edit_estimate_fir1Frame,text="Customers",font=("arial",15))
    edit_estimate_labelframee1.place(x=10,y=5,width=640,height=160)

    def est_to_combo_1(event):
      global inv_sel_combo_1
      est_to_str_1 = edit_to.get()
      sql = "SELECT * FROM Customer WHERE businessname=%s"
      val = (est_to_str_1,)
      fbcursor.execute(sql,val)
      est_sel_combo_1 = fbcursor.fetchone()
      edit_estimate_ee2.delete('1.0',END)
      edit_estimate_ee2.insert('1.0',est_sel_combo_1[5])
      edit_estimate_ee3.delete(0, END)
      edit_estimate_ee3.insert(0, est_sel_combo_1[6])
      edit_estimate_ee4.delete('1.0',END)
      edit_estimate_ee4.insert('1.0',est_sel_combo_1[7])
      edit_estimate_ee5.delete(0,END)
      edit_estimate_ee5.insert(0,est_sel_combo_1[9])
      edit_estimate_ee6.delete(0,END)
      edit_estimate_ee6.insert(0,est_sel_combo_1[12])


    def edit_copy_cust_details_1():
      est_to_str_2 = edit_to.get()
      if est_to_str_2 != "":
        sql = "SELECT * FROM Customer WHERE businessname=%s"
        val = (est_to_str_2,)
        fbcursor.execute(sql,val)
        est_sel_combo_2 = fbcursor.fetchone()
        edit_estimate_ee3.delete(0, END)
        edit_estimate_ee3.insert(0, est_sel_combo_2[6])
        edit_estimate_ee4.delete('1.0',END)
        edit_estimate_ee4.insert('1.0',est_sel_combo_2[7])
      else:
        edit_estimate_ee3.delete(0, END)
        edit_estimate_ee3.insert(0, edit_est_data[24])
        edit_estimate_ee4.delete('1.0',END)
        edit_estimate_ee4.insert('1.0',edit_est_data[25])


    sql = "select businessname from Customer"
    fbcursor.execute(sql,)
    edit_cdata = fbcursor.fetchall()

    edit_estimate_orderr1 = Label(edit_estimate_labelframee1, text="Estimate to").place(x=10,y=5)
    edit_to = StringVar()
    edit_estimate_ee1 = ttk.Combobox(edit_estimate_labelframee1,width=28,textvariable=edit_to)
    edit_estimate_ee1.place(x=80,y=5)
    edit_estimate_ee1['values'] = edit_cdata
    edit_estimate_ee1.bind("<<ComboboxSelected>>", est_to_combo_1)

    edit_estimate_addresss=Label(edit_estimate_labelframee1,text="Address").place(x=10,y=30)
    edit_estimate_ee2=Text(edit_estimate_labelframee1,width=23)
    edit_estimate_ee2.place(x=80,y=30,height=70)

    edit_estimate_shipp=Label(edit_estimate_labelframee1,text="Ship to").place(x=342,y=5)
    edit_estimate_ee3=Entry(edit_estimate_labelframee1,width=30)
    edit_estimate_ee3.place(x=402,y=3)

    edit_estimate_addresss1=Label(edit_estimate_labelframee1,text="Address").place(x=340,y=30)
    edit_estimate_ee4=Text(edit_estimate_labelframee1,width=23)
    edit_estimate_ee4.place(x=402,y=30,height=70)

    edit_estimate_bttn1=Button(edit_estimate_labelframee1,width=3,height=2,compound = LEFT,text=">>",command=edit_copy_cust_details_1)
    edit_estimate_bttn1.place(x=280, y=50)
    
    edit_estimate_labelframee2 = LabelFrame(edit_estimate_fir1Frame,text="")
    edit_estimate_labelframee2.place(x=10,y=130,width=640,height=42)
    edit_estimate_emaill=Label(edit_estimate_labelframee2,text="Email").place(x=10,y=5)
    edit_estimate_ee5=Entry(edit_estimate_labelframee2,width=30)
    edit_estimate_ee5.place(x=80,y=5)

    edit_estimate_smms=Label(edit_estimate_labelframee2,text="SMS Number").place(x=328,y=5)
    edit_estimate_ee6=Entry(edit_estimate_labelframee2,width=30)
    edit_estimate_ee6.place(x=402,y=5)

    # edit_estimate_ee1.delete(0,END)
    # edit_estimate_ee1.insert(0,edit_est_data[20])
    # edit_estimate_ee2.delete('1.0',END)
    # edit_estimate_ee2.insert('1.0',edit_est_data[21])
    # edit_estimate_ee3.delete(0, END)
    # edit_estimate_ee3.insert(0, edit_est_data[22])
    # edit_estimate_ee4.delete('1.0',END)
    # edit_estimate_ee4.insert('1.0',edit_est_data[23])
    # edit_estimate_ee5.delete(0,END)
    # edit_estimate_ee5.insert(0,edit_est_data[24])
    # edit_estimate_ee6.delete(0,END)
    # edit_estimate_ee6.insert(0,edit_est_data[25])
      
    edit_estimate_labelframe = LabelFrame(edit_estimate_fir1Frame,text="Estimate",font=("arial",15))
    edit_estimate_labelframe.place(x=652,y=5,width=290,height=170)
    edit_estimate_order0=Label(edit_estimate_labelframe,text="Estimate#").place(x=5,y=5)

    edit_estimate_ee01=Entry(edit_estimate_labelframe,width=25)
    edit_estimate_ee01.place(x=100,y=5,)

    edit_estimate_orderdate=Label(edit_estimate_labelframe,text="Estimate date").place(x=5,y=33)
    edit_estimate_ee02=Entry(edit_estimate_labelframe,width=20)
    edit_estimate_ee02.place(x=150,y=33)

    edit_estimate_checkvarStatus5=IntVar()
    edit_estimate_duedate=Checkbutton(edit_estimate_labelframe,variable = edit_estimate_checkvarStatus5,text="Due date",onvalue =0 ,offvalue = 1).place(x=5,y=62)
    edit_estimate_ee03=Entry(edit_estimate_labelframe,width=20)
    edit_estimate_ee03.place(x=150,y=62)

    edit_estimate_termss=Label(edit_estimate_labelframe,text="Terms").place(x=5,y=92)
    edit_estimate_ee04=ttk.Combobox(edit_estimate_labelframe, value="",width=25)
    edit_estimate_ee04.place(x=100,y=92)

    edit_estimate_reff=Label(edit_estimate_labelframe,text="Order ref#").place(x=5,y=118)
    edit_estimate_ee11=Entry(edit_estimate_labelframe,width=27)
    edit_estimate_ee11.place(x=100,y=118)

    edit_estimate_fir2Frame=Frame(edit_estimate_pop, height=150,width=100,bg="#f5f3f2")
    edit_estimate_fir2Frame.pack(side="top", fill=X)
    edit_estimate_listFrame = Frame(edit_estimate_fir2Frame, bg="white", height=140,borderwidth=5,  relief=RIDGE)
    
    edit_estimate_tree=ttk.Treeview(edit_estimate_listFrame)
    edit_estimate_tree["columns"]=["1","2","3","4","5","6","7","8"]

    edit_estimate_tree.column("#0", width=40)
    edit_estimate_tree.column("1", width=80)
    edit_estimate_tree.column("2", width=190)
    edit_estimate_tree.column("3", width=190)
    edit_estimate_tree.column("4", width=80)
    edit_estimate_tree.column("5", width=60)
    edit_estimate_tree.column("6", width=60)
    edit_estimate_tree.column("7", width=60)
    edit_estimate_tree.column("8", width=80)
    
    edit_estimate_tree.heading("#0")
    edit_estimate_tree.heading("1",text="ID/SKU")
    edit_estimate_tree.heading("2",text="Product/Service")
    edit_estimate_tree.heading("3",text="Description")
    edit_estimate_tree.heading("4",text="Unit Price")
    edit_estimate_tree.heading("5",text="Quality")
    edit_estimate_tree.heading("6",text="Pcs/Weight")
    edit_estimate_tree.heading("7",text="Tax1")
    edit_estimate_tree.heading("8",text="Price")
    
    edit_estimate_tree.pack(fill="both", expand=1)
    edit_estimate_listFrame.pack(side="top", fill="both", padx=5, pady=3, expand=1)

    edit_estimate_fir3Frame=Frame(edit_estimate_pop,height=200,width=700,bg="#f5f3f2")
    edit_estimate_fir3Frame.place(x=0,y=490)

    edit_estimate_tabStyle = ttk.Style()
    edit_estimate_tabStyle.theme_use('default')
    edit_estimate_tabStyle.configure('TNotebook.Tab', background="#999999", width=12, padding=5)
    edit_estimate_myNotebookk=ttk.Notebook(edit_estimate_fir3Frame)
    edit_estimate_orderFrame = Frame(edit_estimate_myNotebookk, height=200, width=800)
    edit_estimate_headerFrame = Frame(edit_estimate_myNotebookk, height=200, width=800)
    edit_estimate_commentFrame = Frame(edit_estimate_myNotebookk, height=200, width=800)
    edit_estimate_termsFrame = Frame(edit_estimate_myNotebookk, height=200, width=800)
    edit_estimate_noteFrame = Frame(edit_estimate_myNotebookk, height=200, width=800)
    edit_estimate_documentFrame = Frame(edit_estimate_myNotebookk, height=200, width=800)
    
    edit_estimate_myNotebookk.add(edit_estimate_orderFrame,compound="left", text="Estimate")
    edit_estimate_myNotebookk.add(edit_estimate_headerFrame,compound="left",  text="Header/Footer")
    edit_estimate_myNotebookk.add(edit_estimate_commentFrame,compound="left",  text="Comments")
    edit_estimate_myNotebookk.add(edit_estimate_termsFrame,compound="left", text="Terms")
    edit_estimate_myNotebookk.add(edit_estimate_noteFrame,compound="left",  text="Private notes")
    edit_estimate_myNotebookk.add(edit_estimate_documentFrame,compound="left",  text="Documents")
    edit_estimate_myNotebookk.pack(expand = 1, fill ="both")  

    edit_estimate_labelfram1 = LabelFrame(edit_estimate_orderFrame,text="",font=("arial",15))
    edit_estimate_labelfram1.place(x=1,y=1,width=800,height=170)

    edit_estimates_cost1=Label(edit_estimate_labelfram1,text="Extra cost name").place(x=2,y=5)
    edit_estimates_e1=ttk.Combobox(edit_estimate_labelfram1, value="",width=20).place(x=115,y=5)

    edit_estimates_rate=Label(edit_estimate_labelfram1,text="Discount rate").place(x=370,y=5)
    edit_estimates_e2=Spinbox(edit_estimate_labelfram1,width=6,from_=0,to=10,justify=RIGHT)
    edit_estimates_e2.place(x=460,y=5)

    edit_estimates_cost2=Label(edit_estimate_labelfram1,text="Extra cost").place(x=35,y=35)
    edit_estimates_e3=Entry(edit_estimate_labelfram1,width=10).place(x=115,y=35)
    edit_estimates_tax=Label(edit_estimate_labelfram1,text="Tax1").place(x=420,y=35)
    edit_estimates_e4=Entry(edit_estimate_labelfram1,width=7).place(x=460,y=35)
    edit_estimates_template=Label(edit_estimate_labelfram1,text="Template").place(x=37,y=70)
    edit_estimates_e5=ttk.Combobox(edit_estimate_labelfram1, value="",width=25).place(x=115,y=70)
    edit_estimates_sales=Label(edit_estimate_labelfram1,text="Sales Person").place(x=25,y=100)
    edit_estimates_e6=Entry(edit_estimate_labelfram1,width=18).place(x=115,y=100)
    edit_estimates_category=Label(edit_estimate_labelfram1,text="Category").place(x=300,y=100)
    edit_estimates_e7=Entry(edit_estimate_labelfram1,width=22).place(x=370,y=100)
    
    edit_estimate_statusfrme = LabelFrame(edit_estimate_labelfram1,text="Status",font=("arial",15))
    edit_estimate_statusfrme.place(x=540,y=0,width=160,height=160)
    edit_estimates_draft=Label(edit_estimate_statusfrme, text="Draft",font=("arial", 15, "bold"), fg="grey").place(x=50, y=3)
    edit_estimates_on1=Label(edit_estimate_statusfrme, text="Emailed on:").place( y=50)
    edit_estimates_nev1=Label(edit_estimate_statusfrme, text="Never").place(x=100,y=50)
    edit_estimates_on2=Label(edit_estimate_statusfrme, text="Printed on:").place( y=90)
    edit_estimates_nev2=Label(edit_estimate_statusfrme, text="Never").place(x=100,y=90)

    edit_estimates_text01=Label(edit_estimate_headerFrame,text="Title text").place(x=50,y=5)
    edit_estimates_e01=ttk.Combobox(edit_estimate_headerFrame, value="",width=60).place(x=125,y=5)
    edit_estimates_text02=Label(edit_estimate_headerFrame,text="Page header text").place(x=2,y=45)
    edit_estimates_e11=ttk.Combobox(edit_estimate_headerFrame, value="",width=60).place(x=125,y=45)
    edit_estimates_text03=Label(edit_estimate_headerFrame,text="Footer text").place(x=35,y=85)
    edit_estimates_e21=ttk.Combobox(edit_estimate_headerFrame, value="",width=60).place(x=125,y=85)

    edit_estimates_texttt=Label(edit_estimate_noteFrame,text="Private notes(not shown on invoice/order/estemates)").place(x=10,y=10)
    edit_estimates_e41=Text(edit_estimate_noteFrame,width=100,height=7).place(x=10,y=32)

    edit_estimates_e51=Text(edit_estimate_termsFrame,width=100,height=9).place(x=10,y=10)

    edit_estimates_e61=Text(edit_estimate_commentFrame,width=100,height=9).place(x=10,y=10)

    edit_estimates_btn1=Button(edit_estimate_documentFrame,height=2,width=3,text="+").place(x=5,y=10)
    edit_estimates_btn2=Button(edit_estimate_documentFrame,height=2,width=3,text="-").place(x=5,y=50)
    edit_estimates_texttt1=Label(edit_estimate_documentFrame,text="Attached documents or image files.If you attach large email then email taken long time to send").place(x=50,y=10)
    edit_estimates_cusventtree=ttk.Treeview(edit_estimate_documentFrame, height=5)
    edit_estimates_cusventtree["columns"]=["1","2","3"]
    edit_estimates_cusventtree.column("#0", width=20)
    edit_estimates_cusventtree.column("1", width=250)
    edit_estimates_cusventtree.column("2", width=250)
    edit_estimates_cusventtree.column("2", width=200)
    edit_estimates_cusventtree.heading("#0",text="", anchor=W)
    edit_estimates_cusventtree.heading("1",text="Attach to Email")
    edit_estimates_cusventtree.heading("2",text="Filename")
    edit_estimates_cusventtree.heading("3",text="Filesize")  
    edit_estimates_cusventtree.place(x=50, y=45)
    

    edit_estimate_fir4Frame1=Frame(edit_estimate_pop,height=190,width=210,bg="#f5f3f2")
    edit_estimate_fir4Frame1.place(x=740,y=520)
    edit_estimate_summaryfrme = LabelFrame(edit_estimate_fir4Frame1,text="Summary",font=("arial",15))
    edit_estimate_summaryfrme.place(x=0,y=0,width=200,height=170)
    edit_estimate_discounttt=Label(edit_estimate_summaryfrme, text="Discount").place(x=0 ,y=0)
    edit_estimate_discounttt1=Label(edit_estimate_summaryfrme, text="$0.00").place(x=130 ,y=0)
    edit_estimate_subbb=Label(edit_estimate_summaryfrme, text="Subtotal").place(x=0 ,y=21)
    edit_estimate_subbb1=Label(edit_estimate_summaryfrme, text="$0.00").place(x=130 ,y=21)
    edit_estimate_ttaax=Label(edit_estimate_summaryfrme, text="Tax1").place(x=0 ,y=42)
    edit_estimate_ttax1=Label(edit_estimate_summaryfrme, text="$0.00").place(x=130 ,y=42)
    edit_estimate_costt=Label(edit_estimate_summaryfrme, text="Extra cost").place(x=0 ,y=63)
    edit_estimate_costtt=Label(edit_estimate_summaryfrme, text="$0.00").place(x=130 ,y=63)
    edit_estimate_orderrr=Label(edit_estimate_summaryfrme, text="Order total").place(x=0 ,y=84)
    edit_estimate_orderrr1=Label(edit_estimate_summaryfrme, text="$0.00").place(x=130 ,y=84)
    edit_estimate_totalll=Label(edit_estimate_summaryfrme, text="Total paid").place(x=0 ,y=105)
    edit_estimate_totalll1=Label(edit_estimate_summaryfrme, text="$0.00").place(x=130 ,y=105)
    edit_estimate_balancee=Label(edit_estimate_summaryfrme, text="Balance").place(x=0 ,y=126)
    edit_estimate_balancee1=Label(edit_estimate_summaryfrme, text="$0.00").place(x=130 ,y=126)

    edit_estimate_fir5Frame1=Frame(edit_estimate_pop,height=38,width=210)
    edit_estimate_fir5Frame1.place(x=735,y=485)
    edit_estimate_btndown=Button(edit_estimate_fir5Frame1, compound="left", text="Line Down").place(x=75, y=0)
    edit_estimate_btnup=Button(edit_estimate_fir5Frame1, compound="left", text="Line Up").place(x=150, y=0)

  ############################ End view/edit estimate ###########################
  #printselected order
    
  def estimate_printsele():

    def estimate_property1():
      estimate_propert=Toplevel()
      estimate_propert.title("Microsoft Print To PDF Advanced Document Settings")
      estimate_propert.geometry("670x500+240+150")

      def estimate_property2():
        estimate_propert1=Toplevel()
        estimate_propert1.title("Microsoft Print To PDF Advanced Document Settings")
        estimate_propert1.geometry("670x500+240+150")

        estimate_ename=Label(estimate_propert1, text="Microsoft Print To PDF Advanced Document Settings").place(x=10, y=5)
        estimate_epaper=Label(estimate_propert1, text="Paper/Output").place(x=30, y=35)
        estimate_esize=Label(estimate_propert1, text="Paper size").place(x=55, y=65)
        estimate_en = StringVar()
        estimate_search = ttk.Combobox(estimate_propert1, width = 15, textvariable = estimate_en )
        estimate_search['values'] = ('letter')
        estimate_search.place(x=150,y=65)
        estimate_search.current(0)
        estimate_copy=Label(estimate_propert1, text="Copy count:").place(x=55, y=95)

        estimate_okbtn=Button(estimate_propert1,compound = LEFT,image=tick , text="Ok", width=60).place(x=460, y=450)
        estimate_canbtn=Button(estimate_propert1,compound = LEFT,image=cancel, text="Cancel", width=60).place(x=570, y=450)
        
        


      estimate_estyle = ttk.Style()
      estimate_estyle.theme_use('default')
      estimate_estyle.configure('TNotebook.Tab', background="#999999", padding=5)
      estimate_property_Notebook = ttk.Notebook(estimate_propert)
      estimate_property_Frame = Frame(estimate_property_Notebook, height=500, width=670)
      estimate_property_Notebook.add(estimate_property_Frame, text="Layout")
      estimate_property_Notebook.place(x=0, y=0)

      estimate_nname=Label(estimate_property_Frame, text="Orientation:").place(x=10, y=5)
      estimate_en1 = StringVar()
      estimate_esearch = ttk.Combobox(estimate_property_Frame, width = 23, textvariable = estimate_en1 )
      estimate_esearch['values'] = ('Portrait')
      estimate_esearch.place(x=10,y=25)
      estimate_esearch.current(0)

      estimate_etext1=Text(estimate_property_Frame,width=50).place(x=250, y=5,height=350)

      estimate_ebtn=Button(estimate_property_Frame, text="Advanced",command=estimate_property2).place(x=550, y=380)
      estimate_ebtn1=Button(estimate_property_Frame,compound = LEFT,image=tick  ,text="OK", width=60,).place(x=430, y=420)
      estimate_ebtn2=Button(estimate_property_Frame,compound = LEFT,image=cancel , text="Cancel", width=60,).place(x=550, y=420)     


      
    if(False):
        messagebox.showwarning("FBilling Revelution 2020", "Customer is required, Please select customer for this invoice\nbefore printing")
    elif(False):
        messagebox.showinfo("FBilling Revelution 2020", "Print job has been completed.")
    else:
        estimate_print1=Toplevel()
        estimate_print1.title("Print")
        estimate_print1.geometry("670x400+240+150")
        
        estimate_printerframe=LabelFrame(estimate_print1, text="Printer", height=80, width=650)
        estimate_printerframe.place(x=7, y=5)      
        estimate_pname=Label(estimate_printerframe, text="Name:").place(x=10, y=5)
        estimate_pe1= ttk.Combobox(estimate_printerframe, width=40).place(x=70, y=5)
        estimate_where=Label(estimate_printerframe, text="Where:").place(x=10, y=30)
        estimate_printocheckvar=IntVar()
        estimate_printochkbtn=Checkbutton(estimate_printerframe,text="Print to file",variable=estimate_printocheckvar,onvalue=1,offvalue=0,height=1,width=10)
        estimate_printochkbtn.place(x=450, y=30)
        estimate_pbtn=Button(estimate_printerframe, text="Properties", width=10,command=estimate_property1).place(x=540, y=5)

        estimate_pageslblframe=LabelFrame(estimate_print1, text="Pages", height=140, width=320)
        estimate_pageslblframe.place(x=10, y=90)
        estimate_radvar=IntVar()
        estimate_radioall=Radiobutton(estimate_pageslblframe, text="All", variable=estimate_radvar, value="1").place(x=10, y=5)
        estimate_radiocpage=Radiobutton(estimate_pageslblframe, text="Current Page", variable=estimate_radvar, value="2").place(x=10, y=25)
        estimate_radiopages=Radiobutton(estimate_pageslblframe, text="Pages: ", variable=estimate_radvar, value="3").place(x=10, y=45)
        estimate_pagecountentry = Entry(estimate_pageslblframe, width=23).place(x=80, y=47)
        estimate_pageinfolabl=Label(estimate_pageslblframe, text="Enter page numbers and/or page ranges\nseperated by commas. For example:1,3,5-12")
        estimate_pageinfolabl.place(x=5, y=75)

        estimate_copylblframe=LabelFrame(estimate_print1, text="Copies", height=140, width=320)
        estimate_copylblframe.place(x=335, y=90)
        estimate_nolabl=Label(estimate_copylblframe, text="Number of copies").place(x=5, y=5)      
        estimate_noentry = Entry(estimate_copylblframe, width=18).place(x=130, y=5)      
        estimate_one=Frame(estimate_copylblframe, width=30, height=40, bg="black").place(x=20, y=40)     
        estimate_two=Frame(estimate_copylblframe, width=30, height=40, bg="grey").place(x=15, y=45)     
        estimate_three=Frame(estimate_copylblframe, width=30, height=40, bg="white").place(x=10, y=50)      
        estimate_four=Frame(estimate_copylblframe, width=30, height=40, bg="black").place(x=80, y=40)      
        estimate_fiv=Frame(estimate_copylblframe, width=30, height=40, bg="grey").place(x=75, y=45)      
        estimate_six=Frame(estimate_copylblframe, width=30, height=40, bg="white").place(x=70, y=50)      
        estimate_collatecheckvar=IntVar()
        estimate_collatechkbtn=Checkbutton(estimate_copylblframe,text="Collate",variable=estimate_collatecheckvar,onvalue=1,offvalue=0,height=1,width=10)
        estimate_collatechkbtn.place(x=130, y=70)

        estimate_othrlblframe=LabelFrame(estimate_print1, text="Other", height=120, width=320)
        estimate_othrlblframe.place(x=10, y=235)
        estimate_printlb=Label(estimate_othrlblframe, text="Print").place(x=5, y=0)
        estimate_dropprint = ttk.Combobox(estimate_othrlblframe, width=23).place(x=80, y=0)
        estimate_orderlb=Label(estimate_othrlblframe, text="Order").place(x=5, y=25)
        estimate_dropord = ttk.Combobox(estimate_othrlblframe, width=23).place(x=80, y=25)
        estimate_duplexlb=Label(estimate_othrlblframe, text="Duplex").place(x=5, y=50)
        estimate_droplex = ttk.Combobox(estimate_othrlblframe, width=23).place(x=80, y=50)

        estimate_prmodelblframe=LabelFrame(estimate_print1, text="Print mode", height=120, width=320)
        estimate_prmodelblframe.place(x=335, y=235)
        estimate_dropscal = ttk.Combobox(estimate_prmodelblframe, width=30).place(x=5, y=5)
        estimate_poslb=Label(estimate_prmodelblframe, text="Print on sheet").place(x=5, y=35)
        estimate_droppos = ttk.Combobox(estimate_prmodelblframe, width=10).place(x=155, y=35)

        estimate_eokbtn=Button(estimate_print1,compound = LEFT,image=tick , text="Ok", width=60).place(x=460, y=370)
        estimate_ecanbtn=Button(estimate_print1,compound = LEFT,image=cancel, text="Cancel", width=60).place(x=570, y=370)
        


  #email
        
  def estimate_emailord():
    estimate_mailDetail=Toplevel()
    estimate_mailDetail.title("Orders E-Mail")
    estimate_ep2 = PhotoImage(file = "images/fbicon.png")
    estimate_mailDetail.iconphoto(False, estimate_ep2)
    estimate_mailDetail.geometry("1030x550+150+120")
  
    def estimate_my_SMTP():
        if True:
            estimate_em_ser_conbtn.destroy()
            estimate_mysmtpservercon=LabelFrame(estimate_account_Frame,text="SMTP server connection(ask your ISP for your SMTP settings)", height=165, width=380)
            estimate_mysmtpservercon.place(x=610, y=110)
            estimate_lbl_hostn=Label(estimate_mysmtpservercon, text="Hostname").place(x=5, y=10)
            estimate_hostnent=Entry(estimate_mysmtpservercon, width=30).place(x=80, y=10)
            estimate_lbl_portn=Label(estimate_mysmtpservercon, text="Port").place(x=5, y=35)
            estimate_portent=Entry(estimate_mysmtpservercon, width=30).place(x=80, y=35)
            estimate_elbl_usn=Label(estimate_mysmtpservercon, text="Username").place(x=5, y=60)
            estimate_unament=Entry(estimate_mysmtpservercon, width=30).place(x=80, y=60)
            estimate_eelbl_pasn=Label(estimate_mysmtpservercon, text="Password").place(x=5, y=85)
            estimate_pwdent=Entry(estimate_mysmtpservercon, width=30).place(x=80, y=85)
            estimate_ssl_chkvar=IntVar()
            estimate_ssl_chkbtn=Checkbutton(estimate_mysmtpservercon, variable=estimate_ssl_chkvar, text="This server requires a secure connection(SSL)", onvalue=1, offvalue=0)
            estimate_ssl_chkbtn.place(x=50, y=110)
            estimate_em_ser_conbtn1=Button(estimate_account_Frame, text="Test E-mail Server Connection").place(x=610, y=285)
        else:
            pass
      
    estimate_mystyle = ttk.Style()
    estimate_mystyle.theme_use('default')
    estimate_mystyle.configure('TNotebook.Tab', background="#999999", padding=5)
    estimate_email_Notebook = ttk.Notebook(estimate_mailDetail)
    estimate_email_Frame = Frame(estimate_email_Notebook, height=500, width=1080)
    estimate_account_Frame = Frame(estimate_email_Notebook, height=550, width=1080)
    estimate_email_Notebook.add(estimate_email_Frame, text="E-mail")
    estimate_email_Notebook.add(estimate_account_Frame, text="Account")
    estimate_email_Notebook.place(x=0, y=0)
    estimate_messagelbframe=LabelFrame(estimate_email_Frame,text="Message", height=495, width=730)
    estimate_messagelbframe.place(x=5, y=5)
    estimate_mylbl_emailtoaddr=Label(estimate_messagelbframe, text="Email to address").place(x=5, y=5)
    estimate_emailtoent=Entry(estimate_messagelbframe, width=50).place(x=120, y=5)
    estimate_sendemail_btn=Button(estimate_messagelbframe, text="Send Email", width=10, height=1).place(x=600, y=10)
    estimate_lbl_carcopyto=Label(messagelbframe, text="Carbon copy to").place(x=5, y=32)
    estimate_carcopyent=Entry(messagelbframe, width=50).place(x=120, y=32)
    estimate_stopemail_btn=Button(messagelbframe, text="Stop sending", width=10, height=1).place(x=600, y=40)
    estimate_lbl_subject=Label(messagelbframe, text="Subject").place(x=5, y=59)
    estimate_subent=Entry(messagelbframe, width=50).place(x=120, y=59)

    estimate_nstyle = ttk.Style()
    estimate_nstyle.theme_use('default')
    estimate_nstyle.configure('TNotebook.Tab', background="#999999", width=20, padding=5)
    estimate_mess_Notebook = ttk.Notebook(estimate_messagelbframe)
    estimate_emailmessage_Frame = Frame(estimate_mess_Notebook, height=350, width=710)
    estimate_htmlsourse_Frame = Frame(estimate_mess_Notebook, height=350, width=710)
    estimate_mess_Notebook.add(estimate_emailmessage_Frame, text="E-mail message")
    estimate_mess_Notebook.add(estimate_htmlsourse_Frame, text="Html sourse code")
    estimate_mess_Notebook.place(x=5, y=90)

    estimate_mybtn1=Button(estimate_emailmessage_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)  
    estimate_mybtn2=Button(estimate_emailmessage_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
    estimate_mybtn3=Button(estimate_emailmessage_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
    estimate_mybtn4=Button(estimate_emailmessage_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
    estimate_mybtn5=Button(estimate_emailmessage_Frame,width=31,height=23,compound = LEFT,image=undo).place(x=140, y=1)
    estimate_mybtn6=Button(estimate_emailmessage_Frame,width=31,height=23,compound = LEFT,image=redo).place(x=175, y=1)
    estimate_mybtn7=Button(estimate_emailmessage_Frame,width=31,height=23,compound = LEFT,image=bold).place(x=210, y=1)
    estimate_mybtn8=Button(estimate_emailmessage_Frame,width=31,height=23,compound = LEFT,image=italics).place(x=245, y=1)
    estimate_mybtn9=Button(estimate_emailmessage_Frame,width=31,height=23,compound = LEFT,image=underline).place(x=280, y=1)
    estimate_mybtn10=Button(estimate_emailmessage_Frame,width=31,height=23,compound = LEFT,image=left).place(x=315, y=1)
    estimate_mybtn11=Button(estimate_emailmessage_Frame,width=31,height=23,compound = LEFT,image=right).place(x=350, y=1)
    estimate_mybtn12=Button(estimate_emailmessage_Frame,width=31,height=23,compound = LEFT,image=center).place(x=385, y=1)
    estimate_mybtn13=Button(estimate_emailmessage_Frame,width=31,height=23,compound = LEFT,image=hyperlink).place(x=420, y=1)
    estimate_mybtn14=Button(estimate_emailmessage_Frame,width=31,height=23,compound = LEFT,image=remove).place(x=455, y=1)

    estimate_dropcomp = ttk.Combobox(estimate_emailmessage_Frame, width=12, height=3).place(x=500, y=5)
    estimate_mydropcompo = ttk.Combobox(estimate_emailmessage_Frame, width=6, height=3).place(x=600, y=5)
    estimate_mframe=Frame(estimate_emailmessage_Frame, height=350, width=710, bg="white")
    estimate_mframe.place(x=0, y=28)
    estimate_e_btn1=Button(estimate_htmlsourse_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)
    estimate_e_btn2=Button(estimate_htmlsourse_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
    estimate_e_btn3=Button(estimate_htmlsourse_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
    estimate_e_btn4=Button(estimate_htmlsourse_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
    estimate_e_mframe=Frame(estimate_htmlsourse_Frame, height=350, width=710, bg="white")
    estimate_e_mframe.place(x=0, y=28)
    estimate_attachlbframe=LabelFrame(estimate_email_Frame,text="Attachment(s)", height=350, width=280)
    estimate_attachlbframe.place(x=740, y=5)
    estimate_htcodeframe=Frame(estimate_attachlbframe, height=220, width=265, bg="white").place(x=5, y=5)
    estimate_lbl_btn_info=Label(estimate_attachlbframe, text="Double click on attachment to view").place(x=30, y=230)
    estimate_e_btn17=Button(estimate_attachlbframe, width=20, text="Add attacment file...").place(x=60, y=260)
    estimate_e_btn18=Button(estimate_attachlbframe, width=20, text="Remove attacment").place(x=60, y=295)
    estimate_lbl_tt_info=Label(estimate_email_Frame, text="You can create predefined invoice, order, estimate\nand payment receipt email templates under Main\nmenu/Settings/E-Mail templates tab")
    estimate_lbl_tt_info.place(x=740, y=370)

    estimate_ready_frame=Frame(estimate_mailDetail, height=20, width=1080, bg="#b3b3b3").place(x=0,y=530)
    
    estimate_sendatalbframe=LabelFrame(estimate_account_Frame,text="E-Mail(Sender data)",height=270, width=600)
    estimate_sendatalbframe.place(x=5, y=5)
    estimate_lbl_sendermail=Label(estimate_sendatalbframe, text="Your company email address").place(x=5, y=30)
    estimate_sentent=Entry(estimate_sendatalbframe, width=40).place(x=195, y=30)
    estimate_lbl_orcompanyname=Label(estimate_sendatalbframe, text="Your name or company name").place(x=5, y=60)
    estimate_nament=Entry(estimate_sendatalbframe, width=40).place(x=195, y=60)
    estimate_lbl_reply=Label(estimate_sendatalbframe, text="Reply to email address").place(x=5, y=90)
    estimate_replyent=Entry(estimate_sendatalbframe, width=40).place(x=195, y=90)
    estimate_lbl_sign=Label(estimate_sendatalbframe, text="Signature").place(x=5, y=120)
    estimate_signent=Entry(estimate_sendatalbframe,width=50).place(x=100, y=120,height=75)
    estimate_confirm_chkvar=IntVar()
    estimate_confirm_chkbtn=Checkbutton(estimate_sendatalbframe, variable=estimate_confirm_chkvar, text="Confirmation reading", onvalue=1, offvalue=0)
    estimate_confirm_chkbtn.place(x=200, y=215)
    estimate_e_mybtn18=Button(estimate_account_Frame, width=15, text="Save settings").place(x=25, y=285)

    estimate_esendatalbframe=LabelFrame(estimate_account_Frame,text="SMTP Server",height=100, width=380)
    estimate_esendatalbframe.place(x=610, y=5)
    estimate_servar=IntVar()
    estimate_SMTP_rbtn=Radiobutton(estimate_sendatalbframe, text="Use the Built-In SMTP Server Settings", variable=estimate_servar, value=1)
    estimate_SMTP_rbtn.place(x=10, y=10)
    estimate_MySMTP_rbtn=Radiobutton(estimate_sendatalbframe, text="Use My Own SMTP Server Settings(Recommended)", variable=estimate_servar, value=2, command=estimate_my_SMTP)
    estimate_MySMTP_rbtn.place(x=10, y=40)
    estimate_em_ser_conbtn=Button(estimate_account_Frame, text="Test E-mail Server Connection")
    estimate_em_ser_conbtn.place(x=710, y=110)



  #sms notification order
    
  def estimate_sms():
    estimate_send_SMS=Toplevel()
    estimate_send_SMS.geometry("700x480+240+150")
    estimate_send_SMS.title("Send SMS notification")

    estimate_sms_style = ttk.Style()
    estimate_sms_style.theme_use('default')
    estimate_sms_style.configure('TNotebook.Tab', background="#999999", padding=5)
    estimate_sms_Notebook = ttk.Notebook(estimate_send_SMS)
    estimate_SMS_Notification = Frame(estimate_sms_Notebook, height=470, width=700)
    estimate_SMS_Service_Account = Frame(estimate_sms_Notebook, height=470, width=700)
    estimate_sms_Notebook.add(estimate_SMS_Notification, text="SMS Notification")
    estimate_sms_Notebook.add(estimate_SMS_Service_Account, text="SMS Service Account")
    estimate_sms_Notebook.place(x=0, y=0)

    estimate_numlbel=Label(estimate_SMS_Notification, text="SMS number or comma seperated SMS number list(Please start each SMS number with the country code)")
    estimate_numlbel.place(x=10, y=10)
    estimate_numentry=Entry(estimate_SMS_Notification, width=92).place(x=10, y=30)
    estimate_stexbel=Label(estimate_SMS_Notification, text="SMS Text").place(x=10, y=60)
    estimate_stex=Entry(estimate_SMS_Notification, width=40).place(x=10, y=85,height=120)
    
    estimate_dclbel=Label(estimate_SMS_Notification, text="Double click to insert into text")
    estimate_dclbel.place(x=410, y=60)
    estimate_dcl=Entry(estimate_SMS_Notification, width=30)
    estimate_dcl.place(x=400, y=85,height=200)
    
    estimate_mysmstype=LabelFrame(estimate_SMS_Notification, text="SMS message type", width=377, height=60)
    estimate_mysmstype.place(x=10, y=223)
    estimate_Mysnuvar=IntVar()
    estimate_normal_rbtn=Radiobutton(estimate_mysmstype, text="Normal SMS(160 chars)", variable=estimate_Mysnuvar, value=1)
    estimate_normal_rbtn.place(x=5, y=5)
    estimate_unicode_rbtn=Radiobutton(estimate_mysmstype, text="Unicode SMS(70 chars)", variable=estimate_Mysnuvar, value=2)
    estimate_unicode_rbtn.place(x=190, y=5)
    estimate_tiplbf=LabelFrame(estimate_SMS_Notification, text="Tips", width=680, height=120)
    estimate_tiplbf.place(x=10, y=290)
    estimate_Mytiplabl=Label(estimate_tiplbf,justify=LEFT,fg="red",  text="Always start the SMS nymber with the country code. Do not use the + sign at the beginning(example\nUS number:8455807546). Do not use any special characters in your normal SMS text. Please use the\nstndard SMS characters or the English alphabet and numbers only. Otherwise the SMS will be\nunreadable or undeliverable. If you need to enter international characters, accents,email address, or\nspecial characters to the SMS text field then choose the Unicode SMS format.")
    estimate_Mytiplabl.place(x=5, y=5)

    estimate_Mybtn1=Button(estimate_SMS_Notification, width=20, text="Send SMS notification").place(x=10, y=420)
    estimate_Mybtn2=Button(estimate_SMS_Notification, width=25, text="Confirm SMS cost before sending").place(x=280, y=420)
    estimate_Mybtn3=Button(estimate_SMS_Notification, width=15, text="Cancel").place(x=550, y=420)
    

    estimate_e_smstype=LabelFrame(estimate_SMS_Service_Account, text="Select the notification service provider", width=670, height=65)
    estimate_e_smstype.place(x=10, y=5)
    estimate_e_snumvar=IntVar()
    estimate_normal_rbtn=Radiobutton(estimate_e_smstype,text="BULKSMS(www.bulksms.com)",variable=estimate_e_snumvar,value=1,)
    estimate_normal_rbtn.place(x=5, y=5)
    estimate_unicode_rbtn=Radiobutton(estimate_e_smstype, text="Unicode SMS(70 chars)-Recommended", variable=estimate_e_snumvar, value=2)
    estimate_unicode_rbtn.place(x=290, y=5)

    estimate_sms1type=LabelFrame(estimate_SMS_Service_Account, text="Your BULKSMS.COM Account", width=670, height=100)
    estimate_sms1type.place(x=10, y=80)
    estimate_Myname=Label(estimate_sms1type, text="Username").place(x=10, y=5)
    estimate_na=Entry(estimate_sms1type, width=20).place(x=100, y=5)
    estimate_Mypassword=Label(estimate_sms1type, text="Password").place(x=10, y=45)
    estimate_Mypas=Entry(estimate_sms1type, width=20).place(x=100, y=45)
    estimate_combo=Label(estimate_sms1type, text="Route").place(x=400, y=5)
    estimate_My_n = StringVar()
    estimate_combo1 = ttk.Combobox(estimate_sms1type, width = 20, textvariable = estimate_My_n ).place(x=450,y=5)
    estimate_My_btn1=Button(estimate_sms1type, width=10, text="Save settings").place(x=550, y=45)

    
    estimate_Mytiplbf=LabelFrame(estimate_SMS_Service_Account, text="Terms of service", width=680, height=250)
    estimate_Mytiplbf.place(x=10, y=190)
    estimate_mytiplabl=Label(estimate_Mytiplbf,justify=LEFT,fg="red",  text="The SMS notification service is not free.This service costs you creadit.You must have your own account\nat BULKSMS.COM and you need to have sufficient creadit and an active internet connection to use\nthis feature.Please review all fields in this form for accuracy")
    estimate_mytiplabl.place(x=0, y=5)
    estimate_my_tiplabl1=Label(estimate_Mytiplbf,justify=LEFT,fg="black",  text="visit www.bulksms.com website to create your own account.please make sure the BULKSMS .COM\n service works well in your country before you busy creadit")
    estimate_my_tiplabl1.place(x=0, y=60)
    estimate_My_tiplabl2=Label(estimate_Mytiplbf,justify=LEFT,fg="black",  text="Our SMS notification tool comes without any warranty.our software only forwards your SMS message\nthe BULKSMS API server .The BULKSMS API server will try to sent SMS message your recipient")
    estimate_My_tiplabl2.place(x=0, y=100)
    estimate_eMy_tiplabl3=Label(estimate_Mytiplbf,justify=LEFT,fg="red",  text="Please note that you access and use the SMS notification tool your own risk.F-Billing software is not\nresponsible for any type of loss or damage or undelivered SMS massage which you may as a result\nof accessing and using the SMS notification service.")
    estimate_eMy_tiplabl3.place(x=0, y=140)
    estimate_My_checkvar1=IntVar()
    estimate_Mychkbtn1=Checkbutton(estimate_Mytiplbf,text="I have read and agree to the terms of service above",variable=estimate_My_checkvar1,onvalue=1,offvalue=0).place(x=70, y=200)  



  #print preview order
  def estimate_Myprintpreview():
    messagebox.showerror("F-Billing Revolution","Customer is required,please select customer for this order before printing.")



  #convert to invoice
  def estimate_convert():
    if messagebox.askyesno("Make invoice from Orders", "Are you sure to make invoice from this Orders ") == True:
          messagebox.askyesno("Make invoice from Estimate", "Invoice Creation was Successfull.\n New Invoice is \n Would you like to open this invoice ")
    else:
          messagebox.destroy()
    

  #delete orders  
  def estimate_dele():  
    messagebox.askyesno("Delete order", "Are you sure to delete this order? All products will be placed back into stock")




  #search in orders  
  def estimate_search():  
      estimate_etop = Toplevel()     
      estimate_etop.title("Find Text")   
      estimate_etop.geometry("600x250+390+250")
      estimate_findwhat1=Label(estimate_etop,text="Find What:",pady=5,padx=10).place(x=5,y=20)
      estimate_e_n = StringVar()
      estimate_findwhat = ttk.Combobox(estimate_etop, width = 40, textvariable = estimate_e_n ).place(x=90,y=25)
    
      estimate_findin1=Label(estimate_etop,text="Find in:",pady=5,padx=10).place(x=5,y=47)
      estimate_my_n1 = StringVar()
      estimate_findIN = ttk.Combobox(estimate_etop, width = 30, textvariable = estimate_my_n1 )
      estimate_findIN['values'] = ('Product/Service id', ' Category', ' Active',' name',' stock',' location', ' image',' <<All>>')                       
      estimate_findIN.place(x=90,y=54)
      estimate_findIN.current(0)

      estimate_findButton = Button(estimate_etop, text ="Find next",width=10).place(x=480,y=22)
      estimate_closeButton = Button(estimate_etop,text ="Close",width=10).place(x=480,y=52)
      
      estimate_match1=Label(estimate_etop,text="Match:",pady=5,padx=10).place(x=5,y=74)
      estimate_my_n2 = StringVar()
      estimate_match = ttk.Combobox(estimate_etop, width = 23, textvariable = estimate_my_n2 )   
      estimate_match['values'] = ('From Any part',' Whole Field',' From the beginning of the field')                                   
      estimate_match.place(x=90,y=83)
      estimate_match.current(0)

      estimate_my_search1=Label(estimate_etop,text="Search:",pady=5,padx=10).place(x=5,y=102)
      estimate_my_n3 = StringVar()
      estimate_my_search = ttk.Combobox(estimate_etop, width = 23, textvariable = estimate_my_n3 )
      estimate_my_search['values'] = ('All', 'up',' Down')
      estimate_my_search.place(x=90,y=112)
      estimate_my_search.current(0)
      estimate_checkvarStatus4=IntVar()  
      estimate_my_Button4 = Checkbutton(estimate_etop,variable = estimate_checkvarStatus4,text="Match Case",onvalue =0 ,offvalue = 1,height=3,width = 15)
      estimate_my_Button4.place(x=90,y=141)
      estimate_checkvarStatus5=IntVar()   
      estimate_my_Button5 = Checkbutton(estimate_etop,variable = estimate_checkvarStatus5,text="Match Format",onvalue =0 ,offvalue = 1,height=3,width = 15)
      estimate_my_Button5.place(x=300,y=141)





  estimate_mainFrame=Frame(tab3, relief=GROOVE, bg="#f8f8f2")
  estimate_mainFrame.pack(side="top", fill=BOTH)

  estimate_midFrame=Frame(estimate_mainFrame, bg="#f5f3f2", height=60)
  estimate_midFrame.pack(side="top", fill=X)

  estimate_w = Canvas(estimate_midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  estimate_w.pack(side="left", padx=(5, 2))
  estimate_w1 = Canvas(estimate_midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  estimate_w1.pack(side="left", padx=(0, 5))

  estimate_invoiceLabel = Button(estimate_midFrame,compound="top", text="Create new\nEstimate",relief=RAISED, image=photo,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=estimate_create)
  estimate_invoiceLabel.pack(side="left", pady=3, ipadx=4)

  estimate_orderLabel = Button(estimate_midFrame,compound="top", text="View/Edit\nEstimate",relief=RAISED, image=photo1,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=edit_estimates_create)
  estimate_orderLabel.pack(side="left")

  estimate_estimateLabel = Button(estimate_midFrame,compound="top", text="Delete\nSelected",relief=RAISED, image=photo2,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=estimate_dele)
  estimate_estimateLabel.pack(side="left")

  estimate_w3 = Canvas(estimate_midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  estimate_w3.pack(side="left", padx=5)

  estimate_recurLabel = Button(estimate_midFrame,compound="top", text="Convert to\nInvoice",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=estimate_convert)
  estimate_recurLabel.pack(side="left")

  estimate_w4 = Canvas(estimate_midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  estimate_w4.pack(side="left", padx=5)

  estimate_previewLabel = Button(estimate_midFrame,compound="top", text="Print\nPreview",relief=RAISED, image=photo4,bg="#f8f8f2", fg="black", height=55, bd=1, width=55, activebackground="red",command=estimate_Myprintpreview)
  estimate_previewLabel.pack(side="left")

  estimate_purchaseLabel = Button(estimate_midFrame,compound="top", text="Print\nSelected",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=estimate_printsele)
  estimate_purchaseLabel.pack(side="left")

  estimate_w5 = Canvas(estimate_midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
  estimate_w5.pack(side="left", padx=5)

  estimate_expenseLabel = Button(estimate_midFrame,compound="top", text=" E-mail \nEstimate",relief=RAISED, image=photo6,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=estimate_emailord)
  estimate_expenseLabel.pack(side="left")

  estimate_smsLabel = Button(estimate_midFrame,compound="top", text="Send SMS\nnotification",relief=RAISED, image=photo10,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=estimate_sms)
  estimate_smsLabel.pack(side="left")

  estimate_w6 = Canvas(estimate_midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
  estimate_w6.pack(side="left", padx=5)

  estimate_productLabel = Button(estimate_midFrame,compound="top", text="Search\nEstimate",relief=RAISED, image=photo7,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=estimate_search)
  estimate_productLabel.pack(side="left")

  estimate_lbframe = LabelFrame(estimate_midFrame, height=60, width=200, bg="#f8f8f2")
  estimate_lbframe.pack(side="left", padx=10, pady=0)
  estimate_lbl_invdt = Label(estimate_lbframe, text="Estimate date from : ", bg="#f8f8f2")
  estimate_lbl_invdt.grid(row=0, column=0, pady=5, padx=(5, 0))
  estimate_lbl_invdtt = Label(estimate_lbframe, text="Estimate date to  :  ", bg="#f8f8f2")
  estimate_lbl_invdtt.grid(row=1, column=0, pady=5, padx=(5, 0))
  estimate_invdt = Entry(estimate_lbframe, width=15)
  estimate_invdt.grid(row=0, column=1)
  estimate_invdtt = Entry(estimate_lbframe, width=15)
  estimate_invdtt.grid(row=1, column=1)
  estimate_checkvarr1 = IntVar()
  estimate_chkbtnn1 = Checkbutton(estimate_lbframe, text = "Apply filter", variable = estimate_checkvarr1, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2")
  estimate_chkbtnn1.grid(row=0, column=2, rowspan=2, padx=(5,5))

  # # Refresh Invoice
  # def est_refresh_estimates():
  #   for record in tree.get_children():
  #     tree.delete(record)
  #     count = 0
  #   fbcursor.execute('SELECT * FROM estimate;')
  #   for i in fbcursor:
  #     if True:
  #       tree.insert(parent='',index='end',iid=i,text='',value=('',i[1],i[2],i[3],'',i[4],i[5],i[6],i[7],i[8]))
  #     else:
  #       pass
  #     count += 1
   

  estimate_productLabel = Button(estimate_midFrame,compound="top", text="Refresh\nEstimates",relief=RAISED, image=photo8,fg="black", height=55, bd=1, width=55)
  estimate_productLabel.pack(side="left")

  estimate_w7 = Canvas(estimate_midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
  estimate_w7.pack(side="left", padx=5)

  estimate_productLabell = Button(estimate_midFrame,compound="top", text="Hide totals\nSum",relief=RAISED, image=photo9,bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
  estimate_productLabell.pack(side="left")

  estimate_invoilabell = Label(estimate_mainFrame, text="Estimate(All)", font=("arial", 18), bg="#f8f8f2")
  estimate_invoilabell.pack(side="left", padx=(20,0))
  estimate_drop = ttk.Combobox(estimate_mainFrame, value="Hello")
  estimate_drop.pack(side="right", padx=(0,10))
  estimate_invoilabell1 = Label(estimate_mainFrame, text="Category filter", font=("arial", 15), bg="#f8f8f2")
  estimate_invoilabell1.pack(side="right", padx=(0,10))

  class MyApp:
    def __init__(self, parent):
      
      self.myParent = parent 

      self.myContainer1 = Frame(parent) 
      self.myContainer1.pack()
      
      self.top_frame = Frame(self.myContainer1) 
      self.top_frame.pack(side=TOP,
        fill=BOTH, 
        expand=YES,
        )  

      self.left_frame = Frame(self.top_frame, background="white",
        borderwidth=5,  relief=RIDGE,
        height=250, 
        width=2000, 
        )
      self.left_frame.pack(side=LEFT,
        fill=BOTH, 
        expand=YES,
        )

      
      tree = ttk.Treeview(self.left_frame, columns = (1,2,3,4,5,6,7,8,9,10), height = 15, show = "headings")
      tree.pack(side = 'top')
      tree.heading(1)
      tree.heading(2, text="Estimate#")
      tree.heading(3, text="Estimate date")
      tree.heading(4, text="Due date")
      tree.heading(5, text="Customer Name")
      tree.heading(6, text="Status")
      tree.heading(7, text="Emailed on")
      tree.heading(8, text="Printed on")
      tree.heading(9, text="SMS on")
      tree.heading(10, text="Estimate Total")   
      tree.column(1, width = 30)
      tree.column(2, width = 150)
      tree.column(3, width = 140)
      tree.column(4, width = 130)
      tree.column(5, width = 200)
      tree.column(6, width = 130)
      tree.column(7, width = 150)
      tree.column(8, width = 130)
      tree.column(9, width = 130)
      tree.column(10, width = 160)

      sql = "SELECT * FROM estimate"
      fbcursor.execute(sql)
      estimate_records = fbcursor.fetchall()

      count = 0
      for i in estimate_records:
        if True:
          tree.insert(parent='',index='end',iid=i,text='',values=('',i[1],i[2],i[3],'',i[4],i[5],i[6],i[7],i[8]))
        else:
          pass
      count += 1

      scrollbar = Scrollbar(self.left_frame)
      scrollbar.place(x=990+330+15, y=0, height=300+20)
      scrollbar.config( command=tree.yview )

      tabControl = ttk.Notebook(self.left_frame,width=1)
      tab1 = ttk.Frame(tabControl)
      tab2 = ttk.Frame(tabControl)
      tab3=  ttk.Frame(tabControl)
      tab4 = ttk.Frame(tabControl)
      tabControl.add(tab1,image=invoices,compound = LEFT, text ='Estimate Items',)
      tabControl.add(tab2,image=photo11,compound = LEFT, text ='Private Notes')
      tabControl.add(tab3,image=smslog,compound = LEFT, text ='SMS Log')
      tabControl.add(tab4,image=photo11,compound = LEFT, text ='Documents')
      tabControl.pack(expand = 1, fill ="both")
      
      tree = ttk.Treeview(tab1, columns = (1,2,3,4,5,6,7,8,), height = 15, show = "headings")
      tree.pack(side = 'top')
      tree.heading(1)
      tree.heading(2, text="Product/Service ID",)
      tree.heading(3, text="Name")
      tree.heading(4, text="Description")
      tree.heading(5, text="Price")
      tree.heading(6, text="QTY")
      tree.heading(7, text="Tax1")
      tree.heading(8, text="Line Total")   
      tree.column(1, width = 50)
      tree.column(2, width = 270)
      tree.column(3, width = 250)
      tree.column(4, width = 300)
      tree.column(5, width = 130)
      tree.column(6, width = 100)
      tree.column(7, width = 100)
      tree.column(8, width = 150)

      note1=Text(tab2, width=170,height=10).place(x=10, y=10)

      note1=Text(tab3, width=170,height=10).place(x=10, y=10)

      tree = ttk.Treeview(tab4, columns = (1,2,3), height = 15, show = "headings")
      tree.pack(side = 'top')
      tree.heading(1)
      tree.heading(2, text="Attach to Email",)
      tree.heading(3, text="Filename")
      tree.column(1, width = 70)
      tree.column(2, width = 270)
      tree.column(3, width = 1000)

      scrollbar = Scrollbar(self.left_frame)
      scrollbar.place(x=990+330+15, y=360, height=190)
      scrollbar.config( command=tree.yview )
        
  myapp = MyApp(tab3)
  
  
  ######################## FRONT PAGE OF CUSTOMER SECTION   #######################################################################
  
      
  settingsframe=Frame(tab10, relief=GROOVE, bg="#f8f8f2")
  settingsframe.pack(side="top", fill=BOTH)
  
  settframe=Frame(settingsframe, bg="#f5f3f2", height=60)
  settframe.pack(side="top", fill=X)
  
  pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
  pn.pack(side="left", padx=(5, 2))
  pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
  pn.pack(side="left", padx=(0, 5))
  # def upload_filelogo():
  #   global imglogo,filename
  #   f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
  #   filena = filedialog.askopenfilename(filetypes=f_types)
  #   shutil.copyfile(filena, os.getcwd()+'/images/'+filena.split('/')[-1])
  #   print(filena.split('/')[-1])
  #   image = Image.open(filena)
  #   resize_image = image.resize((280, 160))
  #   imglogo = ImageTk.PhotoImage(resize_image)
    # b2 = Button(secondtab,image=img)
    # b2.place(x=130, y=80)
  
    # btlogo = Button(secondtab,width=280,height=160,image=imglogo)
    # btlogo.place(x=580,y=280)
  global filename
  filename = ""
  def save_company():
    company_name = comname.get()
    company_address = caddent.get(1.0,END)
    company_mail = comemail.get()
    company_salestax =comsalestax.get()
    currency = comcur.get()
    currencysign = comcursign.get()
    currencysign_placement = comcursignpla.get()
    decimal_sepator = comdecsep.get()
    currency_example = comex.get()
    date_format = comdaf.get()
    example_dateformat = exd.get_date()
    tax = radtax.get()
    tax1name = tax1namee.get()
    tax1rate = tax1ratee.get()
    printtax1 = comptax1.get()
    tax2name = tax2namee.get()
    tax2rate = tax2ratee.get()
    printtax2 = comptax2.get()
    printimage = compimg.get()
    win_menu_colour = win_menu.get()
    radiobut = radema.get()
    cbut1 = checkb1.get()
    cbut2 = checkb2.get()
    cbut3 = checkb3.get()
    cbut4 = checkb4.get()
    cbut5 = checkb5.get()
    cbut6 = checkb6.get()
    est_prefix = est_str.get()
    est_header = win_menu1.get()
    est_text1 = est_str1.get()
    est_text2 = est_str2.get()
    est_text3 = est_str3.get()
    est_text4 = est_str4.get()
    est_text5 = est_str5.get()
    est_text6 = est_str6.get()
    est_predefined = est_str7.get(1.0,END)
    est_default = win_menu2.get()
    est_spin1 = spin1.get()
    adv_default = adv_win_menu8.get()

    child = exctree.get_children()
    var = json.dumps(child)
    sql = "select image from company"
    fbcursor.execute(sql)
    im = fbcursor.fetchone()
    sql = "select * from company"
    fbcursor.execute(sql)
    i = fbcursor.fetchall()
    if not i:
      if filename == "":
        print(12)
        sql = 'insert into company(name, address, email,salestaxno,currency,currencysign,currsignplace,  decimalseperator,excurrency,dateformat,exdate,taxtype,printimageornot,tax1name,tax1rate,printtax1,  tax2name,tax2rate,printtax2,attachment_file_type,miscellanoustab_cbutton1,miscellanoustab_cbutton2,miscellanoustab_cbutton3,miscellanoustab_cbutton4,miscellanoustab_cbutton5,miscellanoustab_cbutton6,Estimate_prefix,Customizeestimatetextlabels,Customizeestimatetextlabels1,Customizeestimatetextlabels2,Customizeestimatetextlabels3,Customizeestimatetextlabels4,Customizeestimatetextlabels5,Defaultestimatetemplate,Startingestimatenumber,Predefinedtextforestimates,adv_Selectedtemplatepreview,est_Headerboxbackgroundcolor) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        val = (company_name,company_address,company_mail,company_salestax,currency,currencysign,  currencysign_placement,decimal_sepator,currency_example,date_format,example_dateformat,tax,printimage,  tax1name,tax1rate,printtax1,tax2name,tax2rate,printtax2,radiobut,cbut1,cbut2,cbut3,cbut4,cbut5,cbut6,est_prefix,est_text1,est_text2,est_text3,est_text4,est_text5,est_text6,est_default,est_spin1,est_predefined,adv_default,est_header)
        fbcursor.execute(sql, val)
        fbilldb.commit()
      else:
        shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
        sql = 'insert into company(name, address, email,salestaxno,currency,currencysign,currsignplace,  decimalseperator,excurrency,dateformat,exdate,taxtype,printimageornot,tax1name,tax1rate,printtax1,  tax2name,tax2rate,printtax2,image,attachment_file_type,miscellanoustab_cbutton1,miscellanoustab_cbutton2,miscellanoustab_cbutton3,miscellanoustab_cbutton4,miscellanoustab_cbutton5,miscellanoustab_cbutton6,Estimate_prefix,Customizeestimatetextlabels,Customizeestimatetextlabels1,Customizeestimatetextlabels2,Customizeestimatetextlabels3,Customizeestimatetextlabels4,Customizeestimatetextlabels5,Defaultestimatetemplate,Startingestimatenumber,Predefinedtextforestimates,adv_Selectedtemplatepreview,est_Headerboxbackgroundcolor) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        val = (company_name,company_address,company_mail,company_salestax,currency,currencysign,  currencysign_placement,decimal_sepator,currency_example,date_format,example_dateformat,tax,printimage,  tax1name,tax1rate,printtax1,tax2name,tax2rate,printtax2,filename.split('/')[-1],radiobut,cbut1,cbut2,cbut3,cbut4,cbut5,cbut6,est_prefix,est_text1,est_text2,est_text3,est_text4,est_text5,est_text6,est_default,est_spin1,est_predefined,adv_default,est_header)
        fbcursor.execute(sql, val)
        fbilldb.commit()
    else:
      if filename == "":
        sql = "update company set name=%s, address=%s, email=%s,salestaxno=%s,currency=%s,currencysign=%s,  currsignplace=%s,decimalseperator=%s,excurrency=%s,dateformat=%s,exdate=%s,taxtype=%s,  printimageornot=%s,tax1name=%s,tax1rate=%s,printtax1=%s,tax2name=%s,tax2rate=%s,printtax2=%s,attachment_file_type=%s,miscellanoustab_cbutton1=%s,miscellanoustab_cbutton2=%s,miscellanoustab_cbutton3=%s,miscellanoustab_cbutton4=%s,miscellanoustab_cbutton5=%s,miscellanoustab_cbutton6=%s,Estimate_prefix=%s,Customizeestimatetextlabels=%s,Customizeestimatetextlabels1=%s,Customizeestimatetextlabels2=%s,Customizeestimatetextlabels3=%s,Customizeestimatetextlabels4=%s,Customizeestimatetextlabels5=%s,Defaultestimatetemplate=%s,Startingestimatenumber=%s,Predefinedtextforestimates=%s,adv_Selectedtemplatepreview=%s,est_Headerboxbackgroundcolor=%s"
        val = (company_name,company_address,company_mail,company_salestax,currency,currencysign,  currencysign_placement,decimal_sepator,currency_example,date_format,example_dateformat,tax,printimage,  tax1name,tax1rate,printtax1,tax2name,tax2rate,printtax2,radiobut,cbut1,cbut2,cbut3,cbut4,cbut5,cbut6,est_prefix,est_text1,est_text2,est_text3,est_text4,est_text5,est_text6,est_default,est_spin1,est_predefined,adv_default,est_header)
        fbcursor.execute(sql, val)
        fbilldb.commit()
      else:
        shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
        sql = "update company set name=%s, address=%s, email=%s,salestaxno=%s,currency=%s,currencysign=%s,  currsignplace=%s,decimalseperator=%s,excurrency=%s,dateformat=%s,exdate=%s,taxtype=%s,  printimageornot=%s,tax1name=%s,tax1rate=%s,printtax1=%s,tax2name=%s,tax2rate=%s,printtax2=%s,image=%s,attachment_file_type=%s,miscellanoustab_cbutton1=%s,miscellanoustab_cbutton2=%s,miscellanoustab_cbutton3=%s,miscellanoustab_cbutton4=%s,miscellanoustab_cbutton5=%s,miscellanoustab_cbutton6=%s,Estimate_prefix=%s,Customizeestimatetextlabels=%s,Customizeestimatetextlabels1=%s,Customizeestimatetextlabels2=%s,Customizeestimatetextlabels3=%s,Customizeestimatetextlabels4=%s,Customizeestimatetextlabels5=%s,Defaultestimatetemplate=%s,Startingestimatenumber=%s,Predefinedtextforestimates=%s,adv_Selectedtemplatepreview=%s,est_Headerboxbackgroundcolor=%s"
        val = (company_name,company_address,company_mail,company_salestax,currency,currencysign,  currencysign_placement,decimal_sepator,currency_example,date_format,example_dateformat,tax,printimage,  tax1name,tax1rate,printtax1,tax2name,tax2rate,printtax2,filename.split('/')[-1],radiobut,cbut1,cbut2,cbut3,cbut4,cbut5,cbut6,est_prefix,est_text1,est_text2,est_text3,est_text4,est_text5,est_text6,est_default,est_spin1,est_predefined,adv_default,est_header)
        fbcursor.execute(sql, val)
        fbilldb.commit()
      
      
  
  addcustomerIcon = ImageTk.PhotoImage(Image.open("images/user_add.png"))
  save_setting = Button(settframe,compound="top", text="Save\nSettings",relief=RAISED,    command=save_company, image=saves, font=("arial", 8),bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
  save_setting.pack(side="left", pady=3, ipadx=4)
  pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
  pn.pack(side="left", padx=(0, 5))
  
  def wiz_page():
    global filname
    filname = ""
    def upload_cfilelogo():
      global filname
      f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
      filname = filedialog.askopenfilename(filetypes=f_types)
      shutil.copyfile(filname, os.getcwd()+'/images/'+filname.split('/')[-1])
      image = Image.open(filname)
      resize_image = image.resize((280, 140))
      imgclogo = ImageTk.PhotoImage(resize_image)
      btclogo = Button(wiz,width=280,height=140,image=imgclogo)
      btclogo.place(x=30,y=240)
      btclogo.photo = imgclogo
    def csave():
      company_name = company_namee.get()
      company_address = company_addresse.get('1.0', 'end-1c')
      company_email = company_emaile.get()
      salestaxregno = salestaxregnoe.get()
      cprint_logopic = cplogopic.get()
      sql = "select image from company"
      fbcursor.execute(sql)
      im = fbcursor.fetchone()
      sql = "select * from company"
      fbcursor.execute(sql)
      i = fbcursor.fetchall()
      if not i:
        if filname == "":
          sql = 'insert into company(name, address, email,salestaxno,printimageornot) values(%s, %s, %s, %s, %s)'
          val = (company_name,company_address,company_email,salestaxregno,cprint_logopic)
          fbcursor.execute(sql, val)
          fbilldb.commit()
        else:
          shutil.copyfile(filname, os.getcwd()+'/images/'+filname.split('/')[-1])
          sql = 'insert into company(name, address, email,salestaxno,printimageornot,image) values(%s, %s, %s, %s, %s, %s)'
          val = (company_name,company_address,company_email,salestaxregno,cprint_logopic,filname.split('/')[-1],)
          fbcursor.execute(sql, val)
          fbilldb.commit()
      else:
        if filname == "":
          sql = "update company set name=%s, address=%s, email=%s,salestaxno=%s,printimageornot=%s"
          val = (company_name,company_address,company_email,salestaxregno,cprint_logopic)
          fbcursor.execute(sql, val)
          fbilldb.commit()
        else:
          shutil.copyfile(filname, os.getcwd()+'/images/'+filname.split('/')[-1])
          sql = "update company set name=%s, address=%s, email=%s,salestaxno=%s,printimageornot=%s,image=%s"
          val = (company_name,company_address,company_email,salestaxregno,cprint_logopic,filname.split('/')[-1])
          fbcursor.execute(sql, val)
          fbilldb.commit()
      centry.delete(0, END)
      centry.insert(0, company_name)
      caddent.delete('1.0', END)
      caddent.insert('1.0', company_address)
      cemailentry.delete(0, END)
      cemailentry.insert(0, company_email)
      ste.delete(0, END)
      ste.insert(0, salestaxregno)
      if cprint_logopic == 1:
        primage.select()
      else:
        primage.deselect()
      try:
        image = Image.open("images/"+filname.split('/')[-1])
        resize_image = image.resize((280, 160))
        image = ImageTk.PhotoImage(resize_image)
        btlogo = Button(secondtab,width=280,height=160,image=image)
        btlogo.place(x=580,y=280)
        btlogo.photo = image
      except:
        pass
      wiz.destroy()


      
      

    
    wiz = Toplevel()
    wiz.geometry("500x449+400+167")
    wiz.title("Wellcome to Quick Start Wizard")
    sql = "select * from company"
    fbcursor.execute(sql)
    secctab = fbcursor.fetchone()
    comp_infor = Label(wiz,text="Enter Your Company Information",font='arial 13 bold',fg="blue")
    comp_infor.place(x=15,y=15)
    company_da_laframe = LabelFrame(wiz,text="Company data",height=180, width=460)
    company_da_laframe.place(x=15,y=40)
    company_name = Label(wiz,text="Company name")
    company_name.place(x=30,y=60)
    company_namee = Entry(wiz,width=50)
    company_namee.place(x=160,y=60)
    if  not secctab:
      pass
    else:
      company_namee.insert(0, secctab[1])
  
    company_address = Label(wiz,text="Company address")
    company_address.place(x=30,y=90)
    company_addresse = scrolledtext.ScrolledText(wiz,)
    company_addresse.place(x=160,y=90,width=250,height=60)
    if  not secctab:
      pass
    else:
      company_addresse.insert('1.0', secctab[2])

    company_email = Label(wiz,text="Email address")
    company_email.place(x=30,y=160)
    company_emaile = Entry(wiz,width=50)
    company_emaile.place(x=160,y=160)
    if  not secctab:
      pass
    else:
      company_emaile.insert(0, secctab[3])

    salestaxregno = Label(wiz,text="Sales Tax.Reg.No")
    salestaxregno.place(x=30,y=190)
    salestaxregnoe = Entry(wiz,width=50)
    salestaxregnoe.place(x=160,y=190)
    if  not secctab:
      pass
    else:
      salestaxregnoe.insert(0, secctab[4])
    
    
    company_da_laframe = LabelFrame(wiz,text="Company logo",height=190, width=460)
    company_da_laframe.place(x=15,y=220)
    try:
      image_wiz = Image.open("images/"+secctab[13])
      resize_image = image_wiz.resize((280, 140))
      image_wiza = ImageTk.PhotoImage(resize_image)
      btclogo = Button(wiz,width=280,height=140,image=image_wiza)
      btclogo.place(x=30,y=240)
      btclogo.photo = image_wiza
    except:
      pass
    cplogopic = BooleanVar()
    cprint_logopic = Checkbutton(wiz,text='Print logo picture',bg='white',onvalue =1,
                        offvalue = 0,variable=cplogopic)
    cprint_logopic.place(x=320,y=250)
    if  not secctab:
      pass
    else:
      if secctab[14] == 1:
        cprint_logopic.select()
      else:
        cprint_logopic.deselect()
      
    load_img = Button(wiz,text='Load logo image',command=upload_cfilelogo)
    load_img.place(x=320,y=360)
    save_com_wiz = Button(wiz,text='Save',width=10,command=csave)
    save_com_wiz.place(x=370,y=415)

  quick_start_wiz = Button(settframe,compound="top", text="Quick\nStart Wizard ",relief=RAISED,    command=wiz_page, image=photo, font=("arial", 8),bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
  quick_start_wiz.pack(side="left", pady=3, ipadx=4)
  pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
  pn.pack(side="left", padx=(0, 5))
  
  
  
  invoi1label = Label(settingsframe, text="Settings", font=("arial", 18), bg="#f8f8f2")
  invoi1label.pack(side="left", padx=(20,0))
  
  global tab06
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
  
  ################### tab01 ###################################
  sql = "select * from company"
  fbcursor.execute(sql)
  sectab = fbcursor.fetchone()
  
  firsttab1=Frame(tab01, relief=GROOVE, bg="#f8f8f2")
  firsttab1.pack(side="top", fill=BOTH)
  
  firsttab=Frame(firsttab1, bg="#f5f3f2", height=700)
  firsttab.pack(side="top", fill=BOTH)
  
  messagelbframe=LabelFrame(firsttab,text="Menu and Window Color Style", height=60, width=180)
  messagelbframe.place(x=5, y=15)
  
  win_menu = StringVar()
  winstyle = ttk.Combobox(firsttab,textvariable=win_menu)
  winstyle.place(x=22 ,y=40)
  winstyle['values'] = ('whidbey','windows XP','windows 7','windows 8','windows 10')
  winstyle.current(0)
  fbill = Label(firsttab,text="F-Billing Revolution 2022",font="arial 12 bold").place(x=220,y=20)
  
  dbhost=LabelFrame(firsttab,text="Database Server Hostname", height=60, width=415)
  dbhost.place(x=5, y=85)
  
  db = Label(firsttab, text="DESKTOP-2K")
  db.place(x=15,y=110)
  
  exc=LabelFrame(firsttab,text="Extra cost name", height=180, width=415)
  exc.place(x=5, y=155)
  
  
  
  def insert_valueexc():
    i = varexc.get()
    if i == "":
      pass
    else:
      entryexc.delete(0, END)
      sql1 = "select * from company"
      fbcursor.execute(sql1)
      com = fbcursor.fetchone()
      if not com:
        messagebox.showinfo("Alert", "Create Company Settings.")
      else:
        companyid = com[0]
        sql = 'insert into extra_cost_name(companyid,extra_cost_name) values(%s,%s)'
        val = (companyid,i)
        fbcursor.execute(sql,val)
        fbilldb.commit()
        for record in exctree.get_children():
          exctree.delete(record)
        sql = 'select * from extra_cost_name'
        fbcursor.execute(sql)
        setexctree = fbcursor.fetchall()
        countp = 0
        for i in setexctree:
          immm = str(i[2])
          imn = str.replace(immm," ","_")
          exctree.insert(parent='', index='end', iid=countp, text='hello', values=(imn))
          countp += 1
  # new_value = String
        
        
  
  def edit_valueexc(event):
    selected_item = exctree.selection()[0]
    temp = list(exctree.item(selected_item , 'values'))
    entryexc.delete(0, END)
    entryexc.insert(0, temp)
  
  def save_valueexc():
    i = entryexc.get()
    if i == "":
      pass
    else:
      selected0 = exctree.focus()
      valuz1= exctree.item(selected0)["values"]
      idgettingextracnid=valuz1[0]
      print(i,idgettingextracnid)
      sql1 = "select * from company"
      fbcursor.execute(sql1)
      com = fbcursor.fetchone()
      companyid = com[0]
      if not com:
        pass
      else:
        sql = 'update extra_cost_name set extra_cost_name=%s where extra_cost_name=%s'
        val = (i,idgettingextracnid)
        fbcursor.execute(sql,val)
        fbilldb.commit()
        entryexc.delete(0, END)
        for record in exctree.get_children():
            exctree.delete(record)
        fbcursor.execute("select *  from extra_cost_name")
        pandsdata = fbcursor.fetchall()
        countp = 0
        for i in pandsdata:
          immm = str(i[2])
          imn = str.replace(immm," ","_")
          exctree.insert('', index='end', iid=countp, text='', values=(imn))
          countp += 1
    
    
  
  def del_valueexc():
    itemid = exctree.item(exctree.focus())["values"][0]
    sql = "delete from extra_cost_name where extra_cost_name = %s"
    val = (itemid, )
    fbcursor.execute(sql, val)
    fbilldb.commit()
    exctree.delete(exctree.selection()[0])
      
      
  
    
    
    
  
  
  
  scrollbarx = Scrollbar(firsttab, orient=HORIZONTAL)
  scrollbary = Scrollbar(firsttab, orient=VERTICAL)
  exctree = ttk.Treeview(firsttab, columns=("1"),height=40,selectmode='browse', yscrollcommand=scrollbary.set,   xscrollcommand=scrollbarx.set)
  # exctree["show"]='headings'
  scrollbary.config(command=exctree.yview)
  scrollbary.place(x=394,y=200,height=125)
  scrollbarx.config(command=exctree.xview)
  scrollbarx.place(x=15,y=310, width=380)
  exctree.heading('1', text="Extra cost name",)
  # exctree.column('#0', stretch=NO, minwidth=0, width=0)
  exctree.column("#0",width=0,anchor='c', stretch=False)
  exctree.column('1',width=378,anchor='c')
  exctree.place(x=15,y=200,height=115,width=380)
  exctree.bind('<Double-Button-1>' , edit_valueexc)
  sql = 'select * from extra_cost_name'
  fbcursor.execute(sql)
  setexctree = fbcursor.fetchall()
  countp = 0
  for i in setexctree:
      print(i[2])
      immm = str(i[2])
      imn = str.replace(immm," ","_")
      exctree.insert(parent='', index='end', iid=countp, text='', values=(imn))
      countp += 1
  # new_value = StringVar()
  
  # def edit_window_box(val):
      
  #     edit_window = Toplevel(root)
  #     edit_window.title("Edit the value or cancel")
  #     edit_window.geometry("1000x250")
  #     label_edit = Label(edit_window , text='Enter value to edit or press cancel', 
  #     font = ("Times New Roman", 10)).grid(column=0,row=1,padx=0, pady = 2)
  #     #create edit box
  #     edit_box = Entry(edit_window)
  #     edit_box.insert(0,val)
  #     edit_box.grid(column=1,row=1,padx=0,pady=2)
  #     #auto select edit window 
  #     edit_window.focus()
      
  #     def value_assignment(event):
  #         printing = edit_box.get()
  #         new_value.set(printing)
  #         #only destroy will not update the value (perhaps event keeps running in background)
  #         #quit allows event to stop n update value in tree but does not close the window in single click 
  #         #rather on dbl click shuts down entire app 
  #         edit_window.quit()
  #         edit_window.destroy()
      
  #     edit_window.bind('<Return>', value_assignment )
  
  #     B1 = Button(edit_window, text="Okay")
  #     B1.bind('<Button-1>',value_assignment)
  #     B1.grid(column=0,row=10,padx=0, pady = 20)
      
  #     B2 = Button(edit_window, text="Cancel", command = edit_window.destroy).grid(column=1,row=10,padx=10,   pady = 20)
  #     edit_window.mainloop()
      
  # #will explain
  # #variable to hold col value (col clicked)
  # shape1 = IntVar()
  # #tracks both col , row on mouse click
  # def tree_click_handler(event):
  #     cur_item = exctree.item(exctree.focus())
  #     col = exctree.identify_column(event.x)[1:]
  #     rowid = exctree.identify_row(event.y)[1:]
  #     #updates list
  #     shape1.set(col)
  #     try:
  #         x,y,w,h = exctree.bbox('I'+rowid,'#'+col)
  #     except:pass
  #     #tree.tag_configure("highlight", background="yellow")
  #     return(col)
      
  # #code linked to event    
  # exctree.bind('<ButtonRelease-1>', tree_click_handler)
  
  # def edit(event):
  #     try:
  #         selected_item = exctree.selection()[0]
  #         temp = list(exctree.item(selected_item , 'values'))
  #         tree_click_handler
  #         col_selected = int(shape1.get())-1
  #         edit_window_box(temp[col_selected])
  #         #do not run if edit window is open
  #         #use edit_window.mainloop() so value assign after window closes
  #         temp[col_selected] = new_value.get()
  #         exctree.item(selected_item, values= temp)
  #     except: pass
      
      
  # #binding allows to edit on screen double click
  # exctree.bind('<Double-Button-1>' , edit)
  varexc = StringVar()
  entryexc = Entry(firsttab,width=25,textvariable=varexc)
  entryexc.place(x=15,y=173)
  
  btexcadd = Button(firsttab,text="Add new line",command=insert_valueexc)
  btexcadd.place(x=175,y=171)
  
  btexcedit = Button(firsttab,text="Edit line   ",command=save_valueexc)
  btexcedit.place(x=260,y=171)
  btexcadd = Button(firsttab,text=" Delete line  ",command=del_valueexc)
  btexcadd.place(x=330,y=171)
  
  exc=LabelFrame(firsttab,text="Predefined text records for header and footer", height=180, width=415)
  exc.place(x=5, y=350)
  
  def insert_valuepre():
    i = prestr.get()
    if i == "":
      pass
    else:
      entrypre.delete(0, END)
      sql1 = "select * from company"
      fbcursor.execute(sql1)
      com = fbcursor.fetchone()
      if not com:
        messagebox.showinfo("Alert", "Create Company Settings.")
      else:
        companyid = com[0]
        sql = 'insert into header_and_footer(companyid,headerandfooter) values(%s,%s)'
        val = (companyid,i)
        fbcursor.execute(sql,val)
        fbilldb.commit()
        for record in pretree.get_children():
          pretree.delete(record)
        sql = 'select * from header_and_footer'
        fbcursor.execute(sql)
        setexctree = fbcursor.fetchall()
        countp = 0
        for i in setexctree:
          pret = str(i[2])
          pre = str.replace(pret," ","_")
          pretree.insert(parent='', index='end', iid=countp, text='hello', values=(pre))
          countp += 1
  # new_value = String
        
        
  
  def edit_valuepre(event):
    selected_item = pretree.selection()[0]
    temp = list(pretree.item(selected_item , 'values'))
    entrypre.delete(0, END)
    entrypre.insert(0, temp)
  
  def save_valuepre():
    i = prestr.get()
    if i == "":
      pass
    else:
      selected0 = pretree.focus()
      valuz1= pretree.item(selected0)["values"]
      idgettingextracnid=valuz1[0]
      print(i,idgettingextracnid)
      sql1 = "select * from company"
      fbcursor.execute(sql1)
      com = fbcursor.fetchone()
      companyid = com[0]
      if not com:
        pass
      else:
        sql = 'update header_and_footer set headerandfooter=%s where headerandfooter=%s'
        val = (i,idgettingextracnid)
        fbcursor.execute(sql,val)
        fbilldb.commit()
        entryexc.delete(0, END)
        for record in pretree.get_children():
            pretree.delete(record)
        fbcursor.execute("select *  from header_and_footer")
        pandsdata = fbcursor.fetchall()
        countp = 0
        for i in pandsdata:
          pret = str(i[2])
          pre = str.replace(pret," ","_")
          pretree.insert('', index='end', iid=countp, text='', values=(pre))
          countp += 1
    
    
  
  def del_valuepre():
    itemid = pretree.item(pretree.focus())["values"][0]
    print(itemid)
    sql = "delete from header_and_footer where headerandfooter = %s"
    val = (itemid,)
    fbcursor.execute(sql, val)
    fbilldb.commit()
    for record in pretree.get_children():
      pretree.delete(record)
    fbcursor.execute("select *  from header_and_footer")
    pandsdata = fbcursor.fetchall()
    countp = 0
    for i in pandsdata:
      pret = str(i[2])
      pre = str.replace(pret," ","_")
      pretree.insert('', index='end', iid=countp, text='', values=(pre))
      countp += 1
    
      
  
  scrollbarx = Scrollbar(firsttab, orient=HORIZONTAL)
  scrollbary = Scrollbar(firsttab, orient=VERTICAL)
  pretree = ttk.Treeview(firsttab, columns=("1"),height=400,     selectmode="extended",   yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
  # exctree["show"]='headings'
  scrollbary.config(command=pretree.yview)
  scrollbary.place(x=395,y=400,height=115)
  scrollbarx.config(command=pretree.xview)
  scrollbarx.place(x=15,y=510, width=380)
  pretree.heading('1', text="header and footer",)
  pretree.column('#0', stretch=NO, minwidth=0, width=0)
  pretree.column('1', stretch=NO, width=378)
  pretree.place(x=15,y=400,height=115,width=380)
  pretree.bind('<Double-Button-1>' , edit_valuepre)
  sql = 'select * from header_and_footer'
  fbcursor.execute(sql)
  setexctree = fbcursor.fetchall()
  countp = 0
  for i in setexctree:
    pret = str(i[2])
    pre = str.replace(pret," ","_")
    pretree.insert(parent='', index='end', iid=countp, text='hello', values=(pre))
    countp += 1
  prestr = StringVar()
  entrypre = Entry(firsttab,width=25,textvariable=prestr)
  entrypre.place(x=15,y=370)
  btexcadd = Button(firsttab,text="Add new line",command=insert_valuepre)
  btexcadd.place(x=175,y=370)
  btpredit = Button(firsttab,text="Edit line   ",command=save_valuepre)
  btpredit.place(x=260,y=370)
  btexcadd = Button(firsttab,text=" Delete line   ",command=del_valuepre)
  btexcadd.place(x=330,y=370)
  
  ver = Label(firsttab,text="FREE version.Upgrade PRO version for all features and Ad free invoice")
  ver.place(x=480,y=15)
  
  
  chapass=LabelFrame(firsttab,text="Change Password", height=150, width=500)
  chapass.place(x=480, y=40)
  
  enterold = StringVar()
  lenold = Label(firsttab,text="Enter your old password")
  lenold.place(x=495,y=60)
  enold = Entry(firsttab,textvariable=enterold)
  enold.place(x=640,y=60)
  
  enternew = StringVar()
  ennew = Label(firsttab,text="New password")
  ennew.place(x=495,y=90)
  newpass = Entry(firsttab,textvariable=enternew)
  newpass.place(x=640,y=90)
  
  
  cnewpass = StringVar()
  cnp = Label(firsttab,text="Confirm new password")
  cnp.place(x=495,y=120)
  cnewp = Entry(firsttab,textvariable=cnewpass)
  cnewp.place(x=640,y=120)

  def change_pass():
    old_pass = enterold.get()
    new_pass = enternew.get()
    cnew_pass = cnewpass.get()
    usna = username1.get()
    print(usna)
    sql='SELECT * FROM users WHERE username=%s'
    val=(usna,)
    fbcursor.execute(sql,val)
    chpass = fbcursor.fetchone()
    print(chpass)
    if old_pass == "" or new_pass == "" or cnew_pass == "":
        messagebox.showerror('Password Error','Plz enter password')
    elif old_pass == chpass[4]:
      if new_pass == cnew_pass:
        sqll='UPDATE users SET password=%s,confirm_password=%s WHERE userID=%s'
        vall=(new_pass,cnew_pass,chpass[0])
        fbcursor.execute(sqll,vall,)
        fbilldb.commit()
        messagebox.showinfo('Updated','Password updated successfully')
      else:
        messagebox.showerror('Password Error','password is not match')
    else:
      messagebox.showerror('Password Error','Old Password is Incorrect')
  chabtn = Button(firsttab,text="Change password",command=change_pass)
  chabtn.place(x=840,y=150)
  
  termf=LabelFrame(firsttab,text="Terms of payment", height=150, width=500)
  termf.place(x=480, y=190)


  def insert_valueterm():
    first = entrytopstr.get()
    second = entrydsstr.get()
    if first == "" or second == "":
      pass
    else:
      entrytop.delete(0, END)
      entryds.delete(0, END)
      sql1 = "select * from company"
      fbcursor.execute(sql1)
      com = fbcursor.fetchone()
      if not com:
        messagebox.showinfo("Alert", "Create Company Settings.")
      else:
        companyid = com[0]
        sql = 'insert into terms_of_payment(companyid,terms_of_payment,Date_shift) values(%s,%s,%s)'
        val = (companyid,first,second)
        fbcursor.execute(sql,val)
        fbilldb.commit()
        for record in termtree.get_children():
          termtree.delete(record)
        sql = 'select * from terms_of_payment'
        fbcursor.execute(sql)
        setexctree = fbcursor.fetchall()
        countp = 0
        for i in setexctree:
          
          termtree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[3]))
          countp += 1
  # new_value = String
        
        
  
  def edit_valueterm(event):
    itemid = termtree.item(termtree.focus())["values"][0]
    sql = "select * from terms_of_payment where terms_of_payment = %s"
    val = (itemid,)
    fbcursor.execute(sql,val)
    editterm = fbcursor.fetchone()
    entrytop.delete(0, END)
    entryds.delete(0, END)
    entrytop.insert(0, editterm[2])
    entryds.insert(0, editterm[3])
  
  def save_valueterm():
    first = entrytopstr.get()
    second = entrydsstr.get()
    if first == "" or second == "":
      pass
    else:
      itemid = termtree.item(termtree.focus())["values"][0]
      sql1 = "select * from company"
      fbcursor.execute(sql1)
      com = fbcursor.fetchone()
      if not com:
        pass
      else:
        sql = "select * from terms_of_payment where terms_of_payment=%s"
        val = (itemid,)
        fbcursor.execute(sql,val)
        payt = fbcursor.fetchone()
        sql2 = 'update terms_of_payment set terms_of_payment=%s,Date_shift=%s where terms_of_paymentID=%s'
        val2 = (first,second,payt[0])
        fbcursor.execute(sql2,val2)
        fbilldb.commit()
        entrytop.delete(0, END)
        entryds.delete(0, END)
        for record in termtree.get_children():
          termtree.delete(record)
        fbcursor.execute("select *  from terms_of_payment")
        pandsdata = fbcursor.fetchall()
        countp = 0
        for i in pandsdata:
          
          termtree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[3]))
          countp += 1
    
    
  
  def del_valueterm():
    itemid = termtree.item(termtree.focus())["values"][0]
    print(itemid)
    sql = "delete from terms_of_payment where terms_of_payment = %s"
    val = (itemid,)
    fbcursor.execute(sql, val)
    fbilldb.commit()
    for record in termtree.get_children():
        termtree.delete(record)
    fbcursor.execute("select *  from terms_of_payment")
    pandsdata = fbcursor.fetchall()
    countp = 0
    for i in pandsdata:
      termtree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[3]))
      countp += 1
  
  
  
  scrollbarx = Scrollbar(firsttab, orient=HORIZONTAL)
  scrollbary = Scrollbar(firsttab, orient=VERTICAL)
  termtree = ttk.Treeview(firsttab, columns=("1","2"),height=400,selectmode="extended",   yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
  # exctree["show"]='headings'
  scrollbary.config(command=termtree.yview)
  scrollbary.place(x=870,y=228,height=100)
  scrollbarx.config(command=termtree.xview)
  scrollbarx.place(x=495,y=313, width=380)
  termtree.heading('1', text="Terms of payment",)
  termtree.heading('2', text="Date shift (days)",)
  termtree.column('#0', stretch=NO, minwidth=0, width=0)
  termtree.column('1', stretch=NO, minwidth=0, width=250)
  termtree.column('2', stretch=NO, minwidth=0, width=128)
  termtree.place(x=495,y=235,height=80,width=380)
  termtree.bind('<Double-Button-1>' , edit_valueterm)

  sql = 'select * from terms_of_payment'
  fbcursor.execute(sql)
  termt = fbcursor.fetchall()
  countp = 0
  for i in termt:
      termtree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[3]))
      countp += 1
  entrytopstr = StringVar()
  entrytop = Entry(firsttab,width=25,textvariable=entrytopstr)
  entrytop.place(x=495,y=208)
  entrydsstr = StringVar()
  entryds = Entry(firsttab,textvariable=entrydsstr)
  entryds.place(x=670,y=208)
  bttermadd = Button(firsttab,text="Add new line",command=insert_valueterm)
  bttermadd.place(x=800,y=205)
  bttermedit = Button(firsttab,text="     Edit line  ",command=save_valueterm)
  bttermedit.place(x=890,y=205)
  bttermdel = Button(firsttab,text="  Delete line  ",command=del_valueterm)
  bttermdel.place(x=890,y=240)
  
  radem=LabelFrame(firsttab,text="Invoice/Oder/Estimate/P.order Email Attachment file type", height=60,   width=500)
  radem.place(x=480, y=340)
  radema = StringVar()
  radpdf = Radiobutton(firsttab,variable=radema,value="PDF",text='PDF')
  radpdf.place(x= 485, y= 360 )
  radhtml = Radiobutton(firsttab,variable=radema,value="HTML",text='HTML')
  radhtml.place(x= 660, y= 360 )
  if  not sectab:
    pass
  else:
    if sectab[22] == 'PDF':
      radpdf.select()
    elif sectab[22] == 'HTML':
      radhtml.select()
    else:
      pass
  
  checkb1 = IntVar()
  check1 = Checkbutton(firsttab,variable = checkb1, 
                        text="PDF attachment with Embedded Fonts (PDF file size will be larger,but readable on   all devices) ", 
                        onvalue =1 ,
                        offvalue = 0,
                        )
  
  check1.place(x=480,y=400)
  if  not sectab:
    pass
  else:
    if sectab[23] == 1:
      check1.select()
    else:
      check1.deselect()
  
  checkb2 = IntVar()
  check2 = Checkbutton(firsttab,variable = checkb2, 
                        text="invoice numbering with leading zero and current year", 
                        onvalue =1 ,
                        offvalue = 0,
                       )
  
  check2.place(x=480,y=420)
  if  not sectab:
    pass
  else:
    if sectab[24] == 1:
      check2.select()
    else:
      check2.deselect()
  
  checkb3 = IntVar()
  check3 = Checkbutton(firsttab,variable = checkb3, 
                        text="Order numbering with leading zero and current year", 
                        onvalue =1 ,
                        offvalue = 0,
                        )
  
  check3.place(x=480,y=440)
  if  not sectab:
    pass
  else:
    if sectab[25] == 1:
      check3.select()
    else:
      check3.deselect()
  
  checkb4 = IntVar()
  check4 = Checkbutton(firsttab,variable = checkb4, 
                        text="Estimate numbering with leading zero and current year", 
                        onvalue =1 ,
                        offvalue = 0,
                       )
  
  check4.place(x=480,y=460)
  if  not sectab:
    pass
  else:
    if sectab[26] == 1:
      check4.select()
    else:
      check4.deselect()
  
  checkb5 = IntVar()
  check5 = Checkbutton(firsttab,variable = checkb5, 
                        text="Purchsae order numbering with leading zero and current year", 
                        onvalue =1 ,
                        offvalue = 0,
                        )
  check5.place(x=480,y=480)
  if  not sectab:
    pass
  else:
    if sectab[27] == 1:
      check5.select()
    else:
      check5.deselect()
  
  checkb6 = IntVar()
  check6 = Checkbutton(firsttab,variable = checkb6, 
                        text="Confirmation before closing F-billing Revolution", 
                        onvalue =1 ,
                        offvalue = 0,
                      )
  
  check6.place(x=480,y=500)
  if  not sectab:
    pass
  else:
    if sectab[28] == 1:
      check6.select()
    else:
      check6.deselect()
  
  ################### tab02 ###################################
  sql = "select * from company"
  fbcursor.execute(sql)
  sectab = fbcursor.fetchone()
  print(sectab)
  
  
  secondtab1=Frame(tab02, relief=GROOVE, bg="#f8f8f2")
  secondtab1.pack(side="top", fill=BOTH)
  
  secondtab=Frame(secondtab1, bg="#f5f3f2", height=700)
  secondtab.pack(side="top", fill=BOTH)
  
  comdata=LabelFrame(secondtab,text="Company data", height=200, width=500)
  comdata.place(x=5, y=15)
  cname = Label(secondtab,text="Company name")
  cname.place(x=20, y =35)
  comname = StringVar()
  centry = Entry(secondtab,textvariable=comname)
  if  not sectab:
    pass
  else:
    centry.insert(0, sectab[1])
  centry.place(x=160,y=35,width=280)
  
  
  cadd = Label(secondtab,text="Company Address")
  cadd.place(x=20, y =65)
  caddent = scrolledtext.ScrolledText(secondtab)
  if  not sectab:
    pass
  else:
    caddent.insert('1.0', sectab[2])
  caddent.place(x=160,y=65,height=80,width=280)
  
  cemail = Label(secondtab,text="E-mail Address")
  cemail.place(x=20, y =160)
  comemail = StringVar()
  cemailentry = Entry(secondtab,textvariable=comemail)
  if  not sectab:
    pass
  else:
    cemailentry.insert(0, sectab[3])
  cemailentry.place(x=160,y=160,width=280)
  
  stl = Label(secondtab,text="sales Tax.Reg.No.")
  stl.place(x=20, y =185)
  comsalestax = StringVar()
  ste = Entry(secondtab,textvariable=comsalestax)
  if  not sectab:
    pass
  else:
    ste.insert(0, sectab[4])
  ste.place(x=160,y=185,width=280)
  
  
  curre=LabelFrame(secondtab,text="Currency", height=125, width=500)
  curre.place(x=5, y=220)
  currl = Label(secondtab,text="Currency")
  currl.place(x=20,y= 240)
  comcur = StringVar()
  currbox = ttk.Combobox(secondtab,width=10,textvariable=comcur)
  currbox['values'] =('ALL','AFN','ARS','AWG','AUD','AZN','BSD','BBD','BYN','BZD','BMD','BOB','BAM','BWP',  'BGN','BRL','BND','KHR','CAD','KYD','CLP','CNY','COP','CRC','HRK','CUP','CZK','DKK','DOP','XCD','EGP','SVC',  'EUR','FKP','FJD','GHS','GIP','GTQ','GGP','GYD','HNL','HKD','HUF','ISK','INR','IDR','IRR','IMP','ILS','JMD',  'JPY','JEP','KZT','KPW','KRW','KGS','LAK','LBP','LRD','MKD','MYR','MUR','MXN','MNT','MNT','MZN','NAD','NPR',  'ANG','NZD','NIO','NGN','NOK','OMR','PKR','PAB','PYG','PEN','PHP','PLN','QAR','RON','RUB','SHP','SAR','RSD',  'SCR','SGD','SBD','SOS','KRW','ZAR','LKR','SEK','CHF','SRD','SYP','TWD','THB','TTD','TRY','TVD','UAH','AED',  'GBP','USD','UYU','UZS','VEF','VND','YER','ZWD',)
  if  not sectab:
    pass
  elif sectab[5]:
    currbox.insert(0, sectab[5])
  currbox.place(x=80,y=240)
  
  def signpl(event):
    amsgpl = comcursignpla.get()
    currsign = comcursign.get()
    if amsgpl == "before amount":
      exbox.delete(0, END)
      exbox.insert(0, currsign+'8347.26')
    elif amsgpl == "after amount":
      exbox.delete(0, END)
      exbox.insert(0, '8347.26'+currsign)
    elif amsgpl == "before amount with space":
      exbox.delete(0, END)
      exbox.insert(0, currsign+'  8347.26')
    elif amsgpl == "after amount with space":
      exbox.delete(0, END)
      exbox.insert(0, '8347.26  '+currsign)
  
  
  currsignl = Label(secondtab,text="Currency sign")
  currsignl.place(x=180,y=240)
  comcursign = StringVar()
  currsignbox = ttk.Combobox(secondtab,width=10,textvariable=comcursign)
  currsignbox.bind("<<ComboboxSelected>>", signpl)
  currsignbox["values"] = ('Lek','؋','$','ƒ','$','₼','$','$','Br','BZ$','$','$b','KM','P','лв','R$','$','៛',  '$','$','$','¥','$','₡','kn','₱','Kč','kr','RD$','$','£','$','€','£','$','¢','£','Q','£','$','L','$','Ft',  'kr','₹','Rp','﷼','£','₪','J$','¥','£','лв','₩','₩','₭','£','$','ден','RM','₨','$','₮',' د.إ','MT','$','₨',  'ƒ','$','C$','₦','kr','﷼','₨','B/.','Gs','S/.','₱','zł','﷼','lei','₽','£','﷼','Дин.','₨','S','₩','R','₨',  'kr','CHF','£','NT$','฿','TT$','₺','$','₴','د.إ','$U','лв','Bs','₫','﷼','Z$')
  if  not sectab:
    pass
  elif sectab[6]:
    currsignbox.insert(0, sectab[6])
  currsignbox.place(x=265,y=240)
  
  cspl = Label(secondtab,text="Currency sign placement")
  cspl.place(x=20,y=270)
  
  def amountsignspace(event):
    amsgpl = comcursignpla.get()
    currsign = comcursign.get()
    if amsgpl == "before amount":
      exbox.delete(0, END)
      exbox.insert(0, currsign+'8347.26')
    elif amsgpl == "after amount":
      exbox.delete(0, END)
      exbox.insert(0, '8347.26'+currsign)
    elif amsgpl == "before amount with space":
      exbox.delete(0, END)
      exbox.insert(0, currsign+'  8347.26')
    elif amsgpl == "after amount with space":
      exbox.delete(0, END)
      exbox.insert(0, '8347.26  '+currsign)
    
      
      
  comcursignpla = StringVar()
  cspe = ttk.Combobox(secondtab,width=24,textvariable=comcursignpla,)
  cspe.bind("<<ComboboxSelected>>", amountsignspace)
  cspe["values"] = ("before amount","after amount",'before amount with space',"after amount with space")
  if  not sectab:
    pass
  elif sectab[7]:
    cspe.insert(0, sectab[7])
  cspe.place(x=180,y=270)
  
  def decpl(event):
    dec = comdecsep.get()
    ex = comex.get()
    if dec == ",":
      var = str.replace(ex,".",",")
      exbox.delete(0, END)
      exbox.insert(0, var)
    elif dec == ".":
      var1 = str.replace(ex,",",".")
      exbox.delete(0, END)
      exbox.insert(0, var1)
  dsl = Label(secondtab,text="Decimal separator")
  dsl.place(x=20,y=300)
  comdecsep = StringVar()
  currbox = ttk.Combobox(secondtab,width=5,textvariable=comdecsep)
  currbox.bind("<<ComboboxSelected>>",decpl)
  currbox['values'] = ('.',',')
  if  not sectab:
    pass
  elif sectab[8]:
    currbox.insert(0, sectab[8])
  currbox.place(x=130,y=300)
  
  exl = Label(secondtab,text="Example")
  exl.place(x=185,y=300)
  comex = StringVar()
  exbox = Entry(secondtab,width=15,textvariable=comex)
  if  not sectab:
    exbox.insert(0, 84367.26)
  elif sectab[9]:
    exbox.insert(0, sectab[9])
  exbox.place(x=245,y=300)
  
  btred = Button(secondtab,text="Restore Default")
  btred.place(x=400,y=270)
  btsc = Button(secondtab,text="SET CURRENCY")
  btsc.place(x=400,y=300)
  
  datef=LabelFrame(secondtab,text="Date format", height=60, width=500)
  datef.place(x=5, y=355)
  
  def daffun(event):
    dafget = daf.get()
    if dafget == "mm-dd-yyyy":
      exd._set_text(exd._date.strftime('%m-%d-%Y'))
    elif dafget == "dd-mm-yyyy":
      exd._set_text(exd._date.strftime('%d-%m-%Y'))
    elif dafget == "yyy.mm.dd":
      exd._set_text(exd._date.strftime('%Y.%m.%d'))
    elif dafget == "mm/dd/yyyy":
      exd._set_text(exd._date.strftime('%m/%d/%Y'))
    elif dafget == "dd/mm/yyy":
      exd._set_text(exd._date.strftime('%d/%m/%Y'))
    elif dafget == "dd.mm.yyyy":
      exd._set_text(exd._date.strftime('%d.%m.%Y'))
    elif dafget == "yyyy/mm/dd":
      exd._set_text(exd._date.strftime('%Y/%m/%d'))
    
  
  comdaf = StringVar()
  daf = ttk.Combobox(secondtab,textvariable=comdaf)
  daf["values"] = ("Default",'mm-dd-yyyy','dd-mm-yyyy','yyy.mm.dd','mm/dd/yyyy','dd/mm/yyy','dd.mm.yyyy','yyyy/  mm/dd')
  daf.bind("<<ComboboxSelected>>",daffun)
  if not sectab:
    pass
  elif sectab[10]:
    daf.insert(0, sectab[10])
  daf.place(x=60,y=380)
  
  
  exd = DateEntry(secondtab,)
  exd.place(x=280,y=380)
  if  not sectab:
    pass
  elif sectab[11]:
    exd.delete(0, END)
    exd.insert(0, sectab[11])
  
  tnr=LabelFrame(secondtab,text="Tax name and rate", height=200, width=500)
  tnr.place(x=560, y=15)
  
  stt=LabelFrame(secondtab,text="Select tax type", height=120, width=180)
  stt.place(x=580, y=30)
  def rtax1():
    ch = radtax.get()
    if ch == 1:
      tax1namel.place_forget()
      tax1namee.place_forget()
      tax1ratel.place_forget()
      tax1ratee.place_forget()
      tax1ratee.place_forget()
      ptax1.place_forget()
  
      tax2namel.place_forget()
      tax2namee.place_forget()
      tax2ratel.place_forget()
      tax2ratee.place_forget()
      ptax2.place_forget()
    elif ch == 2:
      tax1namel.place(x=800, y=40)
      tax1namee.place(x=880,y=40)
      tax1ratel.place(x=800, y=70)
      tax1ratee.place(x=880,y=70)
      ptax1.place(x=580,y=160)
      tax2namel.place_forget()
      tax2namee.place_forget()
      tax2ratel.place_forget()
      tax2ratee.place_forget()
      ptax2.place_forget()
    elif ch == 3:
      tax1namel.place(x=800, y=40)
      tax1namee.place(x=880,y=40)
      tax1ratel.place(x=800, y=70)
      tax1ratee.place(x=880,y=70)
      ptax1.place(x=580,y=160)
      tax2namel.place(x=800, y=110)
      tax2namee.place(x=880,y=110)
      tax2ratel.place(x=800, y=140)
      tax2ratee.place(x=880,y=140)
      ptax2.place(x=580,y=185)
    
  radtax = IntVar()
  rdnotax = Radiobutton(secondtab,text="Do not use TAX",value="1",variable=radtax,command=rtax1)
  rdnotax.place(x=590,y=50)
  
  
  rdtax1 = Radiobutton(secondtab,text="1 level of Tax",value="2",variable=radtax,command=rtax1)
  rdtax1.place(x=590,y=80)
  ptax01 = IntVar()
  tax1namel = Label(secondtab,text="Tax1 name")
  
  
  tax1namee = Entry(secondtab)
  if  not sectab:
    pass
  elif sectab[15]:
    tax1namee.insert(0, sectab[15])
  tax1namee.place(x=60,y=380)
  
  
  tax1ratel = Label(secondtab,text="Tax1 rate")
  
  
  tax1ratee = Entry(secondtab)
  if  not sectab:
    pass
  elif sectab[16]:
    tax1ratee.insert(0, sectab[16])
  
  comptax1 = BooleanVar()
  ptax1 = Checkbutton(secondtab,text="Print TAX1" ,onvalue =1 ,offvalue = 0,variable=comptax1)
  if  not sectab:
    pass
  elif sectab[17] == 1:
    ptax1.select()
  else:
    ptax1.deselect()
  
  rdtax2 = Radiobutton(secondtab,text="2 level of Tax",value="3",variable=radtax,command=rtax1)
  rdtax2.place(x=590,y=110)
  
  
  tax2namel = Label(secondtab,text="Tax2 name")
  
  
  tax2namee = Entry(secondtab)
  if  not sectab:
    pass
  elif sectab[18]:
    tax2namee.insert(0, sectab[18])
  
  tax2ratel = Label(secondtab,text="Tax2 rate")
  
  tax2ratee = Entry(secondtab)
  if  not sectab:
    pass
  elif sectab[19]:
    tax2ratee.insert(0, sectab[19])
  
  comptax2 = BooleanVar()
  ptax2 = Checkbutton(secondtab,text="Print TAX2" ,onvalue =1 ,offvalue = 0,variable=comptax2)
  if  not sectab:
    pass
  else:
    if sectab[20] == 1:
      ptax2.select()
    else:
      ptax2.deselect()
  
  if  not sectab:
    pass
  else:
    if sectab[12] == "1":
      rdnotax.select()
      tax1namel.place_forget()
      tax1namee.place_forget()
      tax1ratel.place_forget()
      tax1ratee.place_forget()
      tax1ratee.place_forget()
      ptax1.place_forget()
  
      tax2namel.place_forget()
      tax2namee.place_forget()
      tax2ratel.place_forget()
      tax2ratee.place_forget()
      ptax2.place_forget()
    elif sectab[12] == "2":
      tax1namel.place(x=800, y=40)
      tax1namee.place(x=880,y=40)
      tax1ratel.place(x=800, y=70)
      tax1ratee.place(x=880,y=70)
      ptax1.place(x=580,y=160)
      tax2namel.place_forget()
      tax2namee.place_forget()
      tax2ratel.place_forget()
      tax2ratee.place_forget()
      ptax2.place_forget()
      rdtax1.select()
    elif sectab[12] == "3":
      rdtax2.select()
      tax1namel.place(x=800, y=40)
      tax1namee.place(x=880,y=40)
      tax1ratel.place(x=800, y=70)
      tax1ratee.place(x=880,y=70)
      ptax1.place(x=580,y=160)
      tax2namel.place(x=800, y=110)
      tax2namee.place(x=880,y=110)
      tax2ratel.place(x=800, y=140)
      tax2ratee.place(x=880,y=140)
      ptax2.place(x=580,y=185)
    else:
      pass
  
  
  comlo=LabelFrame(secondtab,text="Comapny Logo", height=260, width=320)
  comlo.place(x=560, y=240)
  
  def upload_filelogo():
    global imglogo,filename
    f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
    image = Image.open(filename)
    resize_image = image.resize((280, 160))
    imglogo = ImageTk.PhotoImage(resize_image)
    # b2 = Button(secondtab,image=img)
    # b2.place(x=130, y=80)
  
    btlogo = Button(secondtab,width=280,height=160,image=imglogo)
    btlogo.place(x=580,y=280)
  
  try:
    image = Image.open("images/"+sectab[13])
    resize_image = image.resize((280, 160))
    image = ImageTk.PhotoImage(resize_image)
    btlogo = Button(secondtab,width=280,height=160,image=image)
    btlogo.place(x=580,y=280)
    btlogo.photo = image
  except:
    pass
  
    
  btloadim = Button(secondtab,text="Load logo image",command=upload_filelogo)
  btloadim.place(x=580,y=460)
  
  compimg = BooleanVar()
  primage = Checkbutton(secondtab,text="Print logo image",variable = compimg,onvalue =1 ,offvalue = 0)
  primage.place(x=740,y=460)
  
  ################### tab06 ###################################
  
  def user():
    display = displaystart.get()
    user_name = usernae.get()
    password = userpase.get()
    conformpassword = usercpase.get()
   
    create_inv = creinvbol.get()
    delete_inv = delinvbol.get()
    void_inv = voinvbol.get()
    mark_inv_as_paid = markinvbol.get()
    
    create_ord = creordbol.get()
    delete_ord = delordbol.get()
    turn_inv_ord = turninvbol.get()
    smsnofi = smsinvbol.get()
    
    create_est = creestimatebol.get()
    delete_est = delestimatebol.get()
    turn_est = turnestiinvbol.get()
  
    create_exp = creexpensebol.get()
    delete_exp = delexpensebol.get()
    rebill_exp = rebillexpebol.get()
    
    create_cus = crecusbol.get()
    delete_cus = delcusbol.get()
    imp_cus = impcusbol.get()
  
    create_pros = creprosbol.get()
    delete_pros = delprosbol.get()
    import_pros = impprosbol.get()
  
    runrep = runrepbol.get()
    gen_rec = genrecinvbol.get()
  
    create_pur = crepurbol.get()
    delete_pur = delpurbol.get()
  
    modify_inv = modifyinvbol.get()
    modify_ord = modifyordbol.get()
    modify_est = modifyestibol.get()
  
    if user_name=="" or password=="":
      messagebox.showerror('',"Please complete the form")
    else:
      sql='SELECT * FROM users WHERE username=%s'# selecting entire table from db,taking username , nd check   the existance
      val=(user_name,)
      fbcursor.execute(sql,val)
      if fbcursor.fetchone()is not None:
        sql='SELECT * FROM users WHERE username=%s'
        val=(user_name,)
        fbcursor.execute(sql,val)
        whuser = fbcursor.fetchone()
        print(whuser[0])
        if password == conformpassword:
        # messagebox.showerror('Warming','User name already exist!!')
          sqll= 'UPDATE users SET displayloginscreen=%s,username=%s,password=%s,confirm_password=%s,create_invoice=%s,delete_invoice=%s,void_invoice=%s,mark_invoice_as_paid=%s,create_order=%s,delete_order=%s,turn_order_into_invoice=%s,send_sms_nofitication=%s,create_estimate=%s,delete_estimate=%s,turn_oestimate_into_invoice=%s,create_expense=%s,delete_expense=%s,rebill_exprense=%s,create_customer=%s,delete_customer=%s,import_customer=%s,	create_product_service=%s,delete_product_service=%s,import_product_service=%s,run_reports=%s,generate_recurring_invoice=%s,create_purchase_order=%s,delete_purchase_order=%s,modify_invoice_settings=%s,modify_order_settings=%s,modify_estimate_settings=%s WHERE userID=%s'
          vall=(display,user_name,password,conformpassword,create_inv,delete_inv,void_inv,mark_inv_as_paid,  create_ord,delete_ord,turn_inv_ord,smsnofi,create_est,delete_est,turn_est,create_exp,delete_exp,  rebill_exp,create_cus,delete_cus,imp_cus,create_pros,delete_pros,import_pros,runrep,gen_rec,create_pur,  delete_pur,modify_inv,modify_ord,modify_est,whuser[0])
          fbcursor.execute(sqll,vall)
          fbilldb.commit()
        else:
          messagebox.showerror('Warming','Password not match!!')
      else:
        if password == conformpassword:
          sql="INSERT INTO users(displayloginscreen,username,password,confirm_password,create_invoice,  delete_invoice,void_invoice,mark_invoice_as_paid,create_order,delete_order,turn_order_into_invoice,  send_sms_nofitication,create_estimate,delete_estimate,turn_oestimate_into_invoice,	create_expense,	  delete_expense,rebill_exprense,create_customer,delete_customer,import_customer,	create_product_service,  delete_product_service,	import_product_service,run_reports,generate_recurring_invoice,  create_purchase_order,delete_purchase_order,modify_invoice_settings,modify_order_settings,  modify_estimate_settings) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,  %s,%s,%s,%s,%s,%s,%s,%s)" #adding values into db
          val=(display,user_name,password,conformpassword,create_inv,delete_inv,void_inv,mark_inv_as_paid,  create_ord,delete_ord,turn_inv_ord,smsnofi,create_est,delete_est,turn_est,create_exp,delete_exp,  rebill_exp,create_cus,delete_cus,imp_cus,create_pros,delete_pros,import_pros,runrep,gen_rec,create_pur,  delete_pur,modify_inv,modify_ord,modify_est)
          fbcursor.execute(sql,val)
          fbilldb.commit()
          for record in uactree.get_children():
            uactree.delete(record)
          sql = "select * from users"
          fbcursor.execute(sql)
          sixuactree = fbcursor.fetchall()
          coutset = 0
          for i in sixuactree:
           uactree.insert(parent='', index='end', iid=coutset, text='hello', values=(i[3]))
           coutset += 1
        else:
          messagebox.showerror('Warming','Password not match!!')
        

   
    
  
  
  
  
    
  
    
  sixtab1=Frame(tab06, relief=GROOVE, bg="#f8f8f2")
  sixtab1.pack(side="top", fill=BOTH)
  
  sixtab=Frame(sixtab1, bg="#f5f3f2", height=700)
  sixtab.pack(side="top", fill=BOTH)
  
  displaystart = BooleanVar()
  displaylocsc = Checkbutton(sixtab,text="Display Login screen startup",onvalue =1 ,offvalue = 0,  variable=displaystart)
  displaylocsc.place(x=20,y=30)
  
  userac=LabelFrame(sixtab,text="User Acounts", height=400, width=260)
  userac.place(x=20, y=55)
  
  
  selper = Label(sixtab,text="Select username to modify permissions")
  selper.place(x=30,y=75)
  
  def focususer(event):
    itemid = uactree.item(uactree.focus())["values"][0]
    sql = "select * from users where username = %s"
    val = (itemid,)
    fbcursor.execute(sql,val)
    sixtabdataback = fbcursor.fetchone()
    print(sixtabdataback)
    usernae.delete(0,END)
    usernae.insert(0,itemid)
    if itemid == "adminstator":
        usernae.delete(0,END)
        usernae.insert(0,itemid)
        usernae["state"] = DISABLED
        creinv["state"] = DISABLED
        delinv["state"] = DISABLED
        voinv["state"] = DISABLED
        markinv["state"] = DISABLED
        creord["state"] = DISABLED
        delord["state"] = DISABLED
        turninv["state"] = DISABLED
        smsinv["state"] = DISABLED
        creestimate["state"] = DISABLED
        delestimate["state"] = DISABLED
        turnestiinv["state"] = DISABLED
        creexpense["state"] = DISABLED
        delexpense["state"] = DISABLED
        rebillexpe["state"] = DISABLED
        crecus["state"] = DISABLED
        delcus["state"] = DISABLED
        impcus["state"] = DISABLED
        crepros["state"] = DISABLED
        delpros["state"] = DISABLED
        imppros["state"] = DISABLED
        runrep["state"] = DISABLED
        genrecinv["state"] = DISABLED
        crepur["state"] = DISABLED
        delpur["state"] = DISABLED
        modifyinv["state"] = DISABLED
        modifyord["state"] = DISABLED
        modifyesti["state"] = DISABLED
    else:
        userpase.delete(0, END)
        usercpase.delete(0, END)
        usernae.delete(0,END)
        usernae.insert(0,itemid)
        usernae["state"] = NORMAL
        creinv["state"] = NORMAL
        delinv["state"] = NORMAL
        voinv["state"] = NORMAL
        markinv["state"] = NORMAL
        creord["state"] = NORMAL
        delord["state"] = NORMAL
        turninv["state"] = NORMAL
        smsinv["state"] = NORMAL
        creestimate["state"] = NORMAL
        delestimate["state"] = NORMAL
        turnestiinv["state"] = NORMAL
        creexpense["state"] = NORMAL
        delexpense["state"] = NORMAL
        rebillexpe["state"] = NORMAL
        crecus["state"] = NORMAL
        delcus["state"] = NORMAL
        impcus["state"] = NORMAL
        crepros["state"] = NORMAL
        delpros["state"] = NORMAL
        imppros["state"] = NORMAL
        runrep["state"] = NORMAL
        genrecinv["state"] = NORMAL
        crepur["state"] = NORMAL
        delpur["state"] = NORMAL
        modifyinv["state"] = NORMAL
        modifyord["state"] = NORMAL
        modifyesti["state"] = NORMAL
    if not sixtabdataback:
      userpase.delete(0, END)
      usercpase.delete(0, END)
      creinv.deselect()
      delinv.deselect()
      voinv.deselect()
      markinv.deselect()
      creord.deselect()
      delord.deselect()
      turninv.deselect()
      smsinv.deselect()
      creestimate.deselect()
      delestimate.deselect()
      turnestiinv.deselect()
      creexpense.deselect()
      delexpense.deselect()
      rebillexpe.deselect()
      crecus.deselect()
      delcus.deselect()
      impcus.deselect()
      crepros.deselect()
      delpros.deselect()
      imppros.deselect()
      runrep.deselect()
      genrecinv.deselect()
      crepur.deselect()
      delpur.deselect()
      modifyinv.deselect()
      modifyord.deselect()
      modifyesti.deselect()
      if itemid == "adminstator":
        usernae.delete(0,END)
        usernae.insert(0,itemid)
        usernae["state"] = DISABLED
        creinv["state"] = DISABLED
        delinv["state"] = DISABLED
        voinv["state"] = DISABLED
        markinv["state"] = DISABLED
        creord["state"] = DISABLED
        delord["state"] = DISABLED
        turninv["state"] = DISABLED
        smsinv["state"] = DISABLED
        creestimate["state"] = DISABLED
        delestimate["state"] = DISABLED
        turnestiinv["state"] = DISABLED
        creexpense["state"] = DISABLED
        delexpense["state"] = DISABLED
        rebillexpe["state"] = DISABLED
        crecus["state"] = DISABLED
        delcus["state"] = DISABLED
        impcus["state"] = DISABLED
        crepros["state"] = DISABLED
        delpros["state"] = DISABLED
        imppros["state"] = DISABLED
        runrep["state"] = DISABLED
        genrecinv["state"] = DISABLED
        crepur["state"] = DISABLED
        delpur["state"] = DISABLED
        modifyinv["state"] = DISABLED
        modifyord["state"] = DISABLED
        modifyesti["state"] = DISABLED
      else:
        userpase.delete(0, END)
        usercpase.delete(0, END)
        usernae.delete(0,END)
        usernae.insert(0,itemid)
        usernae["state"] = NORMAL
        creinv["state"] = NORMAL
        delinv["state"] = NORMAL
        voinv["state"] = NORMAL
        markinv["state"] = NORMAL
        creord["state"] = NORMAL
        delord["state"] = NORMAL
        turninv["state"] = NORMAL
        smsinv["state"] = NORMAL
        creestimate["state"] = NORMAL
        delestimate["state"] = NORMAL
        turnestiinv["state"] = NORMAL
        creexpense["state"] = NORMAL
        delexpense["state"] = NORMAL
        rebillexpe["state"] = NORMAL
        crecus["state"] = NORMAL
        delcus["state"] = NORMAL
        impcus["state"] = NORMAL
        crepros["state"] = NORMAL
        delpros["state"] = NORMAL
        imppros["state"] = NORMAL
        runrep["state"] = NORMAL
        genrecinv["state"] = NORMAL
        crepur["state"] = NORMAL
        delpur["state"] = NORMAL
        modifyinv["state"] = NORMAL
        modifyord["state"] = NORMAL
        modifyesti["state"] = NORMAL
    else:
      userpase.delete(0, END)
      usercpase.delete(0, END)
      userpase.insert(0, sixtabdataback[4])
      usercpase.insert(0, sixtabdataback[5])
      if sixtabdataback[6] == 1:
        creinv.select()
      else:
        creinv.deselect()
      if sixtabdataback[7] == 1:
        delinv.select()
      else:
        delinv.deselect()
      if sixtabdataback[8] == 1:
        voinv.select()
      else:
        voinv.deselect()
      if sixtabdataback[9] == 1:
        markinv.select()
      else:
        markinv.deselect()
      if sixtabdataback[10] == 1:
        creord.select()
      else:
        creord.deselect()
      if sixtabdataback[11] == 1:
        delord.select()
      else:
        delord.deselect()
      if sixtabdataback[12] == 1:
        turninv.select()
      else:
        turninv.deselect()
      if sixtabdataback[13] == 1:
        smsinv.select()
      else:
        smsinv.deselect()
      if sixtabdataback[14] == 1:
        creestimate.select()
      else:
        creestimate.deselect()
      if sixtabdataback[15] == 1:
        delestimate.select()
      else:
        delestimate.deselect()
      if sixtabdataback[16] == 1:
        turnestiinv.select()
      else:
        turnestiinv.deselect()
      if sixtabdataback[17] == 1:
        creexpense.select()
      else:
        creexpense.deselect()
      if sixtabdataback[18] == 1:
        delexpense.select()
      else:
        delexpense.deselect()
      if sixtabdataback[19] == 1:
        rebillexpe.select()
      else:
        rebillexpe.deselect()
      if sixtabdataback[20] == 1:
        crecus.select()
      else:
        crecus.deselect()
      if sixtabdataback[21] == 1:
        delcus.select()
      else:
        delcus.deselect()
      if sixtabdataback[22] == 1:
        impcus.select()
      else:
        impcus.deselect()
      if sixtabdataback[23] == 1:
        crepros.select()
      else:
        crepros.deselect()
      if sixtabdataback[24] == 1:
        delpros.select()
      else:
        delpros.deselect()
      if sixtabdataback[25] == 1:
        imppros.select()
      else:
        imppros.deselect()
      if sixtabdataback[26] == 1:
        runrep.select()
      else:
        runrep.deselect()
      if sixtabdataback[27] == 1:
        genrecinv.select()
      else:
        genrecinv.deselect()
      if sixtabdataback[28] == 1:
        crepur.select()
      else:
        crepur.deselect()
      if sixtabdataback[29] == 1:
        delpur.select()
      else:
        delpur.deselect()
      if sixtabdataback[30] == 1:
        modifyinv.select()
      else:
        modifyinv.deselect()
      if sixtabdataback[31] == 1:
        modifyord.select()
      else:
        modifyord.deselect()
      if sixtabdataback[32] == 1:
        modifyesti.select()
      else:
        modifyesti.deselect()
         
  
  scrollbarx = Scrollbar(sixtab, orient=HORIZONTAL)
  scrollbary = Scrollbar(sixtab, orient=VERTICAL)
  uactree = ttk.Treeview(sixtab, columns=("1"),height=400,selectmode="extended", yscrollcommand=scrollbary.  set, xscrollcommand=scrollbarx.set)
  scrollbary.config(command=uactree.yview)
  scrollbary.place(x=245,y=100,height=300)
  uactree.heading('1', text="Username",)
  uactree.column('#0', stretch=NO, minwidth=0, width=0)
  uactree.column('1', stretch=NO, minwidth=0, width=218)
  uactree.place(x=30,y=100,height=300,width=220)
  uactree.bind('<Double-Button-1>' , focususer)
  sql = "select * from users"
  fbcursor.execute(sql)
  sixuactree = fbcursor.fetchall()
  coutset = 0
  if not sixuactree:
    uactree.insert('', index='end', text='hello', values=("adminstator"))
  else:
    for i in sixuactree:
      uactree.insert(parent='', index='end', iid=coutset, text='hello', values=(i[3]))
      coutset += 1
  
  def adduser():
    uactree.insert('', index='end', text='hello', values=("Rename User"))
  
  btadd = Button(sixtab,text="Add new User",command=adduser)
  btadd.place(x=30,y=415)
  
  def users():
    itemid = uactree.item(uactree.focus())["values"][0]
    if itemid == "adminstator":
      messagebox.showerror('F-Billing Revolution', 'Cannot delete adminstator user.')
    else:
      delusermess = messagebox.askyesno("Delete user", "Are you sure to delete this user?")
      if delusermess == True:
        sql = "delete from users where username = %s"
        val = (itemid, )
        fbcursor.execute(sql, val)
        fbilldb.commit()
        for record in uactree.get_children():
          uactree.delete(record)
        sql = "select * from users"
        fbcursor.execute(sql)
        sixuactree = fbcursor.fetchall()
        coutset = 0
        for i in sixuactree:
          uactree.insert(parent='', index='end', iid=coutset, text='hello', values=(i[3]))
          coutset += 1
      else:
        pass
        
  
  btdus = Button(sixtab,text="Delete User",command=users)
  btdus.place(x=180,y=415)
  
  userpro=LabelFrame(sixtab,text="User Profile", height=400, width=750)
  userpro.place(x=300, y=55)
  
  
  userna = Label(sixtab,text="Username")
  userna.place(x=340,y=90)
  usernae = Entry(sixtab,)
  usernae.place(x=460,y=90)
  
  userpas = Label(sixtab,text="Password")
  userpas.place(x=340,y=120)
  userpase = Entry(sixtab,)
  userpase.place(x=460,y=120)
  
  usercpas = Label(sixtab,text="Confirm Password")
  usercpas.place(x=340,y=150)
  usercpase = Entry(sixtab,)
  usercpase.place(x=460,y=150)
  
  saveuserprofile = Button(sixtab,text="save user profile",command=user)
  saveuserprofile.place(x=650,y=120)
  
  creinvbol = BooleanVar()
  creinv = Checkbutton(sixtab,text="Create invoice",onvalue= 1 ,offvalue= 0,variable=creinvbol)
  creinv.place(x=340,y=200)
  delinvbol = BooleanVar()
  delinv = Checkbutton(sixtab,text="Delete invoice",onvalue= 1 ,offvalue= 0,variable=delinvbol)
  delinv.place(x=340,y=225)
  voinvbol = BooleanVar()
  voinv = Checkbutton(sixtab,text="Void invoice",onvalue= 1 ,offvalue= 0,variable=voinvbol)
  voinv.place(x=340,y=250)
  markinvbol = BooleanVar()
  markinv = Checkbutton(sixtab,text="Mark invoice as Paid",onvalue= 1 ,offvalue= 0,variable=markinvbol)
  markinv.place(x=340,y=275)
  
  creordbol = BooleanVar()
  creord = Checkbutton(sixtab,text="Create Order",onvalue= 1 ,offvalue= 0,variable=creordbol)
  creord.place(x=500,y=200)
  delordbol = BooleanVar()
  delord = Checkbutton(sixtab,text="Delete Order",onvalue= 1 ,offvalue= 0,variable=delordbol)
  delord.place(x=500,y=225)
  turninvbol = BooleanVar()
  turninv = Checkbutton(sixtab,text="Turn order into invoice",onvalue= 1 ,offvalue= 0,variable=turninvbol)
  turninv.place(x=500,y=250)
  smsinvbol = BooleanVar()
  smsinv = Checkbutton(sixtab,text="Send sms nofitication",onvalue= 1 ,offvalue= 0,variable=smsinvbol)
  smsinv.place(x=500,y=275)
  
  creestimatebol = BooleanVar()
  creestimate = Checkbutton(sixtab,text="Create estimate",onvalue= 1 ,offvalue= 0,variable=creestimatebol)
  creestimate.place(x=680,y=200)
  delestimatebol = BooleanVar()
  delestimate = Checkbutton(sixtab,text="Delete estimate",onvalue= 1 ,offvalue= 0,variable=delestimatebol)
  delestimate.place(x=680,y=225)
  turnestiinvbol = BooleanVar()
  turnestiinv = Checkbutton(sixtab,text="Turn estimates into invoice",onvalue= 1 ,offvalue= 0,  variable=turnestiinvbol)
  turnestiinv.place(x=680,y=250)
  
  creexpensebol = BooleanVar()
  creexpense = Checkbutton(sixtab,text="Create expenses",onvalue= 1 ,offvalue= 0,variable=creexpensebol)
  creexpense.place(x=880,y=200)
  delexpensebol = BooleanVar()
  delexpense = Checkbutton(sixtab,text="Delete expenses",onvalue= 1 ,offvalue= 0,variable=delexpensebol)
  delexpense.place(x=880,y=225)
  rebillexpebol = BooleanVar()
  rebillexpe = Checkbutton(sixtab,text="Rebill expenses",onvalue= 1 ,offvalue= 0,variable=rebillexpebol)
  rebillexpe.place(x=880,y=250)
  
  crecusbol = BooleanVar()
  crecus = Checkbutton(sixtab,text="Create customer",onvalue= 1 ,offvalue= 0,variable=crecusbol)
  crecus.place(x=340,y=320)
  delcusbol = BooleanVar()
  delcus = Checkbutton(sixtab,text="Delete customer",onvalue= 1 ,offvalue= 0,variable=delcusbol)
  delcus.place(x=340,y=340)
  impcusbol = BooleanVar()
  impcus = Checkbutton(sixtab,text="Import customer",onvalue= 1 ,offvalue= 0,variable=impcusbol)
  impcus.place(x=340,y=360)
  
  creprosbol = BooleanVar()
  crepros = Checkbutton(sixtab,text="Create product\services",onvalue= 1 ,offvalue= 0,variable=creprosbol)
  crepros.place(x=500,y=320)
  delprosbol = BooleanVar()
  delpros = Checkbutton(sixtab,text="Delete product\services",onvalue= 1 ,offvalue= 0,variable=delprosbol)
  delpros.place(x=500,y=340)
  impprosbol = BooleanVar()
  imppros = Checkbutton(sixtab,text="Import product\services",onvalue= 1 ,offvalue= 0,variable=impprosbol)
  imppros.place(x=500,y=360)
  
  runrepbol = BooleanVar()
  runrep = Checkbutton(sixtab,text="Run reports",onvalue= 1 ,offvalue= 0,variable=runrepbol)
  runrep.place(x=680,y=320)
  genrecinvbol = BooleanVar()
  genrecinv = Checkbutton(sixtab,text="Generate recurring invoices",onvalue= 1 ,offvalue= 0,  variable=genrecinvbol)
  genrecinv.place(x=680,y=340)
  
  crepurbol = BooleanVar()
  crepur = Checkbutton(sixtab,text="Create Purchase order",onvalue =1 ,offvalue = 0,variable=crepurbol)
  crepur.place(x=880,y=320)
  delpurbol = BooleanVar()
  delpur = Checkbutton(sixtab,text="Delete Purchase order",onvalue =1 ,offvalue = 0,variable=delpurbol)
  delpur.place(x=880,y=340)
  
  undersetlab = Label(sixtab,text="Under Settings menu tab")
  undersetlab.place(x=340,y=400)
  
  modifyinvbol = BooleanVar()
  modifyinv = Checkbutton(sixtab,text="Modify invoice settings",onvalue =1 ,offvalue = 0,variable=modifyinvbol)
  modifyinv.place(x=340,y=425)
  
  modifyordbol = BooleanVar()
  modifyord = Checkbutton(sixtab,text="Modify order settings",onvalue =1 ,offvalue = 0,variable=modifyordbol)
  modifyord.place(x=500,y=425)
  
  modifyestibol = BooleanVar()
  modifyesti = Checkbutton(sixtab,text="Modify estimate settings",onvalue =1 ,offvalue = 0,  variable=modifyestibol)
  modifyesti.place(x=680,y=425)

################### tab05 ###################################
  fifthtab1=Frame(tab05, relief=GROOVE, bg="#f8f8f2")
  fifthtab1.pack(side="top", fill=BOTH)

  fifthtab=Frame(fifthtab1, bg="#f5f3f2", height=700)
  fifthtab.pack(side="top", fill=BOTH)

  sql = "select * from company"
  fbcursor.execute(sql)
  estdata = fbcursor.fetchone()
  print(estdata)



  ver = Label(fifthtab,text="Estimate# prefix")
  ver.place(x=5,y=40)

  est_str = StringVar() 
  est_entry = Entry(fifthtab, textvariable=est_str)
  est_entry.place(x=100,y=40)
  if not estdata:
    est_str.set('EST')
  else:
    est_entry.insert(0, estdata[29])

  ver = Label(fifthtab,text="Starting estimate number")
  ver.place(x=25,y=80)

  def callback(input):
      
    if input.isdigit():
        print(input)
        return True
                          
    elif input is "":
        print(input)
        return True
  
    else:
        print(input)
        return False

  spin1 = Spinbox(fifthtab,from_=0,to=1000000,width=15)
  reg = fifthtab.register(callback)
  
  spin1.config(validate ="key", 
         validatecommand =(reg, '%S'))
  if not estdata:
    pass
  else:
    spin1.delete(0, END)
    spin1.insert(0,estdata[38])
  spin1.place(x=50,y=100)

  ver = Label(fifthtab,text="Header box background color")
  ver.place(x=5,y=140)

  win_menu1 = StringVar()
  winstyle1 = ttk.Combobox(fifthtab,textvariable=win_menu1)
  #est_win1 = win_menu1.get()
  winstyle1['values'] = ('Default','Black','Maroon','Green','Olive','Navy','Purple','Teal','Gray','Silver','Red','Lime','Yellow','Blue','Fuchsia','Aqua','White','ScrollBar','Background','ActiveCaption','InactiveCaption','Menu','Window','WindowFrame','MenuText','WindowText','CaptionText','ActiveBorder','InactiveBorder','AppWorkSpace','Highlight','HighlightText','BtnFace','InactiveCaptionText','BtnHighlight','3DDkShadow','3DLight','InfoText','InfoBk','Custom')
  if not estdata:
    winstyle1.current(0)
  else:
    winstyle1.insert(0, estdata[30])
  winstyle1.place(x=6 ,y=160)
  #winstyle1.current(0)

  ver = Label(fifthtab,text="Customize Estimate text labels")
  ver.place(x=5,y=190)
  
  est_str1 = StringVar() 
  est_lbx1 = Entry(fifthtab, width=30,textvariable=est_str1)
  # est_str1.set('Estimate')
  if not estdata:
    est_str1.set('Estimate')
  else:
    est_lbx1.insert(0, estdata[31])
  est_lbx1.place(x=5,y=220)
  
  est_str2 = StringVar() 
  est_lbx2 = Entry(fifthtab, width=30,textvariable=est_str2)
  if not estdata:
    est_str2.set('Estimate#')
  else:
    est_lbx2.insert(0,estdata[33])
  est_lbx2.place(x=5,y=240)
  
  
  est_str3 = StringVar() 
  est_lbx3 = Entry(fifthtab,width=30,textvariable=est_str3)
  if not estdata:
    est_str3.set('Estimate date')
  else:
    est_lbx3.insert(0, estdata[34])
  est_lbx3.place(x=5,y=260) 

  est_str4 = StringVar() 
  est_lbx4 = Entry(fifthtab,width=30,textvariable=est_str4)
  if not estdata:
    est_str4.set('Due date')
  else:
    est_lbx4.insert(0, estdata[35])
  est_lbx4.place(x=5,y=280)

  est_str5 = StringVar() 
  est_lbx5 = Entry(fifthtab,width=30,textvariable=est_str5)
  if not estdata:
    est_str5.set('Estimate to')
  else:
    est_lbx5.insert(0, estdata[36])
  est_lbx5.place(x=5,y=300)

  est_str6 = StringVar() 
  est_lbx6 = Entry(fifthtab, width=30,textvariable=est_str6)
  if not estdata:
    est_str6.set('Estimate total')
  else:
    est_lbx6.insert(0, estdata[37])
  est_lbx6.place(x=5,y=320)


  ver = Label(fifthtab,text="Default Estimate template(example,click on preview for mouse scrolling)")
  ver.place(x=248,y=55 )

  ver = Label(fifthtab,text="Default Estimate template")
  ver.place(x=619,y=40)



  messagelbframe=LabelFrame(fifthtab,text="Predefined terms and conditions text for estimates", height=70, width=980)
  messagelbframe.place(x=248, y=396)

  
  # est_str7 = StringVar() 
  # entry1=Entry(fifthtab, width=155,textvariable=est_str7)
  # if not estdata:
  #   pass
  # else:
  #   entry1.insert(0, estdata[39])
  # entry1.place(x=260, y=415, height=36)
  
  est_str7 = scrolledtext.ScrolledText(fifthtab)
  if  not estdata:
    pass
  else:
    est_str7.insert('1.0', estdata[39])
  est_str7.place(x=260,y=415,height=38,width=950)


  def restore_defaulttt1():
        est_lbx1.delete(0, 'end')
        est_lbx1.insert(0, 'Estimate')
        est_lbx2.delete(0, 'end')
        est_lbx2.insert(0,'Estimate#')
        est_lbx3.delete(0, 'end')
        est_lbx3.insert(0, 'Estimate date')
        est_lbx4.delete(0, 'end')
        est_lbx4.insert(0, 'Due date')
        est_lbx5.delete(0, 'end')
        est_lbx5.insert(0, 'Estimate to')
        est_lbx6.delete(0, 'end')
        est_lbx6.insert(0, 'Estimate total')

  bttermadd_01 = Button(fifthtab,text="Restore defaults", command=restore_defaulttt1)
  bttermadd_01.place(x=32,y=430)


#------------Professional 1 (logo on left side)-------------
  def maindropmenu(event):
      menuvar=win_menu2.get()
      print(menuvar,"hello")
      sql = "select * from company"
      fbcursor.execute(sql)
      estdata1 = fbcursor.fetchone()

      if menuvar == 'Professional 1 (logo on left side)':
        frame = Frame(fifthtab, width=953, height=300)
        frame.pack(expand=True, fill=BOTH)
        frame.place(x=247,y=90)
        canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
              
        vertibar=Scrollbar(frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=canvas.yview)
          
        canvas.config(width=953,height=300)
        canvas.config(yscrollcommand=vertibar.set)
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(100, 8, 850, 687 , outline='yellow',fill='white')
        canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        try:
          est_image = Image.open("images/"+estdata1[13])
          est_resize_image = est_image.resize((200,100))
          est_image = ImageTk.PhotoImage(est_resize_image)

          est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
          window_image = canvas.create_window(175, 45, anchor="nw", window=est_btlogo)
          est_btlogo.photo = est_image
        except:
          pass  
        canvas.create_text(202, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(215, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(200, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(191, 220, text="Terms", fill="black", font=('Helvetica 11'))
        canvas.create_text(205, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
        canvas.create_text(350, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(350, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(350, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(340, 220, text="NET 15", fill="black", font=('Helvetica 11'))
          
        canvas.create_text(720, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
        # canvas.create_text(700, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'), width=125)
        T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
        T_address.tag_configure('tag_name',justify='right')
        T_address.insert('1.0', estdata1[2])
        T_address.tag_add('tag_name','1.0', 'end')
        T_address_window = canvas.create_window(520, 80, anchor="nw", window=T_address)
        canvas.create_text(695, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
        canvas.create_text(700, 205, text=" "+est_str1.get(), fill="black", font=('Helvetica 14 bold'))
        canvas.create_text(706, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
          
        canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
        canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
      
        s = ttk.Style()
        s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

        tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_1.Treeview')

        tree.column("# 1", anchor=E, stretch=NO, width=100)
        tree.heading("# 1", text="ID/SKU")
        tree.column("# 2", anchor=E, stretch=NO, width=350)
        tree.heading("# 2", text="Product/Service - Description")
        tree.column("# 3", anchor=E, stretch=NO, width=80)
        tree.heading("# 3", text="Quantity")
        tree.column("# 4", anchor=E, stretch=NO, width=90)
        tree.heading("# 4", text="Unit Price")
        tree.column("# 5", anchor=E, stretch=NO, width=80)
        tree.heading("# 5", text="Price")
          
        window = canvas.create_window(120, 340, anchor="nw", window=tree)

        canvas.create_line(120, 390, 820, 390 )
        canvas.create_line(120, 340, 120, 365 )
        canvas.create_line(120, 365, 120, 390 )
        canvas.create_line(820, 340, 820, 540 )
        canvas.create_line(740, 340, 740, 540 )
        canvas.create_line(570, 340, 570, 540 )
        canvas.create_line(570, 415, 820, 415 )
        canvas.create_line(570, 440, 820, 440 )
        canvas.create_line(570, 465, 820, 465 )
        canvas.create_line(570, 490, 820, 490 )
        canvas.create_line(570, 515, 820, 515 )
        canvas.create_line(650, 340, 650, 390 )
        canvas.create_line(220, 340, 220, 390 )
        canvas.create_line(570, 540, 820, 540 )

        canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
        canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
    
        if comcursignpla.get() == "before amount":
          canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        elif comcursignpla.get() == "after amount":
          canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(704, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))

        else:
          pass
        # canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        
        if comcursignpla.get() == "before amount":
          canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
        else:
          pass

        # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))
        
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

        canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
          
        canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        canvas.create_line(150, 608, 795, 608)
        # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10')) 
        T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
        T.insert(END, estdata1[39])
        T_window = canvas.create_window(155, 612, anchor="nw", window=T)

        canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
          

#----------------Professional 2 (logo on right side)------------------
      elif menuvar == 'Professional 2 (logo on right side)':
        frame = Frame(fifthtab, width=953, height=300)
        frame.pack(expand=True, fill=BOTH)
        frame.place(x=247,y=90)
      
        canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
          
        vertibar=Scrollbar(frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=canvas.yview)
        canvas.config(width=953,height=300)
          
        canvas.config(yscrollcommand=vertibar.set)
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
        canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        try:
          est_image = Image.open("images/"+estdata1[13])
          est_resize_image = est_image.resize((200,100))
          est_image = ImageTk.PhotoImage(est_resize_image)

          est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
          window_image = canvas.create_window(500, 45, anchor="nw", window=est_btlogo)
          est_btlogo.photo = est_image
        except:
          pass  
        canvas.create_text(250, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
        # canvas.create_text(215, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
        T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
        T_address.tag_configure('tag_name',justify='right')
        T_address.insert('1.0', estdata1[2])
        T_address.tag_add('tag_name','1.0', 'end')
        T_address_window = canvas.create_window(100, 80, anchor="nw", window=T_address)
        #T_address_window = canvas.create_window(175, 80, anchor="nw", window=T_address)

        canvas.create_text(215, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
        canvas.create_text(225, 205, text=""+est_str1.get(), fill="black", font=('Helvetica 14 bold'))
        canvas.create_text(232, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
          
        canvas.create_text(502, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(515, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(500, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(491, 220, text="Terms", fill="black", font=('Helvetica 11'))
        canvas.create_text(505, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
        canvas.create_text(690, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(690, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(690, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(680, 220, text="NET 15", fill="black", font=('Helvetica 11'))      
          
        canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
        canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

        s = ttk.Style()
        s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

        tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_1.Treeview')
          
        tree.column("# 1", anchor=E, stretch=NO, width=100)
        tree.heading("# 1", text="ID/SKU")
        tree.column("# 2", anchor=E, stretch=NO, width=350)
        tree.heading("# 2", text="Product/Service - Description")
        tree.column("# 3", anchor=E, stretch=NO, width=80)
        tree.heading("# 3", text="Quantity")
        tree.column("# 4", anchor=E, stretch=NO, width=90)
        tree.heading("# 4", text="Unit Price")
        tree.column("# 5", anchor=E, stretch=NO, width=80)
        tree.heading("# 5", text="Price")
          
        window = canvas.create_window(120, 340, anchor="nw", window=tree)

        canvas.create_line(120, 390, 820, 390 )
        canvas.create_line(120, 340, 120, 365 )
        canvas.create_line(120, 365, 120, 390 )
        canvas.create_line(820, 340, 820, 540 )
        canvas.create_line(740, 340, 740, 540 )
        canvas.create_line(570, 340, 570, 540 )
        canvas.create_line(570, 415, 820, 415 )
        canvas.create_line(570, 440, 820, 440 )
        canvas.create_line(570, 465, 820, 465 )
        canvas.create_line(570, 490, 820, 490 )
        canvas.create_line(570, 515, 820, 515 )
        canvas.create_line(650, 340, 650, 390 )
        canvas.create_line(220, 340, 220, 390 )
        canvas.create_line(570, 540, 820, 540 )

        canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
        canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(704, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
        else:
          pass

        # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))
        
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

        canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

        canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        canvas.create_line(150, 608, 795, 608)
        # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
        T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
        T.insert(END, estdata1[39])
        T_window = canvas.create_window(155, 612, anchor="nw", window=T)
        canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
#----------------Simplified 1 (logo on left side)------------------ 
      elif menuvar == 'Simplified 1 (logo on left side)':
        print('hello')
        frame = Frame(fifthtab, width=953, height=300)
        frame.pack(expand=True, fill=BOTH)
        frame.place(x=247,y=90)
        canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))

        vertibar=Scrollbar(frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=canvas.yview)
        canvas.config(width=953,height=300)

        canvas.config(yscrollcommand=vertibar.set)
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
        canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        try:
          est_image = Image.open("images/"+estdata1[13])
          est_resize_image = est_image.resize((200,100))
          est_image = ImageTk.PhotoImage(est_resize_image)

          est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
          window_image = canvas.create_window(175, 45, anchor="nw", window=est_btlogo)
          est_btlogo.photo = est_image
        except:
          pass  
        canvas.create_text(202, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(215, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(200, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(191, 220, text="Terms", fill="black", font=('Helvetica 11'))
        canvas.create_text(205, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
        canvas.create_text(350, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(350, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(350, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(340, 220, text="NET 15", fill="black", font=('Helvetica 11'))      

        canvas.create_text(720, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
        #canvas.create_text(710, 200, text=caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
        T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
        T_address.tag_configure('tag_name',justify='right')
        T_address.insert('1.0', estdata1[2])
        T_address.tag_add('tag_name','1.0', 'end')
        T_address_window = canvas.create_window(520, 80, anchor="nw", window=T_address)

        canvas.create_text(708, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
        canvas.create_text(710, 205, text=""+est_str1.get(), fill="black", font=('Helvetica 14 bold'))
          
        canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
        canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

        s = ttk.Style()
        s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

        tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_1.Treeview')
          
        tree.column("# 1", anchor=E, stretch=NO, width=530)
        tree.heading("# 1", text="Product/Service - Description")
        tree.column("# 2", anchor=E, stretch=NO, width=90)
        tree.heading("# 2", text="Quantity")
        tree.column("# 3", anchor=E, stretch=NO, width=80)
        tree.heading("# 3", text="Price")
          
        window = canvas.create_window(120, 340, anchor="nw", window=tree)

        canvas.create_line(120, 390, 820, 390 )
        canvas.create_line(120, 340, 120, 365 )
        canvas.create_line(120, 365, 120, 390 )
        canvas.create_line(820, 340, 820, 540 )
        canvas.create_line(740, 340, 740, 540 )
        canvas.create_line(570, 390, 570, 540 )
        canvas.create_line(570, 415, 820, 415 )
        canvas.create_line(570, 440, 820, 440 )
        canvas.create_line(570, 465, 820, 465 )
        canvas.create_line(570, 490, 820, 490 )
        canvas.create_line(570, 515, 820, 515 )
        canvas.create_line(650, 340, 650, 390 )
        canvas.create_line(570, 540, 820, 540 )

      
        canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        canvas.create_text(710, 372, text="1", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

        canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

        canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        canvas.create_line(150, 608, 795, 608)
        # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
        T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
        T.insert(END, estdata1[39])
        T_window = canvas.create_window(155, 612, anchor="nw", window=T)
        canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))

#----------------Simplified 2 (logo on right side)------------------ 
      elif menuvar == 'Simplified 2 (logo on right side)':
        frame = Frame(fifthtab, width=953, height=300)
        frame.pack(expand=True, fill=BOTH)
        frame.place(x=247,y=90)

        canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))

        vertibar=Scrollbar(frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=canvas.yview)
        canvas.config(width=953,height=300)

        canvas.config(yscrollcommand=vertibar.set)
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
        canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        try:
          est_image = Image.open("images/"+estdata1[13])
          est_resize_image = est_image.resize((200,100))
          est_image = ImageTk.PhotoImage(est_resize_image)

          est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
          window_image = canvas.create_window(500, 45, anchor="nw", window=est_btlogo)
          est_btlogo.photo = est_image
        except:
          pass  
        canvas.create_text(250, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
        # canvas.create_text(224, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
        T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
        T_address.tag_configure('tag_name',justify='right')
        T_address.insert('1.0', estdata1[2])
        T_address.tag_add('tag_name','1.0', 'end')
        T_address_window = canvas.create_window(100, 80, anchor="nw", window=T_address)

        canvas.create_text(224, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
        canvas.create_text(225, 205, text=""+est_str1.get(), fill="black", font=('Helvetica 14 bold'))

        canvas.create_text(502, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(515, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(500, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(491, 220, text="Terms", fill="black", font=('Helvetica 11'))
        canvas.create_text(505, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
        canvas.create_text(680, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(680, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(680, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(670, 220, text="NET 15", fill="black", font=('Helvetica 11'))      

        canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
        canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

        s = ttk.Style()
        s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

        tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_1.Treeview')
          
        tree.column("# 1", anchor=E, stretch=NO, width=530)
        tree.heading("# 1", text="Product/Service - Description")
        tree.column("# 2", anchor=E, stretch=NO, width=90)
        tree.heading("# 2", text="Quantity")
        tree.column("# 3", anchor=E, stretch=NO, width=80)
        tree.heading("# 3", text="Price")
          
        window = canvas.create_window(120, 340, anchor="nw", window=tree)

        canvas.create_line(120, 390, 820, 390 )
        canvas.create_line(120, 340, 120, 365 )
        canvas.create_line(120, 365, 120, 390 )
        canvas.create_line(820, 340, 820, 540 )
        canvas.create_line(740, 340, 740, 540 )
        canvas.create_line(570, 390, 570, 540 )
        canvas.create_line(570, 415, 820, 415 )
        canvas.create_line(570, 440, 820, 440 )
        canvas.create_line(570, 465, 820, 465 )
        canvas.create_line(570, 490, 820, 490 )
        canvas.create_line(570, 515, 820, 515 )
        canvas.create_line(650, 340, 650, 390 )
        canvas.create_line(570, 540, 820, 540 )

          
        canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        canvas.create_text(710, 372, text="1", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass

        # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

        canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

        canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        canvas.create_line(150, 608, 795, 608)
        # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
        T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
        T.insert(END, estdata1[39])
        T_window = canvas.create_window(155, 612, anchor="nw", window=T)
        canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))

#----------------Business Classic------------------ 
      elif menuvar == 'Business Classic':
        frame = Frame(fifthtab, width=953, height=300)
        frame.pack(expand=True, fill=BOTH)
        frame.place(x=247,y=90)
          
        canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
          
        vertibar=Scrollbar(frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=canvas.yview)
        canvas.config(width=953,height=300)
          
        canvas.config(yscrollcommand=vertibar.set)
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
        canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        canvas.create_line(150, 70, 800, 70, fill='orange')
        
        try:
          est_image = Image.open("images/"+estdata1[13])
          est_resize_image = est_image.resize((200,100))
          est_image = ImageTk.PhotoImage(est_resize_image)

          est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
          window_image = canvas.create_window(140, 120, anchor="nw", window=est_btlogo)
          est_btlogo.photo = est_image
        except:
          pass  

        canvas.create_text(500, 90, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
        # canvas.create_text(485, 220, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
        T_address = Text(canvas, height=5, width=35, font=('Helvetica 10'),borderwidth=0)
        T_address.tag_configure('tag_name',justify='right')
        T_address.insert('1.0', estdata1[2])
        T_address.tag_add('tag_name','1.0', 'end')
        T_address_window = canvas.create_window(350, 100, anchor="nw", window=T_address)
        
        canvas.create_text(480, 210, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))

        canvas.create_text(655, 100, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(696, 120, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(706, 135, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(665, 150, text="United States", fill="black", font=('Helvetica 10'))

        canvas.create_text(659, 180, text=""+est_str1.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(675, 210, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
        canvas.create_text(659, 240, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))

        canvas.create_text(776, 180, text="EST1/2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(776, 210, text="05 May 2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(776, 240, text="20-05-2022", fill="black", font=('Helvetica 11'))

        s = ttk.Style()
        s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

        tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_1.Treeview')
          
        tree.column("# 1", anchor=E, stretch=NO, width=200)
        tree.heading("# 1", text="Product/Service")
        tree.column("# 2", anchor=E, stretch=NO, width=250)
        tree.heading("# 2", text="Description")
        tree.column("# 3", anchor=E, stretch=NO, width=90)
        tree.heading("# 3", text="Unit Price")
        tree.column("# 4", anchor=E, stretch=NO, width=80)
        tree.heading("# 4", text="Quantity")
        tree.column("# 5", anchor=E, stretch=NO, width=80)
        tree.heading("# 5", text="Price")
      
        window = canvas.create_window(120, 255, anchor="nw", window=tree)

        canvas.create_line(120, 295, 820, 295 )
        canvas.create_line(120, 255, 120, 295 )
        canvas.create_line(320, 255, 320, 295 )
        canvas.create_line(570, 255, 570, 295 )
        canvas.create_line(660, 255, 660, 295 )
        canvas.create_line(740, 255, 740, 295 )
        canvas.create_line(820, 255, 820, 445 )
        canvas.create_line(570, 320, 820, 320 )
        canvas.create_line(570, 345, 820, 345 )
        canvas.create_line(570, 370, 820, 370 )
        canvas.create_line(570, 395, 820, 395 )
        canvas.create_line(570, 420, 820, 420 )
        canvas.create_line(570, 445, 820, 445 )
      
        canvas.create_text(160, 285, text="PROD-0001", fill="black", font=('Helvetica 10'))
        canvas.create_text(450, 285, text="Example product - Description text...", fill="black", font=('Helvetica 10'))

        if comcursignpla.get() == "before amount":
          canvas.create_text(624, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(624, 285, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(624, 285, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(624, 285, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(624, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(700, 285, text="1", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 285, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 285, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 285, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(784, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 310, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 310, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 310, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 310, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(784, 310, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(789, 335, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(789, 335, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(789, 335, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(789, 335, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(789, 335, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(789, 360, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(789, 360, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(789, 360, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(789, 360, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(789, 360, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 385, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 385, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 385, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 385, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(784, 385, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 410, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 410, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 410, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 410, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(784, 410, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(784, 435, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(784, 435, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(784, 435, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(784, 435, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(784, 435, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(595, 310, text="Subtotal", fill="black", font=('Helvetica 10'))
        canvas.create_text(585, 335, text="TAX1", fill="black", font=('Helvetica 10'))
        canvas.create_text(635, 360, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        canvas.create_text(615, 385, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))
        canvas.create_text(600, 410, text="Total Paid", fill="black", font=('Helvetica 10'))
        canvas.create_text(595, 435, text="Balance", fill="black", font=('Helvetica 10'))

        canvas.create_line(150, 470, 800, 470, fill='orange')
        canvas.create_text(275, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 510, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 520, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(182, 530, text="...", fill="black", font=('Helvetica 10'))
          
        canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        canvas.create_line(150, 608, 795, 608, fill='orange')
        # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
        T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
        T.insert(END, estdata1[39])
        T_window = canvas.create_window(155, 612, anchor="nw", window=T)
        canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
      else:
        pass

  win_menu2 = StringVar()
  winstyle2 = ttk.Combobox(fifthtab,textvariable=win_menu2)
  winstyle2.bind("<<ComboboxSelected>>", maindropmenu)
  winstyle2["values"] = ("Professional 1 (logo on left side)","Professional 2 (logo on right side)","Simplified 1 (logo on left side)","Simplified 2 (logo on right side)","Business Classic")
  if not estdata:
    winstyle2.current(0)
    frame = Frame(fifthtab, width=953, height=300)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=247,y=90)
    canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
          
    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
      
    canvas.config(width=953,height=300)
    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(100, 8, 850, 687 , outline='yellow',fill='white')
    canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
  
    #canvas.create_image(120,0, anchor=NW, image=est_logo)  
    canvas.create_text(285, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))
      
    canvas.create_text(202, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(215, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(200, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(191, 220, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(205, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(340, 220, text="NET 15", fill="black", font=('Helvetica 11'))
      
    canvas.create_text(720, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(700, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'), width=125)
    # T_address = Text(canvas, height=5, width=20 , font=('Helvetica 10'))
    # T_address.insert(END, estdata[2])
    # T_address_window = canvas.create_window(645, 80, anchor="nw", window=T_address)
    canvas.create_text(700, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
    canvas.create_text(700, 205, text=" "+est_str1.get(), fill="black", font=('Helvetica 14 bold'))
    canvas.create_text(706, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
      
    canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
      
    s = ttk.Style()
    s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_1.Treeview')

    tree.column("# 1", anchor=E, stretch=NO, width=100)
    tree.heading("# 1", text="ID/SKU")
    tree.column("# 2", anchor=E, stretch=NO, width=350)
    tree.heading("# 2", text="Product/Service - Description")
    tree.column("# 3", anchor=E, stretch=NO, width=80)
    tree.heading("# 3", text="Quantity")
    tree.column("# 4", anchor=E, stretch=NO, width=90)
    tree.heading("# 4", text="Unit Price")
    tree.column("# 5", anchor=E, stretch=NO, width=80)
    tree.heading("# 5", text="Price")
      
    window = canvas.create_window(120, 340, anchor="nw", window=tree)

    canvas.create_line(120, 390, 820, 390 )
    canvas.create_line(120, 340, 120, 365 )
    canvas.create_line(120, 365, 120, 390 )
    canvas.create_line(820, 340, 820, 540 )
    canvas.create_line(740, 340, 740, 540 )
    canvas.create_line(570, 340, 570, 540 )
    canvas.create_line(570, 415, 820, 415 )
    canvas.create_line(570, 440, 820, 440 )
    canvas.create_line(570, 465, 820, 465 )
    canvas.create_line(570, 490, 820, 490 )
    canvas.create_line(570, 515, 820, 515 )
    canvas.create_line(650, 340, 650, 390 )
    canvas.create_line(220, 340, 220, 390 )
    canvas.create_line(570, 540, 820, 540 )

    canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
    canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
    
    if comcursignpla.get() == "before amount":
      canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount":
      canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(704, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    else:
      pass
    # canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
    
    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
    else:
      pass

    # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))
    
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
      
    canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(150, 608, 795, 608)
    # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10')) 
    # T = Text(canvas, height=3, width=105, font=('Helvetica 10'))
    # T.insert(END, estdata[39])
    # T_window = canvas.create_window(105, 612, anchor="nw", window=T)


    canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10')) 
  elif estdata[32] == 'Professional 1 (logo on left side)':
    winstyle2.insert(0, estdata[32])
    frame = Frame(fifthtab, width=953, height=300)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=247,y=90)
    canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
          
    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
      
    canvas.config(width=953,height=300)
    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(100, 8, 850, 687 , outline='yellow',fill='white')
    canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    try:
      est_image = Image.open("images/"+estdata[13])
      est_resize_image = est_image.resize((200,100))
      est_image = ImageTk.PhotoImage(est_resize_image)

      est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
      window_image = canvas.create_window(175, 45, anchor="nw", window=est_btlogo)
      est_btlogo.photo = est_image
    except:
      pass  
    canvas.create_text(202, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(215, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(200, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(191, 220, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(205, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(340, 220, text="NET 15", fill="black", font=('Helvetica 11'))
      
    canvas.create_text(720, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(700, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'), width=125)
    T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', estdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(520, 80, anchor="nw", window=T_address)
    canvas.create_text(695, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
    canvas.create_text(700, 205, text=" "+est_str1.get(), fill="black", font=('Helvetica 14 bold'))
    canvas.create_text(706, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
      
    canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
      
    s = ttk.Style()
    s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_1.Treeview')

    tree.column("# 1", anchor=E, stretch=NO, width=100)
    tree.heading("# 1", text="ID/SKU")
    tree.column("# 2", anchor=E, stretch=NO, width=350)
    tree.heading("# 2", text="Product/Service - Description")
    tree.column("# 3", anchor=E, stretch=NO, width=80)
    tree.heading("# 3", text="Quantity")
    tree.column("# 4", anchor=E, stretch=NO, width=90)
    tree.heading("# 4", text="Unit Price")
    tree.column("# 5", anchor=E, stretch=NO, width=80)
    tree.heading("# 5", text="Price")
      
    window = canvas.create_window(120, 340, anchor="nw", window=tree)

    canvas.create_line(120, 390, 820, 390 )
    canvas.create_line(120, 340, 120, 365 )
    canvas.create_line(120, 365, 120, 390 )
    canvas.create_line(820, 340, 820, 540 )
    canvas.create_line(740, 340, 740, 540 )
    canvas.create_line(570, 340, 570, 540 )
    canvas.create_line(570, 415, 820, 415 )
    canvas.create_line(570, 440, 820, 440 )
    canvas.create_line(570, 465, 820, 465 )
    canvas.create_line(570, 490, 820, 490 )
    canvas.create_line(570, 515, 820, 515 )
    canvas.create_line(650, 340, 650, 390 )
    canvas.create_line(220, 340, 220, 390 )
    canvas.create_line(570, 540, 820, 540 )

    canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
    canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
    
    if comcursignpla.get() == "before amount":
      canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount":
      canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(704, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    else:
      pass
    # canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
    
    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
    else:
      pass

    # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))
    
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
      
    canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(150, 608, 795, 608)
    # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10')) 
    T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
    T.insert(END, estdata[39])
    T_window = canvas.create_window(155, 612, anchor="nw", window=T)

    canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  elif estdata[32] == 'Professional 2 (logo on right side)':
    winstyle2.insert(0, estdata[32])
    frame = Frame(fifthtab, width=953, height=300)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=247,y=90)
      
    canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
      
    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=953,height=300)
      
    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
    canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    try:
      est_image = Image.open("images/"+estdata[13])
      est_resize_image = est_image.resize((200,100))
      est_image = ImageTk.PhotoImage(est_resize_image)

      est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
      window_image = canvas.create_window(500, 45, anchor="nw", window=est_btlogo)
      est_btlogo.photo = est_image
    except:
      pass  
    canvas.create_text(250, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(225, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
    T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', estdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(100, 80, anchor="nw", window=T_address)
    canvas.create_text(225, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
    canvas.create_text(225, 205, text=""+est_str1.get(), fill="black", font=('Helvetica 14 bold'))
    canvas.create_text(232, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
      
    canvas.create_text(502, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(515, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(500, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(491, 220, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(505, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(690, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(690, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(690, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(680, 220, text="NET 15", fill="black", font=('Helvetica 11'))      
      
    canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

    s = ttk.Style()
    s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_1.Treeview')
      
    tree.column("# 1", anchor=E, stretch=NO, width=100)
    tree.heading("# 1", text="ID/SKU")
    tree.column("# 2", anchor=E, stretch=NO, width=350)
    tree.heading("# 2", text="Product/Service - Description")
    tree.column("# 3", anchor=E, stretch=NO, width=80)
    tree.heading("# 3", text="Quantity")
    tree.column("# 4", anchor=E, stretch=NO, width=90)
    tree.heading("# 4", text="Unit Price")
    tree.column("# 5", anchor=E, stretch=NO, width=80)
    tree.heading("# 5", text="Price")
      
    window = canvas.create_window(120, 340, anchor="nw", window=tree)

    canvas.create_line(120, 390, 820, 390 )
    canvas.create_line(120, 340, 120, 365 )
    canvas.create_line(120, 365, 120, 390 )
    canvas.create_line(820, 340, 820, 540 )
    canvas.create_line(740, 340, 740, 540 )
    canvas.create_line(570, 340, 570, 540 )
    canvas.create_line(570, 415, 820, 415 )
    canvas.create_line(570, 440, 820, 440 )
    canvas.create_line(570, 465, 820, 465 )
    canvas.create_line(570, 490, 820, 490 )
    canvas.create_line(570, 515, 820, 515 )
    canvas.create_line(650, 340, 650, 390 )
    canvas.create_line(220, 340, 220, 390 )
    canvas.create_line(570, 540, 820, 540 )

    canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
    canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(704, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
      canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
    else:
      pass

    # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))
    
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

    canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(150, 608, 795, 608)
    # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
    T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
    T.insert(END, estdata[39])
    T_window = canvas.create_window(155, 612, anchor="nw", window=T)
    canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  elif estdata[32] == 'Simplified 1 (logo on left side)':
    winstyle2.insert(0, estdata[32])
    frame = Frame(fifthtab, width=953, height=300)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=247,y=90)
    canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))

    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=953,height=300)

    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
    canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    try:
      est_image = Image.open("images/"+estdata[13])
      est_resize_image = est_image.resize((200,100))
      est_image = ImageTk.PhotoImage(est_resize_image)

      est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
      window_image = canvas.create_window(175, 45, anchor="nw", window=est_btlogo)
      est_btlogo.photo = est_image
    except:
      pass  
    canvas.create_text(202, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(215, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(200, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(191, 220, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(205, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(340, 220, text="NET 15", fill="black", font=('Helvetica 11'))      

    canvas.create_text(720, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(710, 200, text=caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
    T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', estdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(520, 80, anchor="nw", window=T_address)

    canvas.create_text(708, 170, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
    canvas.create_text(710, 205, text=""+est_str1.get(), fill="black", font=('Helvetica 14 bold'))
      
    canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

    s = ttk.Style()
    s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_1.Treeview')
      
    tree.column("# 1", anchor=E, stretch=NO, width=530)
    tree.heading("# 1", text="Product/Service - Description")
    tree.column("# 2", anchor=E, stretch=NO, width=90)
    tree.heading("# 2", text="Quantity")
    tree.column("# 3", anchor=E, stretch=NO, width=80)
    tree.heading("# 3", text="Price")
      
    window = canvas.create_window(120, 340, anchor="nw", window=tree)

    canvas.create_line(120, 390, 820, 390 )
    canvas.create_line(120, 340, 120, 365 )
    canvas.create_line(120, 365, 120, 390 )
    canvas.create_line(820, 340, 820, 540 )
    canvas.create_line(740, 340, 740, 540 )
    canvas.create_line(570, 390, 570, 540 )
    canvas.create_line(570, 415, 820, 415 )
    canvas.create_line(570, 440, 820, 440 )
    canvas.create_line(570, 465, 820, 465 )
    canvas.create_line(570, 490, 820, 490 )
    canvas.create_line(570, 515, 820, 515 )
    canvas.create_line(650, 340, 650, 390 )
    canvas.create_line(570, 540, 820, 540 )

      
    canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(710, 372, text="1", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

    canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(150, 608, 795, 608)
    # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
    T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
    T.insert(END, estdata[39])
    T_window = canvas.create_window(155, 612, anchor="nw", window=T)
    canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  elif estdata[32] == 'Simplified 2 (logo on right side)':
    winstyle2.insert(0, estdata[32])
    frame = Frame(fifthtab, width=953, height=300)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=247,y=90)

    canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))

    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=953,height=300)

    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
    canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    try:
      est_image = Image.open("images/"+estdata[13])
      est_resize_image = est_image.resize((200,100))
      est_image = ImageTk.PhotoImage(est_resize_image)

      est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
      window_image = canvas.create_window(500, 45, anchor="nw", window=est_btlogo)
      est_btlogo.photo = est_image
    except:
      pass  
    canvas.create_text(250, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(224, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
    T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', estdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(100, 80, anchor="nw", window=T_address)
    canvas.create_text(224, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
    canvas.create_text(225, 205, text=""+est_str1.get(), fill="black", font=('Helvetica 14 bold'))

    canvas.create_text(502, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(515, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(500, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(491, 220, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(505, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(680, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(680, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(680, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(670, 220, text="NET 15", fill="black", font=('Helvetica 11'))      

    canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

    s = ttk.Style()
    s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_1.Treeview')
      
    tree.column("# 1", anchor=E, stretch=NO, width=530)
    tree.heading("# 1", text="Product/Service - Description")
    tree.column("# 2", anchor=E, stretch=NO, width=90)
    tree.heading("# 2", text="Quantity")
    tree.column("# 3", anchor=E, stretch=NO, width=80)
    tree.heading("# 3", text="Price")
      
    window = canvas.create_window(120, 340, anchor="nw", window=tree)

    canvas.create_line(120, 390, 820, 390 )
    canvas.create_line(120, 340, 120, 365 )
    canvas.create_line(120, 365, 120, 390 )
    canvas.create_line(820, 340, 820, 540 )
    canvas.create_line(740, 340, 740, 540 )
    canvas.create_line(570, 390, 570, 540 )
    canvas.create_line(570, 415, 820, 415 )
    canvas.create_line(570, 440, 820, 440 )
    canvas.create_line(570, 465, 820, 465 )
    canvas.create_line(570, 490, 820, 490 )
    canvas.create_line(570, 515, 820, 515 )
    canvas.create_line(650, 340, 650, 390 )
    canvas.create_line(570, 540, 820, 540 )

      
    canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(710, 372, text="1", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass

    # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

    canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(150, 608, 795, 608)
    # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
    T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
    T.insert(END, estdata[39])
    T_window = canvas.create_window(155, 612, anchor="nw", window=T)
    canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  elif estdata[32] == 'Business Classic':
    winstyle2.insert(0, estdata[32])
    frame = Frame(fifthtab, width=953, height=300)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=247,y=90)
      
    canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
      
    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=953,height=300)
      
    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
    canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_line(150, 70, 800, 70, fill='orange')
    
    try:
      est_image = Image.open("images/"+estdata[13])
      est_resize_image = est_image.resize((200,100))
      est_image = ImageTk.PhotoImage(est_resize_image)

      est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
      window_image = canvas.create_window(140, 120, anchor="nw", window=est_btlogo)
      est_btlogo.photo = est_image
    except:
      pass  

    canvas.create_text(500, 90, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(480, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
    T_address = Text(canvas, height=5, width=35, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', estdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(350, 100, anchor="nw", window=T_address)
        
        
    canvas.create_text(480, 210, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))

    canvas.create_text(655, 100, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(696, 120, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(706, 135, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(665, 150, text="United States", fill="black", font=('Helvetica 10'))

    canvas.create_text(659, 180, text=""+est_str1.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(675, 210, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
    canvas.create_text(659, 240, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))

    canvas.create_text(776, 180, text="EST1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(776, 210, text="05 May 2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(776, 240, text="20-05-2022", fill="black", font=('Helvetica 11'))

    s = ttk.Style()
    s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_1.Treeview')
      
    tree.column("# 1", anchor=E, stretch=NO, width=200)
    tree.heading("# 1", text="Product/Service")
    tree.column("# 2", anchor=E, stretch=NO, width=250)
    tree.heading("# 2", text="Description")
    tree.column("# 3", anchor=E, stretch=NO, width=90)
    tree.heading("# 3", text="Unit Price")
    tree.column("# 4", anchor=E, stretch=NO, width=80)
    tree.heading("# 4", text="Quantity")
    tree.column("# 5", anchor=E, stretch=NO, width=80)
    tree.heading("# 5", text="Price")
      
    window = canvas.create_window(120, 255, anchor="nw", window=tree)

    canvas.create_line(120, 295, 820, 295 )
    canvas.create_line(120, 255, 120, 295 )
    canvas.create_line(320, 255, 320, 295 )
    canvas.create_line(570, 255, 570, 295 )
    canvas.create_line(660, 255, 660, 295 )
    canvas.create_line(740, 255, 740, 295 )
    canvas.create_line(820, 255, 820, 445 )
    canvas.create_line(570, 320, 820, 320 )
    canvas.create_line(570, 345, 820, 345 )
    canvas.create_line(570, 370, 820, 370 )
    canvas.create_line(570, 395, 820, 395 )
    canvas.create_line(570, 420, 820, 420 )
    canvas.create_line(570, 445, 820, 445 )
      
    canvas.create_text(160, 285, text="PROD-0001", fill="black", font=('Helvetica 10'))
    canvas.create_text(450, 285, text="Example product - Description text...", fill="black", font=('Helvetica 10'))

    if comcursignpla.get() == "before amount":
      canvas.create_text(624, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(624, 285, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(624, 285, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(624, 285, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(624, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(700, 285, text="1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 285, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 285, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 285, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 310, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 310, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 310, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 310, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 310, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(789, 335, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(789, 335, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(789, 335, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(789, 335, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(789, 335, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(789, 360, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(789, 360, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(789, 360, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(789, 360, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(789, 360, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 385, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 385, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 385, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 385, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 385, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 410, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 410, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 410, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 410, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 410, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(784, 435, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(784, 435, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(784, 435, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(784, 435, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(784, 435, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(595, 310, text="Subtotal", fill="black", font=('Helvetica 10'))
    canvas.create_text(585, 335, text="TAX1", fill="black", font=('Helvetica 10'))
    canvas.create_text(635, 360, text="Shipping and handling", fill="black", font=('Helvetica 10'))
    canvas.create_text(615, 385, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(600, 410, text="Total Paid", fill="black", font=('Helvetica 10'))
    canvas.create_text(595, 435, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_line(150, 470, 800, 470, fill='orange')
    canvas.create_text(275, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 510, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 520, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(182, 530, text="...", fill="black", font=('Helvetica 10'))
      
    canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(150, 608, 795, 608, fill='orange')
    # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
    T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
    T.insert(END, estdata[39])
    T_window = canvas.create_window(155, 612, anchor="nw", window=T)
    canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  else:
    pass
  winstyle2.place(x=770 ,y=40, width=220)
  #winstyle2.current(0)



################### tab07 ###################################
  seventhtab1=Frame(tab07, relief=GROOVE, bg="#f8f8f2")
  seventhtab1.pack(side="top", fill=BOTH)

  sql = "select * from company"
  fbcursor.execute(sql)
  advdata = fbcursor.fetchone()
  #print(estdata)


  seventhtab=Frame(seventhtab1, bg="#f5f3f2", height=700)
  seventhtab.pack(side="top", fill=BOTH)

  adv_messagelbframe=LabelFrame(seventhtab,text="Template advanced settings", height=250, width=1150)
  adv_messagelbframe.place(x=2, y=10)

  adv_fbill = Label(seventhtab,text="Template",font="arial 10 bold").place(x=20,y=30)

  adv_ver = Label(seventhtab,text="Professional 1 (logo on left side)")
  adv_ver.place(x=20,y=60)

  adv_ver = Label(seventhtab,text="Professional 2 (logo on right side)")
  adv_ver.place(x=20,y=90)

  adv_ver = Label(seventhtab,text="Simplified 1 (logo on left side)")
  adv_ver.place(x=20,y=120)

  adv_ver = Label(seventhtab,text="Simplified 2 (logo on right side)")
  adv_ver.place(x=20,y=150)

  adv_ver = Label(seventhtab,text="Business Classic")
  adv_ver.place(x=20,y=180)

  adv_fbill = Label(seventhtab,text="Page size",font="arial 10 bold").place(x=255,y=30)

  adv_win_menu3 = StringVar()
  adv_winstyle3 = ttk.Combobox(seventhtab,textvariable=adv_win_menu3)
  adv_winstyle3['values'] = ('Letter','A4')
  adv_win_menu3.set('Letter')
  #adv_winstyle3.current(0)
  adv_winstyle3.place(x=225 ,y=60)
    
  
  adv_win_menu4 = StringVar()
  adv_winstyle4 = ttk.Combobox(seventhtab,textvariable=adv_win_menu4)
  adv_winstyle4.place(x=225,y=90)
  adv_winstyle4['values'] = ("Letter","A4")
  adv_winstyle4.set("Letter")
  adv_winstyle4.current(0)

  adv_win_menu5 = StringVar()
  adv_winstyle5 = ttk.Combobox(seventhtab,textvariable=adv_win_menu5)
  adv_winstyle5.place(x=225,y=120)
  adv_winstyle5['values'] = ("Letter","A4")
  adv_winstyle5.set("Letter")
  adv_winstyle5.current(0)

  adv_win_menu6 = StringVar()
  adv_winstyle6 = ttk.Combobox(seventhtab,textvariable=adv_win_menu6)
  adv_winstyle6.place(x=225,y=150)
  adv_winstyle6['values'] = ("Letter","A4")
  adv_winstyle6.set("Letter")
  adv_winstyle6.current(0)

  adv_win_menu7 = StringVar()
  adv_winstyle7 = ttk.Combobox(seventhtab,textvariable=adv_win_menu7)
  adv_winstyle7.place(x=225,y=180)
  adv_winstyle7['values'] = ("Letter","A4")
  adv_winstyle7.set("Letter")
  adv_winstyle7.current(0)

  adv_fbill = Label(seventhtab,text="Right Margin(mm)",font="arial 10 bold").place(x=450,y=30)

  adv_spin00 = Spinbox(seventhtab,from_=5,to=20,width=10)
  adv_spin00.place(x=465,y=60)

  adv_spin01 = Spinbox(seventhtab,from_=5,to=20,width=10)
  adv_spin01.place(x=465,y=90)

  adv_spin02 = Spinbox(seventhtab,from_=5,to=20,width=10)
  adv_spin02.place(x=465,y=120)

  adv_spin03 = Spinbox(seventhtab,from_=5,to=20,width=10)
  adv_spin03.place(x=465,y=150)

  adv_spin04 = Spinbox(seventhtab,from_=5,to=20,width=10)
  adv_spin04.place(x=465,y=180)


  adv_fbill = Label(seventhtab,text="'Invoice to'block position shift(mm)",font="arial 10 bold").place(x=650,y=30)

  adv_lbl1 = Label(seventhtab, text="Left : ").place(x=651,y=60)
  adv_lbl1 = Label(seventhtab, text="Left : ").place(x=651,y=90)
  adv_lbl1 = Label(seventhtab, text="Left : ").place(x=651,y=120)
  adv_lbl1 = Label(seventhtab, text="Left : ").place(x=651,y=150)

  adv_spin10 = Spinbox(seventhtab,from_=-10,to=100,width=10)
  adv_spin10.place(x=685,y=60)

  adv_spin11 = Spinbox(seventhtab,from_=-10,to=100,width=10)
  adv_spin11.place(x=685,y=90)

  adv_spin12 = Spinbox(seventhtab,from_=-10,to=100,width=10)
  adv_spin12.place(x=685,y=120)

  adv_spin13 = Spinbox(seventhtab,from_=-10,to=100,width=10)
  adv_spin13.place(x=685,y=150)

  adv_lbl1 = Label(seventhtab, text="Top : ").place(x=785,y=60)
  adv_lbl1 = Label(seventhtab, text="Top : ").place(x=785,y=90)
  adv_lbl1 = Label(seventhtab, text="Top : ").place(x=785,y=120)
  adv_lbl1 = Label(seventhtab, text="Top : ").place(x=785,y=150)

  adv_spin20 = Spinbox(seventhtab,from_=0,to=100,width=10)
  adv_spin20.place(x=820,y=60)

  adv_spin21 = Spinbox(seventhtab,from_=0,to=100,width=10)
  adv_spin21.place(x=820,y=90)

  adv_spin22 = Spinbox(seventhtab,from_=0,to=100,width=10)
  adv_spin22.place(x=820,y=120)

  adv_spin23 = Spinbox(seventhtab,from_=0,to=100,width=10)
  adv_spin23.place(x=820,y=150)

  adv_bttermadd = Button(seventhtab,image=photo8,compound = LEFT,text="Refresh preview",width=115)
  adv_bttermadd.place(x=1000,y=50)

  adv_bttermadd = Button(seventhtab,image=saves,compound = LEFT,text="Save Settings",width=115)
  adv_bttermadd.place(x=1000,y=140)

  def adv_restore():
    adv_spin10.delete(0,'end')
    adv_spin10.insert(0,"0")
    adv_spin11.delete(0,'end')
    adv_spin11.insert(0,"0")
    adv_spin12.delete(0,'end')
    adv_spin12.insert(0,"0")
    adv_spin13.delete(0,'end')
    adv_spin13.insert(0,"0")
    adv_spin20.delete(0,'end')
    adv_spin20.insert(0,"0")
    adv_spin21.delete(0,'end')
    adv_spin21.insert(0,"0")
    adv_spin22.delete(0,'end')
    adv_spin22.insert(0,"0")
    adv_spin23.delete(0,'end')
    adv_spin23.insert(0,"0")
    adv_spin00.delete(0,'end')
    adv_spin00.insert(0,"10")
    adv_spin01.delete(0,'end')
    adv_spin01.insert(0,"10")
    adv_spin02.delete(0,'end')
    adv_spin02.insert(0,"10")
    adv_spin03.delete(0,'end')
    adv_spin03.insert(0,"10")
    adv_spin04.delete(0,'end')
    adv_spin04.insert(0,"10")
    adv_winstyle3.delete(0,'end')
    adv_winstyle3.insert(0,"Letter")
    adv_winstyle4.delete(0,'end')
    adv_winstyle4.insert(0,"Letter")
    adv_winstyle5.delete(0,'end')
    adv_winstyle5.insert(0,"Letter")
    adv_winstyle6.delete(0,'end')
    adv_winstyle6.insert(0,"Letter")
    adv_winstyle7.delete(0,'end')
    adv_winstyle7.insert(0,"Letter")

  adv_bttermadd = Button(seventhtab,text="Restore defaults",width=16, command=adv_restore)
  adv_bttermadd.place(x=1000,y=180)

  adv_ver = Label(seventhtab,text="By positioning 'Invoice to'block,the customer name/address can be displayed in right place in the windowed envelope. If you networking, you need to setup this on all computer.\nExample:(Left:20 and Top:10 means that shift 'Invoice to'block to right 20mm and shift down 10mm) Original position Left:0 Top:0")
  adv_ver.place(x=50,y=210)

  adv_ver = Label(seventhtab,text="Selected template preview (example, click on preview for mouse scrolling)")
  adv_ver.place(x=230,y=270)

#------------Professional 1 (logo on left side)------------- 
  def adv_maindropmenu(event):
      menuvar=adv_win_menu8.get()
      print(menuvar)
      sql = "select * from company"
      fbcursor.execute(sql)
      advdata1 = fbcursor.fetchone()

      if menuvar == 'Professional 1 (logo on left side)':
          frame = Frame(seventhtab, width=1200, height=155)
          frame.pack(expand=True, fill=BOTH)
          frame.place(x=2,y=309)
          canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

          vertibar=Scrollbar(frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=canvas.yview)
          canvas.config(width=1200,height=155)

          canvas.config(yscrollcommand=vertibar.set)
          canvas.pack(expand=True,side=LEFT,fill=BOTH)
          canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')

          canvas.create_text(600, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))

          try:
            adv_image = Image.open("images/"+advdata1[13])
            adv_resize_image = adv_image.resize((200,75))
            adv_image = ImageTk.PhotoImage(adv_resize_image)

            adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
            adv_window_image = canvas.create_window(150, 30, anchor="nw", window=adv_btlogo)
            adv_btlogo.photo = adv_image
          except:
            pass  

          canvas.create_text(130, 120, text="Invoice#", fill="black", font=('Helvetica 11'))
          canvas.create_text(141, 140, text="Invoice date", fill="black", font=('Helvetica 11'))
          canvas.create_text(130, 160, text="Due date", fill="black", font=('Helvetica 11'))
          canvas.create_text(120, 180, text="Terms", fill="black", font=('Helvetica 11'))
          canvas.create_text(134, 200, text="Order ref.#", fill="black", font=('Helvetica 11'))
          canvas.create_text(347, 120, text="INV1/2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(350, 140, text="03-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(350, 160, text="18-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(340, 180, text="NET 15", fill="black", font=('Helvetica 11'))

          canvas.create_text(1050, 65, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
          # canvas.create_text(1080, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
          T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
          T_address.tag_configure('tag_name',justify='right')
          T_address.insert('1.0', advdata[2])
          T_address.tag_add('tag_name','1.0', 'end')
          T_address_window = canvas.create_window(850, 80, anchor="nw", window=T_address)
          canvas.create_text(1050, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
          # canvas.create_text(1085, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
          # canvas.create_text(1085, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
          # canvas.create_text(1080, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
          # canvas.create_text(1080, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
          canvas.create_text(1050, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))
          canvas.create_text(1050, 210, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))

          canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
          canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
          canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
          canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

          s = ttk.Style()
          s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')
              
          tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')
            
          tree.column("# 1", anchor=E, stretch=NO, width=150)
          tree.heading("# 1", text="ID/SKU")
          tree.column("# 2", anchor=E, stretch=NO, width=400)
          tree.heading("# 2", text="Product/Service - Description")
          tree.column("# 3", anchor=E, stretch=NO, width=150)
          tree.heading("# 3", text="Quantity")
          tree.column("# 4", anchor=E, stretch=NO, width=150)
          tree.heading("# 4", text="Unit Price")
          tree.column("# 5", anchor=E, stretch=NO, width=150)
          tree.heading("# 5", text="Price")
            
          window = canvas.create_window(120, 290, anchor="nw", window=tree)

          canvas.create_line(120, 330, 1120, 330 )
          canvas.create_line(120, 290, 120, 330 )
          canvas.create_line(270, 290, 270, 330 )
          canvas.create_line(670, 290, 670, 330 )
          canvas.create_line(820, 290, 820, 330 )
          canvas.create_line(970, 290, 970, 330 )
          canvas.create_line(1120, 290, 1120, 330 )
          canvas.create_line(670, 330, 670, 480)
          canvas.create_line(970, 330, 970, 480)
          canvas.create_line(1120, 330, 1120, 480)
          canvas.create_line(670, 355, 1120, 355)
          canvas.create_line(670, 380, 1120, 380)
          canvas.create_line(670, 405, 1120, 405)
          canvas.create_line(670, 430, 1120, 430)
          canvas.create_line(670, 455, 1120, 455)
          canvas.create_line(670, 480, 1120, 480)

          canvas.create_text(165, 320, text="PROD-0001", fill="black", font=('Helvetica 10'))
          canvas.create_text(400, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          canvas.create_text(740, 320, text="1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(884, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(884, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(884, 320, text="$200.00", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 320, text="$200.00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 345, text="$200.00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1085, 370, text="$18.00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1085, 395, text="$20.00", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 420, text="$238.00", fill="black", font=('Helvetica 10 bold'))
          canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 445, text="$100.00", fill="black", font=('Helvetica 10'))
          canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 465, text="$138.00", fill="black", font=('Helvetica 10'))
          canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))


          canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

          canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
          canvas.create_line(110, 600, 1120, 600)
          canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
          canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
          canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))

#------------Professional 2 (logo on right side)------------- 

      elif menuvar == 'Professional 2 (logo on right side)':
          frame = Frame(seventhtab, width=1200, height=155)
          frame.pack(expand=True, fill=BOTH)
          frame.place(x=2,y=309)
          canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

          vertibar=Scrollbar(frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=canvas.yview)
          canvas.config(width=1200,height=155)

          canvas.config(yscrollcommand=vertibar.set)
          canvas.pack(expand=True,side=LEFT,fill=BOTH)
          canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
          canvas.create_text(600, 45, text="Title text goes here...", fill="black", font=('Helvetica 10'))

          try:
            adv_image = Image.open("images/"+advdata1[13])
            adv_resize_image = adv_image.resize((200,75))
            adv_image = ImageTk.PhotoImage(adv_resize_image)

            adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
            adv_window_image = canvas.create_window(850, 25, anchor="nw", window=adv_btlogo)
            adv_btlogo.photo = adv_image
          except:
            pass  

          # canvas.create_text(1000, 70, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

          canvas.create_text(829, 110, text="Invoice#", fill="black", font=('Helvetica 11'))
          canvas.create_text(841, 130, text="Invoice date", fill="black", font=('Helvetica 11'))
          canvas.create_text(830, 150, text="Due date", fill="black", font=('Helvetica 11'))
          canvas.create_text(820, 170, text="Terms", fill="black", font=('Helvetica 11'))
          canvas.create_text(834, 190, text="Order ref.#", fill="black", font=('Helvetica 11'))
          canvas.create_text(1047, 110, text="INV1/2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(1050, 130, text="06-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(1050, 150, text="21-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(1040, 170, text="NET 15", fill="black", font=('Helvetica 11'))

          canvas.create_text(170, 65, text=""+comname.get(), fill="black", font=('Helvetica 12 '))
          # canvas.create_text(130, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
          T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
          T_address.tag_configure('tag_name',justify='right')
          T_address.insert('1.0', advdata[2])
          T_address.tag_add('tag_name','1.0', 'end')
          T_address_window = canvas.create_window(10, 80, anchor="nw", window=T_address)
          #T_address_window = canvas.create_window(95, 80, anchor="nw", window=T_address)
          canvas.create_text(130, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
          # canvas.create_text(130, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
          # canvas.create_text(130, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
          # canvas.create_text(136, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
          # canvas.create_text(136, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
          canvas.create_text(124, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))

          canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
          canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
          canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
          canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

          tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')
      
          tree.column("# 1", anchor=E, stretch=NO, width=150)
          tree.heading("# 1", text="ID/SKU")
          tree.column("# 2", anchor=E, stretch=NO, width=400)
          tree.heading("# 2", text="Product/Service - Description")
          tree.column("# 3", anchor=E, stretch=NO, width=150)
          tree.heading("# 3", text="Quantity")
          tree.column("# 4", anchor=E, stretch=NO, width=150)
          tree.heading("# 4", text="Unit Price")
          tree.column("# 5", anchor=E, stretch=NO, width=150)
          tree.heading("# 5", text="Price")
      
          window = canvas.create_window(120, 290, anchor="nw", window=tree)

          canvas.create_line(120, 330, 1120, 330 )
          canvas.create_line(120, 290, 120, 330 )
          canvas.create_line(270, 290, 270, 330 )
          canvas.create_line(670, 290, 670, 330 )
          canvas.create_line(820, 290, 820, 330 )
          canvas.create_line(970, 290, 970, 330 )
          canvas.create_line(1120, 290, 1120, 330 )
          canvas.create_line(670, 330, 670, 480)
          canvas.create_line(970, 330, 970, 480)
          canvas.create_line(1120, 330, 1120, 480)
          canvas.create_line(670, 355, 1120, 355)
          canvas.create_line(670, 380, 1120, 380)
          canvas.create_line(670, 405, 1120, 405)
          canvas.create_line(670, 430, 1120, 430)
          canvas.create_line(670, 455, 1120, 455)
          canvas.create_line(670, 480, 1120, 480)

          canvas.create_text(165, 320, text="PROD-0001", fill="black", font=('Helvetica 10'))
          canvas.create_text(400, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          canvas.create_text(740, 320, text="1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(884, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(884, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 320, text="$200.00", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 320, text="$200.00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 345, text="$200.00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1089, 370, text="$18.00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1089, 395, text="$20.00", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 420, text="$238.00", fill="black", font=('Helvetica 10 bold'))
          canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 445, text="$100.00", fill="black", font=('Helvetica 10'))
          canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 465, text="$138.00", fill="black", font=('Helvetica 10'))
          canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))

          canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

          canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
          canvas.create_line(110, 600, 1120, 600)
          canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
          canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
          canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))

#------------Simplified 1 (logo on left side)------------- 

      elif menuvar == 'Simplified 1 (logo on left side)':
          frame = Frame(seventhtab, width=1200, height=155)
          frame.pack(expand=True, fill=BOTH)
          frame.place(x=2,y=309)
          canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

          vertibar=Scrollbar(frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=canvas.yview)
          canvas.config(width=1200,height=155)

          canvas.config(yscrollcommand=vertibar.set)
          canvas.pack(expand=True,side=LEFT,fill=BOTH)
          canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
          canvas.create_text(600, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
          try:
            adv_image = Image.open("images/"+advdata1[13])
            adv_resize_image = adv_image.resize((200,75))
            adv_image = ImageTk.PhotoImage(adv_resize_image)

            adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
            adv_window_image = canvas.create_window(150, 25, anchor="nw", window=adv_btlogo)
            adv_btlogo.photo = adv_image
          except:
            pass  
          #canvas.create_text(250, 70, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

          canvas.create_text(130, 120, text="Invoice#", fill="black", font=('Helvetica 11'))
          canvas.create_text(141, 140, text="Invoice date", fill="black", font=('Helvetica 11'))
          canvas.create_text(130, 160, text="Due date", fill="black", font=('Helvetica 11'))
          canvas.create_text(120, 180, text="Terms", fill="black", font=('Helvetica 11'))
          canvas.create_text(134, 200, text="Order ref.#", fill="black", font=('Helvetica 11'))
          canvas.create_text(347, 120, text="INV1/2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(350, 140, text="06-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(350, 160, text="21-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(340, 180, text="NET 15", fill="black", font=('Helvetica 11'))

          canvas.create_text(1050, 65, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
          # canvas.create_text(1080, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
          T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
          T_address.tag_configure('tag_name',justify='right')
          T_address.insert('1.0', advdata[2])
          T_address.tag_add('tag_name','1.0', 'end')
          T_address_window = canvas.create_window(850, 80, anchor="nw", window=T_address)
          canvas.create_text(1050, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
          # canvas.create_text(1085, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
          # canvas.create_text(1085, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
          # canvas.create_text(1080, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
          # canvas.create_text(1080, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
          canvas.create_text(1050, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))

          canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
          canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
          canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
          canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

          s = ttk.Style()
          s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')

          tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_2.Treeview')
      
          tree.column("# 1", anchor=E, stretch=NO, width=700)
          tree.heading("# 1", text="Product/Service - Description")
          tree.column("# 2", anchor=E, stretch=NO, width=150)
          tree.heading("# 2", text="Quantity")
          tree.column("# 3", anchor=E, stretch=NO, width=150)
          tree.heading("# 3", text="Price")
            
          window = canvas.create_window(120, 290, anchor="nw", window=tree)

          canvas.create_line(120, 330, 1120, 330 )
          canvas.create_line(120, 290, 120, 330 )
          canvas.create_line(820, 290, 820, 330 )
          canvas.create_line(970, 290, 970, 330 )
          canvas.create_line(1120, 290, 1120, 330 )
          canvas.create_line(670, 330, 670, 480)
          canvas.create_line(970, 330, 970, 480)
          canvas.create_line(1120, 330, 1120, 480)
          canvas.create_line(670, 355, 1120, 355)
          canvas.create_line(670, 380, 1120, 380)
          canvas.create_line(670, 405, 1120, 405)
          canvas.create_line(670, 430, 1120, 430)
          canvas.create_line(670, 455, 1120, 455)
          canvas.create_line(670, 480, 1120, 480)

          canvas.create_text(250, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          canvas.create_text(900, 320, text="1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1089, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1089, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
          canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))

          canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

          canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
          canvas.create_line(110, 600, 1120, 600)
          canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
          canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
          canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))


#------------Simplified 2 (logo on right side)-------------

      elif menuvar == 'Simplified 2 (logo on right side)':
          frame = Frame(seventhtab, width=1200, height=155)
          frame.pack(expand=True, fill=BOTH)
          frame.place(x=2,y=309)
          canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

          vertibar=Scrollbar(frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=canvas.yview)
          canvas.config(width=1200,height=155)

          canvas.config(yscrollcommand=vertibar.set)
          canvas.pack(expand=True,side=LEFT,fill=BOTH)
          canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
          canvas.create_text(600, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
          try:
            adv_image = Image.open("images/"+advdata1[13])
            adv_resize_image = adv_image.resize((200,75))
            adv_image = ImageTk.PhotoImage(adv_resize_image)

            adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
            adv_window_image = canvas.create_window(850, 25, anchor="nw", window=adv_btlogo)
            adv_btlogo.photo = adv_image
          except:
            pass  

          # canvas.create_text(1000, 70, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

          canvas.create_text(829, 120, text="Invoice#", fill="black", font=('Helvetica 11'))
          canvas.create_text(841, 140, text="Invoice date", fill="black", font=('Helvetica 11'))
          canvas.create_text(830, 160, text="Due date", fill="black", font=('Helvetica 11'))
          canvas.create_text(820, 180, text="Terms", fill="black", font=('Helvetica 11'))
          canvas.create_text(834, 200, text="Order ref.#", fill="black", font=('Helvetica 11'))
          canvas.create_text(1047, 120, text="INV1/2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(1050, 140, text="06-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(1050, 160, text="21-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(1040, 180, text="NET 15", fill="black", font=('Helvetica 11'))

          canvas.create_text(170, 65, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
          # canvas.create_text(130, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
          T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
          T_address.tag_configure('tag_name',justify='right')
          T_address.insert('1.0', advdata[2])
          T_address.tag_add('tag_name','1.0', 'end')
          T_address_window = canvas.create_window(10, 80, anchor="nw", window=T_address)
          canvas.create_text(130, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
          # canvas.create_text(130, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
          # canvas.create_text(130, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
          # canvas.create_text(136, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
          # canvas.create_text(136, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
          canvas.create_text(124, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))

          canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
          canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
          canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
          canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

          s = ttk.Style()
          s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')

          tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_2.Treeview')
              
          tree.column("# 1", anchor=E, stretch=NO, width=700)
          tree.heading("# 1", text="Product/Service - Description")
          tree.column("# 2", anchor=E, stretch=NO, width=150)
          tree.heading("# 2", text="Quantity")
          tree.column("# 3", anchor=E, stretch=NO, width=150)
          tree.heading("# 3", text="Price")
        
          window = canvas.create_window(120, 290, anchor="nw", window=tree)

          canvas.create_line(120, 330, 1120, 330 )
          canvas.create_line(120, 290, 120, 330 )
          canvas.create_line(820, 290, 820, 330 )
          canvas.create_line(970, 290, 970, 330 )
          canvas.create_line(1120, 290, 1120, 330 )
          canvas.create_line(670, 330, 670, 480)
          canvas.create_line(970, 330, 970, 480)
          canvas.create_line(1120, 330, 1120, 480)
          canvas.create_line(670, 355, 1120, 355)
          canvas.create_line(670, 380, 1120, 380)
          canvas.create_line(670, 405, 1120, 405)
          canvas.create_line(670, 430, 1120, 430)
          canvas.create_line(670, 455, 1120, 455)
          canvas.create_line(670, 480, 1120, 480)

          canvas.create_text(250, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          canvas.create_text(900, 320, text="1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1089, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

          canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1089, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
          canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1084, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))

          canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

          canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
          canvas.create_line(110, 600, 1120, 600)
          canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
          canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
          canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))

  #------------Business Classic------------- 

      elif menuvar == 'Business Classic':
          frame = Frame(seventhtab, width=1200, height=155)
          frame.pack(expand=True, fill=BOTH)
          frame.place(x=2,y=309)
          canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

          vertibar=Scrollbar(frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=canvas.yview)
          canvas.config(width=1200,height=155)

          canvas.config(yscrollcommand=vertibar.set)
          canvas.pack(expand=True,side=LEFT,fill=BOTH)
          canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
          canvas.create_text(600, 45, text="Title text goes here...", fill="black", font=('Helvetica 10'))
          canvas.create_line(100, 60, 1120, 60, fill="orange")
          #canvas.create_line(1000, 60, 600, 60, fill="grey")

          try:
            adv_image = Image.open("images/"+advdata1[13])
            adv_resize_image = adv_image.resize((200,100))
            adv_image = ImageTk.PhotoImage(adv_resize_image)

            adv_btlogo = Label(canvas,width=200,height=100,image = adv_image) 
            adv_window_image = canvas.create_window(140, 100, anchor="nw", window=adv_btlogo)
            adv_btlogo.photo = adv_image
          except:
            pass  


          # canvas.create_text(250, 155, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

          canvas.create_text(560, 85, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
          # canvas.create_text(535, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
          T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
          T_address.tag_configure('tag_name',justify='right')
          T_address.insert('1.0', advdata[2])
          T_address.tag_add('tag_name','1.0', 'end')
          T_address_window = canvas.create_window(350, 100, anchor="nw", window=T_address)
          # adv_btlabel = Label(canvas,width=20,height=10,text=""+caddent.get('1.0', 'end-1c')) 
          # adv_window_label = canvas.create_window(530, 110, anchor="nw", window=adv_btlabel)
          canvas.create_text(530, 190, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
          # canvas.create_text(530, 140, text="Address line 3", fill="black", font=('Helvetica 10'))
          # canvas.create_text(530, 155, text="Address line 4", fill="black", font=('Helvetica 10'))
          # canvas.create_text(536, 170, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
          # canvas.create_text(536, 190, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
          canvas.create_text(524, 210, text="Invoice", fill="black", font=('Helvetica 14 bold'))

          canvas.create_text(749, 95, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas.create_text(791, 110, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(800, 125, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(760, 140, text="United States", fill="black", font=('Helvetica 10'))

          canvas.create_text(745, 160, text="Invoice", fill="black", font=('Helvetica 11'))
          canvas.create_text(760, 180, text="Invoice date", fill="black", font=('Helvetica 11'))
          canvas.create_text(750, 200, text="Due date", fill="black", font=('Helvetica 11'))

          canvas.create_text(947, 160, text="INV1/2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(950, 180, text="06-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(950, 200, text="21-05-2022", fill="black", font=('Helvetica 11'))
          s = ttk.Style()
          s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')

          tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')
        
          tree.column("# 1", anchor=E, stretch=NO, width=150)
          tree.heading("# 1", text="Product/Service")
          tree.column("# 2", anchor=E, stretch=NO, width=400)
          tree.heading("# 2", text="Description")
          tree.column("# 3", anchor=E, stretch=NO, width=150)
          tree.heading("# 3", text="Unit Price")
          tree.column("# 4", anchor=E, stretch=NO, width=150)
          tree.heading("# 4", text="Quantity")
          tree.column("# 5", anchor=E, stretch=NO, width=150)
          tree.heading("# 5", text="Price")
              
          window = canvas.create_window(120, 230, anchor="nw", window=tree)

          canvas.create_line(120, 270, 1120, 270 )
          canvas.create_line(120, 230, 120, 270 )
          canvas.create_line(270, 230, 270, 270 )
          canvas.create_line(670, 230, 670, 270 )
          canvas.create_line(820, 230, 820, 270 )
          canvas.create_line(970, 230, 970, 270 )
          canvas.create_line(1120, 230, 1120, 270)
          canvas.create_line(1120, 270, 1120, 420)
          canvas.create_line(670, 295, 1120, 295)
          canvas.create_line(670, 320, 1120, 320)
          canvas.create_line(670, 345, 1120, 345)
          canvas.create_line(670, 370, 1120, 370)
          canvas.create_line(670, 395, 1120, 395)
          canvas.create_line(670, 420, 1120, 420)

          canvas.create_text(165, 260, text="PROD-0001", fill="black", font=('Helvetica 10'))
          canvas.create_text(400, 260, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(734, 260, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(734, 260, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(734, 260, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(734, 260, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(734, 260, text="$200.00", fill="black", font=('Helvetica 10'))
          canvas.create_text(890, 260, text="1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 260, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 260, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 260, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 260, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          # canvas.create_text(1080, 260, text="$200.00", fill="black", font=('Helvetica 10'))

          canvas.create_text(697, 285, text="Subtotal", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 285, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 285, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 285, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 285, text="$200.00", fill="black", font=('Helvetica 10'))

          canvas.create_text(692, 310, text="TAX1", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 310, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 310, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 310, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 310, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1085, 310, text="$18.00", fill="black", font=('Helvetica 10'))

          canvas.create_text(737, 335, text="Shipping and handling", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1085, 335, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1085, 335, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1085, 335, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1085, 335, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1085, 335, text="$20.00", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 360, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 360, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 360, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 360, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 360, text="$238.00", fill="black", font=('Helvetica 10 bold'))
          canvas.create_text(715, 360, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 385, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 385, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 385, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 385, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 385, text="100.00", fill="black", font=('Helvetica 10'))
          canvas.create_text(705, 385, text="Total Paid", fill="black", font=('Helvetica 10'))
          if comcursignpla.get() == "before amount":
            canvas.create_text(1080, 410, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount":
            canvas.create_text(1080, 410, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "before amount with space":
            canvas.create_text(1080, 410, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
          elif comcursignpla.get() == "after amount with space":
            canvas.create_text(1080, 410, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
          else:
            pass
          #canvas.create_text(1080, 410, text="$138.00", fill="black", font=('Helvetica 10'))
          canvas.create_text(700, 410, text="Balance", fill="black", font=('Helvetica 10'))

          canvas.create_line(100, 480, 1120, 480, fill="orange")
          canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
          canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

          canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
          canvas.create_line(100, 600, 1120, 600, fill="orange")
          canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
          canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
          canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
      else:
          pass

  adv_win_menu8 = StringVar()
  adv_winstyle8 = ttk.Combobox(seventhtab,textvariable=adv_win_menu8)
  adv_winstyle8.bind("<<ComboboxSelected>>", adv_maindropmenu)
  adv_winstyle8["values"] = ("Professional 1 (logo on left side)","Professional 2 (logo on right side)","Simplified 1 (logo on left side)","Simplified 2 (logo on right side)","Business Classic")
  if not advdata:
    adv_winstyle8.current(0)
    frame = Frame(seventhtab, width=1200, height=155)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=2,y=309)
    canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1200,height=155)

    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')

    canvas.create_text(600, 45, text="Title text goes here...", fill="black", font=('Helvetica 10'))

    canvas.create_text(250, 70, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

    canvas.create_text(130, 120, text="Invoice#", fill="black", font=('Helvetica 11'))
    canvas.create_text(141, 140, text="Invoice date", fill="black", font=('Helvetica 11'))
    canvas.create_text(130, 160, text="Due date", fill="black", font=('Helvetica 11'))
    canvas.create_text(120, 180, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(134, 200, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(347, 120, text="INV1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 140, text="03-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 160, text="18-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(340, 180, text="NET 15", fill="black", font=('Helvetica 11'))

    canvas.create_text(1050, 65, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(1080, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
    # T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    # T_address.tag_configure('tag_name',justify='right')
    # T_address.insert('1.0', advdata[2])
    # T_address.tag_add('tag_name','1.0', 'end')
    # T_address_window = canvas.create_window(850, 80, anchor="nw", window=T_address)
    canvas.create_text(1050, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
    # canvas.create_text(1085, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
    # canvas.create_text(1085, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
    # canvas.create_text(1080, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
    # canvas.create_text(1080, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
    canvas.create_text(1050, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))
    canvas.create_text(1050, 210, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))

    canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

    s = ttk.Style()
    s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')
        
    tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')
      
    tree.column("# 1", anchor=E, stretch=NO, width=150)
    tree.heading("# 1", text="ID/SKU")
    tree.column("# 2", anchor=E, stretch=NO, width=400)
    tree.heading("# 2", text="Product/Service - Description")
    tree.column("# 3", anchor=E, stretch=NO, width=150)
    tree.heading("# 3", text="Quantity")
    tree.column("# 4", anchor=E, stretch=NO, width=150)
    tree.heading("# 4", text="Unit Price")
    tree.column("# 5", anchor=E, stretch=NO, width=150)
    tree.heading("# 5", text="Price")
      
    window = canvas.create_window(120, 290, anchor="nw", window=tree)

    canvas.create_line(120, 330, 1120, 330 )
    canvas.create_line(120, 290, 120, 330 )
    canvas.create_line(270, 290, 270, 330 )
    canvas.create_line(670, 290, 670, 330 )
    canvas.create_line(820, 290, 820, 330 )
    canvas.create_line(970, 290, 970, 330 )
    canvas.create_line(1120, 290, 1120, 330 )
    canvas.create_line(670, 330, 670, 480)
    canvas.create_line(970, 330, 970, 480)
    canvas.create_line(1120, 330, 1120, 480)
    canvas.create_line(670, 355, 1120, 355)
    canvas.create_line(670, 380, 1120, 380)
    canvas.create_line(670, 405, 1120, 405)
    canvas.create_line(670, 430, 1120, 430)
    canvas.create_line(670, 455, 1120, 455)
    canvas.create_line(670, 480, 1120, 480)

    canvas.create_text(165, 320, text="PROD-0001", fill="black", font=('Helvetica 10'))
    canvas.create_text(400, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(740, 320, text="1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(884, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(884, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(884, 320, text="$200.00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 320, text="$200.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 345, text="$200.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1085, 370, text="$18.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1085, 395, text="$20.00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 420, text="$238.00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 445, text="$100.00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 465, text="$138.00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))


    canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

    canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(110, 600, 1120, 600)
    canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
    canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  elif advdata[32] == 'Professional 1 (logo on left side)':
    adv_winstyle8.insert(0, advdata[40])
    frame = Frame(seventhtab, width=1200, height=155)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=2,y=309)
    canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1200,height=155)

    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')

    canvas.create_text(600, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))

    try:
      adv_image = Image.open("images/"+advdata[13])
      adv_resize_image = adv_image.resize((200,75))
      adv_image = ImageTk.PhotoImage(adv_resize_image)

      adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
      adv_window_image = canvas.create_window(150, 30, anchor="nw", window=adv_btlogo)
      adv_btlogo.photo = adv_image
    except:
      pass  

    canvas.create_text(130, 120, text="Invoice#", fill="black", font=('Helvetica 11'))
    canvas.create_text(141, 140, text="Invoice date", fill="black", font=('Helvetica 11'))
    canvas.create_text(130, 160, text="Due date", fill="black", font=('Helvetica 11'))
    canvas.create_text(120, 180, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(134, 200, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(347, 120, text="INV1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 140, text="03-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 160, text="18-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(340, 180, text="NET 15", fill="black", font=('Helvetica 11'))

    canvas.create_text(1050, 65, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(1080, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
    T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', advdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(850, 80, anchor="nw", window=T_address)
        
    canvas.create_text(1050, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
    # canvas.create_text(1085, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
    # canvas.create_text(1085, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
    # canvas.create_text(1080, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
    # canvas.create_text(1080, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
    canvas.create_text(1050, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))
    canvas.create_text(1050, 210, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))

    canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

    s = ttk.Style()
    s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')
        
    tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')
      
    tree.column("# 1", anchor=E, stretch=NO, width=150)
    tree.heading("# 1", text="ID/SKU")
    tree.column("# 2", anchor=E, stretch=NO, width=400)
    tree.heading("# 2", text="Product/Service - Description")
    tree.column("# 3", anchor=E, stretch=NO, width=150)
    tree.heading("# 3", text="Quantity")
    tree.column("# 4", anchor=E, stretch=NO, width=150)
    tree.heading("# 4", text="Unit Price")
    tree.column("# 5", anchor=E, stretch=NO, width=150)
    tree.heading("# 5", text="Price")
      
    window = canvas.create_window(120, 290, anchor="nw", window=tree)

    canvas.create_line(120, 330, 1120, 330 )
    canvas.create_line(120, 290, 120, 330 )
    canvas.create_line(270, 290, 270, 330 )
    canvas.create_line(670, 290, 670, 330 )
    canvas.create_line(820, 290, 820, 330 )
    canvas.create_line(970, 290, 970, 330 )
    canvas.create_line(1120, 290, 1120, 330 )
    canvas.create_line(670, 330, 670, 480)
    canvas.create_line(970, 330, 970, 480)
    canvas.create_line(1120, 330, 1120, 480)
    canvas.create_line(670, 355, 1120, 355)
    canvas.create_line(670, 380, 1120, 380)
    canvas.create_line(670, 405, 1120, 405)
    canvas.create_line(670, 430, 1120, 430)
    canvas.create_line(670, 455, 1120, 455)
    canvas.create_line(670, 480, 1120, 480)

    canvas.create_text(165, 320, text="PROD-0001", fill="black", font=('Helvetica 10'))
    canvas.create_text(400, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(740, 320, text="1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(884, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(884, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(884, 320, text="$200.00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 320, text="$200.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 345, text="$200.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1085, 370, text="$18.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1085, 395, text="$20.00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 420, text="$238.00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 445, text="$100.00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 465, text="$138.00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))


    canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

    canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(110, 600, 1120, 600)
    canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
    canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  elif advdata[32] == 'Professional 2 (logo on right side)':
    adv_winstyle8.insert(0, advdata[40])
    frame = Frame(seventhtab, width=1200, height=155)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=2,y=309)
    canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1200,height=155)

    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
    canvas.create_text(600, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    try:
      adv_image = Image.open("images/"+advdata[13])
      adv_resize_image = adv_image.resize((200,75))
      adv_image = ImageTk.PhotoImage(adv_resize_image)

      adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
      adv_window_image = canvas.create_window(850, 25, anchor="nw", window=adv_btlogo)
      adv_btlogo.photo = adv_image
    except:
      pass  
    #canvas.create_text(1000, 70, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

    canvas.create_text(829, 110, text="Invoice#", fill="black", font=('Helvetica 11'))
    canvas.create_text(841, 130, text="Invoice date", fill="black", font=('Helvetica 11'))
    canvas.create_text(830, 150, text="Due date", fill="black", font=('Helvetica 11'))
    canvas.create_text(820, 170, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(834, 190, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(1047, 110, text="INV1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(1050, 130, text="06-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(1050, 150, text="21-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(1040, 170, text="NET 15", fill="black", font=('Helvetica 11'))

    canvas.create_text(170, 65, text=""+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(130, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
    T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', advdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(10, 80, anchor="nw", window=T_address)
    canvas.create_text(125, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
    # canvas.create_text(130, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
    # canvas.create_text(130, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
    # canvas.create_text(136, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
    # canvas.create_text(136, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
    canvas.create_text(124, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))

    canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))
    
    s = ttk.Style()
    s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')
      
    tree.column("# 1", anchor=E, stretch=NO, width=150)
    tree.heading("# 1", text="ID/SKU")
    tree.column("# 2", anchor=E, stretch=NO, width=400)
    tree.heading("# 2", text="Product/Service - Description")
    tree.column("# 3", anchor=E, stretch=NO, width=150)
    tree.heading("# 3", text="Quantity")
    tree.column("# 4", anchor=E, stretch=NO, width=150)
    tree.heading("# 4", text="Unit Price")
    tree.column("# 5", anchor=E, stretch=NO, width=150)
    tree.heading("# 5", text="Price")
      
    window = canvas.create_window(120, 290, anchor="nw", window=tree)

    canvas.create_line(120, 330, 1120, 330 )
    canvas.create_line(120, 290, 120, 330 )
    canvas.create_line(270, 290, 270, 330 )
    canvas.create_line(670, 290, 670, 330 )
    canvas.create_line(820, 290, 820, 330 )
    canvas.create_line(970, 290, 970, 330 )
    canvas.create_line(1120, 290, 1120, 330 )
    canvas.create_line(670, 330, 670, 480)
    canvas.create_line(970, 330, 970, 480)
    canvas.create_line(1120, 330, 1120, 480)
    canvas.create_line(670, 355, 1120, 355)
    canvas.create_line(670, 380, 1120, 380)
    canvas.create_line(670, 405, 1120, 405)
    canvas.create_line(670, 430, 1120, 430)
    canvas.create_line(670, 455, 1120, 455)
    canvas.create_line(670, 480, 1120, 480)

    canvas.create_text(165, 320, text="PROD-0001", fill="black", font=('Helvetica 10'))
    canvas.create_text(400, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(740, 320, text="1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(884, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(884, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 320, text="$200.00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 320, text="$200.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 345, text="$200.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1089, 370, text="$18.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1089, 395, text="$20.00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 420, text="$238.00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 445, text="$100.00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 465, text="$138.00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

    canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(110, 600, 1120, 600)
    canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
    canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))


  elif advdata[32] == 'Simplified 1 (logo on left side)':
    adv_winstyle8.insert(0, advdata[40])
    frame = Frame(seventhtab, width=1200, height=155)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=2,y=309)
    canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1200,height=155)

    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
    canvas.create_text(600, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    try:
      adv_image = Image.open("images/"+advdata[13])
      adv_resize_image = adv_image.resize((200,75))
      adv_image = ImageTk.PhotoImage(adv_resize_image)

      adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
      adv_window_image = canvas.create_window(150, 25, anchor="nw", window=adv_btlogo)
      adv_btlogo.photo = adv_image
    except:
      pass  
    #canvas.create_text(250, 70, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

    canvas.create_text(130, 120, text="Invoice#", fill="black", font=('Helvetica 11'))
    canvas.create_text(141, 140, text="Invoice date", fill="black", font=('Helvetica 11'))
    canvas.create_text(130, 160, text="Due date", fill="black", font=('Helvetica 11'))
    canvas.create_text(120, 180, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(134, 200, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(347, 120, text="INV1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 140, text="06-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(350, 160, text="21-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(340, 180, text="NET 15", fill="black", font=('Helvetica 11'))

    canvas.create_text(1050, 65, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(1080, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
    T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', advdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(850, 80, anchor="nw", window=T_address)
    canvas.create_text(1050, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
    # canvas.create_text(1085, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
    # canvas.create_text(1085, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
    # canvas.create_text(1080, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
    # canvas.create_text(1080, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
    canvas.create_text(1050, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))

    canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

    s = ttk.Style()
    s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_2.Treeview')
      
    tree.column("# 1", anchor=E, stretch=NO, width=700)
    tree.heading("# 1", text="Product/Service - Description")
    tree.column("# 2", anchor=E, stretch=NO, width=150)
    tree.heading("# 2", text="Quantity")
    tree.column("# 3", anchor=E, stretch=NO, width=150)
    tree.heading("# 3", text="Price")
      
    window = canvas.create_window(120, 290, anchor="nw", window=tree)

    canvas.create_line(120, 330, 1120, 330 )
    canvas.create_line(120, 290, 120, 330 )
    canvas.create_line(820, 290, 820, 330 )
    canvas.create_line(970, 290, 970, 330 )
    canvas.create_line(1120, 290, 1120, 330 )
    canvas.create_line(670, 330, 670, 480)
    canvas.create_line(970, 330, 970, 480)
    canvas.create_line(1120, 330, 1120, 480)
    canvas.create_line(670, 355, 1120, 355)
    canvas.create_line(670, 380, 1120, 380)
    canvas.create_line(670, 405, 1120, 405)
    canvas.create_line(670, 430, 1120, 430)
    canvas.create_line(670, 455, 1120, 455)
    canvas.create_line(670, 480, 1120, 480)

    canvas.create_text(250, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(900, 320, text="1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1089, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1089, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

    canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(110, 600, 1120, 600)
    canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
    canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  elif advdata[32] == 'Simplified 2 (logo on right side)':
    adv_winstyle8.insert(0, advdata[40])
    frame = Frame(seventhtab, width=1200, height=155)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=2,y=309)
    canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1200,height=155)

    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
    canvas.create_text(600, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    try:
      adv_image = Image.open("images/"+advdata[13])
      adv_resize_image = adv_image.resize((200,75))
      adv_image = ImageTk.PhotoImage(adv_resize_image)

      adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
      adv_window_image = canvas.create_window(850, 25, anchor="nw", window=adv_btlogo)
      adv_btlogo.photo = adv_image
    except:
      pass  

    # canvas.create_text(1000, 70, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

    canvas.create_text(829, 120, text="Invoice#", fill="black", font=('Helvetica 11'))
    canvas.create_text(841, 140, text="Invoice date", fill="black", font=('Helvetica 11'))
    canvas.create_text(830, 160, text="Due date", fill="black", font=('Helvetica 11'))
    canvas.create_text(820, 180, text="Terms", fill="black", font=('Helvetica 11'))
    canvas.create_text(834, 200, text="Order ref.#", fill="black", font=('Helvetica 11'))
    canvas.create_text(1047, 120, text="INV1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(1050, 140, text="06-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(1050, 160, text="21-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(1040, 180, text="NET 15", fill="black", font=('Helvetica 11'))

    canvas.create_text(170, 55, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(135, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
    T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', advdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(10, 80, anchor="nw", window=T_address)
    canvas.create_text(130, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
    # canvas.create_text(130, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
    # canvas.create_text(130, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
    # canvas.create_text(136, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
    # canvas.create_text(136, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
    canvas.create_text(124, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))

    canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
    canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
    canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

    s = ttk.Style()
    s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_2.Treeview')
        
    tree.column("# 1", anchor=E, stretch=NO, width=700)
    tree.heading("# 1", text="Product/Service - Description")
    tree.column("# 2", anchor=E, stretch=NO, width=150)
    tree.heading("# 2", text="Quantity")
    tree.column("# 3", anchor=E, stretch=NO, width=150)
    tree.heading("# 3", text="Price")
        
    window = canvas.create_window(120, 290, anchor="nw", window=tree)

    canvas.create_line(120, 330, 1120, 330 )
    canvas.create_line(120, 290, 120, 330 )
    canvas.create_line(820, 290, 820, 330 )
    canvas.create_line(970, 290, 970, 330 )
    canvas.create_line(1120, 290, 1120, 330 )
    canvas.create_line(670, 330, 670, 480)
    canvas.create_line(970, 330, 970, 480)
    canvas.create_line(1120, 330, 1120, 480)
    canvas.create_line(670, 355, 1120, 355)
    canvas.create_line(670, 380, 1120, 380)
    canvas.create_line(670, 405, 1120, 405)
    canvas.create_line(670, 430, 1120, 430)
    canvas.create_line(670, 455, 1120, 455)
    canvas.create_line(670, 480, 1120, 480)

    canvas.create_text(250, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    canvas.create_text(900, 320, text="1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1089, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

    canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1089, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1084, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

    canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(110, 600, 1120, 600)
    canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
    canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  elif advdata[32] == 'Business Classic':
    adv_winstyle8.insert(0, advdata[40])
    frame = Frame(seventhtab, width=1200, height=155)
    frame.pack(expand=True, fill=BOTH)
    frame.place(x=2,y=309)
    canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

    vertibar=Scrollbar(frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1200,height=155)

    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
    canvas.create_text(600, 45, text="Title text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_line(100, 60, 1120, 60, fill="orange")
    #canvas.create_line(1000, 60, 600, 60, fill="grey")

    try:
      adv_image = Image.open("images/"+advdata[13])
      adv_resize_image = adv_image.resize((200,100))
      adv_image = ImageTk.PhotoImage(adv_resize_image)

      adv_btlogo = Label(canvas,width=200,height=100,image = adv_image) 
      adv_window_image = canvas.create_window(140, 100, anchor="nw", window=adv_btlogo)
      adv_btlogo.photo = adv_image
    except:
      pass  


    # canvas.create_text(250, 155, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

    canvas.create_text(560, 85, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
    # canvas.create_text(535, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
    T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
    T_address.tag_configure('tag_name',justify='right')
    T_address.insert('1.0', advdata[2])
    T_address.tag_add('tag_name','1.0', 'end')
    T_address_window = canvas.create_window(350, 100, anchor="nw", window=T_address)
    # adv_btlabel = Label(canvas,width=20,height=10,text=""+caddent.get('1.0', 'end-1c')) 
    # adv_window_label = canvas.create_window(530, 110, anchor="nw", window=adv_btlabel)
    canvas.create_text(530, 190, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
    # canvas.create_text(530, 140, text="Address line 3", fill="black", font=('Helvetica 10'))
    # canvas.create_text(530, 155, text="Address line 4", fill="black", font=('Helvetica 10'))
    # canvas.create_text(536, 170, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
    # canvas.create_text(536, 190, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
    canvas.create_text(524, 210, text="Invoice", fill="black", font=('Helvetica 14 bold'))

    canvas.create_text(749, 95, text="John Doe", fill="black", font=('Helvetica 10 '))
    canvas.create_text(791, 110, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
    canvas.create_text(800, 125, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
    canvas.create_text(760, 140, text="United States", fill="black", font=('Helvetica 10'))

    canvas.create_text(745, 160, text="Invoice", fill="black", font=('Helvetica 11'))
    canvas.create_text(760, 180, text="Invoice date", fill="black", font=('Helvetica 11'))
    canvas.create_text(750, 200, text="Due date", fill="black", font=('Helvetica 11'))

    canvas.create_text(947, 160, text="INV1/2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(950, 180, text="06-05-2022", fill="black", font=('Helvetica 11'))
    canvas.create_text(950, 200, text="21-05-2022", fill="black", font=('Helvetica 11'))
    s = ttk.Style()
    s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')

    tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')
        
    tree.column("# 1", anchor=E, stretch=NO, width=150)
    tree.heading("# 1", text="Product/Service")
    tree.column("# 2", anchor=E, stretch=NO, width=400)
    tree.heading("# 2", text="Description")
    tree.column("# 3", anchor=E, stretch=NO, width=150)
    tree.heading("# 3", text="Unit Price")
    tree.column("# 4", anchor=E, stretch=NO, width=150)
    tree.heading("# 4", text="Quantity")
    tree.column("# 5", anchor=E, stretch=NO, width=150)
    tree.heading("# 5", text="Price")
        
    window = canvas.create_window(120, 230, anchor="nw", window=tree)

    canvas.create_line(120, 270, 1120, 270 )
    canvas.create_line(120, 230, 120, 270 )
    canvas.create_line(270, 230, 270, 270 )
    canvas.create_line(670, 230, 670, 270 )
    canvas.create_line(820, 230, 820, 270 )
    canvas.create_line(970, 230, 970, 270 )
    canvas.create_line(1120, 230, 1120, 270)
    canvas.create_line(1120, 270, 1120, 420)
    canvas.create_line(670, 295, 1120, 295)
    canvas.create_line(670, 320, 1120, 320)
    canvas.create_line(670, 345, 1120, 345)
    canvas.create_line(670, 370, 1120, 370)
    canvas.create_line(670, 395, 1120, 395)
    canvas.create_line(670, 420, 1120, 420)

    canvas.create_text(165, 260, text="PROD-0001", fill="black", font=('Helvetica 10'))
    canvas.create_text(400, 260, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(734, 260, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(734, 260, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(734, 260, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(734, 260, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(734, 260, text="$200.00", fill="black", font=('Helvetica 10'))
    canvas.create_text(890, 260, text="1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 260, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 260, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 260, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 260, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    # canvas.create_text(1080, 260, text="$200.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(697, 285, text="Subtotal", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 285, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 285, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 285, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 285, text="$200.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(692, 310, text="TAX1", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 310, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 310, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 310, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 310, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1085, 310, text="$18.00", fill="black", font=('Helvetica 10'))

    canvas.create_text(737, 335, text="Shipping and handling", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1085, 335, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1085, 335, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1085, 335, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1085, 335, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1085, 335, text="$20.00", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 360, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 360, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 360, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 360, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 360, text="$238.00", fill="black", font=('Helvetica 10 bold'))
    canvas.create_text(715, 360, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 385, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 385, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 385, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 385, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 385, text="100.00", fill="black", font=('Helvetica 10'))
    canvas.create_text(705, 385, text="Total Paid", fill="black", font=('Helvetica 10'))
    if comcursignpla.get() == "before amount":
      canvas.create_text(1080, 410, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount":
      canvas.create_text(1080, 410, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "before amount with space":
      canvas.create_text(1080, 410, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
    elif comcursignpla.get() == "after amount with space":
     canvas.create_text(1080, 410, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
    else:
      pass
    #canvas.create_text(1080, 410, text="$138.00", fill="black", font=('Helvetica 10'))
    canvas.create_text(700, 410, text="Balance", fill="black", font=('Helvetica 10'))

    canvas.create_line(100, 480, 1120, 480, fill="orange")
    canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
    canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

    canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
    canvas.create_line(100, 600, 1120, 600, fill="orange")
    canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
    canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
    canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
  else:
    pass
  adv_winstyle8.place(x=2 ,y=270, width=220)
  #adv_winstyle8.current(0)

  


root.mainloop()

