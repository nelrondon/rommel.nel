import time, tkinter as tk
import threading

temp = False

def validarEntrada(txt, motivo, content):
    maxCaracter = 2

    if motivo =="1":
        if len(content) > maxCaracter:
            return False
        if not txt.isdigit():
            return False
    return True


def startFunc():
    global temp
    while True:
        if temp:
            hrs = hrsVar.get()
            min = minVar.get()
            sec = secVar.get()

            if [hrs, min, sec] == [0,0,0]: 
                temp = False
                print("Termino!!")
                continue

            if sec > 0: 
                secVar.set(sec-1)
            else:
                if min > 0: 
                    minVar.set(min-1)
                    secVar.set(59)
                else:
                    if hrs > 0: 
                        hrsVar.set(hrs-1)
                        minVar.set(59)
        time.sleep(1)

hilo = threading.Thread(target=startFunc)
hilo.start()

def setTrue():
    global temp 
    temp = True

ventana = tk.Tk()
ventana.option_add("*Font", ("Inter", 12))

validacion = ventana.register(validarEntrada)

hrsVar = tk.IntVar()
minVar = tk.IntVar()
secVar = tk.IntVar()

hrsInput = tk.Entry(ventana, width=3, justify="center", textvariable=hrsVar, validate="key", validatecommand=(validacion, "%S", "%d", "%P"))
minInput = tk.Entry(ventana, width=3, justify="center", textvariable=minVar, validate="key", validatecommand=(validacion, "%S", "%d", "%P"))
secInput = tk.Entry(ventana, width=3, justify="center", textvariable=secVar, validate="key", validatecommand=(validacion, "%S", "%d", "%P"))
tk.Label(ventana, text="H", font=("Inter", 10)).grid(row=1, column=0)
tk.Label(ventana, text="M", font=("Inter", 10)).grid(row=1, column=1, padx=5)
tk.Label(ventana, text="S", font=("Inter", 10)).grid(row=1, column=2)

btn = tk.Button(ventana, text="Empezar", font=("Inter", 10), command=setTrue)

hrsInput.grid(row=0, column=0, pady=(10, 0))
minInput.grid(row=0, column=1, pady=(10, 0))
secInput.grid(row=0, column=2, pady=(10, 0))

btn.grid(row=2, column=1, pady=10)




ventana.resizable(False, False)
ventana.mainloop()