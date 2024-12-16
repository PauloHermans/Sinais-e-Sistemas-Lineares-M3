# -*- coding: utf-8 -*-
"""PauloSinaisCircuitos.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1z1PXbJIWFLVKB2iunhX3-_Y3lSDuXV7B

# TRABALHO APRESENTADO COM REQUISITO AVALIATIVO DA DISCIPLINA DE SINAIS E SISTEMAS LINEARES
ALUNO: PAULO MARTINO HERMANS\
DATA: 02/07/2024
"""

!pip install control

import control as ct
import matplotlib.pyplot as plt
import numpy as np

"""## GUIA DE DOCUMENTAÇÃO:

Link de acesso ao relatório: https://docs.google.com/document/d/17XSa4ITLbGqShZZ1yS6QvoblxVoz3D6hzNPBqqFM1Fk/edit?usp=sharing \
Na biblioteca control, a função *control.tf* recebe como parâmetros dois vetores nomeados *num* [numerador] e *den* [denominador].\
Tais vetores aceitam no máximo 3 posições e definem uma função nos formatos {ax^2+bx+c} {ax+b} {a}.\
Exemplo: [2, 3, 4] = 2x^2 + 3x + 4 ou [1, -2] = x - 2

# LISTA DE CIRCUITOS:
"""

#Função para plotagem de gráficos
def plotCircuito(num, den):
  Hs = ct.tf(num, den, name = 'H(s)') #obter função transferência

  plt.figure() #plotar polos e zeros
  ct.pole_zero_map(Hs).plot() #obter polos e zeros

  plt.figure() #plotar resposta no tempo
  ct.step_response(Hs).plot() #obter resposta no tempo

  plt.figure() #plotar diagrama de bode
  ct.frequency_response(Hs).plot() #obter resposta na frequência

"""## EXERCÍCIO 1:"""

#Alocação de variaveis
print('Valor da resistência: ')
R = float(input())
print('Valor da capacitância: ')
C = float(input())

#Definição de numerador e denominador:
num = [1/(R*C)]
den = [1, 1/(R*C)]

plotCircuito(num, den)

"""## EXERCÍCIO 2:"""

#Alocação de variaveis
print('Valor da resistência: ')
R = float(input())
print('Valor da capacitância: ')
C = float(input())

#Definição de numerador e denominador:
num = [1, 0]
den = [1, 1/(R*C)]

plotCircuito(num, den)

"""## EXERCÍCIO 3:"""

#Alocação de variaveis
print('Valor da resistência: ')
R = float(input())
print('Valor da indutância: ')
L = float(input())

#Definição de numerador e denominador:
num = [R, 0]
den = [1, R/L]

plotCircuito(num, den)

"""## EXERCÍCIO 4:"""

#Alocação de variaveis
print('Valor da resistência: ')
R = float(input())
print('Valor da indutância: ')
L = float(input())
print('Valor da capacitância: ')
C = float(input())

#Definição de numerador e denominador:
num = [1, 0, 0]
den = [1, R/L, 1/(L*C)]

plotCircuito(num, den)

"""## EXERCÍCIO 5:"""

#Alocação de variaveis
print('Valor da resistência: ')
R = float(input())
print('Valor da indutância: ')
L = float(input())
print('Valor da capacitância: ')
C = float(input())

#Definição de numerador e denominador:
num = [1/(R*C), 0]
den = [1, 1/(R*C), 1/(L*C)]

plotCircuito(num, den)

"""# LISTA DIAGRAMA DE BODE:

"""

#Função para plotar diagrama de bode
def plotBode(num, den):
  Hs = ct.tf(num, den, name = 'H(s)') #obter função transferência

  ct.bode_plot(Hs, omega_limits=[1e-2, 1e4]) #obter resposta na frequência

"""## EXERCÍCIO 1:"""

#Definição de numerador e denominador:
num = [1, 0]
den = [1, 100]

plotBode(num, den)

"""## EXERCÍCIO 2:"""

#Definição de numerador e denominador:
num = [100]
den = [1, 10]

plotBode(num, den)

"""## EXERCÍCIO 3:"""

#Definição de numerador e denominador:
num = [100]
den = [1, 101, 100]

plotBode(num, den)

"""## EXERCÍCIO 4:"""

#Definição de numerador e denominador:
num = [2500]
den = [1, 20, 2500]

plotBode(num, den)

"""# LISTA CONTROLE:"""

#Função dos gráficos do controle
def plotControle(num, den):
  Hs = ct.tf(num, den, name = 'H(s)') #obter função transferência

  plt.figure()
  ct.pole_zero_map(Hs).plot()#obter polos e zeros

  plt.figure() #plotar resposta no tempo
  ct.step_response(Hs).plot() #obter resposta no tempo

  plt.figure() #plotar resposta na frequência
  ct.bode_plot(Hs, omega_limits=[1e-2, 1e4]) #obter resposta na frequência

"""## EXERCÍCIO:"""

#Alocação de variaveis
print('Valor de K: ')
K = float(input())

#Definição de numerador e denominador:
num = [K, (2*K)]
den = [1, (2+K), (3+(2*K))]

plotControle(num, den)

