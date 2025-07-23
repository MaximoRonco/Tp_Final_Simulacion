import tkinter as tk
from tkinter import ttk, messagebox

def abrir_euler():
    root.destroy()
    import Euler  # Asegúrate que el archivo se llama exactamente así y tiene la interfaz de Euler

def abrir_rk():
    root.destroy()
    import RungeKutta
    # Aquí deberías llamar a tu ventana principal de Runge-Kutta (cuando la tengas)
    # Por ejemplo: import rungekutta

root = tk.Tk()
root.title("Simulador de Osciladores - Inicio")
root.configure(bg="#e3f2fd")

# Estilos
style = ttk.Style()
style.theme_use('clam')
style.configure("Titulo.TLabel", font=("Arial", 22, "bold"), background="#e3f2fd", foreground="#1565c0")
style.configure("Subtitulo.TLabel", font=("Arial", 14, "bold"), background="#e3f2fd", foreground="#1976d2")
style.configure("Opcion.TLabel", font=("Arial", 13, "bold"), background="#e3f2fd", foreground="#263238")
style.configure("Desc.TLabel", font=("Arial", 11), background="#e3f2fd", foreground="#263238")

# Botones modernos sin borde y con esquinas redondeadas usando tk.Button
def boton_moderno(master, text, command, bg, fg):
    return tk.Button(
        master, text=text, command=command,
        font=("Arial", 12, "bold"),
        bg=bg, fg=fg, activebackground=bg, activeforeground=fg,
        relief="flat", bd=0, width=22, height=2,
        highlightthickness=0,
        cursor="hand2"
    )

# Título
lbl_titulo = ttk.Label(root, text="Simulador del Oscilador de Van der Pol", style="Titulo.TLabel", anchor="center")
lbl_titulo.pack(pady=(30, 10))

def mostrar_enunciado():
    ventana = tk.Toplevel(root)
    ventana.title("Enunciado y derivación")
    ventana.configure(bg="#e3f2fd")
    ventana.geometry("500x400")

    titulo = tk.Label(ventana, text="Enunciado", font=("Arial", 14, "bold"), fg="#1565c0", bg="#e3f2fd")
    titulo.pack(pady=(10, 5))

    texto = tk.Text(ventana, wrap="word", bg="#e3f2fd", font=("Arial", 11), fg="#005f99", relief="flat", height=14)
    texto.pack(padx=20, pady=(0, 10), fill="both", expand=True)

    texto.tag_configure("bold", font=("Arial", 11, "bold"))

    texto.insert("end", "La ecuación de Van der Pol es:\n", "bold")
    texto.insert("end", "    d²y/dt² - μ(1 - y²) dy/dt + y = 0\n\n")

    texto.insert("end", "1. Reordenamos:\n", "bold")
    texto.insert("end", "    d²y/dt² = μ(1 - y²) dy/dt - y\n\n")

    texto.insert("end", "2. Definimos:\n", "bold")
    texto.insert("end", "    x₁ = y\n")
    texto.insert("end", "    x₂ = dy/dt\n\n")

    texto.insert("end", "3. Sistema equivalente:\n", "bold")
    texto.insert("end", "    x₁' = x₂\n")
    texto.insert("end", "    x₂' = μ(1 - x₁²) x₂ - x₁\n")

    texto.config(state="disabled")  # Desactiva la edición

    btn_cerrar = tk.Button(ventana, text="Cerrar", command=ventana.destroy, bg="#039be5", fg="white",
                           font=("Arial", 10, "bold"), relief="flat", padx=10, pady=5)
    btn_cerrar.pack(pady=10)



btn_enunciado = boton_moderno(root, "Mostrar enunciado", mostrar_enunciado, "#17a2b8", "white")
btn_enunciado.pack(pady=(10, 10))




# Subtítulo
lbl_subtitulo = ttk.Label(root, text="Elija el método numérico para resolver el sistema:", style="Subtitulo.TLabel", anchor="center")
lbl_subtitulo.pack(pady=(0, 20))

# Frame para opciones (sin fondo blanco)
frame_opciones = tk.Frame(root, bg="#e3f2fd")
frame_opciones.pack()

# Opción Euler
lbl_euler = ttk.Label(frame_opciones, text="Método de Euler", style="Opcion.TLabel", background="#e3f2fd")
lbl_euler.grid(row=0, column=0, sticky="w", pady=(0, 2))
lbl_euler_desc = ttk.Label(frame_opciones, text="Rápido y simple, pero menos preciso para pasos grandes.", style="Desc.TLabel", background="#e3f2fd")
lbl_euler_desc.grid(row=1, column=0, sticky="w", pady=(0, 10))
btn_euler = boton_moderno(frame_opciones, "Resolver con Euler", abrir_euler, "#43a047", "white")
btn_euler.grid(row=2, column=0, pady=(0, 18), sticky="ew", ipadx=0)
btn_euler.configure(highlightbackground="#43a047", highlightcolor="#43a047")

# Opción Runge-Kutta
lbl_rk = ttk.Label(frame_opciones, text="Método de Runge-Kutta", style="Opcion.TLabel", background="#e3f2fd")
lbl_rk.grid(row=3, column=0, sticky="w", pady=(0, 2))
lbl_rk_desc = ttk.Label(frame_opciones, text="Más preciso y estable, ideal para simulaciones largas o pasos grandes.", style="Desc.TLabel", background="#e3f2fd")
lbl_rk_desc.grid(row=4, column=0, sticky="w", pady=(0, 10))
btn_rk = boton_moderno(frame_opciones, "Resolver con Runge-Kutta", abrir_rk, "#039be5", "white")
btn_rk.grid(row=5, column=0, pady=(0, 0), sticky="ew", ipadx=0)
btn_rk.configure(highlightbackground="#039be5", highlightcolor="#039be5")

# Redondear esquinas (solo en sistemas modernos, requiere tk >= 8.6.9)
try:
    btn_euler.config(borderwidth=0, highlightthickness=0)
    btn_rk.config(borderwidth=0, highlightthickness=0)
    btn_euler.config(overrelief="flat")
    btn_rk.config(overrelief="flat")
    btn_euler.config(relief="flat")
    btn_rk.config(relief="flat")
    btn_euler.config(border=0)
    btn_rk.config(border=0)
except Exception:
    pass

# Footer
lbl_footer = ttk.Label(root, text="Máximo Ronco 91247 | 2025", font=("Arial", 9), background="#e3f2fd", foreground="#90a4ae")
lbl_footer.pack(side="bottom", pady=(10, 5))

root.geometry("600x420")

# Centrar ventana
root.update_idletasks()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
size = tuple(int(_) for _ in root.geometry().split('+')[0].split('x'))
x = w//2 - size[0]//2
y = h//2 - size[1]//2
root.geometry("%dx%d+%d+%d" % (size + (x, y)))

root.mainloop()