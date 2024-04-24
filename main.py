import numpy as np


def regra_cramer(coeficientes, constantes):
    det_coeficientes = np.linalg.det(coeficientes)


    #lista para armazenar os coeficientes
    solucoes = []

    #calcula o valor de cada variável
    for i in range(len(coeficientes)):
        #copia da matriz dos coeficientes
        coeficientes_modificados = coeficientes.copy()
        coeficientes_modificados[:, i] = constantes


         # Calcula o determinante da matriz modificada
        coeficientes_modificados_det = np.linalg.det(coeficientes_modificados)

          # Calcula a solução e a adiciona à lista de soluções

        solucoes.append(coeficientes_modificados_det / det_coeficientes)
    return solucoes
        

coeficientes = np.array([[1, 2, 1],
                         [2, -1, 1],
                         [-1, 3, 1]])

constantes = np.array([0, 1, -2])

solucoes = regra_cramer(coeficientes, constantes)


# Exibe as soluções
print("Soluções do sistema:")
for i, sol in enumerate(solucoes):
    print(f"x{i+1} =", sol)

        

