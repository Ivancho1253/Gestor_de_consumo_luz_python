import tkinter as tk
from tkinter import messagebox

# Función para calcular corriente y facturación
def calcular_facturacion():
    try:
        # Obtiene los valores ingresados
        consumoI = float(entry_consumoI.get())  # en kWh Inicial
        consumoF = float(entry_consumoF.get())  # en kWh Final
        tension = float(entry_tension.get())  # en Voltios

        # Cálculo para obtener el consumo actual
        consumo = consumoF - consumoI

        if consumo < 0:
            raise ValueError("El consumo final debe ser mayor o igual al consumo inicial.")

        # Cálculo de la corriente
        potencia = consumo * 1000  # Convertir kWh a W (1 kWh = 1000 W)
        corriente = potencia / tension  # I = P / V

        # Cálculo de facturación por tramos
        facturacion = 0

        # Tramo 1: 0 a 600 kWh
        if consumo > 600:
            facturacion += 600 * 123.9694
            consumo -= 600
        else:
            facturacion += consumo * 123.9694
            consumo = 0

        # Tramo 2: 600 a 742 kWh
        if consumo > 142:  # 742 - 600 = 142
            facturacion += 142 * 134.8474
            consumo -= 142
        else:
            facturacion += consumo * 134.8474
            consumo = 0

        # Tramo 3: 742 a 785 kWh
        if consumo > 43:  # 785 - 742 = 43
            facturacion += 43 * 162.1050
            consumo -= 43
        else:
            facturacion += consumo * 162.1050
            consumo = 0

        # Tramo 4: Más de 785 kWh
        if consumo > 0:
            facturacion += consumo * 166.658

        # Se le resta 800 del beneficio social y se le suma 11421.888 del cargo fijo x suministro
        facturacion = ((facturacion - 800) + 11421.888)

        # Se le descuenta el subsidio del 20%
        facturacion_bimestral_basico = facturacion - (facturacion * 0.2)
        label_facturacionBimestralBasico_resultado.config(text=f"${facturacion_bimestral_basico:.2f}")

        # Facturación después de agregar el alumbrado público y el IVA
        facturacion_final = facturacion_bimestral_basico
        # Le agregamos el alumbrado público (2.8%)
        facturacion_final += facturacion_final * 0.028

        # Le agregamos el IVA (21%)
        facturacion_final += facturacion_final * 0.21

        # Mostramos los resultados en las etiquetas
        label_consumo_actual_resultado.config(text=f"{(consumoF - consumoI):.2f} kWh")
        label_corriente_resultado.config(text=f"{corriente:.2f} A")
        label_facturacion_resultado.config(text=f"${facturacion_final:.2f}")

    except ValueError as e:
        messagebox.showerror("Entrada inválida", str(e))

# Función para cambiar de pantalla a la de cálculo
def mostrar_calculadora():
    pantalla_bienvenida.pack_forget()
    pantalla_calculo.pack()

# Interfaz de bienvenida
def crear_pantalla_bienvenida(root):
    global pantalla_bienvenida
    pantalla_bienvenida = tk.Frame(root, bg='blue')  # Fondo azul
    pantalla_bienvenida.pack()

    label_bienvenida = tk.Label(pantalla_bienvenida, text="Bienvenido al Sistema de Facturación", font=("Helvetica", 16), fg="yellow", bg="blue")  # Texto amarillo
    label_bienvenida.pack(pady=20)

    boton_empezar = tk.Button(pantalla_bienvenida, text="Empezar", font=("Helvetica", 12), fg="yellow", bg="blue", command=mostrar_calculadora)  # Texto amarillo, fondo azul
    boton_empezar.pack(pady=10)

