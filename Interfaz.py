import tkinter as tk
from tkinter import *
#from tkintermapview import TkinterMapView
from tkinter import messagebox
import os
#import requests
    
#------------------------------------------------------------------------------------------------------------#
def soporte_tecnico():
    global soporte
    soporte = tk.Toplevel(main_screen)
    soporte.title("Soporte Tecnico")
    soporte.geometry("400x400")
    soporte.configure(background="grey")
    
    tk.Label(soporte, text="Ingrese sus datos personales y su queja", bg="green", width="40", height="2", font=("Copperplate Gothic Bold", 13)).pack()
    tk.Label(soporte, text="", bg="grey").pack()
    
    global soporte_text 
    soporte_text = tk.Text(soporte, height=10, width=50)   #Variable para almacenar la opinion del usuario
    soporte_text.pack()
    tk.Label(soporte, text="", bg="grey").pack()
    
    tk.Button(soporte, text="Enviar Numero", height="2", bg="skyblue",command=soporteinfo, width="30", font=("Copperplate Gothic Bold", 15)).pack()
    tk.Label(soporte, text="", bg="grey").pack()
    
    tk.Button(soporte, text="Volver", height="2", bg="skyblue",command=delete_soporte, width="30", font=("Copperplate Gothic Bold", 15)).pack()
    
def delete_soporte(): 
    soporte.destroy()    
    
def soporteinfo():
    soporteinfo = soporte_text.get("1.0", tk.END).strip()
    if soporteinfo:
        with open("soporte.txt", "a") as file:
            file.write(soporteinfo + "\n---\n")
        soporte_text.delete("1.0", tk.END)  
        messagebox.showinfo("Exito", "Soporte se comunicara contigo en breve")
    else:
        messagebox.showwarning("Advertencia", "No puede estar vacia la información")
        
    

#------------------------------------------------------------------------------------------------------------#

# Función para mostrar ventana al ser el login exitoso
def login_success():
    global login_success_screen
    login_success_screen = tk.Toplevel(main_screen)
    login_success_screen.title("LoginExitoso")
    login_success_screen.geometry("500x500")
    login_success_screen.configure(background="grey")

    tk.Label(login_success_screen, text="Login Exitoso- Bienvenido al Sistema", bg="green", width="40", height="2" ,font=("Copperplate Gothic Bold", 15)).pack()
    tk.Label(login_success_screen, text="", bg="grey").pack()

    tk.Button(login_success_screen, text="Ver Rutas", height="2",bg="skyblue",command=ver_rutas , width="28" ,font=("Copperplate Gothic Bold", 13)).pack()
    tk.Label(login_success_screen, text="", bg="grey").pack()

    tk.Button(login_success_screen, text="Ver Destino", height="2",bg="skyblue" , width="28" ,font=("Copperplate Gothic Bold", 13)).pack()
    tk.Label(login_success_screen, text="", bg="grey").pack()

    tk.Button(login_success_screen, text="Ver carga del camion", height="2",bg="skyblue", command=carga_camion, width="28", font=("Copperplate Gothic Bold", 13)).pack()
    tk.Label(login_success_screen, text="", bg="grey").pack()

    tk.Button(login_success_screen, text="Deja tu Opinion", height="2",bg="skyblue", command=opiniones, width="28", font=("Copperplate Gothic Bold", 13)).pack()
    tk.Label(login_success_screen, text="", bg="grey").pack()

    tk.Button(login_success_screen, text="Recompensas", height="2",bg="skyblue", command=recompensa_viajes, width="28", font=("Copperplate Gothic Bold", 13)).pack()
    tk.Label(login_success_screen, text="", bg="grey").pack()

    tk.Button(login_success_screen, text="Volver", height="2", bg="skyblue", width="28", command= delete_login_success, font=("Copperplate Gothic Bold", 13)).pack()

# Función para eliminar ventana emergente de login exitoso
def delete_login_success():
    login_success_screen.destroy()

#------------------------------------------------------------------------------------------------------------#

