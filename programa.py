import simplex
continua = False
big_M = False

"""#Ex 1
print("Max 3x1 + 5x2")
print("x1 <=4")
print("2x2 <=12")
print("3x1 + 2x2 <=18")
z = [3,5,0]
r1 = [1,0,4]
r2 = [0,2,12]
r3 = [3,2,18]
objetivo = "max"
matriz = [z,r1,r2,r3]
inequacoes = ["<=","<=","<="]
v = ["x1","x2","b"]"""

"""#Ex 2
print("Max z = 4x1 + x2")
print("2x1 + x2 <=8")
print("2x1 + 3x2 <=12")
objetivo = "max"
z = [4,1,0]
r1 = [2,1,8]
r2 = [2,3,12]
v = ["x1","x2","b"]
inequacoes = ["<=","<="]
matriz = [z,r1,r2]"""

"""
#Ex 3
print("Min 10x1 + 7x2")
print("2x1 + 2x2 >= 10")
print("3x1 + x2 = 5")
objetivo = "min"
z = [10,7,0]
r1 = [2.0,2.0,10.0]
r2 = [3.0,1.0,5.0]
v = ["x1","x2","b"]
inequacoes = [">=","="]
matriz = [z,r1,r2]
big_M = True"""


"""#Ex 4
print("Min 1700x1 + 750x2 + 800x3")
print("2x1+2x2+5x3>=20")
print("3x1+x2+5x3=10")
inequacoes = [">=","="]
v = ["x1","x2","x3","b"]
objetivo = "min"
z = [1700,750,800,0]
r1 = [2,2,5,20]
r2 = [3,1,5,10]
matriz = [z,r1,r2]
big_M = True"""

#Ex 5
print("Min z = 0,4x1 + 0,5x2")
print("0,3x1 + 0,1x2 <= 2,7")
print("0,5x1 + 0,5x2 = 6")
print("0,6x1+0,4x2 >=6")
z = [0.4,0.5,0]
r1 = [0.3,0.1,2.7]
r2 = [0.5,0.5,6]
r3 = [0.6,0.4,6]

matriz = [z,r1,r2,r3]
v = ["x1","x2","b"]
inequacoes = ["<=","=",">="]
objetivo = "min"
big_M = True




variaveis = simplex.gerar_variaveis(inequacoes,v)
variaveis = simplex.adicionar_s(inequacoes,variaveis)
base = simplex.desenhar_tabela(variaveis,matriz)
tabela = simplex.adicionar_variaveis_base(matriz,base)
identidade = simplex.criar_matriz_identidade(inequacoes)
tabela = simplex.criar_tabela_completa(tabela,identidade,matriz)

    
if(big_M == True):
    tabela = simplex.adicionar_sobras(tabela,variaveis,inequacoes)
    tabela[0] = simplex.adicionar_M(tabela[0],variaveis)
    tabela = simplex.big_M(tabela,inequacoes)

if(objetivo == "max"):
    tabela[0] = simplex.inverter_z(tabela[0])

cont = 0
while(continua!=True):
    colunaPivo = simplex.coluna_pivo(tabela)          
    linhaPivo = simplex.linha_pivo(tabela,colunaPivo)
    novaLinhaPivo = simplex.nova_linha_pivo(tabela,linhaPivo,colunaPivo)
    tabela[linhaPivo] = novaLinhaPivo    
    for i in range(len(tabela)):
        if(i!=linhaPivo):
            tabela[i] = simplex.nova_linha(tabela[i],colunaPivo,novaLinhaPivo)               
    continua = simplex.solucao(tabela)
    cont+=1
    
        
so = simplex.mostrar_tabela(variaveis,tabela)
z = float(simplex.mostrar_z(tabela,variaveis))
if(objetivo == "min"):
    print("z = ",z*-1)
else:    
    print("z = ",z)
print("Número de iterações:",cont)








            
    
