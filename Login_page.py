import tkinter as tk
from tkinter import ttk
import sys

LARGE_FONT=("Verdana",18)
SMALL_FONT=("Verdana",14)
SMALLER_FONT=("Verdana",10)

Details={'a':"a",'b':"b"} 


def insert(UsernameR,PasswordR,PhoneR):
    if(len(UsernameR.get())==0 or len(PasswordR.get())==0  or len(PhoneR.get())==0):
        popupmsg("Fields cannot be Empty","Fill All Fields","OK")
        sys.exit(1)
    else:
        if UsernameR.get() not in Details:
            Details[UsernameR.get()]=PasswordR.get() 
            print(Details)
            ResetReg(UsernameR,PhoneR,PasswordR) 



def CheckCred(Username,Password):
    if(len(Username.get())==0 or len(Password.get())==0):
        popupmsg("Invalid Credentials","Invalid Login","Try Again")
    
    else:
        if Username.get() in Details:
            r=tk.Tk()
            r.geometry('500x500')
            r.wm_title("Successfully Logged In")
            rlbl=tk.Label(r,text="Welcome ",font=LARGE_FONT)
            rlbl.pack(pady=20,padx=20)

            rlbl1=tk.Label(r,text="Username: "+Username.get(),font=SMALL_FONT)
            rlbl1.pack(pady=10,padx=10)

            rlbl2=tk.Label(r,text=
                "You have Successfully Logged in",
                font=SMALLER_FONT)
            rlbl2.pack(pady=10,padx=10)

            r.mainloop()
        else:
            Reset(Username,Password)
            popupmsg("Invalid Credentials","Invalid Login","Try Again")


def popupmsg(msg,heading,buttonText):
    popup=tk.Tk()
    popup.geometry('300x150')
    popup.wm_title(heading)
    label=tk.Label(popup,text=msg,font=SMALLER_FONT)
    label.pack(side="top",fill="x",pady=20,padx=20)
    b1=ttk.Button(popup,text=buttonText,command=popup.destroy)
    b1.pack()
    popup.mainloop()


class GUI(tk.Tk):
    def __init__(self,*args,**kwargs):
        
        tk.Tk.__init__(self,*args,**kwargs)
        
        
        tk.Tk.wm_title(self,"Registration-Login Page")
        
        
        container=tk.Frame(self) 
        container.pack(side="top",fill="both",expand=False)        
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1) #0 is the min size
        
        self.frames={} 
        
        for F in (StartPage,RegPage,SuccessRegPage):
            frame=F(container,self)        
            self.frames[F]= frame 
            frame.grid(row=0,column=0,sticky="nsew") 
        
        self.show_frame(StartPage)
        
    def show_frame(self,cont):
        frame=self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame): 
    
    def __init__(self,parent,controller):
        nameEnterV=tk.StringVar()
        passEnterV=tk.StringVar()
        tk.Frame.__init__(self,parent) 
        
        Wel=tk.Label(self,text="*******WELCOME*******",font=LARGE_FONT)
        Wel.pack(pady=10,padx=10) 
        
        LIFB=tk.Label(self,text="Log In",font=SMALL_FONT)
        LIFB.pack(pady=10,padx=10) 
        
        Username=tk.Label(self,text="Username",font=("Verdana",11))
        Username.pack(pady=5,padx=5)
        nameEnter=tk.Entry(self,bd=4,textvariable=nameEnterV)
        nameEnter.pack()
        
        Password=tk.Label(self,text="Password",font=("Verdana",11))
        Password.pack(pady=5,padx=5)
        passEnter=tk.Entry(self,show='*',bd=4,textvariable=passEnterV)
        passEnter.pack()
        
        Loginbutton=ttk.Button(self,text="Log in",command=lambda:CheckCred(nameEnter,passEnter))
                                                                  
        Loginbutton.pack(pady=20,padx=25)
        
        ResButton=ttk.Button(self,text="Reset",command=lambda: Reset(nameEnter,passEnter))
        ResButton.pack(pady=10,padx=10)
        
        NU=tk.Label(self,text="New User?",font=("Verdana",12))
        NU.pack(pady=25,padx=15)
        
        RH=ttk.Button(self,text="Register Here",
                command=lambda: controller.show_frame(RegPage))
        RH.pack()
        
def Reset(Username,Password):
    Username.delete(0,'end')
    Password.delete(0,'end')


class RegPage(tk.Frame):
    def __init__(self,parent,controller):
        nameEnterV=tk.StringVar()
        passEnterV=tk.StringVar()
        tk.Frame.__init__(self,parent)
        
        RHSB=ttk.Label(self,text="*******REGISTER*******",font=LARGE_FONT)
        RHSB.pack(pady=10,padx=10) 
        
        UsernameR=tk.Label(self,text="Username",font=("Verdana",11))
        UsernameR.pack(pady=5,padx=5)
        nameEnter=tk.Entry(self,bd=4,textvariable=nameEnterV)
        nameEnter.pack()
        
        
        Phone=tk.Label(self,text="Phone Number",font=("Verdana",11))
        Phone.pack(pady=5,padx=5)
        phoneEnter=tk.Entry(self,bd=4)
        phoneEnter.pack()
        
        PasswordR=tk.Label(self,text="Password",font=("Verdana",11))
        PasswordR.pack(pady=5,padx=5)
        passEnter=tk.Entry(self,show='*',bd=4,textvariable=passEnterV)
        passEnter.pack()
        
        SU=ttk.Button(self,text="Sign Up ",command=lambda:[insert(nameEnter,passEnter,phoneEnter),controller.show_frame(SuccessRegPage)])
        SU.pack(pady=15,padx=15)
    
        ResetButton=ttk.Button(self,text="Reset",command=lambda:ResetReg(nameEnter,phoneEnter,passEnter))
        ResetButton.pack(pady=15,padx=15) 
        
        AHA=tk.Label(self,text="Already have an account?",font=SMALLER_FONT)
        AHA.pack(pady=30,padx=10)
        
        Loginbutton2=ttk.Button(self,text="Go to Login Page",command=lambda:controller.show_frame(StartPage))                                                         
        Loginbutton2.pack(pady=0,padx=25)
        
def ResetReg(Nentry,Eentry,Pentry,Passentry):
    Nentry.delete(0,'end')
    Eentry.delete(0,'end')
    Pentry.delete(0,'end')
    Passentry.delete(0,'end')  

class SuccessRegPage(tk.Frame):
        def __init__(self,parent,controller):
            tk.Frame.__init__(self,parent)
            label=ttk.Label(self,text="Succesfully Registered",font=SMALL_FONT)
            label.pack(pady=10,padx=10)

            button4=ttk.Button(self,text="Go To Login Page",
                    command=lambda: controller.show_frame(StartPage))
            button4.pack()

app=GUI() 
app.geometry('600x600')
app.mainloop() 