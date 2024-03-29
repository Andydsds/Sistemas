from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
import sympy as sp
import numpy as np
from sympy import symbols, sympify
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #Graficar
#from tkinter.ttk import *
  
master = Tk()  #Pestaña principal
master.geometry("580x480")  #cambiar tamaño
master.title("Calculadora numérica")
master.config(bg="pink") #cambiar color de fondo 

x = sp.Symbol('x')
y = sp.Symbol('y')
#Leer cadena en caso de un numero y caracter juntos
def leer_string(cadena):
  lista=[]
 # cadena = cadena.replace("(","").replace(")","") #Eliminar parentesis
  for c in range(0,len(cadena)):
    if (cadena[c].isalpha() & cadena[c-1].isnumeric()):
      lista.append('*')
      lista.append(cadena[c])
    else:
      lista.append(cadena[c])
  cadena=''.join(lista)
  return cadena

#método de Euler y mostrar resultados
def mostrar_euler(window,x_num,y_num,h,xi,xf,expresion): 
    #Mostrar los resultados como matriz con barra de de desplazamiento
    #crear una vista de arbol y una barra de desplazamiento
    
    texto=Label(window, text ="Resultados",width=20,font=("Arial",17),bg="powder blue")
    texto.grid(row=0,column=1,columnspan=4)

    treev = ttk.Treeview(window)
    treev.grid(row=1,column=2,ipadx=15,pady=15,sticky=E)

    #barra de desplazamiento
    barra=ttk.Scrollbar(window,orient="vertical",command=treev.yview)
    barra.grid(row=1,column=3,pady=15,sticky=W)
    #configuracion del treeview
    treev.configure(xscrollcommand = barra.set)
    treev["columns"] = ("1", "2", "3") #Numero de columnas (i,x,y)
    treev['show'] = 'headings'
    # Asignar ancho de las columnas y centrar texto
    treev.column("1", width = 90, anchor ='c')
    treev.column("2", width = 90, anchor ='c')
    treev.column("3", width = 90, anchor ='c')
    #Titulo de encabezados
    treev.heading("1", text ="i")
    treev.heading("2", text ="x")
    treev.heading("3", text ="y")
    #Graficar
    figure = plt.Figure(figsize=(3,2.3), dpi=100)
    ax = figure.add_subplot(111)
    #Posicionar la gráfica
    grafica=FigureCanvasTkAgg(figure, window)
    grafica.get_tk_widget().grid(row=1,column=4,pady=15,padx=15)
    #Mensajes de error
    if (xf<xi):
        messagebox.showinfo(message="El valor de xi tiene que ser menor que xf ", title="Error")
    if (h<=0):
        messagebox.showinfo(message="El valor de h tiene que ser positivo ", title="Error")
    else:
        #Calculo de iteraciones
        nc=(xf-xi)/h
        nc=int(nc)
        for i in range(1,nc+1):
            try: 
                y_num=y_num+float(sp.N(expresion.subs(x, x_num)))*h #Evaluación numerica
            except:
                messagebox.showinfo(message="La función no está definida en el intervalo ", title="Error") 
            x_num=x_num+h
            x_num=round(x_num,2)
            y_num=round(y_num,3)
            
            #Imprimir resultados
            treev.insert("",'end',values=(i,x_num,y_num))
            ax.scatter(x_num, y_num)
            grafica.draw()