def recompensa_viajes():
    global recompensa_viajes_screen
    recompensa_viajes_screen=tk.Toplevel(login_success_screen)
    recompensa_viajes_screen.title("Recompensa en base a lo que se cumplio")
    recompensa_viajes_screen.geometry("500x500")
    recompensa_viajes_screen.configure(background="grey")
    tk.Label(recompensa_viajes_screen, text="Objetivos cumplidos:", bg="green", width="40", height="2", font=("Copperplate Gothic Bold", 15)).pack()
    tk.Label(recompensa_viajes_screen, text="", bg="grey").pack()

    tk.Label(recompensa_viajes_screen, text="| Puntos acumulados= 15000 |", bg="grey",font=("Copperplate Gothic Bold", 10)).pack()
    tk.Label(recompensa_viajes_screen, text="| Entrega en la fecha destinada -----> Se entrego en la fecha pactada |", bg="grey",font=("Copperplate Gothic Bold", 10)).pack()
    tk.Label(recompensa_viajes_screen, text="| Combustible gastado -----> 228 Litros |", bg="grey",font=("Copperplate Gothic Bold", 10)).pack()
    tk.Label(recompensa_viajes_screen, text="| Sin complicaciones -----> No hubo complicaciones en la ruta |", bg="grey",font=("Copperplate Gothic Bold", 10)).pack()
    tk.Label(recompensa_viajes_screen, text="| A ganado 1500 puntos |", bg="grey",font=("Copperplate Gothic Bold", 10)).pack()
    tk.Label(recompensa_viajes_screen, text="| Puntos totales = 16500 puntos |", bg="grey",font=("Copperplate Gothic Bold",10)).pack()
    tk.Label(recompensa_viajes_screen, text="", bg="grey")
    tk.Button(recompensa_viajes_screen, text="Volver", height="2", bg="skyblue", width="28", command= delete_recompensas, font=("Copperplate Gothic Bold", 13)).pack()

def delete_recompensas():
    recompensa_viajes_screen.destroy()
#------------------------------------------------------------------------------------------------------------#

def opiniones():
    global opiniones_screen
    opiniones_screen=tk.Toplevel(login_success_screen)
    opiniones_screen.title("Deja la opinion del viaje")
    opiniones_screen.geometry("500x500")
    opiniones_screen.configure(background="grey")

    tk.Label(opiniones_screen, text="Deje su opinión sobre el viaje", bg="green", width="40", height="2", font=("Copperplate Gothic Bold", 15)).pack()
    tk.Label(opiniones_screen, text="", bg="grey").pack()

    global opinion_text 
    opinion_text = tk.Text(opiniones_screen, height=10, width=50)   #Variable para almacenar la opinion del usuario
    opinion_text.pack()
    tk.Label(opiniones_screen, text="", bg="grey").pack()

    tk.Button(opiniones_screen, text="Enviar Opinión", height="2", bg="skyblue", command= guardar_opinion, width="30", font=("Copperplate Gothic Bold", 15)).pack()
    tk.Label(opiniones_screen, text="", bg="grey").pack()

    tk.Button(opiniones_screen, text="Volver", height="2", bg="skyblue", width="30", command=delete_opiniones, font=("Copperplate Gothic Bold", 15)).pack()

def guardar_opinion():
    opinion = opinion_text.get("1.0", tk.END).strip()
    if opinion:
        with open("opiniones.txt", "a") as file:
            file.write(opinion + "\n---\n")
        opinion_text.delete("1.0", tk.END)  
        messagebox.showinfo("Exito", "Opinion Enviada Exitosamente")
    else:
        messagebox.showwarning("Advertencia", "La opinion no puede estar vacia")

def delete_opiniones():
    opiniones_screen.destroy()

