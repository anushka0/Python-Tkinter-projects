from tkinter import *
import tkinter.messagebox 
root=Tk()
root.geometry("750x900+0+0")
root.configure(bg='#195c44')
root.maxsize(780,900)
root.title("Tic tac toe Game")


player1=IntVar()
player2=IntVar()

player1.set(0)
player2.set(0)

buttons=StringVar()
click=TRUE
def check(buttons):
    global click
    if buttons["text"]== "" and click==True:
        buttons["text"]="X"
        click=False
        score()
    elif buttons["text"]=="" and click==False:
        buttons["text"]="O"
        click=True
        score()

def reset():
    button1['text']=""
    button2['text']=""
    button3['text']=""
    button4['text']=""
    button5['text']=""
    button6['text']=""
    button7['text']=""
    button8['text']=""
    button9['text']=""

    button1.configure(background='#a5d4e8')
    button2.configure(background='#a5d4e8')
    button3.configure(background='#a5d4e8')
    button4.configure(background='#a5d4e8')
    button5.configure(background='#a5d4e8')
    button6.configure(background='#a5d4e8')
    button7.configure(background='#a5d4e8')
    button8.configure(background='#a5d4e8')
    button9.configure(background='#a5d4e8')
    

def newgame():
    button1['text']=""
    button2['text']=""
    button3['text']=""
    button4['text']=""
    button5['text']=""
    button6['text']=""
    button7['text']=""
    button8['text']=""
    button9['text']=""
    
    button1.configure(background='#a5d4e8')
    button2.configure(background='#a5d4e8')
    button3.configure(background='#a5d4e8')
    button4.configure(background='#a5d4e8')
    button5.configure(background='#a5d4e8')
    button6.configure(background='#a5d4e8')
    button7.configure(background='#a5d4e8')
    button8.configure(background='#a5d4e8')
    button9.configure(background='#a5d4e8')
    player1.set(0)
    player2.set(0)

def score():
    if button1['text']=='X' and button2['text']=='X'and button3['text']=='X':
        button1.configure(background='#369e79')
        button2.configure(background='#369e79')
        button3.configure(background='#369e79')
        n=int(player1.get())
        score=n+1
        player1.set(score)
        tkinter.messagebox.showinfo("RESULT","Congrats player 1 winner")
        reset()
        
    
    if button4['text']=='X' and button5['text']=='X'and button6['text']=='X':
        button4.configure(background='#369e79')
        button5.configure(background='#369e79')
        button6.configure(background='#369e79')
        n=int(player1.get())
        score=n+1
        player1.set(score)
        tkinter.messagebox.showinfo("RESULT","Congrats player 1 winner")
        reset()
        

    if button7['text']=='X' and button8['text']=='X'and button9['text']=='X':
        button7.configure(background='#369e79')
        button8.configure(background='#369e79')
        button9.configure(background='#369e79')
        n=int(player1.get())
        score=n+1
        player1.set(score)
        tkinter.messagebox.showinfo("RESULT","Congrats player 1 winner")
        reset()

    if button1['text']=='X' and button4['text']=='X'and button7['text']=='X':
        button1.configure(background='#369e79')
        button4.configure(background='#369e79')
        button7.configure(background='#369e79')
        n=int(player1.get())
        score=n+1
        player1.set(score)
        tkinter.messagebox.showinfo("RESULT","Congrats player 1 winner")
        reset()

    if button2['text']=='X' and button5['text']=='X'and button8['text']=='X':
        button2.configure(background='#369e79')
        button5.configure(background='#369e79')
        button8.configure(background='#369e79')
        n=int(player1.get())
        score=n+1
        player1.set(score)
        tkinter.messagebox.showinfo("RESULT","Congrats player 1 winner")
        reset()

    if button3['text']=='X' and button6['text']=='X'and button9['text']=='X':
        button3.configure(background='#369e79')
        button6.configure(background='#369e79')
        button9.configure(background='#369e79')
        n=int(player1.get())
        score=n+1
        player1.set(score)
        tkinter.messagebox.showinfo("RESULT","Congrats player 1 winner")
        reset()

    if button1['text']=='X' and button5['text']=='X'and button9['text']=='X':
        button1.configure(background='#369e79')
        button5.configure(background='#369e79')
        button9.configure(background='#369e79')
        n=int(player1.get())
        score=n+1
        player1.set(score)
        tkinter.messagebox.showinfo("RESULT","Congrats player 1 winner")
        reset()

    if button3['text']=='X' and button5['text']=='X'and button7['text']=='X':
        button3.configure(background='#369e79')
        button5.configure(background='#369e79')
        button7.configure(background='#369e79')
        n=int(player1.get())
        score=n+1
        player1.set(score)
        tkinter.messagebox.showinfo("RESULT","Congrats player 1 winner")
        reset()
        
    if button1['text']=='O' and button2['text']=='O'and button3['text']=='O':
        button1.configure(background='#369e79')
        button2.configure(background='#369e79')
        button3.configure(background='#369e79')
        n=int(player2.get())
        score=n+1
        player2.set(score)
        tkinter.messagebox.showinfo("RESULT","Congrats player 2 winner")
        reset()
    
    if button4['text']=='O' and button5['text']=='O'and button6['text']=='O':
        button4.configure(background='#369e79')
        button5.configure(background='#369e79')
        button6.configure(background='#369e79')
        n=int(player2.get())
        score=n+1
        player2.set(score)
        tkinter.messagebox.showinfo("RESULT","Congrats player 2 winner")
        reset()

    if button7['text']=='O' and button8['text']=='O'and button9['text']=='O':
        button7.configure(background='#369e79')
        button8.configure(background='#369e79')
        button9.configure(background='#369e79')
        n=int(player2.get())
        score=n+1
        player2.set(score)
        tkinter.messagebox.showinfo("RESULT","Congrats player 2 winner")
        reset()

    if button1['text']=='O' and button4['text']=='O'and button7['text']=='O':
        button1.configure(background='#369e79')
        button4.configure(background='#369e79')
        button7.configure(background='#369e79')
        n=int(player2.get())
        score=n+1
        player2.set(score)
        tkinter.messagebox.showinfo("RESULT","Congrats player 2 winner")
        reset()
    
    if button2['text']=='O' and button5['text']=='O'and button8['text']=='O':
        button2.configure(background='#369e79')
        button5.configure(background='#369e79')
        button8.configure(background='#369e79')
        n=int(player2.get())
        score=n+1
        player2.set(score)
        tkinter.messagebox.showinfo("RESULT","Congrats player 2 winner")
        reset()

    if button3['text']=='O' and button6['text']=='O'and button9['text']=='O':
        button3.configure(background='#369e79')
        button6.configure(background='#369e79')
        button9.configure(background='#369e79')
        n=int(player2.get())
        score=n+1
        player2.set(score)
        tkinter.messagebox.showinfo("RESULT","Congrats player 2 winner")
        reset()

    if button1['text']=='O' and button5['text']=='O'and button9['text']=='O':
        button1.configure(background='#369e79')
        button5.configure(background='#369e79')
        button9.configure(background='#369e79')
        n=int(player2.get())
        score=n+1
        player2.set(score)
        tkinter.messagebox.showinfo("RESULT","Congrats player 2 winner")
        reset()
    
    if button3['text']=='O' and button5['text']=='O'and button7['text']=='O':
        button3.configure(background='#369e79')
        button5.configure(background='#369e79')
        button7.configure(background='#369e79')
        n=int(player2.get())
        score=n+1
        player2.set(score)
        tkinter.messagebox.showinfo("RESULT","Congrats player 2 winner")
        reset()
        
    
        
        
        

