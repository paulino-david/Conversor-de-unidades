from tkinter import *

content=Tk()
content.geometry("500x500")
content.resizable(False,False)
content.title("ConversDiv")
content.config(bg="lightblue")
frame=Frame(content,width=450,borderwidth=2,height=400,relief="raised",bg="white")
frame.pack(padx=1,pady=30)

can1de=IntVar()

p=""
div1=""
divisas="FCFA","$         ","€         "
def impirimirde(paises):
    global p
    global div1
    p=paises
    d=Label(frame,text=p)
    d.place(x=90,y=40)
    
    if paises=="Guinea Ecuatorial(FCFA)":
        r=Label(frame,text=divisas[0])
        div1=divisas[0]       
        r.place(x=360,y=80)
    elif paises=="USA($)                                  ":
        r=Label(frame,text=divisas[1])
        div1=divisas[1]       
        r.place(x=360,y=80)
    elif paises=="España(€)                            ":
        r=Label(frame,text=divisas[2])
        div1=divisas[2]       
        r.place(x=360,y=80)
b=""
div2=""
def impirimirde2(paises):
    global b
    global div2
    b=paises
    d=Label(frame,text=b)
    d.place(x=90,y=145)
    if paises=="Guinea Ecuatorial(FCFA)":
        div2=divisas[0]
        r=Label(frame,text=divisas[0])
        r.place(x=360,y=185)
    elif paises=="USA($)                                  ":
        div2=divisas[1]
        r=Label(frame,text=divisas[1])
        r.place(x=360,y=185)
    elif paises=="España(€)                            ":
        div2=divisas[2]
        r=Label(frame,text=divisas[2])
        r.place(x=360,y=185)

def transformador():
    if div1==divisas[0] and div2==divisas[2]:
        cal=can1de.get()/650
        d=Label(frame,text=f"{cal}{div2}                                ",font=70,bg="white")
        d.place(x=80,y=255)
    elif div1==divisas[2] and div2==divisas[0]:
        cal=can1de.get()*650
        d=Label(frame,text=f"{cal}{div2}                                ",font=70,bg="white")
        d.place(x=80,y=255)  

    elif div1==divisas[0] and div2==divisas[1]:
        cal=can1de.get()/600
        d=Label(frame,text=f"{cal}{div2}                                ",font=70,bg="white")
        d.place(x=80,y=255)
    elif div1==divisas[1] and div2==divisas[0]:
        cal=can1de.get()*600
        d=Label(frame,text=f"{cal}{div2}                                ",font=70,bg="white")
        d.place(x=80,y=255)
    
    elif div1==divisas[1] and div2==divisas[2]:
        cal=can1de.get()/1.08
        d=Label(frame,text=f"{cal}{div2}                                ",font=70,bg="white")
        d.place(x=80,y=255)

    elif div1==divisas[2] and div2==divisas[1]:
        cal=can1de.get()*1.08
        d=Label(frame,text=f"{cal}{div2}                                ",font=70,bg="white")
        d.place(x=80,y=255)        
    else:
        d=Label(frame,text=f"{can1de.get()}{div2}                                ",font=70,bg="white")
        d.place(x=80,y=255)  

de=Label(frame,text="Cambiar De:")
de.place(x=10,y=40)

pais=Menubutton(frame,text="Haga click para seleccionar el país o la divisa que quieras")
pais.place(x=80,y=15)
menupais=Menu(pais,tearoff=0)
pais["menu"]=menupais

menupais.add_command(label="Guinea Ecuatorial(FCFA)",command=lambda: impirimirde("Guinea Ecuatorial(FCFA)"))
menupais.add_command(label="USA($)",command=lambda: impirimirde("USA($)                                  "))
menupais.add_command(label="España(€)",command=lambda: impirimirde("España(€)                            "))

cantidad1de=Label(frame,text="Cantidad:")
cantidad1de.place(x=10,y=80)
cantidad1= Entry(frame,width=50,borderwidth=1,textvar=can1de).place(x=90,y=80)

a=Label(frame,text="Cambiar a:")
a.place(x=10,y=145)

pais2=Menubutton(frame,text="Haga click para seleccionar el país o la divisa que quieras")
pais2.place(x=80,y=120)
menupais2=Menu(pais2,tearoff=0)
pais2["menu"]=menupais2

menupais2.add_command(label="Guinea Ecuatorial(FCFA)",command=lambda: impirimirde2("Guinea Ecuatorial(FCFA)"))
menupais2.add_command(label="USA($)",command=lambda: impirimirde2("USA($)                                  "))
menupais2.add_command(label="España(€)",command=lambda: impirimirde2("España(€)                            "))

conversor=Button(frame,text="Convertir",width=10,relief="flat",bg="blue",fg="white",command=transformador).place(x=360,y=360)
mainloop()