from tkinter import*
from PIL import Image
from PIL import ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


class PharmacyManagementSystem:
    def __init__(self, root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")




        #===============addMed variable=========================
        
        self.addmed_var=StringVar()
        self.refMed_var=StringVar() 

        #====================main variable================

        self.ref_var=StringVar()
        self.cmpName_var=StringVar()
        self.typeMed_var=StringVar()
        self.medName_var=StringVar()
        self.lot_var=StringVar()
        self.issuedate_var=StringVar()
        self.expdate_var=StringVar()
        self.uses_var=StringVar()
        self.sideEffect_var=StringVar()
        self.warning_var=StringVar()
        self.dosage_var=StringVar() 
        self.price_var=StringVar()
        self.product_var=StringVar()
        

        lbltitle=Label(self.root,text="PHARMACY MANAGEMENT SYSTEM", bd=15, relief=RIDGE,
                           bg='white',fg="darkgreen",font=("times new roman", 40, "bold"), padx=2, pady=4)
        lbltitle.pack(side=TOP, fill=X)
        
        
        img1=Image.open(r"C:\Users\Admin\Documents\projecct\img\logo.webp")
        img1=img1.resize((90, 70), Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root, image=self.photoimg1, borderwidth=0)
        b1.place(x=50, y=15)

        #================DataFrame================================================
        DataFrame=Frame(self.root, bd=15,relief=RIDGE, padx=20)
        DataFrame.place(x=0, y=90, width=1365, height=390)

        DataFrameLeft=LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=20, text="Medicine Information", 
                                 fg="darkgreen",font=("arial", 12, "bold"))
        DataFrameLeft.place(x=0, y=5, width=800, height=350)
        
        DataFrameright=LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=20, text="Medicine Add Department", 
                                 fg="darkgreen",font=("arial", 12, "bold"))
        DataFrameright.place(x=805, y=5, width=500, height=350)

        #=================buttonsFrame=============================================

        ButtonFrame=Frame(self.root, bd=10,relief=RIDGE, padx=20)
        ButtonFrame.place(x=0, y=470, width=1365, height=60)


        #=========================Main Button=========================
        btnAddData=Button(ButtonFrame,command=self.add_data, text="Medicine Add",bg="darkgreen",fg="white",
                          font=("arial", 12, "bold"))
        btnAddData.grid(row=0, column=0)

        btnUpdateMed=Button(ButtonFrame,command=self.Update, text="UPDATE",bg="darkgreen",fg="white",
                          font=("arial", 13, "bold"), width=10)
        btnUpdateMed.grid(row=0, column=1)

        btnDeleteMed=Button(ButtonFrame,command=self.delete, text="DELETE",bg="red",fg="white",
                          font=("arial", 13, "bold"),width=10)
        btnDeleteMed.grid(row=0, column=2)

        btnRestMed=Button(ButtonFrame, command=self.reset,text="RESET",bg="darkgreen",fg="white",
                          font=("arial", 13, "bold"), width=10)
        btnRestMed.grid(row=0, column=3)

        btnExitMed=Button(ButtonFrame, text="EXIT",bg="darkgreen",fg="white",
                          font=("arial", 13, "bold"), width=10)
        btnExitMed.grid(row=0, column=4)
        
        # ============Search By==================
        lblSearch=Label(ButtonFrame, font=("arial", 17,"bold"),text="Search By", padx=2, bg="red", fg="white")
        lblSearch.grid(row=0, column=5, sticky=W)

        #variable
        self.search_var=StringVar()
        search_combo=ttk.Combobox(ButtonFrame, textvariable=self.search_var, width=12, font=("arial", 17,"bold"), state="readonly")
        search_combo["values"]=("Ref", "Medname", "Lot")
        search_combo.grid(row=0, column=6)
        search_combo.current(0)

        self.searchTxt_var=StringVar()
        txtSearch=Entry(ButtonFrame,textvariable=self.searchTxt_var, bd=3, relief=RIDGE, width=12, font=("arial", 17,"bold"))
        txtSearch.grid(row=0, column=7)

        searchBtn=Button(ButtonFrame, command=self.search_data ,text="SEARCH",bg="darkgreen",fg="white",
                          font=("arial", 13, "bold"), width=13)
        searchBtn.grid(row=0, column=8)

        showAll=Button(ButtonFrame, command=self.fetch_data,text="SHOW ALL",bg="darkgreen",fg="white",
                          font=("arial", 13, "bold"), width=14)
        showAll.grid(row=0, column=9)

        #=====================================Label and entry=================================
        '''lblrefno=Label(DataFrameLeft, font=("arial", 12,"bold"),text="Reference No", padx=2, pady=6)
        lblrefno.grid(row=0, column=0, sticky=W)

        conn=mysql.connector.connect(host="localhost", username="root", password="root", database="data")
        my_cursor=conn.cursor()
        my_cursor.execute("select Ref from pharma")
        r=my_cursor.fetchall()

        ref_combo=ttk.Combobox(DataFrameLeft, textvariable=self.ref_var, width=27, font=("arial", 12,"bold"), state="readonly")
        ref_combo["values"]=r
        ref_combo.grid(row=0, column=1)
        ref_combo.current(0)
        

        lblCmpName=Label(DataFrameLeft, font=("arial", 12,"bold"),text="Company Name:", padx=2, pady=6)
        lblCmpName.grid(row=1, column=0, sticky=W)
        txtCmpName=Entry(DataFrameLeft,textvariable=self.cmpName_var, bd=2, relief=RIDGE, width=29, font=("arial", 13,"bold"))
        txtCmpName.grid(row=1, column=1)

        lblTypeofMedicine=Label(DataFrameLeft, font=("arial", 12,"bold"),text="Type of Medicine:", padx=2, pady=6)
        lblTypeofMedicine.grid(row=2, column=0, sticky=W)

        comTypeofMedicine=ttk.Combobox(DataFrameLeft,textvariable=self.typeMed_var, width=27, font=("arial", 12,"bold"), state="readonly")
        comTypeofMedicine["values"]=("Tablet", "Liquid", "Capsules", "Topical Medicines", "Drops", "Inhales", "Injection")
        comTypeofMedicine.grid(row=2, column=1)
        comTypeofMedicine.current(0)'''

        #====================Add Medicine===================

        lblMedicineName=Label(DataFrameLeft, font=("arial", 12,"bold"),text="Medicine Name:", padx=2, pady=6)
        lblMedicineName.grid(row=3, column=0, sticky=W)

        conn=mysql.connector.connect(host="localhost", username="root", password="root", database="data")
        my_cursor=conn.cursor()
        my_cursor.execute("select MedName from pharma1")
        med=my_cursor.fetchall()

        comMedicineName=ttk.Combobox(DataFrameLeft,textvariable=self.medName_var, width=27, font=("arial", 12,"bold"), state="readonly")
        comMedicineName["values"]=med
        comMedicineName.current(0)
        comMedicineName.grid(row=3, column=1)
        

        lblLotNo=Label(DataFrameLeft, font=("arial", 12,"bold"),text="Lot No:", padx=2, pady=6)
        lblLotNo.grid(row=4, column=0, sticky=W)
        txtLotNo=Entry(DataFrameLeft,textvariable=self.lot_var, bd=2, relief=RIDGE, width=29, font=("arial", 13,"bold"), bg="white")
        txtLotNo.grid(row=4, column=1)

        lblIssueDate=Label(DataFrameLeft, font=("arial", 12,"bold"),text="Issue Date:", padx=2, pady=6)
        lblIssueDate.grid(row=5, column=0, sticky=W)
        txtIssueDate=Entry(DataFrameLeft,textvariable=self.issuedate_var, bd=2, relief=RIDGE, width=29, font=("arial", 13,"bold"), bg="white")
        txtIssueDate.grid(row=5, column=1)

        lblExDate=Label(DataFrameLeft, font=("arial", 12,"bold"),text="Exp Date:", padx=2, pady=6)
        lblExDate.grid(row=6, column=0, sticky=W)
        txtExDate=Entry(DataFrameLeft,textvariable=self.expdate_var, bd=2, relief=RIDGE, width=29, font=("arial", 13,"bold"), bg="white")
        txtExDate.grid(row=6, column=1)

        lblUses=Label(DataFrameLeft, font=("arial", 12,"bold"),text="Uses:", padx=2, pady=6)
        lblUses.grid(row=7, column=0, sticky=W)
        txtUses=Entry(DataFrameLeft,textvariable=self.uses_var, bd=2, relief=RIDGE, width=29, font=("arial", 13,"bold"), bg="white")
        txtUses.grid(row=7, column=1)

        lblSideEffect=Label(DataFrameLeft, font=("arial", 12,"bold"),text="Side Effects:", padx=2, pady=6)
        lblSideEffect.grid(row=8, column=0, sticky=W)
        txtSideEffect=Entry(DataFrameLeft,textvariable=self.sideEffect_var, bd=2, relief=RIDGE, width=29, font=("arial", 13,"bold"), bg="white")
        txtSideEffect.grid(row=8, column=1)

        lblPrecWarning=Label(DataFrameLeft, font=("arial", 12,"bold"),text="Prec&Warning:", padx=15)
        lblPrecWarning.grid(row=0, column=2, sticky=W)
        txtPrecWarning=Entry(DataFrameLeft, textvariable=self.warning_var, bd=2, relief=RIDGE, width=20, font=("arial", 12,"bold"), bg="white")
        txtPrecWarning.grid(row=0, column=3)

        lblDosage=Label(DataFrameLeft, font=("arial", 12,"bold"),text="Dossage:", padx=15, pady=6)
        lblDosage.grid(row=1, column=2, sticky=W)
        txtDosage=Entry(DataFrameLeft,textvariable=self.dosage_var, bd=2, relief=RIDGE, width=20, font=("arial", 12,"bold"), bg="white")
        txtDosage.grid(row=1, column=3)

        lblPrice=Label(DataFrameLeft, font=("arial", 12,"bold"),text="Medicine Price:", padx=15, pady=6)
        lblPrice.grid(row=2, column=2, sticky=W)
        txtPrice=Entry(DataFrameLeft, textvariable=self.price_var, bd=2, relief=RIDGE, width=20, font=("arial", 12,"bold"), bg="white")
        txtPrice.grid(row=2, column=3)

        lblProductQuantity=Label(DataFrameLeft, font=("arial", 12,"bold"),text="Product QTY:", padx=15, pady=6)
        lblProductQuantity.grid(row=3, column=2, sticky=W)
        txtProductQuantity=Entry(DataFrameLeft, textvariable=self.product_var, bd=2, relief=RIDGE, width=20, font=("arial", 12,"bold"), bg="white")
        txtProductQuantity.grid(row=3, column=3)


        #==========================images==========================================
        lblhome=Label(DataFrameLeft, font=("arial", 14,"bold"),text="Stay Home Stay Safe", 
                      padx=2, pady=6, bg="white", fg="red", width=30)
        lblhome.place(x=410 ,y=140)

        img2=Image.open(r"C:\Users\Admin\Documents\projecct\img\Arundhati-Medical-College-jpg.webp")
        img2=img2.resize((170, 135), Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(self.root, image=self.photoimg2, borderwidth=0)
        b1.place(x=475, y=300)

        img3=Image.open(r"C:\Users\Admin\Documents\projecct\img\download.jpg")
        img3=img3.resize((170, 135), Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        b1=Button(self.root, image=self.photoimg3, borderwidth=0)
        b1.place(x=650, y=300)

        #==========================dataframeRight=====================

        DataFrameright=LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=20, text="Medicine Add Department", 
                                 fg="darkgreen",font=("arial", 12, "bold"))
        DataFrameright.place(x=805, y=5, width=500, height=350)
        
        
        img4=Image.open(r"C:\Users\Admin\Documents\projecct\img\Tablets-1-1.jpg")
        img4=img4.resize((150, 75), Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(self.root, image=self.photoimg4, borderwidth=0)
        b1.place(x=850, y=130)

        img5=Image.open(r"C:\Users\Admin\Documents\projecct\img\syrup.jpg")
        img5=img5.resize((150, 75), Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(self.root, image=self.photoimg5, borderwidth=0)
        b1.place(x=1000, y=130)

        img6=Image.open(r"C:\Users\Admin\Documents\projecct\img\doc.jpg")
        img6=img6.resize((180, 140), Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b1=Button(self.root, image=self.photoimg6, borderwidth=0)
        b1.place(x=1150, y=130)

        lblrefno=Label(DataFrameright, font=("arial", 12,"bold"),text="Reference no:", padx=2, pady=6)
        lblrefno.place(x=0, y=80)
        txtrefno=Entry(DataFrameright, textvariable=self.refMed_var, bd=2, relief=RIDGE, width=15, font=("arial", 12,"bold"), bg="white")
        txtrefno.place(x=130, y=85)

        lblmedName=Label(DataFrameright, font=("arial", 12,"bold"),text="Medicine Name:", padx=2, pady=6)
        lblmedName.place(x=0, y=110)
        txtmedName=Entry(DataFrameright,textvariable=self.addmed_var, bd=2, relief=RIDGE, width=15, font=("arial", 12,"bold"), bg="white")
        txtmedName.place(x=130, y=115)


    #======================side frame==================================
        side_frame=Frame(DataFrameright, bd=4, relief=RIDGE, bg="white")
        side_frame.place(x=0, y=150, width=270, height=160)

        sc_x=ttk.Scrollbar(side_frame, orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM, fill=X)
        sc_y=ttk.Scrollbar(side_frame, orient=VERTICAL)
        sc_y.pack(side=RIGHT, fill=Y)

        self.medicine_table=ttk.Treeview(side_frame, column=("ref", "medname"), xscrollcommand=sc_x.set, yscrollcommand=sc_y.set) 
        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref", text="Ref")
        self.medicine_table.heading("medname", text="Medicine Name")

        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH, expand=1)

        self.medicine_table.column("ref", width=100)
        self.medicine_table.column("medname", width=100)

        self.medicine_table.bind("<ButtonRelease-1>", self.Medget_cursor)

        #=============================Medicine add Buttons=================================
        down_frame=Frame(DataFrameright, bd=4, relief=RIDGE, bg="darkgreen")
        down_frame.place(x=310, y=150, width=130, height=160)

        btnAddmed=Button(down_frame,command=self.AddMed, text="ADD",width=12,bg="white",fg="black",
                          font=("arial", 12, "bold"), pady=4)
        btnAddmed.grid(row=0, column=0)

        btnUpdatemed=Button(down_frame,command=self.UpdateMed, text="UPDATE",width=12,bg="purple",fg="white",
                          font=("arial", 12, "bold"), pady=4)
        btnUpdatemed.grid(row=1, column=0)

        btnDeletemed=Button(down_frame,command=self.DeleteMed, text="DELETE",width=12,bg="red",fg="white",
                          font=("arial", 12, "bold"), pady=4)
        btnDeletemed.grid(row=2, column=0)

        btnClearmed=Button(down_frame,command=self.ClearMed, text="CLEAR",width=12,bg="orange",fg="white",
                          font=("arial", 12, "bold"), pady=4)
        btnClearmed.grid(row=3, column=0)

        #=====================Frame Details==========================
        Framedetails=Frame(self.root,bd=10, relief=RIDGE)
        Framedetails.place(x=0, y=530, width=1362, height=170) 

        #====================Main Table & Scrollbar======================
        Table_frame=Frame(Framedetails,bd=6, relief=RIDGE, padx=20)
        Table_frame.place(x=0, y=1, width=1340, height=150) 


        scroll_x=ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y=ttk.Scrollbar(Table_frame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.pharamcy_table=ttk.Treeview(Table_frame, column=("ref", "companyname", "type", "tabletname", "lotno", "issuedate", 
                                                              "expdate", "uses", "sideeffect", "warning", "dosage", "price", "productqt")
                                                              ,xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_x.config(command=self.pharamcy_table.xview)
        scroll_y.config(command=self.pharamcy_table.yview)

        self.pharamcy_table["show"]="headings"

        self.pharamcy_table.heading("ref",text="Reference No")
        self.pharamcy_table.heading("companyname", text="Company Name")
        self.pharamcy_table.heading("type", text="Type of Medicine")
        self.pharamcy_table.heading("tabletname", text="Tablet Name")
        self.pharamcy_table.heading("lotno", text="Lot No")
        self.pharamcy_table.heading("issuedate", text="Issue Date")
        self.pharamcy_table.heading("expdate", text="EXP Date")
        self.pharamcy_table.heading("uses", text="Uses")
        self.pharamcy_table.heading("sideeffect", text="Side Effect")
        self.pharamcy_table.heading("warning", text="Prec&Warning")
        self.pharamcy_table.heading("dosage", text="Dosage")
        self.pharamcy_table.heading("price", text="Price")
        self.pharamcy_table.heading("productqt", text="Product QTY")
        self.pharamcy_table.pack(fill=BOTH, expand=1)

        self.pharamcy_table.column("ref", width=100)
        self.pharamcy_table.column("companyname", width=100)
        self.pharamcy_table.column("type", width=100)
        self.pharamcy_table.column("tabletname", width=100)
        self.pharamcy_table.column("lotno", width=100)
        self.pharamcy_table.column("issuedate", width=100)
        self.pharamcy_table.column("expdate", width=100)
        self.pharamcy_table.column("uses", width=100)
        self.pharamcy_table.column("sideeffect", width=100)
        self.pharamcy_table.column("warning", width=100)
        self.pharamcy_table.column("dosage", width=100)
        self.pharamcy_table.column("price", width=100)
        self.pharamcy_table.column("productqt", width=100)
        self.fetch_datMed()
        self.fetch_data()
        self.pharamcy_table.bind("<ButtonRelease-1>", self.get_cursor)



        #=============================Add Medicine Functionality Declaration=======================

    def AddMed (self):
        conn=mysql.connector.connect(host="localhost", username="root", password="root", database="data")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into pharma(Ref, MedName) values(%s, %s)",
                               (self.refMed_var.get(), self.addmed_var.get(),))
        messagebox.showinfo("Sucsess", "Medicine Added")
   
        conn.commit()
        self.fetch_datMed()
        self.Medget_cursor()
        conn.close()
        
    def fetch_datMed(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="root", database="data")
        my_cursor=conn.cursor()
        my_cursor.execute("select *from pharma1")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for i in rows:
                self.medicine_table.insert("", END, values=i)
            conn.commit()
        conn.close()
    #===============================MedGetCursor==========================
    def Medget_cursor(self, event=""):
        cursor_row=self.medicine_table.focus()
        content=self.medicine_table.item(cursor_row)
        row=content["values"]
        self.refMed_var.set(row[0])
        self.addmed_var.set(row[1])

    def UpdateMed(self):
        if self.refMed_var.get()=="" or self.addmed_var.get()=="":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="root", database="data")
            my_cursor=conn.cursor()
            my_cursor.execute("update pharma set MedName=%s where Ref=%s", (
                                                            self.addmed_var.get(),
                                                            self.refMed_var.get(),
                                                            ))
            conn.commit()
            self.fetch_datMed()
            conn.close()

            messagebox.showinfo("Sucess", "Medicine has been updated")
    
    def DeleteMed(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="root", database="data")
        my_cursor=conn.cursor()

        sql="delete from pharma where Ref=%s"
        val=(self.refMed_var.get(),)
        my_cursor.execute(sql, val)

        conn.commit()
        self.fetch_datMed()
        conn.close()
    
    def ClearMed(self):
        self.refMed_var.set("")
        self.addmed_var.set("")

    #==============================Main Table=====================
    
    def add_data(self):
        if self.ref_var.get()=="" or self.lot_var.get()=="":
            messagebox.showinfo("Error", "All feilds are required")
        else:
            messagebox.showinfo("Success", "data has been inserted")
            conn=mysql.connector.connect(host="localhost", username="root", password="root", database="data")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into pharmacy values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)",(
                                                                                    self.ref_var.get(),
                                                                                    self.cmpName_var.get(),
                                                                                    self.typeMed_var.get(),
                                                                                    self.medName_var.get(),
                                                                                    self.lot_var.get(),
                                                                                    self.issuedate_var.get(),
                                                                                    self.expdate_var.get(),
                                                                                    self.uses_var.get(),
                                                                                    self.sideEffect_var.get(),
                                                                                    self.warning_var.get(),
                                                                                    self.dosage_var.get(), 
                                                                                    self.price_var.get(),
                                                                                    self.product_var.get(),
                                                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "data has been inserted")

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="root", database="data")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharmacy")
        row=my_cursor.fetchall()
        if len(row)!=0:
            self.pharamcy_table.delete(*self.pharamcy_table.get_children())
            for i in row:
                self.pharamcy_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def get_cursor(self, event=""):
        cursor_row=self.pharamcy_table.focus()
        content=self.pharamcy_table.item(cursor_row)
        row=content["values"]
        self.ref_var.set(row[0])
        self.cmpName_var.set(row[1])
        self.typeMed_var.set(row[2])
        self.medName_var.set(row[3])
        self.lot_var.set(row[4])
        self.issuedate_var.set(row[5])
        self.expdate_var.set(row[6])
        self.uses_var.set(row[7])
        self.sideEffect_var.set(row[8])
        self.warning_var.set(row[9])
        self.dosage_var.set(row[10]) 
        self.price_var.set(row[11])
        self.product_var.set(row[12])

    
    
    
    
    
    def Update(self):
        if self.ref_var.get()=="" or self.lot_var.get()=="":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="root", database="data")
            my_cursor=conn.cursor()
            my_cursor.execute("update pharmacy set CmpName=%s, TypeMed=%s, Tabletname=%s, LotNo=%s, Issuedate=%s, Expdate=%s, Uses=%s, Sideffect=%s, warning=%s, dosage=%s, price=%s, product=%s  where Ref_no=%s", (
                                                                                    self.cmpName_var.get(),
                                                                                    self.typeMed_var.get(),
                                                                                    self.medName_var.get(),
                                                                                    self.lot_var.get(),
                                                                                    self.issuedate_var.get(),
                                                                                    self.expdate_var.get(),
                                                                                    self.uses_var.get(),
                                                                                    self.sideEffect_var.get(),
                                                                                    self.warning_var.get(),
                                                                                    self.dosage_var.get(), 
                                                                                    self.price_var.get(),
                                                                                    self.product_var.get(),
                                                                                    self.ref_var.get(),
                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()

            messagebox.showinfo("UPDATE", "record has been updated successfully")

    def delete(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="root", database="data")
        my_cursor=conn.cursor()

        sql="delete from pharmacy where Ref_no=%s"
        val=(self.ref_var.get(),)
        my_cursor.execute(sql, val)

        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Delete", "Info deleted successfully")

    def reset(self):
        #self.ref_var.set("")
        self.cmpName_var.set("")
        #self.typeMed_var.set("")
        #self.medName_var.set("")
        self.lot_var.set("")
        self.issuedate_var.set("")
        self.expdate_var.set("")
        self.uses_var.set("")
        self.sideEffect_var.set("")
        self.warning_var.set("")
        self.dosage_var.set("") 
        self.price_var.set("")
        self.product_var.set("")

    def search_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="root", database="data")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharmacy where " +str(self.search_var.get())+"LIKE"+str(self.searchTxt_var.get())+"%")

        R=my_cursor.fetchall()
        if len(R)!=0:
            self.pharamcy_table.delete(*self.pharamcy_table.get_children())
            for i in R:
                self.pharamcy_table.insert("", END, values=i)
            conn.commit()
        conn.close()
        
    



if __name__=="__main__":
    root=Tk()
    obj=PharmacyManagementSystem(root)
    root.mainloop()
    
    