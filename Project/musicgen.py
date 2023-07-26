from tkinter import *
import mysql.connector
import webbrowser
import random

mydb=mysql.connector.connect(host='localhost',user='root',passwd='root')#password depending on the user pc
mc=mydb.cursor()
mc.execute("use dbms")

def songGenHappy():
    try:
        mc.execute("use dbms")
        mc.execute("select link from happy;")
        op=mc.fetchall() #op= type "list", and the elements are of type "tuple":[('https://',),('https:',)]
        res=random.randint(0,len(op)) #3
        myText.set(op[res]) #myText= op[3]
        x=str(op[res]) # "('https://',)"
        webbrowser.open(x[2:31]) #https-----.com. 
    except:
        print("Error encountered!")

def songGenSad():
    try:
        mc.execute("select link from sad;")
        op2=mc.fetchall()
        res2=random.randint(0,len(op2))
        myText.set(op2[res2])
        y=str(op2[res2])
        webbrowser.open(y[2:31])
    except:
        print("Error encountered!")
   
root = Tk()
root.title("Emotica - The Song Generator")
root.iconbitmap("C:/Users/VarunG/Documents/Project/img.ico")
root.geometry("400x400")

myText=StringVar()
Label(root, text='''How are you feeling right now?''',font=('Helveticabold',15)).grid(row=0, sticky=W)
Label(root, text="The Link:").grid(row=2, sticky=S)
link=Label(root, text="", textvariable=myText, font=('Helveticabold',15),fg="purple",cursor="hand2").grid(row=3,column=0, sticky=S)

b1 = Button(root, text="I'm feeling pretty good! :))",font=('Helveticabold',15),relief=RAISED, command=songGenHappy)
b1.grid(row=0, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=4, pady=4)

b2=Button(root, text='No, not that great... :((',font=('Helveticabold',15),relief=RAISED, command=songGenSad)
b2.grid(row=2,column=2, columnspan=2, rowspan=2, sticky=W+E+N+S,padx=3,pady=3)

mainloop()
