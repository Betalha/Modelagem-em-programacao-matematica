bar_size = int(input("enter the bar size: "))

demands_number = int(input("enter the number of demands: "))

cut_sizes = [int(i) for i in input("enter the cut sizes(ex: 1 2 3): ").split(" ")]

demands = [int(i) for i in input("enter the demands(ex: 1 2 3): ").split(" ")]

print(bar_size, demands_number, cut_sizes, demands)

def gerar_padroes_corte_maximal(tamanho_barra, tamanhos):
    
    n_itens = len(tamanhos)
    padroes = []
    def gerar_recursivo(indice, espaco_restante, padrao_atual):
        if indice == n_itens:
            
            pode_melhorar = False
            for k in range(n_itens):
                if espaco_restante >= tamanhos[k]:
                    pode_melhorar = True
                    break
            if not pode_melhorar and sum(padrao_atual) > 0:
                padroes.append(padrao_atual[:])
            return
        max_quantidade = espaco_restante // tamanhos[indice]
        for quantidade in range(max_quantidade + 1):
            padrao_atual[indice] = quantidade
            novo_espaco = espaco_restante - (quantidade * tamanhos[indice])
            gerar_recursivo(indice + 1, novo_espaco, padrao_atual)
    padrao_inicial = [0] * n_itens
    gerar_recursivo(0, tamanho_barra, padrao_inicial)
    return padroes

patterns = gerar_padroes_corte_maximal(bar_size, cut_sizes)


demands_indexes = [[0] * len(patterns) for _ in range(demands_number)]
for x in range(demands_number):
    for i in range(len(patterns)):
        demands_indexes[x][i] = patterns[i][x]

print(patterns)
print(demands_indexes)