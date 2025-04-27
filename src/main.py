import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
from PIL import Image, ImageTk
import webcam
import os
from datetime import date

mes = {
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio",
    7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
}
dia_semana = {
    0: "Lunes", 1: "Martes", 2: "Miércoles", 3: "Jueves", 4: "Viernes", 5: "Sábado", 6: "Domingo"
}
fecha = f"{dia_semana[date.today().weekday()]} {date.today().day} de {mes[date.today().month]} del {date.today().year}"

root = tk.Tk()
root.title("Facial Scan Assistance")
root.geometry("1280x720")
root.configure(bg="#f0f0f0")

header = tk.Label(root, text=fecha, font=("Helvetica", 14), bg="#f0f0f0")
header.pack(pady=10)

title = tk.Label(root, text="FACIAL SCAN ASSISTANCE", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
title.pack(pady=10)


def agregar_alumno():
    name = simpledialog.askstring("Nuevo Alumno", "Ingrese el nombre del alumno:")
    if name:
        webcam.camara(name)
        messagebox.showinfo("Éxito", f"Alumno {name} agregado y modelo entrenado")


def tomar_asistencia():
    try:
        webcam.assistance()
        messagebox.showinfo("Éxito", "Asistencia tomada correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un problema: {e}")


import tkinter as tk
from tkinter import messagebox
import os
from datetime import datetime

def mostrar_lista():
    alumnos = webcam.lista()
    presentes_actuales = []

    # Intentar leer la lista de presentes del archivo del día
    try:
        fecha_archivo = datetime.now().strftime("%d-%m-%Y")
        archivo_path = f"Presentes/{fecha_archivo}.txt"
        if os.path.exists(archivo_path):
            with open(archivo_path, "r") as f:
                # Actualizar para leer el nuevo formato con checkbox
                presentes_actuales = [line.split(" - ")[0].strip()[4:] for line in f.readlines() if "[x]" in line]
    except Exception as e:
        print("No se pudo leer la lista de presentes:", e)

    lista_ventana = tk.Toplevel()
    lista_ventana.title("Lista de Alumnos")
    lista_ventana.geometry("350x500")

    tk.Label(lista_ventana, text="Lista de Alumnos", font=("Helvetica", 14)).pack(pady=10)

    frame_checkboxes = tk.Frame(lista_ventana)
    frame_checkboxes.pack(fill=tk.BOTH, expand=True)

    checkboxes = {}
    for alumno in alumnos:
        var = tk.BooleanVar(value=alumno in presentes_actuales)
        cb = tk.Checkbutton(frame_checkboxes, text=alumno, variable=var, font=("Helvetica", 12))
        cb.pack(anchor='w', padx=10)
        checkboxes[alumno] = var

    def guardar_cambios():
        nuevos_presentes = [nombre for nombre, var in checkboxes.items() if var.get()]
        try:
            with open(archivo_path, "w") as f:
                # Obtener todos los alumnos y ordenarlos alfabéticamente
                todos_alumnos = sorted(checkboxes.keys())
                for nombre in todos_alumnos:
                    hora_actual = datetime.now().strftime("%H:%M:%S")
                    # Agregar checkbox en formato [x] o [ ]
                    checkbox = "[x]" if nombre in nuevos_presentes else "[ ]"
                    f.write(f"{checkbox} {nombre} - {hora_actual}\n")
            messagebox.showinfo("Guardado", "Lista de presentes actualizada.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar la lista: {e}")

    tk.Button(lista_ventana, text="Guardar cambios", command=guardar_cambios, font=("Helvetica", 12)).pack(pady=10)


frame_buttons = tk.Frame(root, bg="#f0f0f0")
frame_buttons.pack(pady=20)

tk.Button(frame_buttons, text="Agregar Alumno", font=("Helvetica", 12), command=agregar_alumno, compound="left", padx=10).grid(row=0, column=0, padx=10, pady=10)
tk.Button(frame_buttons, text="Tomar Asistencia", font=("Helvetica", 12), command=tomar_asistencia, compound="left", padx=10).grid(row=0, column=1, padx=10, pady=10)
tk.Button(frame_buttons, text="Ver Lista de Alumnos", font=("Helvetica", 12), command=mostrar_lista, compound="left", padx=10).grid(row=0, column=2, padx=10, pady=10)
tk.Button(frame_buttons, text="Entrenar", font=("Helvetica", 12), command=webcam.training, compound="left", padx=10).grid(row=0, column=3, padx=10, pady=10)

tk.Button(root, text="Salir", command=root.quit, font=("Helvetica", 12), bg="#e06666").pack(pady=20)

root.mainloop()