#------------------------------------------------------------------------------------------------------------#
def ver_rutas():
    global ver_rutas_screen
    ver_rutas_screen = tk.Toplevel(login_success_screen)
    ver_rutas_screen.title("Rutas Disponibles")
    ver_rutas_screen.geometry("500x500")
    ver_rutas_screen.configure(background="grey")

    tk.Label(ver_rutas_screen, text="Rutas Disponibles", bg="green", width="40", height="2" ,font=("Copperplate Gothic Bold", 15)).pack()
    tk.Label(ver_rutas_screen, text="", bg="grey").pack()

    tk.Button(ver_rutas_screen, text="Ruta 1", height="2",bg="skyblue",command=ruta1 , width="30" ,font=("Copperplate Gothic Bold", 15)).pack()
    tk.Label(ver_rutas_screen, text="", bg="grey").pack()

    tk.Button(ver_rutas_screen, text="Ruta 2", height="2",bg="skyblue",command=ruta2 , width="30" ,font=("Copperplate Gothic Bold", 15)).pack()
    tk.Label(ver_rutas_screen, text="", bg="grey").pack()

    tk.Button(ver_rutas_screen, text="Volver", height="2", bg="skyblue", width="30", command= delete_ver_rutas, font=("Copperplate Gothic Bold", 15)).pack()

# Función para eliminar ventana de las rutas
def delete_ver_rutas():
    ver_rutas_screen.destroy()

def ruta1():
    global ruta1_screen
    ruta1_screen= tk.Toplevel(ver_rutas_screen)
    ruta1_screen.title("Ruta 1")
    ruta1_screen.geometry("500x500")
    ruta1_screen.configure(background="grey")
    
    tk.Label(ruta1_screen, text="Informacion de la Ruta 1:", bg="skyblue", width="40", height="2" ,font=("Copperplate Gothic Bold", 15)).pack()
    tk.Label(ruta1_screen, text="", bg="grey").pack()
    tk.Label(ruta1_screen, text="| Cantidad de peajes -----> 3 Peajes |",bg="grey",font=("Copperplate Gothic Bold", 12)).pack()
    tk.Label(ruta1_screen, text="| Trafico -----> Trafico devido a un accidente |",bg="grey",font=("Copperplate Gothic Bold", 12)).pack()
    tk.Label(ruta1_screen, text="| Clima de la ruta -----> Soleado |",bg="grey",font=("Copperplate Gothic Bold", 12)).pack()
    tk.Label(ruta1_screen, text="| Hora Aproximada de llegada -----> 10:20 hora |",bg="grey",font=("Copperplate Gothic Bold", 12)).pack()
    tk.Label(ruta1_screen, text="| Tanque -----> Tanque lleno |",bg="grey",font=("Copperplate Gothic Bold", 12)).pack()
    tk.Label(ruta1_screen, text="| Cortes de ruta -----> Sin cortes |",bg="grey",font=("Copperplate Gothic Bold", 12)).pack()
    tk.Label(ruta1_screen, text="| Consumo aproximado de combustible -----> 250 Litros |",bg="grey",font=("Copperplate Gothic Bold", 12)).pack()
    tk.Label(ruta1_screen, text="", bg="grey")

    tk.Button(ruta1_screen, text="Ver Mapa", height="2", bg="skyblue", width="30", command= ver_maparuta1, font=("Copperplate Gothic Bold", 15)).pack()
    tk.Button(ruta1_screen, text="Paradas de Descanso", height="2", bg="skyblue", width="30", command= paradas_descanso1, font=("Copperplate Gothic Bold", 15)).pack()
    tk.Button(ruta1_screen, text="Volver", height="2", bg="skyblue", width="30", command= ruta1_delete, font=("Copperplate Gothic Bold", 15)).pack()

def ruta1_delete():
    ruta1_screen.destroy()

def paradas_descanso1():
    global paradasD1_screen
    paradasD1_screen= tk.Toplevel(ver_rutas_screen)
    paradasD1_screen.title("Mapa - Ruta 1")
    paradasD1_screen.geometry("500x500")
    paradasD1_screen.configure(background="grey")

    #
    #label.pack()

    tk.Button(paradasD1_screen, text="Volver", height="2", bg="skyblue", width="30", command= delete_descanso1, font=("Copperplate Gothic Bold", 15)).pack()

