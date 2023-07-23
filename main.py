class Grafo:
    def __init__(self, vertices):           #Construtor
        self.V = vertices
        self.grafo = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_aresta(self, u, v, peso):     #Método para adicionar as arestas
        self.grafo[u][v] = peso
        self.grafo[v][u] = peso

    def chave_min(self, chave, lista_inc):  #Método para buscar o vertice com menor valor
        valor_min = float('inf')
        indice_min = -1
        for v in range(self.V):
            if chave[v] < valor_min and not lista_inc[v]:
                valor_min = chave[v]
                indice_min = v
        return indice_min

    def prim_am(self):                      #Método para executar o algoritmo de Prim
        pai = [-1] * self.V
        chave = [float('inf')] * self.V
        chave[0] = 0
        lista_inc = [False] * self.V

        for _ in range(self.V):
            u = self.chave_min(chave, lista_inc)
            lista_inc[u] = True
            for v in range(self.V):
                if self.grafo[u][v] > 0 and not lista_inc[v] and self.grafo[u][v] < chave[v]:
                    chave[v] = self.grafo[u][v]
                    pai[v] = u
        return pai

def read_grafo_from_file(file_name):        #Função para ler o arquivo de entrada
    with open(file_name, 'r') as file:
        linhas = file.readlines()
        vertices = len(linhas)
        grafo = Grafo(vertices)
        for i in range(vertices):
            values = linhas[i].strip().split()
            for j in range(vertices):
                grafo.grafo[i][j] = int(values[j])
    return grafo

def print_mst(pai, grafo):                  #Função para printar todas as arestas da árvore
    print("Aresta \t Peso")
    for i in range(1, grafo.V):
        print(f'{pai[i]+1} -- {i+1} [label="{grafo.grafo[i][pai[i]]}"];') # 0 -- 1 [label="220"];


def main():
    file_name = "grafo.txt"
    grafo = read_grafo_from_file(file_name)
    mst_pai = grafo.prim_am()
    print_mst(mst_pai, grafo)

main()