#Ingreso de datos Euler
def ingreso_euler():  
    #Generar una nueva ventana de ingreso de datos
    newWindow = Toplevel(master) 
    newWindow.title("Método de Euler")     
    newWindow.geometry("500x300") 
    newWindow.config(bg='powder blue')
    #Frame de ingreso de datos             
    ingr_dat=Frame(newWindow,bg='powder blue', pady=3, padx=15)
    ingr_dat.pack()
   
    #Función para obtener la información ingresada
    def sendata():  
        funcion_data=str(funcion.get()) 
        #Convertir string a un formato matemático
        funcion_data=leer_string(funcion_data)
        #convertir la función en un objeto matemático 
        funcion_data = sympify(funcion_data) 
        xinitial_value=float(xinitial.get())
        yinitial_value=float(yinitial.get())
        h_value=float(h.get())
        xf_value=float(xf.get())
        xi_value=float(xi.get())
        show_res=Toplevel(newWindow)
        show_res.geometry('650x300')
        show_res.config(bg='powder blue')
        mostrar_euler(show_res,xinitial_value,yinitial_value,h_value,xi_value,xf_value,funcion_data)
    
    #Etiquetas de ingreso de datos y entradas
    Label(ingr_dat,  
          text ="Ingrese la ecuación",width=20,font=("Century gothic",10),bg="powder blue").grid(row=0,column=1,pady=3,padx=4)
    funcion=StringVar()
    entrada_funcion=Entry(ingr_dat,textvariable=funcion,width=20)
    entrada_funcion.insert(0,'-2x^3+12x^2-20x+8.5') #Función predeterminada
    entrada_funcion.grid(row=0,column=2,pady=3,padx=4)
    
    Label(ingr_dat, text="Ingrese el valor inicial de x" ,font=("Century gothic",10),bg="powder blue").grid(row=1,column=1,pady=3,padx=4)
    xinitial=DoubleVar()
    entrada_xinitial=Entry(ingr_dat,textvariable=xinitial,width=20)
    entrada_xinitial.grid(row=1,column=2,pady=3,padx=4)

    Label(ingr_dat, text="Ingrese el valor inicial de y",font=("Century gothic",10),bg="powder blue").grid(row=2,column=1,pady=3,padx=4)
    yinitial=DoubleVar()
    entrada_yinitial=Entry(ingr_dat,textvariable=yinitial,width=20)
    entrada_yinitial.grid(row=2,column=2,pady=3,padx=4)
    
    Label(ingr_dat, text="Ingrese h",font=("Century gothic",10),bg="powder blue").grid(row=3,column=1,pady=3,padx=4)
    h=DoubleVar()
    entrada_h=Entry(ingr_dat,textvariable=h,width=20)
    entrada_h.insert(2,1)  #Valor predeterminado
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
    #Texto como nota 
    label2=Label(ingr_dat, text='*Si la función tiene en su expresión algún polinomio,\n ingrésalo en su forma más reducida')
    label2.config(fg="black",    # Color letras
             bg="powder blue",   # Fondo
             font=("Calibri Light",10)
              )
    label2.grid(row=7,column=1,columnspan=2,pady=15)

#Método del punto medio y mostrar resultados
def mostrar_ptomedio(window,x_num,y_num,h,xi,xf,expresion): 
    #Mostrar los resultados como matriz con barra de de desplazamiento
    #crear una vista de arbol y una barra de desplazamiento
    
    texto=Label(window, text ="Resultados",width=20,font=("Arial",17),bg="PaleGreen1")
    texto.grid(row=0,column=1,columnspan=4)

    treev = ttk.Treeview(window)
    treev.grid(row=1,column=2,ipadx=15,pady=15,sticky=E)

    #barra de desplazamiento
    barra=ttk.Scrollbar(window,orient="vertical",command=treev.yview)
    barra.grid(row=1,column=3,pady=15,sticky=W)
    #configuracion del treeview
    treev.configure(xscrollcommand = barra.set)
    treev["columns"] = ("1", "2", "3") #Numero de columnas (i,x,y)
    treev['show'] = 'headings'
    # Asignar ancho de las columnas y centrar texto
    treev.column("1", width = 90, anchor ='c')
    treev.column("2", width = 90, anchor ='c')
    treev.column("3", width = 90, anchor ='c')
    #Titulo de encabezados
    treev.heading("1", text ="i")
    treev.heading("2", text ="x")
    treev.heading("3", text ="y")
    #Graficar
    figure = plt.Figure(figsize=(3,2.3), dpi=100)
    ax = figure.add_subplot(111)
    #Posicionar la gráfica
    grafica=FigureCanvasTkAgg(figure, window)
    grafica.get_tk_widget().grid(row=1,column=4,pady=15,padx=15)
    #Mensajes de error
    if (xf<xi):
        messagebox.showinfo(message="El valor de xi tiene que ser menor que xf ", title="Error")
    if (h<=0):
        messagebox.showinfo(message="El valor de h tiene que ser positivo ", title="Error")
    else:
        #Calculo de iteraciones
        nc=(xf-xi)/h
        nc=int(nc)
        for i in range(1,nc+1):
            try: 
                ym=y_num+float(sp.N(expresion.subs(x, x_num)))*(h/2) #Evaluación numerica
            except:
                messagebox.showinfo(message="La función no está definida en el intervalo ", title="Error") 
            xm=x_num+h/2
            y_num=ym+float(expresion.subs(x,xm))*h
            x_num=xm+h/2
            x_num=round(x_num, 2)
            y_num=round(y_num, 3)
            
            #Imprimir resultados
            treev.insert("",'end',values=(i,x_num,y_num))
            ax.scatter(x_num, y_num)
            grafica.draw()