def delete_descanso1():
    paradasD1_screen.destroy()

def ver_maparuta1():
    global ruta1mapa_screen
    ruta1mapa_screen= tk.Toplevel(ver_rutas_screen)
    ruta1mapa_screen.title("Mapa - Ruta 1")
    ruta1mapa_screen.geometry("500x500")
    ruta1mapa_screen.configure(background="grey")
    
    tk.Button(ruta1mapa_screen, text="Volver", height="2", bg="skyblue", width="30", command= ruta1mapa_delete, font=("Copperplate Gothic Bold", 15)).pack()

def ruta1mapa_delete():
    ruta1mapa_screen.destroy()

def ruta2():
    global ruta2_screen
    ruta2_screen= tk.Toplevel(ver_rutas_screen)
    ruta2_screen.title("Ruta 2")
    ruta2_screen.geometry("500x500")
    ruta2_screen.configure(background="grey")
    
    tk.Label(ruta2_screen, text="Informacion de la Ruta 2:", bg="skyblue", width="40", height="2" ,font=("Copperplate Gothic Bold", 15)).pack()
    tk.Label(ruta2_screen, text="", bg="grey").pack()
    tk.Label(ruta2_screen, text="| Cantidad de peajes -----> 1 Peajes |",bg="grey",font=("Copperplate Gothic Bold", 12)).pack()
    tk.Label(ruta2_screen, text="| Trafico -----> Trafico libre |",bg="grey",font=("Copperplate Gothic Bold", 12)).pack()
    tk.Label(ruta2_screen, text="| Clima de la ruta -----> Nublado |",bg="grey",font=("Copperplate Gothic Bold", 12)).pack()
    tk.Label(ruta2_screen, text="| Hora Aproximada de llegada -----> 9:20 horas |",bg="grey",font=("Copperplate Gothic Bold", 12)).pack()
    tk.Label(ruta2_screen, text="| Tanque -----> Tanque lleno |",bg="grey",font=("Copperplate Gothic Bold", 12)).pack()
    tk.Label(ruta2_screen, text="| Cortes de ruta -----> Sin cortes |",bg="grey",font=("Copperplate Gothic Bold", 12)).pack()
    tk.Label(ruta2_screen, text="| Consumo aproximado de combustible -----> 228 Litros |",bg="grey",font=("Copperplate Gothic Bold", 12)).pack()
    tk.Label(ruta2_screen, text="", bg="grey")
    tk.Label(ruta2_screen, text="", bg="grey")

    tk.Button(ruta2_screen, text="Ver Mapa", height="2", bg="skyblue", width="30", command= ver_maparuta2, font=("Copperplate Gothic Bold", 15)).pack()
    tk.Button(ruta2_screen, text="Paradas de Descanso", height="2", bg="skyblue", width="30", command= paradas_descanso2, font=("Copperplate Gothic Bold", 15)).pack()
    tk.Button(ruta2_screen, text="Volver", height="2", bg="skyblue", width="30", command= ruta2_delete, font=("Copperplate Gothic Bold", 15)).pack()

def ruta2_delete():
    ruta2_screen.destroy()

def ruta1_delete():
    ruta1_screen.destroy()

def paradas_descanso2():
    global paradasD2_screen
    paradasD2_screen= tk.Toplevel(ver_rutas_screen)
    paradasD2_screen.title("Mapa - Ruta 1")
    paradasD2_screen.geometry("500x500")
    paradasD2_screen.configure(background="grey")


    tk.Button(paradasD2_screen, text="Volver", height="2", bg="skyblue", width="30", command= delete_descanso2, font=("Copperplate Gothic Bold", 15)).pack()

def delete_descanso2():
    paradasD2_screen.destroy()


def ver_maparuta2():
    global ruta2mapa_screen
    ruta2mapa_screen= tk.Toplevel(ver_rutas_screen)
    ruta2mapa_screen.title("Mapa - Ruta 2")
    ruta2mapa_screen.geometry("500x500")
    ruta2mapa_screen.configure(background="grey")
     
#
    
