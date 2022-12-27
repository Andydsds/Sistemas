from tkinter import * 
from tkinter import ttk
import sympy as sp
import numpy as np
from sympy import symbols, sympify
#from tkinter.ttk import *
  
master = Tk()  #Pestaña principal
master.geometry("400x400")  #cambiar tamaño
master.title("Calculadora numérica")
master.config(bg="pink") #cambiar color de fondo 

x = sp.Symbol('x')
y = sp.Symbol('y')
#método de Euler
def euler(window,x_num,y_num,h,xi,xf,expresion): #cond. inicial x, y y tamañano de paso
        #Calculo de iteraciones
        nc=(xf-xi)/h
        nc=int(nc)
        for i in range(1,nc+1): 
            y_num=y_num+float(expresion.subs(x,x_num))*h
            x_num=x_num+h
            x_num=round(x_num,2)
            y_num=round(y_num,3)
           # print(i,x_num,y_num)
            #Imprimir resultados
            #encabezado
            encabezadoi=Label(window,text='i',font=("Century gothic",10,"bold"),bg="powder blue")
            encabezadoi.grid(row=6, column=1,pady=5)
            resultadosi=Label(window,text=i,font=("Century gothic",10),bg="powder blue")
            resultadosi.grid(row=i+6,column=1)
            encabezadox=Label(window,text='x',font=("Century gothic",10,"bold"),bg="powder blue")
            encabezadox.grid(row=6,column=2,pady=5)
            resultadosx=Label(window,text=x_num,font=("Century gothic",10),bg="powder blue")
            resultadosx.grid(row=i+6,column=2)
            encabezadoy=Label(window,text='y',font=("Century gothic",10,"bold"),bg="powder blue")
            encabezadoy.grid(row=6, column=3,pady=5)
            resultadosy=Label(window,text=y_num,font=("Century gothic",10),bg="powder blue")
            resultadosy.grid(row=i+6,column=3)

def pto_medio(window,x_num,y_num,h,xi,xf,expresion):
    #crear una vista de arbol y una barra de desplazamiento
  treev = ttk.Treeview(window)
  treev.pack(side ='left')

  barra=ttk.Scrollbar(window,orient="vertical",command=treev.yview)
  barra.pack(side ='left', fill ='x')
  #configuracion del treeview
  treev.configure(xscrollcommand = barra.set)
  treev["columns"] = ("1", "2", "3")
  treev['show'] = 'headings'

  # Asignar el ancho y que esten centradas las columnas
  treev.column("1", width = 90, anchor ='c')
  treev.column("2", width = 90, anchor ='c')
  treev.column("3", width = 90, anchor ='c')

  treev.heading("1", text ="i")
  treev.heading("2", text ="x")
  treev.heading("3", text ="y")

  #Calculo de iteraciones
  nc=(xf-xi)/h
  nc=int(nc)
  for i in range(1,nc+1): 
   # dydx=(-2*(x**3))+12*(x**2)-(20*x)+8.5
    ym=y_num+float(expresion.subs(x,x_num))*(h/2)
    xm=x_num+h/2
    y_num=ym+float(expresion.subs(x,xm))*h
    x_num=xm+h/2
    x_num=round(x_num, 2)
    y_num=round(y_num, 3)
    #print(i,x_num,y_num)
    #Imprimir resultados
    #encabezado
    treev.insert("",'end',values=(i,x_num,y_num))