#Ingreso de datos método del punto medio
def ingreso_ptomedio():  
    #Generar una nueva ventana de ingreso de datos
    newWindow = Toplevel(master) 
    newWindow.title("Método del punto medio")     
    newWindow.geometry("500x300") 
    newWindow.config(bg='PaleGreen1')
    #Frame de ingreso de datos             
    ingr_dat=Frame(newWindow,bg='PaleGreen1', pady=3, padx=15)
    ingr_dat.pack()
   
    #Función para obtener la información ingresada
    def sendata():  
        funcion_data=str(funcion.get()) 
        #Convertir string a un formato matemático
        funcion_data=leer_string(funcion_data)
        #convertir la función en un objeto matemático 
        funcion_data = sympify(funcion_data) 
        xinitial_value=float(xinitial.get())
        yinitial_value=float(yinitial.get())
        h_value=float(h.get())
        xf_value=float(xf.get())
        xi_value=float(xi.get())
        show_res=Toplevel(newWindow)
        show_res.geometry('650x300')
        show_res.config(bg='PaleGreen1')
        mostrar_ptomedio(show_res,xinitial_value,yinitial_value,h_value,xi_value,xf_value,funcion_data)
    
    #Etiquetas de ingreso de datos y entradas
    Label(ingr_dat,  
          text ="Ingrese la ecuación",width=20,font=("Century gothic",10),bg="PaleGreen1").grid(row=0,column=1,pady=3,padx=4)
    funcion=StringVar()
    entrada_funcion=Entry(ingr_dat,textvariable=funcion,width=20)
    entrada_funcion.insert(0,'-2x^3+12x^2-20x+8.5') #Función predeterminada
    entrada_funcion.grid(row=0,column=2,pady=3,padx=4)
    
    Label(ingr_dat, text="Ingrese el valor inicial de x" ,font=("Century gothic",10),bg="PaleGreen1").grid(row=1,column=1,pady=3,padx=4)
    xinitial=DoubleVar()
    entrada_xinitial=Entry(ingr_dat,textvariable=xinitial,width=20)
    entrada_xinitial.grid(row=1,column=2,pady=3,padx=4)

    Label(ingr_dat, text="Ingrese el valor inicial de y",font=("Century gothic",10),bg="PaleGreen1").grid(row=2,column=1,pady=3,padx=4)
    yinitial=DoubleVar()
    entrada_yinitial=Entry(ingr_dat,textvariable=yinitial,width=20)
    entrada_yinitial.grid(row=2,column=2,pady=3,padx=4)
    
    Label(ingr_dat, text="Ingrese h",font=("Century gothic",10),bg="PaleGreen1").grid(row=3,column=1,pady=3,padx=4)
    h=DoubleVar()
    entrada_h=Entry(ingr_dat,textvariable=h,width=20)
    entrada_h.insert(2,1)  #Valor predeterminado
    entrada_h.grid(row=3,column=2,pady=3,padx=4)

    Label(ingr_dat, text="Ingrese xi",font=("Century gothic",10),bg="PaleGreen1").grid(row=4,column=1,pady=3,padx=4)
    xi=DoubleVar()
    entrada_xi=Entry(ingr_dat,textvariable=xi,width=20)
    entrada_xi.grid(row=4,column=2,pady=3,padx=4)

    Label(ingr_dat, text="Ingrese xf",font=("Century gothic",10),bg="PaleGreen1").grid(row=5,column=1,pady=3,padx=4)
    xf=DoubleVar()
    entrada_xf=Entry(ingr_dat,textvariable=xf,width=20)
    entrada_xf.insert(1,1) #valor predeterminado
    entrada_xf.grid(row=5,column=2,pady=3,padx=4)

    enviaBoton=Button(ingr_dat,text="Enviar",command=sendata)
    enviaBoton.grid(row=6,column=2,pady=3)
    #Texto como nota 
    label2=Label(ingr_dat, text='*Si la función tiene en su expresión algún polinomio,\n ingrésalo en su forma más reducida')
    label2.config(fg="black",    # Color letras
             bg="PaleGreen1",   # Fondo
             font=("Calibri Light",10)
              )
    label2.grid(row=7,column=1,columnspan=2,pady=15)