#
    tk.Button(ruta2mapa_screen, text="Volver", height="2", bg="skyblue", width="30", command= ruta2mapa_delete, font=("Copperplate Gothic Bold", 15)).pack()

def ruta2mapa_delete():
    ruta2mapa_screen.destroy()

#------------------------------------------------------------------------------------------------------------#
        
#Funcion para poder visualizar la carga del camion
def carga_camion():
    global cargacamion_screen
    cargacamion_screen = tk.Toplevel(login_success_screen)
    cargacamion_screen.title("Carga del Camion")
    cargacamion_screen.geometry("500x500")
    cargacamion_screen.configure(background="grey")
    
    tk.Label(cargacamion_screen, text="Carga del Camion", bg="green", width="40", height="2" ,font=("Copperplate Gothic Bold", 15)).pack()
    tk.Label(cargacamion_screen, text="", bg="grey").pack()
    tk.Label(cargacamion_screen, text="| Conductor del camion -----> Juan Jose Caceres      |",bg="grey",font=("Copperplate Gothic Bold", 12)).pack()
    tk.Label(cargacamion_screen, text="| Numero de DNI del conductor -----> 46.066.266      |",bg="grey",font=("Copperplate Gothic Bold", 12)).pack()
    tk.Label(cargacamion_screen, text="| Camión -----> Man TGS 26.480 6x2 BLS               |",bg="grey",font=("Copperplate Gothic Bold", 12)).pack()
    tk.Label(cargacamion_screen, text="| Patente del camion -----> AF-147-MF                |",bg="grey",font=("Copperplate Gothic Bold", 12)).pack()
    tk.Label(cargacamion_screen, text="| Cantidad de madera transportada -----> 40 Toneladas|",bg="grey",font=("Copperplate Gothic Bold", 12)).pack()
    tk.Label(cargacamion_screen, text="| Tipo de madera transportada -----> Madera de Pino  |",bg="grey",font=("Copperplate Gothic Bold", 12)).pack()
    tk.Label(cargacamion_screen, text="| Corte de la madera transportada -----> Tipo Tabla  |",bg="grey",font=("Copperplate Gothic Bold", 12)).pack()
    tk.Label(cargacamion_screen, text="| Ubicacion Actual -----> RN118 Santa Rosa Corrientes|",bg="grey",font=("Copperplate Gothic Bold", 12)).pack()
    tk.Label(cargacamion_screen, text="| Destino  -----> Puerto de Rosario, Rosario, Sta. Fe|",bg="grey",font=("Copperplate Gothic Bold", 12)).pack()
    tk.Label(cargacamion_screen, text="| Fecha de Salida  -----> 20 de Julio del 2024       |",bg="grey",font=("Copperplate Gothic Bold", 12)).pack()
    tk.Label(cargacamion_screen, text="", bg="grey").pack()
    tk.Button(cargacamion_screen, text="Volver", height="2", bg="skyblue", width="30", command= delete_carga_camion, font=("Copperplate Gothic Bold", 15)).pack()#Conductor del camion

#Funcion para eliminar la ventana de la info de la carga del camion en caso de querer VOLVER
def delete_carga_camion():
    cargacamion_screen.destroy()

#------------------------------------------------------------------------------------------------------------#

#------------------------------------------------------------------------------------------------------------#
# Función para mostrar la ventana principal
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.configure(background="white")
    main_screen.geometry("500x500")
    main_screen.title("Consumo Kirchhof")

    #

    Label(text="").pack()
    
    Label(text="Bienvenido a KirchhCal", bg="black", width="20", height="2", font=("Copperplate Gothic Bold", 15)).pack()
    Label(text="").pack()

    Button(text="Calcular Consumo", height="2",bg="black", width="12",border=4, font=("Copperplate Gothic Bold", 13), command=login_success).pack()
    Label(text="").pack()

    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    
    Label(text="@IMERSYS", fg="black", width="10", height="2", font=("Copperplate Gothic Bold", 12)).pack()

    main_screen.mainloop()

main_account_screen()