#Pestaña metodo euler
def openEulerWindow():  

    newWindow = Toplevel(master) #cambiar nombres
    newWindow.title("Método de Euler")     
    newWindow.geometry("500x500") 
   # frame=Frame(newWindow).grid(row=10,bg='blue')
    #Funcion para el método de euler             
    ingr_dat=Frame(newWindow,bg='powder blue', width = 500, height=500, pady=3, padx=15)
    ingr_dat.grid(sticky=EW)
    for i in range(0,5):
        ingr_dat.columnconfigure(i,weight=1)
   # ingr_dat.columnconfigure(1, weight=1)
   # ingr_dat.columnconfigure(1,weight=1)0

    show_res=Frame(newWindow,bg='powder blue', width = 500, height=500, pady=3, padx=15)
    show_res.grid(sticky=EW)
    for i in range(0,5):
        show_res.columnconfigure(i,weight=1)
        #show_res.columnconfigure(1,weight=1)
        #show_res.columnconfigure(2,weight=1)
    def sendata():  #guardar la información que se ingresa
        funcion_data=str(funcion.get()) 
        funcion_data = sympify(funcion_data) #convertir la función en un objeto matemático 
        print(funcion_data,type(funcion_data)) 
        xinitial_value=float(xinitial.get())
        yinitial_value=float(yinitial.get())
        h_value=float(h.get())
        #print("inicial valor de x y tipo",xinitial_value,type(xinitial_value))
        xf_value=float(xf.get())
        xi_value=float(xi.get())
        print(euler(show_res,xinitial_value,yinitial_value,h_value,xi_value,xf_value,funcion_data))
    
    
    Label(ingr_dat,  
          text ="Ingrese la ecuación",width=20,font=("Century gothic",10),bg="powder blue").grid(row=0,column=1,pady=3,padx=4)
    funcion=StringVar()
    entrada_funcion=Entry(ingr_dat,textvariable=funcion,width=20)
    entrada_funcion.insert(0,'(-2*(x**3))+12*(x**2)-(20*x)+8.5')
    entrada_funcion.grid(row=0,column=2,pady=3,padx=4)
    
    Label(ingr_dat, text="Ingrese el valor inicial de x" ,font=("Century gothic",10),bg="powder blue").grid(row=1,column=1,pady=3,padx=4)
    xinitial=DoubleVar()
    entrada_xinitial=Entry(ingr_dat,textvariable=xinitial,width=20)
    entrada_xinitial.grid(row=1,column=2,pady=3,padx=4)

    Label(ingr_dat, text="Ingrese el valor inivial de y",font=("Century gothic",10),bg="powder blue").grid(row=2,column=1,pady=3,padx=4)
    yinitial=DoubleVar()
    entrada_yinitial=Entry(ingr_dat,textvariable=yinitial,width=20)
    entrada_yinitial.grid(row=2,column=2,pady=3,padx=4)
    
    Label(ingr_dat, text="Ingrese h",font=("Century gothic",10),bg="powder blue").grid(row=3,column=1,pady=3,padx=4)
    h=DoubleVar()
    entrada_h=Entry(ingr_dat,textvariable=h,width=20)
    entrada_h.insert(2,1)    
    entrada_h.grid(row=3,column=2,pady=3,padx=4)

    Label(ingr_dat, text="Ingrese xi",font=("Century gothic",10),bg="powder blue").grid(row=4,column=1,pady=3,padx=4)
    xi=DoubleVar()
    entrada_xi=Entry(ingr_dat,textvariable=xi,width=20)
    entrada_xi.grid(row=4,column=2,pady=3,padx=4)

    Label(ingr_dat, text="Ingrese xf",font=("Century gothic",10),bg="powder blue").grid(row=5,column=1,pady=3,padx=4)
    xf=DoubleVar()
    entrada_xf=Entry(ingr_dat,textvariable=xf,width=20)
    entrada_xf.insert(1,1) #valor predeterminado
    entrada_xf.grid(row=5,column=2,pady=3,padx=4)

    enviaBoton=Button(ingr_dat,text="Enviar",command=sendata)
    enviaBoton.grid(row=6,column=2,pady=3)
  #  text=Text(newWindow,height = 5, width = 52) #crear texto

    
    
