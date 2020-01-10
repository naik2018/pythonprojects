# My billing system using python

from tkinter import *
class my_bill:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x800+0+0")
        self.root.title("My billing app")
        
        self.sada_dhosa=IntVar()
        self.rava_dhosa=IntVar()
        self.paper_dhosa=IntVar()
        self.jini_dhosa=IntVar()
        self.masala_dhosa=IntVar()
        
        self.masala_uttapam=IntVar()
        self.onion_uttapam=IntVar()
        self.tomato_uttapam=IntVar()
        self.onion_tomato_uttapam=IntVar()
        
        self.paneer=IntVar()
        self.cheese=IntVar()
        self.sambhar=IntVar()
        self.chatni=IntVar()
        
        self.subtotal=StringVar()
        self.gst=StringVar()
        self.cgst=StringVar()
        self.total=StringVar()
        
        
        
        title=Label(self.root,text="My Billing System",bd=10,relief=GROOVE,bg="blue",fg="yellow",font=("arial",30,"bold"),pady=2).pack(fill="x")
        
        F1=LabelFrame(self.root,text="Customer Details",font=("times new roman",15,"bold"),bg="light blue",fg="purple")
        F1.place(x=0,y=75,relwidth=1)
        
        cname_lbl1=Label(F1,text="Customer Name",fg="white",bg="green",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt1=Entry(F1,width=20,font="arial 15",bd=5,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        
        cname_lbl2=Label(F1,text="Phone Number",fg="white",bg="green",font=("times new roman",15,"bold")).grid(row=0,column=5,padx=20,pady=5)
        cname_txt2=Entry(F1,width=10,font="arial 15",bd=5,relief=SUNKEN).grid(row=0,column=10,pady=5,padx=10)
        
        cname_lbl3=Label(F1,text="Bill Number",fg="white",bg="green",font=("times new roman",15,"bold")).grid(row=0,column=15,padx=20,pady=5)
        cname_txt3=Entry(F1,width=20,font="arial 15",bd=5,relief=SUNKEN).grid(row=0,column=20,pady=5,padx=10)
        
        b1=Button(F1,text="Search",bg='light grey',width=10,bd=8,font=('arial',12,'bold')).grid(row=0,column=25,padx=10,pady=10)
        
        F2=LabelFrame(self.root,text="DHOSA",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),bg="light blue",fg="purple")
        F2.place(x=5,y=180,relwidth=0.28,height=257)
        
        cname_lbl4=Label(F2,text="Sada Dhosa",fg="white",bg="green",width=10,font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt4=Entry(F2,width=10,textvariable=self.sada_dhosa,font="arial 15",bd=5,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)
        
        cname_lbl5=Label(F2,text="Rava Dhosa",fg="white",bg="green",width=10,font=("times new roman",15,"bold")).grid(row=1,column=0,padx=20,pady=5)
        cname_txt5=Entry(F2,width=10,textvariable=self.rava_dhosa,font="arial 15",bd=5,relief=SUNKEN).grid(row=1,column=5,pady=5,padx=10)
        
        cname_lbl6=Label(F2,text="Masala Dhosa",fg="white",bg="green",width=10,font=("times new roman",15,"bold")).grid(row=2,column=0,padx=20,pady=5)
        cname_txt6=Entry(F2,width=10,textvariable=self.masala_dhosa,font="arial 15",bd=5,relief=SUNKEN).grid(row=2,column=5,pady=5,padx=10)
        
        cname_lbl7=Label(F2,text="Paper Dhosa",fg="white",bg="green",width=10,font=("times new roman",15,"bold")).grid(row=3,column=0,padx=20,pady=5)
        cname_txt7=Entry(F2,width=10,textvariable=self.paper_dhosa,font="arial 15",bd=5,relief=SUNKEN).grid(row=3,column=5,pady=5,padx=10)
        
        cname_lbl8=Label(F2,text="Jini Dhosa",fg="white",bg="green",width=10,font=("times new roman",15,"bold")).grid(row=4,column=0,padx=20,pady=5)
        cname_txt8=Entry(F2,width=10,textvariable=self.jini_dhosa,font="arial 15",bd=5,relief=SUNKEN).grid(row=4,column=5,pady=5,padx=10)
        
        F3=LabelFrame(self.root,text="Uttapam",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),bg="light blue",fg="purple")
        F3.place(x=415,y=180,relwidth=0.34,height=257)
        
        cname_lbl9=Label(F3,text="Masala Uttapam",fg="white",bg="green",width=17,font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt9=Entry(F3,width=10,font="arial 15",bd=5,relief=SUNKEN,textvariable=self.masala_uttapam).grid(row=0,column=5,pady=5,padx=10)
        
        cname_lbl10=Label(F3,text="Tomato Uttapam",fg="white",bg="green",width=17,font=("times new roman",15,"bold")).grid(row=1,column=0,padx=20,pady=5)
        cname_txt10=Entry(F3,width=10,font="arial 15",bd=5,relief=SUNKEN,textvariable=self.tomato_uttapam).grid(row=1,column=5,pady=5,padx=10)
        
        cname_lbl11=Label(F3,text="Onion Tomato Uttapam",fg="white",bg="green",width=17,font=("times new roman",15,"bold")).grid(row=2,column=0,padx=20,pady=5)
        cname_txt11=Entry(F3,width=10,font="arial 15",bd=5,relief=SUNKEN,textvariable=self.onion_tomato_uttapam).grid(row=2,column=5,pady=5,padx=10)
        
        cname_lbl12=Label(F3,text="Onion Uttapam",fg="white",bg="green",width=17,font=("times new roman",15,"bold")).grid(row=3,column=0,padx=20,pady=5)
        cname_txt12=Entry(F3,width=10,font="arial 15",bd=5,relief=SUNKEN,textvariable=self.onion_uttapam).grid(row=3,column=5,pady=5,padx=10)
        
        F4=Frame(self.root,bd=10,relief=GROOVE)
        F4.place(x=900,y=180,width=440,height=300)
        bill_title=Label(F4,text="Your Bill",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        
        scroll_y=Scrollbar(F4,orient=VERTICAL)
        self.textarea=Text(F4,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack()
        
        F5=LabelFrame(self.root,text="Extra",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),bg="light blue",fg="purple")
        F5.place(x=0,y=440,relwidth=0.65,height=80)
        
        cname_lbl13=Label(F5,text="cheese" ,fg="white",bg="green",width=6,font=("times new roman",15,"bold")).grid(row=1,column=0,padx=20,pady=5)
        cname_txt13=Entry(F5,width=5,font="arial 15",bd=5,relief=SUNKEN,textvariable=self.cheese).grid(row=1,column=5,pady=5,padx=10)
        
        cname_lbl14=Label(F5,text="Sambhar" ,fg="white",bg="green",width=6,font=("times new roman",15,"bold")).grid(row=1,column=10,padx=20,pady=5)
        cname_txt14=Entry(F5,width=5,font="arial 15",bd=5,relief=SUNKEN,textvariable=self.sambhar).grid(row=1,column=15,pady=5,padx=10)
        
        cname_lbl15=Label(F5,text="Chatni" ,fg="white",bg="green",width=6,font=("times new roman",15,"bold")).grid(row=1,column=20,padx=20,pady=5)
        cname_txt15=Entry(F5,width=5,font="arial 15",bd=5,relief=SUNKEN,textvariable=self.chatni).grid(row=1,column=25,pady=5,padx=10)
        
        cname_lbl16=Label(F5,text="Paneer" ,fg="white",bg="green",width=6,font=("times new roman",15,"bold")).grid(row=1,column=30,padx=20,pady=5)
        cname_txt16=Entry(F5,width=5,font="arial 15",bd=5,relief=SUNKEN,textvariable=self.paneer).grid(row=1,column=35,pady=5,padx=10)
        
        F6=LabelFrame(self.root,text="Main Bill Menu",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),bg="light blue",fg="purple")
        F6.place(x=0,y=535,relwidth=0.65,height=160)
        
        cname_lbl17=Label(F6,text="SubTotal",fg="white",bg="green",width=10,font=("times new roman",15,"bold")).grid(row=1,column=30,padx=20,pady=5)
        cname_txt17=Entry(F6,textvariable=self.subtotal,width=8,font="arial 15",bd=5,relief=SUNKEN).grid(row=1,column=33,pady=5,padx=10)
        
        cname_lbl18=Label(F6,text="GST",fg="white",bg="green",width=10,font=("times new roman",15,"bold")).grid(row=1,column=40,padx=20,pady=5)
        cname_txt18=Entry(F6,width=8,font="arial 15",bd=5,relief=SUNKEN,textvariable=self.gst).grid(row=1,column=43,pady=5,padx=10)
        
        cname_lbl18=Label(F6,text="CGST",fg="white",bg="green",width=10,font=("times new roman",15,"bold")).grid(row=1,column=50,padx=20,pady=5)
        cname_txt18=Entry(F6,width=8,font="arial 15",bd=5,relief=SUNKEN,textvariable=self.cgst).grid(row=1,column=53,pady=5,padx=10)
        
        cname_lbl20=Label(F6,text="TOTAL BILL",fg="white",bg="green",width=10,font=("times new roman",15,"bold")).grid(row=4,column=50,padx=20,pady=5)
        cname_txt20=Entry(F6,width=8,font="arial 15",bd=5,relief=SUNKEN,textvariable=self.total).grid(row=4,column=53,pady=5,padx=10)
        
        
        F7=Frame(self.root,bd=10,relief=GROOVE)
        F7.place(x=900,y=480,width=440,height=210)
        
        sub_total_btn=Button(F7,text="Sub Total",command=self.sub_total,bg="cadetblue",fg="white",bd=5,pady=15,width=11,font="arial").grid(row=0,column=0,padx=5,pady=5)
        gbill_btn=Button(F7,text="Generate Bill",bg="cadetblue",fg="white",bd=5,pady=15,width=11,font="arial").grid(row=0,column=10,padx=5,pady=5)
        print_btn=Button(F7,text="Print",bg="cadetblue",fg="white",bd=5,pady=15,width=11,font="arial").grid(row=0,column=15,padx=5,pady=5)
        total_btn=Button(F7,text="Total",command=self.total_bill,bg="cadetblue",fg="white",bd=5,pady=15,width=11,font="arial").grid(row=1,column=0,padx=5,pady=5)
        clear_btn=Button(F7,text="Clear",bg="cadetblue",fg="white",bd=5,pady=15,width=11,font="arial").grid(row=1,column=10,padx=5,pady=5)
        exit_btn=Button(F7,text="Exit",bg="cadetblue",fg="white",bd=5,pady=15,width=11,font="arial").grid(row=1,column=15,padx=5,pady=5)
        
    def sub_total(self):
        self.st=((self.masala_dhosa.get()*65)+(self.rava_dhosa.get()*80)+(self.jini_dhosa.get()*120)+(self.sada_dhosa.get()*50) +(self.paper_dhosa.get()*90)+(self.masala_uttapam.get())*80+(self.onion_uttapam.get()*85)+(self.tomato_uttapam.get()*85)+(self.onion_tomato_uttapam.get()*90) +(self.cheese.get()*20)+(self.paneer.get()*15)+(self.sambhar.get()*10)+(self.chatni.get()*5))
        self.subtotal.set("Rs."+str(self.st)) 
    
    def total_bill(self):
            self.tl=((self.st+float(self.st)*5/100))
            self.total.set("Rs."+str(self.tl))

root=Tk()
obj1=my_bill(root)
root.mainloop()