topf=Frame(root,width=900,height=100,pady=2,bg="mistyrose",relief= RAISED)
topf.grid(row=0,column=0)
topl=Label(topf,text="Tic Tac Toe Game",bd=10,padx=84,pady=1,font="constantia 35 bold",bg="#1b7280",fg="white",justify=CENTER)
topl.grid(row=0,column=0)
mainf=Frame(root,bg="#298191",height=700,width=1100,relief=RAISED)
mainf.grid(row=1,column=0)
f1=Frame(mainf,bg="#1b7280",height=550,width=650,relief= RAISED,bd=8,pady=2,padx=10)
f1.pack(side=TOP)
f2=Frame(mainf,bg="#1b7280",height=600,width=500,relief=RAISED,bd=7,pady=2,padx=10)
f2.pack(side=BOTTOM)
f21=Frame(f2,bg="#80601b",height=275,width=400,bd=4,pady=2,padx=10,relief=RAISED)
f21.grid(row=0,column=0)
f22=Frame(f2,bg="#80601b",height=300,width=500,bd=4,pady=2,padx=10,relief=RAISED)
f22.grid(row=1,column=0)


button1=Button(f1,text="",font='constantia 24 bold',height=2,width=6,bg='#a5d4e8',command=lambda:check(button1))
button1.grid(row=1,column=0)
button2=Button(f1,text="",font='constantia 24 bold',height=2,width=6,bg='#a5d4e8',command=lambda:check(button2))
button2.grid(row=1,column=1)

button3=Button(f1,text="",font='constantia 24 bold',height=2,width=6,bg='#a5d4e8',command=lambda:check(button3))
button3.grid(row=1,column=2)

button4=Button(f1,text="",font='constantia 24 bold',height=2,width=6,bg='#a5d4e8',command=lambda:check(button4))
button4.grid(row=2,column=0)

button5=Button(f1,text="",font='constantia 24 bold',height=2,width=6,bg='#a5d4e8',command=lambda:check(button5))
button5.grid(row=2,column=1)

button6=Button(f1,text="",font='constantia 24 bold',height=2,width=6,bg='#a5d4e8',command=lambda:check(button6))
button6.grid(row=2,column=2)

button7=Button(f1,text="",font='constantia 24 bold',height=2,width=6,bg='#a5d4e8',command=lambda:check(button7))
button7.grid(row=3,column=0)

button8=Button(f1,text="",font='constantia 24 bold',height=2,width=6,bg='#a5d4e8',command=lambda:check(button8))
button8.grid(row=3,column=1)

button9=Button(f1,text="",font='constantia 24 bold',height=2,width=6,bg='#a5d4e8',command=lambda:check(button9))
button9.grid(row=3,column=2)


player1l=Label(f21,text="Player 1",pady=2,padx=2,font="constantia 30 bold",bg="#27adb0")
player1l.grid(row=0,column=0)
player2l=Label(f21,text="Player 2",pady=2,padx=2,font="constantia 30 bold",bg="#1c7e80")
player2l.grid(row=1,column=0)


Eplayer1=Entry(f21,font="constantia 30 bold",bg="mistyrose",textvariable=player1,width=12,justify=CENTER)
Eplayer1.grid(row=0,column=1)


Eplayer2=Entry(f21,font="constantia 30 bold",bg="mistyrose",textvariable=player2,width=12,justify=CENTER)
Eplayer2.grid(row=1,column=1)
#reset=Button(f22,text="Reset",font='arial 24 bold',height=1,width=12,pady=2,padx=2,bg='#1f871a',command=reset)
#reset.grid(row=1,column=0)
newgame=Button(f22,text="Newgame",font='arial 24 bold',height=1,padx=12,pady=2,width=12,bg='#1f871a',command=newgame)
newgame.grid(row=1,column=1)


root.mainloop()