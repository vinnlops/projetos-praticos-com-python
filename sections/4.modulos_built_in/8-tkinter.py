import tkinter as tk

# Criar a Janela

window = tk.Tk()
window.geometry("300x150")
window.title("Gerencia Frases")

# Adiciona um Frame

frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill='x', expand=True)

# Adiciona o Label

label = tk.Label(frame, text="Olá Mundo")
label.pack(fill='x', expand=True)

# Adiciona o input text

frase_lab = tk.Label(frame, text="Frase")
frase_lab.pack(fill='x', expand=True)

frase_inp = tk.Entry(frame)
frase_inp.pack(fill='x', expand=True)

# Função para alterar texto

def click():
    label.config(text=frase_inp.get())

# Adiciona Botão

button = tk.Button(frame, text="Enviar", command=click)
button.pack()

window.mainloop()