#Ventana para el método de RungeKutta 
#antique white

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

    Label(ingr_dat, text="Ingrese el valor inicial de y",font=("Century gothic",10),bg="antique white" ).grid(row=2,column=1,pady=3,padx=4)
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
    
    label2=Label(master, text='*Si la función tiene en su expresión algún polinomio,\n ingrésalo en su forma más reducida')
    label2.config(fg="black",    # Color letras
             bg="pink",   # Fondo
             font=("Calibri Light",10)
              )
    label2.pack(side=BOTTOM)

def mostrar_runge(window,x_num,y_num,h,xi,xf,expresion): 
    #Mostrar los resultados como matriz con barra de de desplazamiento
    #crear una vista de arbol y una barra de desplazamiento
    
    texto=Label(window, text ="Resultados",width=20,font=("Arial",17),bg="antique white")
    texto.grid(row=0,column=1,columnspan=4)

    treev = ttk.Treeview(window)
    treev.grid(row=1,column=2,ipadx=15,pady=15,sticky=E)

    #barra de desplazamiento
    barra=ttk.Scrollbar(window,orient="vertical",command=treev.yview)
    barra.grid(row=1,column=3,pady=15,sticky=W)
    #configuracion del treeview
    treev.configure(xscrollcommand = barra.set)
    treev["columns"] = ("1", "2", "3") #Numero de columnas (i,x,y)
    treev['show'] = 'headings'
    # Asignar ancho de las columnas y centrar texto
    treev.column("1", width = 90, anchor ='c')
    treev.column("2", width = 90, anchor ='c')
    treev.column("3", width = 90, anchor ='c')
    #Titulo de encabezados
    treev.heading("1", text ="i")
    treev.heading("2", text ="x")
    treev.heading("3", text ="y")
    #Graficar
    figure = plt.Figure(figsize=(3,2.3), dpi=100)
    ax = figure.add_subplot(111)
    #Posicionar la gráfica
    grafica=FigureCanvasTkAgg(figure, window)
    grafica.get_tk_widget().grid(row=1,column=4,pady=15,padx=15)
    #Mensajes de error
    if (xf<xi):
        messagebox.showinfo(message="El valor de xi tiene que ser menor que xf ", title="Error")
    if (h<=0):
        messagebox.showinfo(message="El valor de h tiene que ser positivo ", title="Error")
    else:
        #Calculo de iteraciones
        nc=(xf-xi)/h
        nc=int(nc)
        for i in range(1,nc+1):
            try:
                k1_num=float(sp.N(expresion.subs(x,x_num)))
                k2_num=float(sp.N(expresion.subs(x,x_num+h))) #Evaluación numerica
            except:
                messagebox.showinfo(message="La función no está definida en el intervalo ", title="Error") 
            x_num=x_num+h
            y_num=y_num+(k1_num/2+k2_num/2)*h
            x_num=round(x_num,2)
            y_num=round(y_num,3)
            
            #Imprimir resultados
            treev.insert("",'end',values=(i,x_num,y_num))
            ax.scatter(x_num, y_num)
            grafica.draw()

