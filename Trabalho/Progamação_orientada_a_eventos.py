import tkinter as tk

# Função que será executada quando o botão for clicado
def ao_clicar():
    texto.config(text="Botão clicado!")

# Criação da janela principal
janela = tk.Tk()
janela.title("Exemplo de Programação Orientada a Eventos")
janela.geometry("300x150")

# Rótulo
texto = tk.Label(janela, text="Clique no botão")
texto.pack(pady=10)

# Botão que dispara o evento de clique
botao = tk.Button(janela, text="Clique aqui", command=ao_clicar)
botao.pack(pady=10)

# Loop principal de eventos
janela.mainloop()





















