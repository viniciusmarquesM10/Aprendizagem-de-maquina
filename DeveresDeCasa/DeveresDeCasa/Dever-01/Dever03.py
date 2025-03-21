# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NWs71JlK8e29h7YcT1TlEaMk4ht6ShZ1
"""

import csv

dados = [
    ["Nome", "Idade"],
    ["Ana", 25],
    ["Bruno", 30],
    ["Carla", 22],
    ["Daniel", 28],
    ["Eduardo", 35]
]

with open('dados.csv', mode='w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerows(dados)

print("Arquivo 'dados.csv' criado com sucesso!")

import csv

dados_lidos = []
with open('dados.csv', mode='r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    for linha in leitor_csv:
        dados_lidos.append(linha)

dados_dict = {linha[0]: int(linha[1]) for linha in dados_lidos[1:]}

idade_maxima = max(dados_dict.values())

nome = input("Digite um nome: ")


if nome in dados_dict:
    idade = dados_dict[nome]
    if idade == idade_maxima:
        print(f"{nome} tem {idade} anos, é a pessoa mais velha da lista.")
    else:
        print(f"{nome} tem {idade} anos, não é a pessoa mais velha da lista.")
else:
    print("Nome não encontrado.")

