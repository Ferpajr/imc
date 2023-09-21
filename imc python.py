import tkinter as tk

def pulaLinha():
    texto.config(text=texto.cget("text") + "\n\n")

def mostra(frase):
    texto.config(text=texto.cget("text") + frase + "\n")
    pulaLinha()

def calculaImc(altura, peso):
    return peso / (altura * altura)

def calcular_imc():
    nome = entrada_nome.get()
    altura_informada = float(entrada_altura.get())
    peso_informado = float(entrada_peso.get())

    imc = calculaImc(altura_informada, peso_informado)
    mostra(nome + ", o seu IMC calculado é " + str(imc))

    if imc < 18.5:
        mostra("Você está abaixo do recomendado")

    if imc > 35:
        mostra("Você está acima do recomendado")

    if 18.5 <= imc <= 35:
        mostra("Seu IMC está excelente")

janela = tk.Tk()
janela.title("Teste de título")
janela.geometry("300x300")

rotulo_nome = tk.Label(janela, text="Informe seu nome:")
rotulo_nome.pack()

entrada_nome = tk.Entry(janela)
entrada_nome.pack()

rotulo_altura = tk.Label(janela, text="Informe sua altura:")
rotulo_altura.pack()

entrada_altura = tk.Entry(janela)
entrada_altura.pack()

rotulo_peso = tk.Label(janela, text="Informe seu peso:")
rotulo_peso.pack()

entrada_peso = tk.Entry(janela)
entrada_peso.pack()

botao_calcular = tk.Button(janela, text="Calcular IMC", command=calcular_imc)
botao_calcular.pack()

texto = tk.Label(janela, text="")
texto.pack()

janela.mainloop()