# Interfaz de cálculo
def crear_pantalla_calculo(root):
    global pantalla_calculo, entry_consumoI, entry_consumoF, entry_tension, label_consumo_actual_resultado, label_corriente_resultado, label_facturacionBimestralBasico_resultado, label_facturacion_resultado

    pantalla_calculo = tk.Frame(root, bg='blue')  # Fondo azul

    label_titulo = tk.Label(pantalla_calculo, text="Calculadora de Facturación Eléctrica", font=("Helvetica", 16), fg="yellow", bg="blue")  # Texto amarillo
    label_titulo.grid(row=0, column=0, columnspan=2, pady=10)

    # Etiquetas y campos de entrada
    label_consumoI = tk.Label(pantalla_calculo, text="Consumo Inicial (kWh):", fg="yellow", bg="blue")  # Texto amarillo
    label_consumoI.grid(row=1, column=0, padx=10, pady=10)
    entry_consumoI = tk.Entry(pantalla_calculo)
    entry_consumoI.grid(row=1, column=1, padx=10, pady=10)

    label_consumoF = tk.Label(pantalla_calculo, text="Consumo Final (kWh):", fg="yellow", bg="blue")  # Texto amarillo
    label_consumoF.grid(row=2, column=0, padx=10, pady=10)
    entry_consumoF = tk.Entry(pantalla_calculo)
    entry_consumoF.grid(row=2, column=1, padx=10, pady=10)

    label_tension = tk.Label(pantalla_calculo, text="Tensión (V):", fg="yellow", bg="blue")  # Texto amarillo
    label_tension.grid(row=3, column=0, padx=10, pady=10)
    entry_tension = tk.Entry(pantalla_calculo)
    entry_tension.grid(row=3, column=1, padx=10, pady=10)
    entry_tension.insert(0, "220")  # Valor por defecto

    # Botón para calcular
    boton_calcular = tk.Button(pantalla_calculo, text="Calcular", fg="yellow", bg="blue", command=calcular_facturacion)  # Texto amarillo, fondo azul
    boton_calcular.grid(row=4, columnspan=2, padx=10, pady=10)

    # Resultados
    label_consumo_actual = tk.Label(pantalla_calculo, text="Consumo actual (kWh):", fg="yellow", bg="blue")  # Texto amarillo
    label_consumo_actual.grid(row=5, column=0, padx=10, pady=10)
    label_consumo_actual_resultado = tk.Label(pantalla_calculo, text="0.00 kWh", fg="yellow", bg="blue")  # Texto amarillo
    label_consumo_actual_resultado.grid(row=5, column=1, padx=10, pady=10)

    label_corriente = tk.Label(pantalla_calculo, text="Corriente consumida (A):", fg="yellow", bg="blue")  # Texto amarillo
    label_corriente.grid(row=6, column=0, padx=10, pady=10)
    label_corriente_resultado = tk.Label(pantalla_calculo, text="0.00 A", fg="yellow", bg="blue")  # Texto amarillo
    label_corriente_resultado.grid(row=6, column=1, padx=10, pady=10)

    label_facturacionBimestralBasico = tk.Label(pantalla_calculo, text="Facturación Bimestral Básica:", fg="yellow", bg="blue")  # Texto amarillo
    label_facturacionBimestralBasico.grid(row=7, column=0, padx=10, pady=10)
    label_facturacionBimestralBasico_resultado = tk.Label(pantalla_calculo, text="$0.00", fg="yellow", bg="blue")  # Texto amarillo
    label_facturacionBimestralBasico_resultado.grid(row=7, column=1, padx=10, pady=10)

    label_facturacion = tk.Label(pantalla_calculo, text="Facturación Bimestral Final Total:", fg="yellow", bg="blue")  # Texto amarillo
    label_facturacion.grid(row=8, column=0, padx=10, pady=10)
    label_facturacion_resultado = tk.Label(pantalla_calculo, text="$0.00", fg="yellow", bg="blue")  # Texto amarillo
    label_facturacion_resultado.grid(row=8, column=1, padx=10, pady=10)

# Ventana principal
root = tk.Tk()
root.title("Facturación Eléctrica")

# Crear las pantallas
crear_pantalla_bienvenida(root)
crear_pantalla_calculo(root)

# Ejecutar la aplicación
root.mainloop()