"""# LISTA TRANSFORMADA Z:"""

def plotDiferenca(y):
  fig, ax = plt.subplots()
  ax.stem(y)
  plt.xlabel('$n$')
  plt.ylabel('$y[n]$')

def plotTZZerosPolos(num, den):
  Hz = ct.tf(num, den, name = 'H(z)') #obter função transferência

  plt.figure() #plotar polos e zeros
  ct.pole_zero_map(Hz).plot() #obter polos e zeros

"""## EXERCÍCIO 1:

### a) X(n) = δ(n)
"""

n_max = 100 #definição da quantidade de pontos

x = np.zeros(n_max)
x[0] = 1 #definição da função
y = np.empty(n_max)

for n in range(n_max): #criação de tabela de pontos (n)
    if n < 1:
        x_n1 = 0
        y_n1 = 0
    else:
        x_n1 = x[n-1]
        y_n1 = y[n-1]

    if n < 2:
        x_n2 = 0
        y_n2 = 0
    else:
        x_n2 = x[n-2]
        y_n2 = y[n-2]

    y_n = x[n] + 0.4*x_n1 + x_n2 - 0.25*y_n1 - 0.1*y_n2
    y[n] = y_n

    print(f"y[{n}] = {y_n}")

# Plotar parte da saída
plotDiferenca(y[:10]) #plot de n=0 até n=9

"""###b) X(n) = u(n)"""

n_max = 100

x = np.array([1]*n_max)
y = np.empty(n_max)

for n in range(n_max):
    if n < 1:
        x_n1 = 0
        y_n1 = 0
    else:
        x_n1 = x[n-1]
        y_n1 = y[n-1]

    if n < 2:
        x_n2 = 0
        y_n2 = 0
    else:
        x_n2 = x[n-2]
        y_n2 = y[n-2]

    y_n = x[n] + 0.4*x_n1 + x_n2 - 0.25*y_n1 - 0.1*y_n2
    y[n] = y_n

    print(f"y[{n}] = {y_n}")

plotDiferenca(y[:10])

"""### c) X(n) = (1/2)^n * u(n)"""

n_max = 100

x = np.empty(n_max)
y = np.empty(n_max)

for n in range(n_max):
    x[n] = (1/2)**n

    if n < 1:
        x_n1 = 0
        y_n1 = 0
    else:
        x_n1 = x[n-1]
        y_n1 = y[n-1]

    if n < 2:
        x_n2 = 0
        y_n2 = 0
    else:
        x_n2 = x[n-2]
        y_n2 = y[n-2]

    y_n = x[n] + 0.4*x_n1 + x_n2 - 0.25*y_n1 - 0.1*y_n2
    y[n] = y_n

    print(f"y[{n}] = {y[n]}")

plotDiferenca(y[:10])

"""## EXERCÍCIO 2:

### Polos e Zeros
"""

#Definição de numerador e denominador:
num = [0.2, 0.1]
den = [1, 0.7, (-0.5)]

plotTZZerosPolos(num, den) #Plotagem de polos e zeros da função

"""### a) X(n) = δ(n)"""

n_max = 100

x = np.zeros(n_max)
x[0] = 1
y = np.empty(n_max)

for n in range(n_max):
    if n < 1:
        x_n1 = 0
        y_n1 = 0
    else:
        x_n1 = x[n-1]
        y_n1 = y[n-1]

    if n < 2:
        x_n2 = 0
        y_n2 = 0
    else:
        x_n2 = x[n-2]
        y_n2 = y[n-2]

    y_n = 0.2*x_n1 + 0.1*x_n2 - 0.7*y_n1 + 0.5*y_n2
    y[n] = y_n

    print(f"y[{n}] = {y_n}")

# Plotar parte da saída
plotDiferenca(y[:10])

"""### b) X(n) = u(n)"""

n_max = 100

x = np.array([1]*n_max)
y = np.empty(n_max)

for n in range(n_max):
    if n < 1:
        x_n1 = 0
        y_n1 = 0
    else:
        x_n1 = x[n-1]
        y_n1 = y[n-1]

    if n < 2:
        x_n2 = 0
        y_n2 = 0
    else:
        x_n2 = x[n-2]
        y_n2 = y[n-2]

    y_n = 0.2*x_n1 + 0.1*x_n2 - 0.7*y_n1 + 0.5*y_n2
    y[n] = y_n

    print(f"y[{n}] = {y_n}")

plotDiferenca(y[:10])

"""### c) X(n) = (1/2)^2 * u(n)"""

n_max = 100

x = np.empty(n_max)
y = np.empty(n_max)

for n in range(n_max):
    x[n] = (1/2)**n

    if n < 1:
        x_n1 = 0
        y_n1 = 0
    else:
        x_n1 = x[n-1]
        y_n1 = y[n-1]

    if n < 2:
        x_n2 = 0
        y_n2 = 0
    else:
        x_n2 = x[n-2]
        y_n2 = y[n-2]

    y_n = 0.2*x_n1 + 0.1*x_n2 - 0.7*y_n1 + 0.5*y_n2
    y[n] = y_n

    print(f"y[{n}] = {y[n]}")

plotDiferenca(y[:10])