#Ventana para el método 2
def openPtomedioWindow():    

    newWindow = Toplevel(master) #cambiar nombres
    newWindow.title("Método del Punto medio")     
    newWindow.geometry("500x500") 
   # frame=Frame(newWindow).grid(row=10,bg='blue')
    #Funcion para el método de euler             
    ingr_dat=Frame(newWindow,bg='PaleGreen1', width = 500, height=500, pady=3, padx=15)
    ingr_dat.grid(sticky=EW)
    for i in range(0,4):
        ingr_dat.columnconfigure(i,weight=1)
   # ingr_dat.columnconfigure(1, weight=1)
   # ingr_dat.columnconfigure(1,weight=1)

    show_res=Frame(newWindow,bg='PaleGreen1', width = 500, height=500, pady=3, padx=15)
    show_res.grid(sticky=EW)
    for i in range(0,5):
        show_res.columnconfigure(i,weight=1)
        #show_res.columnconfigure(1,weight=1)
        #show_res.columnconfigure(2,weight=1)
    def sendata():  #guardar la información que se ingresa
        funcion_data=str(funcion.get()) 
        funcion_data = sympify(funcion_data) #convertir la función en un objeto matemático 
        print(funcion_data,type(funcion_data)) 
        xinitial_value=float(xinitial.get())
        yinitial_value=float(yinitial.get())
        h_value=float(h.get())
        print("inicial valor de x y tipo",xinitial_value,type(xinitial_value))
        xf_value=float(xf.get())
        xi_value=float(xi.get())
        print(pto_medio(show_res,xinitial_value,yinitial_value,h_value,xi_value,xf_value,funcion_data))
    
    
    Label(ingr_dat,  
          text ="Ingrese la ecuación",width=20,font=("Century gothic",10),bg="PaleGreen1").grid(row=0,column=1,pady=3,padx=4)
    funcion=StringVar()
    entrada_funcion=Entry(ingr_dat,textvariable=funcion,width=20)
    entrada_funcion.insert(0,'(-2*(x**3))+12*(x**2)-(20*x)+8.5')
    entrada_funcion.grid(row=0,column=2,pady=3,padx=4)
    
    Label(ingr_dat, text="Ingrese el valor inicial de x",font=("Century gothic",10),bg="PaleGreen1" ).grid(row=1,column=1,pady=3,padx=4)
    xinitial=DoubleVar()
    entrada_xinitial=Entry(ingr_dat,textvariable=xinitial,width=20)
    entrada_xinitial.grid(row=1,column=2,pady=3,padx=4)

    Label(ingr_dat, text="Ingrese el valor inivial de y",font=("Century gothic",10),bg="PaleGreen1" ).grid(row=2,column=1,pady=3,padx=4)
    yinitial=DoubleVar()
    entrada_yinitial=Entry(ingr_dat,textvariable=yinitial,width=20)
    entrada_yinitial.grid(row=2,column=2,pady=3,padx=4)
    
    Label(ingr_dat, text="Ingrese h",font=("Century gothic",10),bg="PaleGreen1" ).grid(row=3,column=1,pady=3,padx=4)
    h=DoubleVar()
    entrada_h=Entry(ingr_dat,textvariable=h,width=20)
    entrada_h.insert(2,1)  
    entrada_h.grid(row=3,column=2,pady=3,padx=4)

    Label(ingr_dat, text="Ingrese xi",font=("Century gothic",10),bg="PaleGreen1" ).grid(row=4,column=1,pady=3,padx=4)
    xi=DoubleVar()
    entrada_xi=Entry(ingr_dat,textvariable=xi,width=20)
    entrada_xi.grid(row=4,column=2,pady=3,padx=4)

    Label(ingr_dat, text="Ingrese xf",font=("Century gothic",10),bg="PaleGreen1").grid(row=5,column=1,pady=3,padx=4)
    xf=DoubleVar()
    entrada_xf=Entry(ingr_dat,textvariable=xf,width=20)
    entrada_xf.insert(1,1)
    entrada_xf.grid(row=5,column=2,pady=3,padx=4)

    enviaBoton=Button(ingr_dat,text="Enviar",command=sendata)
    enviaBoton.grid(row=6,column=2,pady=3)

