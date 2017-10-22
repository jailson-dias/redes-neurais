

from numpy import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

from openpyxl import load_workbook
from math import ceil
from random import shuffle

def ler_linhas(planilha, linhas, colunas):
	'''
	Ler as linhas de uma planilha.
	
	Args:
		planilha (openpyxl.worksheet.Worksheet): Planilha de onde as linhas serao lidas
		linhas (int): Numero de linhas a serem lidas
		colunas (int): Numero de colunas a serem lidas
	
	Yields:
		Generator de [float]: Um generator que a cada chamada produz uma lista com os valores presentes em uma linha da planilha.
	'''
	for row in planilha.iter_rows(min_row = 1, max_col = colunas, max_row = linhas):
		saida = []
		for cell in row:
			saida.append(cell.value)
		yield saida

def separar_grupos(planilha, grupo0, grupo1):
    for linha in ler_linhas(planilha, 11183, 7):
        if linha[-1] == 0:
            grupo0.append(linha)
        else:
            grupo1.append(linha)


def eliminar_contradicao(grupo0, grupo1):

    contradicao = 0
    l0 = len(grupo0) - 1
    while l0 >= 0:
        l1 = len(grupo1) - 1
        while (l1 >= 0):
            if (grupo0[l0][:-1] == grupo1[l1][:-1]):
                # print ("contradicao:",grupo0[l0], grupo1[l1])
                grupo0.pop(l0)
                grupo1.pop(l1)
                contradicao += 1
                break
            l1 -= 1
        l0 -= 1
    
    print("Contradições:", contradicao)

def dividir_em_grupos(grupo0, grupo1, quant_grupos = 10):
    
    def split_list(grupo, quant):
        grupos = []
        incremento = int(len(grupo)/quant)
        for g in range(0,len(grupo), incremento):
            grupos.append(grupo[g:g + incremento])
        return grupos[:quant]

    grupo0 = split_list(grupo0, quant_grupos)
    grupo1 = split_list(grupo1, quant_grupos)

    tam_grupo = max(len(grupo0[0]), len(grupo1[0]))

    for i in range(0,len(grupo0)):
        if len(grupo0[i]) < tam_grupo:
            grupo0[i] = grupo0[i] * ceil(tam_grupo/len(grupo0[i]))
            grupo0[i] = grupo0[i][:tam_grupo]
    
    for i in range(0,len(grupo1)):
        if len(grupo1[i]) < tam_grupo:
            grupo1[i] = grupo1[i] * ceil(tam_grupo/len(grupo1[i]))
            grupo1[i] = grupo1[i][:tam_grupo]

    grupos = []
    for i in range(0,quant_grupos):
        grupos.append(grupo0[i] + grupo1[i])
    
    return grupos

def insere_planilha(planilha, grupo):
	'''
	Insere as amostras do grupo na planilha.
	
	Args:
		planilha (openpyxl.worksheet.Worksheet): Planilha onde as amostras serao inseridas
		grupo ([[float]]): Grupo onde estao todas as amostras que serao inseridas
		valor (string): Rotulo das amostras
	'''
	for linha in range(len(grupo)):
		for col in range(len(grupo[linha])):
			planilha.cell(row = linha + 1, column = col + 1, value = grupo[linha][col])
       


cmap = colors.ListedColormap(['blue', 'red'])

xlsx = load_workbook("Entrada.xlsx")

# """
fig, axes = plt.subplots(nrows=1)
axes.set_title('colormaps', fontsize=14)
axes.axis([-0.5, 6.5, 0, 12000])

label = ["", "a","b", "c", "d", "e", "f", "g"]
# x = np.array([0,1,2,3,4,5,6])
frame1 = plt.gca()
frame1.axes.get_xaxis().set_ticklabels(label)
# plt.xticks(x, label)

# axes([0.08, 0.08, 0.94-0.08, 0.94-0.08])
# fig = plt.figure()
# fig.subplots_adjust(left=0.05, bottom=0.05, right=0.98, top=0.98)
# axes=axes.reshape(1,len(axes))
# axes.fill(9,3)

# plt.gca().set_position([0, 0, 1, 1]) # ponto inicial e final do grafico

# data = random.random((5,5))
# a = [(0,0,1,0,0,0,1), (1,0,1,0,0,0,1), (1,0,0,0,0,0,1), (1,0,1,0,1,0,0),(0,0,1,0,1,0,1)]
# for i in range(0,8):
#     a += a

grupo0 = []
grupo1 = []

separar_grupos(xlsx["Original"], grupo0, grupo1)

# print (len(grupo0), len(grupo1))
eliminar_contradicao(grupo0, grupo1)
# print (len(grupo0), len(grupo1))
grupos = dividir_em_grupos(grupo0, grupo1)

insere_planilha(xlsx.create_sheet(title = "Grupo 0"), grupo0)
insere_planilha(xlsx.create_sheet(title = "Grupo 1"), grupo1)

for i in range(len(grupos)):
	'''Embaralha e insere cada grupo em uma planilha propria'''
	shuffle(grupos[i])
	insere_planilha(xlsx.create_sheet(title = "Divisao " + str(i)), grupos[i])

xlsx.save("Saida.xlsx")

# """
"""
dados = []

verdadeiro = 0

vermelhos = 0

for linha in grupo0 + grupo1:
    # print (linha)
    l = []
    if linha[-1] == 1:
        verdadeiro += 1
    for celula in linha[:-1]:
        if celula == 0 or celula == None:
            l.append(1)
            vermelhos += 1
        else:
            l.append(0)
    if linha[-1] != 0 and linha[-1] != None:
        l.append(0)
    else:
        l.append(1)
    dados.append(tuple(l))
img = plt.imshow(dados, cmap=cmap, interpolation='nearest', aspect='auto')
print (verdadeiro, vermelhos)
# img.set_cmap('hot')
# plt.axis('off')
# plt.savefig("test.png", bbox_inches='tight')
plt.show()

# """
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors


# Have colormaps separated into categories:
# http://matplotlib.org/examples/color/colormaps_reference.html
cmaps = [
         ('Qualitative', [
            'Pastel1', 'Pastel2', 'Paired', 'Accent',
            'Dark2', 'Set1', 'Set2', 'Set3',
            'tab10', 'tab20', 'tab20b', 'tab20c']),
         ]

cmap = colors.ListedColormap(['red', 'green', 'yellow', 'black', 'blue'])
# fig, axes = plt.subplots(nrows=50)

nrows = max(len(cmap_list) for cmap_category, cmap_list in cmaps)
gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))

a = [(5,4,1)]
# for i in range(0, 20):
#     a += a

gradient = np.array(a)

print (gradient)

def plot_color_gradients(cmap_category, cmap_list, nrows):
    fig, axes = plt.subplots(ncols=2)
    # fig.subplots_adjust(top=0.95, bottom=0.01, left=0.2, right=0.99)
    axes[0].set_title(cmap_category + ' colormaps', fontsize=14)

    for ax, name in zip(axes, cmap_list):
        
        ax.imshow(gradient, cmap=cmap, interpolation='nearest')
        # pos = list(ax.get_position().bounds)
        # x_text = pos[0] - 0.01
        # y_text = pos[1] + pos[3]/2.
        # fig.text(x_text, y_text, name, va='center', ha='right', fontsize=10)

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axes:
        ax.set_axis_off()


for cmap_category, cmap_list in cmaps:
    plot_color_gradients(cmap_category, cmap_list, nrows)

plt.show()

"""