def ingreso_Runge():  
    #Generar una nueva ventana de ingreso de datos
    newWindow = Toplevel(master) 
    newWindow.title("Método de Runge-Kutta 2o orden")     
    newWindow.geometry("500x300") 
    newWindow.config(bg='antique white')
    #Frame de ingreso de datos             
    ingr_dat=Frame(newWindow,bg='antique white', pady=3, padx=15)
    ingr_dat.pack()
   
    #Función para obtener la información ingresada
    def sendata():  
        funcion_data=str(funcion.get()) 
        #Convertir string a un formato matemático
        funcion_data=leer_string(funcion_data)
        #convertir la función en un objeto matemático 
        funcion_data = sympify(funcion_data) 
        xinitial_value=float(xinitial.get())
        yinitial_value=float(yinitial.get())
        h_value=float(h.get())
        xf_value=float(xf.get())
        xi_value=float(xi.get())
        show_res=Toplevel(newWindow)
        show_res.geometry('650x300')
        show_res.config(bg='antique white')
        mostrar_runge(show_res,xinitial_value,yinitial_value,h_value,xi_value,xf_value,funcion_data)
    
    #Etiquetas de ingreso de datos y entradas
    Label(ingr_dat,  
          text ="Ingrese la ecuación",width=20,font=("Century gothic",10),bg="antique white").grid(row=0,column=1,pady=3,padx=4)
    funcion=StringVar()
    entrada_funcion=Entry(ingr_dat,textvariable=funcion,width=20)
    entrada_funcion.insert(0,'-2x^3+12x^2-20x+8.5') #Función predeterminada
    entrada_funcion.grid(row=0,column=2,pady=3,padx=4)
    
    Label(ingr_dat, text="Ingrese el valor inicial de x" ,font=("Century gothic",10),bg="antique white").grid(row=1,column=1,pady=3,padx=4)
    xinitial=DoubleVar()
    entrada_xinitial=Entry(ingr_dat,textvariable=xinitial,width=20)
    entrada_xinitial.grid(row=1,column=2,pady=3,padx=4)

    Label(ingr_dat, text="Ingrese el valor inivial de y",font=("Century gothic",10),bg="antique white").grid(row=2,column=1,pady=3,padx=4)
    yinitial=DoubleVar()
    entrada_yinitial=Entry(ingr_dat,textvariable=yinitial,width=20)
    entrada_yinitial.grid(row=2,column=2,pady=3,padx=4)
    
    Label(ingr_dat, text="Ingrese h",font=("Century gothic",10),bg="antique white").grid(row=3,column=1,pady=3,padx=4)
    h=DoubleVar()
    entrada_h=Entry(ingr_dat,textvariable=h,width=20)
    entrada_h.insert(2,1)  #Valor predeterminado
    entrada_h.grid(row=3,column=2,pady=3,padx=4)

    Label(ingr_dat, text="Ingrese xi",font=("Century gothic",10),bg="antique white").grid(row=4,column=1,pady=3,padx=4)
    xi=DoubleVar()
    entrada_xi=Entry(ingr_dat,textvariable=xi,width=20)
    entrada_xi.grid(row=4,column=2,pady=3,padx=4)

    Label(ingr_dat, text="Ingrese xf",font=("Century gothic",10),bg="antique white").grid(row=5,column=1,pady=3,padx=4)
    xf=DoubleVar()
    entrada_xf=Entry(ingr_dat,textvariable=xf,width=20)
    entrada_xf.insert(1,1) #valor predeterminado
    entrada_xf.grid(row=5,column=2,pady=3,padx=4)

    enviaBoton=Button(ingr_dat,text="Enviar",command=sendata)
    enviaBoton.grid(row=6,column=2,pady=3)
    #Texto como nota 
    label2=Label(ingr_dat, text='*Si la función tiene en su expresión algún polinomio,\n ingrésalo en su forma más reducida')
    label2.config(fg="black",    # Color letras
             bg="antique white",   # Fondo
             font=("Calibri Light",10)
              )
    label2.grid(row=7,column=1,columnspan=2,pady=15)



#Ventana principal
#Leyendas
label = Label(master, text ="Calculadora numérica de EDOs \n de primer orden") 
label.config(fg="black",    # Color letras
             bg="pink",   # Fondo
             font=("Calibri Light",16,"bold")
              )
label.pack(pady=25)
label2=Label(master, text='Este programa resuelve ecuaciones diferenciales ordinarias de primer grado,\n de la forma y´=f(x) mediante 3 métodos numéricos distintos \n \nSelecciona el método:')
label2.config(fg="black",    # Color letras
             bg="pink",   # Fondo
             font=("Calibri Light",13)
              )
label2.pack(pady=9)
#creación de botones de ventana principal
botonEuler=Button(master,text="Método de Euler",command=ingreso_euler)
botonEuler.config(bg="snow",font=("Calibri Light",13,"italic"))
botonEuler.pack(pady=7)
botonRunge=Button(master,text="Método de Runge-Kutta",command=ingreso_Runge)
botonRunge.config(bg="snow",font=("Calibri Light",13,"italic"))
botonRunge.pack(pady=7)
botonPtomed=Button(master,text="Método del Punto medio",command=ingreso_ptomedio)
botonPtomed.config(bg="snow",font=("Calibri Light",13,"italic"))
botonPtomed.pack(pady=7)

mainloop()



