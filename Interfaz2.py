import tkinter as tk
from tkinter import messagebox

# Función para calcular corriente y facturación
def calcular_facturacion():
    try:
        # Obtiene los valores ingresados
        consumo = float(entry_consumo.get())  # en kWh
        tension = float(entry_tension.get())  # en Voltios

        # Cálculo de la corriente
        potencia = consumo * 1000  # Convertir kWh a W (1 kWh = 1000 W)
        corriente = potencia / tension  # I = P / V

        # Cálculo aproximado de la facturación ($101,820/kWh)
        precio_kwh = 101820
        facturacion = consumo * precio_kwh

        # Mostramos los resultados en las etiquetas
        label_corriente_resultado.config(text=f"{corriente:.2f} A")
        label_facturacion_resultado.config(text=f"${facturacion:.2f}")

    except ValueError:
        messagebox.showerror("Entrada inválida", "Por favor ingrese valores numéricos válidos.")

# Función para cambiar de pantalla a la de cálculo
def mostrar_calculadora():
    pantalla_bienvenida.pack_forget()
    pantalla_calculo.pack()

# Interfaz de bienvenida
def crear_pantalla_bienvenida(root):
    global pantalla_bienvenida
    pantalla_bienvenida = tk.Frame(root)
    pantalla_bienvenida.pack()

    label_bienvenida = tk.Label(pantalla_bienvenida, text="Bienvenido al Sistema de Facturación", font=("Helvetica", 16))
    label_bienvenida.pack(pady=20)

    boton_empezar = tk.Button(pantalla_bienvenida, text="Empezar", font=("Helvetica", 12), command=mostrar_calculadora)
    boton_empezar.pack(pady=10)

# Interfaz de cálculo
def crear_pantalla_calculo(root):
    global pantalla_calculo, entry_consumo, entry_tension, label_corriente_resultado, label_facturacion_resultado

    pantalla_calculo = tk.Frame(root)

    label_titulo = tk.Label(pantalla_calculo, text="Calculadora de Facturación Eléctrica", font=("Helvetica", 16))
    label_titulo.grid(row=0, column=0, columnspan=2, pady=10)

    # Etiquetas y campos de entrada
    label_consumo = tk.Label(pantalla_calculo, text="Consumo (kWh):")
    label_consumo.grid(row=1, column=0, padx=10, pady=10)
    entry_consumo = tk.Entry(pantalla_calculo)
    entry_consumo.grid(row=1, column=1, padx=10, pady=10)

    label_tension = tk.Label(pantalla_calculo, text="Tensión (V):")
    label_tension.grid(row=2, column=0, padx=10, pady=10)
    entry_tension = tk.Entry(pantalla_calculo)
    entry_tension.grid(row=2, column=1, padx=10, pady=10)
    entry_tension.insert(0, "220")  # Valor por defecto

    # Botón para calcular
    boton_calcular = tk.Button(pantalla_calculo, text="Calcular", command=calcular_facturacion)
    boton_calcular.grid(row=3, columnspan=2, padx=10, pady=10)

    # Resultados
    label_corriente = tk.Label(pantalla_calculo, text="Corriente consumida (A):")
    label_corriente.grid(row=4, column=0, padx=10, pady=10)
    label_corriente_resultado = tk.Label(pantalla_calculo, text="0.00 A")
    label_corriente_resultado.grid(row=4, column=1, padx=10, pady=10)

    label_facturacion = tk.Label(pantalla_calculo, text="Facturación aproximada ($):")
    label_facturacion.grid(row=5, column=0, padx=10, pady=10)
    label_facturacion_resultado = tk.Label(pantalla_calculo, text="$0.00")
    label_facturacion_resultado.grid(row=5, column=1, padx=10, pady=10)

# Ventana principal
root = tk.Tk()
root.title("Sistema de Facturación")

# Crear pantallas
crear_pantalla_bienvenida(root)
crear_pantalla_calculo(root)

# Iniciar el loop principal de Tkinter
root.mainloop()