#Ventana para el método de punto medio 
def openRungeWindow():   

    newWindow = Toplevel(master) #cambiar nombres
    newWindow.title("Método de Runge Kutta")     
    newWindow.geometry("500x500") 
   # frame=Frame(newWindow).grid(row=10,bg='blue')
    #Funcion para el método de punto medio             
    ingr_dat=Frame(newWindow, bg="antique white", width = 500, height=500, pady=3, padx=15)
    ingr_dat.grid(sticky=EW)
    for i in range(0,4):
        ingr_dat.columnconfigure(i,weight=1)
   # ingr_dat.columnconfigure(1, weight=1)
   # ingr_dat.columnconfigure(1,weight=1)

    show_res=Frame(newWindow,width = 500, height=500, pady=3, padx=15)
    show_res.grid(sticky=EW)
    for i in range(0,5):
        show_res.columnconfigure(i,weight=1)
        #show_res.columnconfigure(1,weight=1)
        #show_res.columnconfigure(2,weight=1)
    def sendata():  #guardar la información que se ingresa
        funcion_data=str(funcion.get()) 
        funcion_data = sympify(funcion_data) #convertir la función en un objeto matemático 
        print(funcion_data,type(funcion_data)) 
        xinitial_value=float(xinitial.get())
        yinitial_value=float(yinitial.get())
        h_value=float(h.get())
      #  print("inicial valor de x y tipo",xinitial_value,type(xinitial_value))
        xf_value=float(xf.get())
        xi_value=float(xi.get())
        print(pto_medio(show_res,xinitial_value,yinitial_value,h_value,xi_value,xf_value,funcion_data))
    
    
    Label(ingr_dat,  
          text ="Ingrese la ecuación",width=20,font=("Century gothic",10),bg="antique white").grid(row=0,column=1,pady=3,padx=4)
    funcion=StringVar()
    entrada_funcion=Entry(ingr_dat,textvariable=funcion,width=20)
    entrada_funcion.insert(0,'(-2*(x**3))+12*(x**2)-(20*x)+8.5')
    entrada_funcion.grid(row=0,column=2,pady=3,padx=4)
    
    Label(ingr_dat, text="Ingrese el valor inicial de x",font=("Century gothic",10),bg="antique white").grid(row=1,column=1,pady=3,padx=4)
    xinitial=DoubleVar()
    entrada_xinitial=Entry(ingr_dat,textvariable=xinitial,width=20)
    entrada_xinitial.grid(row=1,column=2,pady=3,padx=4)

    Label(ingr_dat, text="Ingrese el valor inivial de y",font=("Century gothic",10),bg="antique white" ).grid(row=2,column=1,pady=3,padx=4)
    yinitial=DoubleVar()
    entrada_yinitial=Entry(ingr_dat,textvariable=yinitial,width=20)
    entrada_yinitial.grid(row=2,column=2,pady=3,padx=4)
    
    Label(ingr_dat, text="Ingrese h" ,font=("Century gothic",10),bg="antique white").grid(row=3,column=1,pady=3,padx=4)
    h=DoubleVar()
    entrada_h=Entry(ingr_dat,textvariable=h,width=20)
    entrada_h.insert(2,1)
    entrada_h.grid(row=3,column=2,pady=3,padx=4)

    Label(ingr_dat, text="Ingrese xi",font=("Century gothic",10),bg="antique white" ).grid(row=4,column=1,pady=3,padx=4)
    xi=DoubleVar()
    entrada_xi=Entry(ingr_dat,textvariable=xi,width=20)
    entrada_xi.grid(row=4,column=2,pady=3,padx=4)

    Label(ingr_dat, text="Ingrese xf",font=("Century gothic",10),bg="antique white" ).grid(row=5,column=1,pady=3,padx=4)
    xf=DoubleVar()
    entrada_xf=Entry(ingr_dat,textvariable=xf,width=20)
    entrada_xf.insert(1,1)
    entrada_xf.grid(row=5,column=2,pady=3,padx=4)

    enviaBoton=Button(ingr_dat,text="Enviar",command=sendata)
    enviaBoton.grid(row=6,column=2,pady=3)

#Ventana principal
#Leyenda 
label = Label(master, text ="Seleccionar un método") 
label.config(fg="black",    # Color letras
             bg="pink",   # Fondo
             font=("Century gothic",15,"bold")
              )
label.pack(pady=35)
#creación de botones
botonEuler=Button(master,text="Método de Euler",command=openEulerWindow)
botonEuler.config(bg="snow",font=("Century gothic",10))
botonEuler.pack(pady=5)
botonRunge=Button(master,text="Método de Runge-Kutta",command=openRungeWindow)
botonRunge.config(bg="snow",font=("Century gothic",10))
botonRunge.pack(pady=5)
botonPtomed=Button(master,text="Método del Punto medio",command=openPtomedioWindow)
botonPtomed.config(bg="snow",font=("Century gothic",10))
botonPtomed.pack(pady=5)
mainloop()
