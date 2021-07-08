def inverter_z(z):
    nvz = []
    for i in z:
        nvz.append(i*-1)
    return nvz

def desenhar_tabela(variaveis,matriz):
    tabela = []
    for i in range(len(matriz)):
        aux =[]
        for j in range(len(variaveis)):
            aux.append(0)
        tabela.append(aux)
    return tabela   
   

def adicionar_variaveis_base(matriz,tabela):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])-1):
            tabela[i][j] = matriz[i][j]
        tabela[i][len(tabela[i])-1] = matriz[i][len(matriz[i])-1]
    return tabela
       
def criar_matriz_identidade(inequacoes):   
    matriz = []
    for i in range(len(inequacoes)):
        aux = []
        for j in range(len(inequacoes)):
            if(i == j):
                aux.append(1)
            else:
                aux.append(0)           
        matriz.append(aux)
                
    return matriz 
                       
def criar_tabela_completa(tabela,identidade,matriz):
    tamanho = len(matriz[1])-1
    for i in range(1,len(tabela)):
        for j in range(len(tabela[i])-2):
            if(j >= tamanho):
                tabela[i][j] = identidade[i-1][j-tamanho]
    return tabela            
    
def coluna_pivo(tabela):
    funcaoObjetivo = tabela[0]
    funcaoObjetivo = funcaoObjetivo[0:len(funcaoObjetivo)-1]
    valor = funcaoObjetivo[0]
    for i in funcaoObjetivo:
        if(i < valor):
            valor = i
    return tabela[0].index(valor)        
    

def linha_pivo(tabela,colunaPivo):
    menorValor = 10**100
    menorIndice = 0
    for i in range(1,len(tabela)):
        if(tabela[i][colunaPivo] > 0):
           divisao = tabela[i][len(tabela[i])-1]/tabela[i][colunaPivo]
           if(divisao < menorValor):
               menorValor = divisao
               menorIndice = i
    return menorIndice
           

def nova_linha_pivo(tabela,linha,coluna):
    pivo = tabela[linha][coluna]
    novaLinhaPivo = []
    for i in tabela[linha]:
        resultado = i/pivo
        novaLinhaPivo.append(resultado)
    return novaLinhaPivo

def nova_linha(linha,colunaPivo,novaLinhaPivo):
    novaLinha = []
    pivo = linha[colunaPivo] *-1
    for i in range(len(linha)):
        multi = pivo*novaLinhaPivo[i]
        novaLinha.append(multi+linha[i])
    return novaLinha   
    

def solucao(tabela):
    fo = tabela[0]
    fo = fo[0:len(fo)-1]
    valor = min(fo)
    if(valor >= 0):    
        return True
    return False        
               
def reduzir_casas(tabela):  
    for i in range(len(tabela)):
        for j in range(len(tabela[i])):
            tabela[i][j] = "%.1f"%tabela[i][j]
    return tabela

def gerar_variaveis(simbolos,variaveis):  
    for i in range(len(simbolos)):        
        if(simbolos[i]=="<="):
            variaveis.insert(len(variaveis)-1,"xf"+str(i+1))
        elif(simbolos[i]==">="):            
            variaveis.insert(len(variaveis)-1,"a"+str(i+1))
                        
        else:
            variaveis.insert(len(variaveis)-1,"a"+str(i+1))
            
    return variaveis

def adicionar_s(inequacoes,variaveis):
    for i in inequacoes:
        if(i == ">="):
            variaveis.insert(len(variaveis)-1,"s")
    return variaveis

def adicionar_sobras(tabela,variaveis,inequacoes):
    coluna = variaveis.index("s")
    linhas = []
    for i in range(len(inequacoes)):
        if(inequacoes[i] == ">="):
            linhas.append(i+1)
    
    for i in range(len(linhas)):
        tabela[linhas[i]][coluna] = -1
    return tabela       
        
        

def mostrar_tabela(variaveis,tabela):
    tabela = reduzir_casas(tabela)
    tabela.insert(0,variaveis)
    for l in range(len(tabela)):
        for c in range(len(tabela[l])):
            print(f'[{tabela[l][c]:^5}]',end='')
        print()

def mostrar_z(tabela,variaveis):
    return tabela[1][len(variaveis)-1]

def adicionar_M(z,variaveis):
    for i in range(len(z)):
        if(variaveis[i][0]=="a"):
            z[i] = 100000
    return z    

       
def mao_direita(s,db,b):
    soma = 0
    for i in range(len(s)):
        for j in range(len(db)):
            if(i==j):
                soma+=(s[i]*db[j])
    if(soma == 0):
        return "infinito"
    return b/-soma

def big_M(tabela,inequacoes):
    rascunho = tabela[1:len(tabela)]
    aux = []
    for i in rascunho[0]:
        aux.append(0)
    for i in range(len(rascunho)):
        for j in range(len(rascunho[i])):
            if(inequacoes[i]!="<="):
                aux[j] = aux[j]+rascunho[i][j]
    for i in range(len(aux)):
        aux[i]*=-100000
    for i in range(len(tabela[0])):
        tabela[0][i] = tabela[0][i] + aux[i]
    return tabela
    
def mostrar_dual(matriz,inequacoes):
    w = []
    s = []
    r = []
    for i in range(1,len(matriz)):
        for j in range(len(matriz[i])):
            if(j == len(matriz[i])-1):
                w.append(matriz[i][j])
    
    for i in range(len(inequacoes)):
        if(inequacoes[i] == "<="):
            s.append(">=")
        elif(inequacoes[i] == ">="):
            s.append("<=")
    quant = len(matriz[1])-1
    rascunho = matriz[1:len(matriz)]
    tamanho = len(rascunho[1])-1
    for c in range(tamanho):
        a = []
        for i in range(len(rascunho)):
            for j in range(len(rascunho[i])-1):
                if(j == c):
                    a.append(rascunho[i][j])
        r.append(a)
    for i in range(len(matriz[0])-1):
        r[i].insert(len(r)+1,matriz[0][i]*-1)
        
    print("w=", w)
    print("sinais=", s)
    for i in range(len(r)):
        print("r="+str(i+1), r[i])
            
      
       
      
               
           
        


            
            

        
       
    
    
            
        









    
