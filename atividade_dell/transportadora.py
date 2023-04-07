'''Esta atividade consiste no desenvolvimento de uma simulação para um sistema de transporte interestadual de cargas. Os dados de distância entre as cidades estão disponíveis no arquivo CSV anexo. Neste arquivo, a primeira linha contém os nomes das cidades para onde ocorrem os transportes; as demais linhas do arquivo constituem uma matriz de distâncias entre as respectivas cidades.
A transportadora Dely tem sua frota composta por caminhões de portes distintos: um modelo de caminhão de porte pequeno transporta até 1 toneladas e possui o custo de R$ 4,87 por km rodado; 
um caminhão de médio porte transporta até 4 toneladas e possui o custo de R$ 11,92 por km rodado; e um caminhão de grande porte transporta até 10 toneladas e possui o custo de R$ 27,44 por km rodado.
Na tabela abaixo, está disponível a relação de custo por km para cada modalidade de transporte.
Itens	Preço por Km (R$/km)
Caminhão de pequeno porte	4,87
Caminhão de médio porte	11,92
Caminhão de grande porte	27,44

Observação: para essa atividade, deverão ser ignoradas as dimensões dos produtos transportados, apenas seus pesos são relevantes. 
Na tabela abaixo estão disponíveis alguns itens de transporte, apenas como exemplo.
Itens	Peso (kg)
Celular	0.5
Geladeira	60.0
Freezer 	100.0
Cadeira	5.0
Luminária	0.8
Lavadora de roupa	120kg

Você deve implementar as seguintes funcionalidades: 
⦁	[Consultar trechos x modalidade] O programa deverá representar em modo texto ou gráfico os trechos disponíveis para 
realização dos transportes, de modo a permitir que o usuário indique o nome de duas cidades 
e a modalidade de transporte: o programa deverá mostrar a distância rodoviária entre elas e o custo total calculado para o trecho; se um nome de cidade não existir, informar ao usuário; 
Por exemplo: de PORTO ALEGRE para SÃO PAULO, utilizando um caminhão de pequeno porte, a distância é de XXX km e o custo será de R$ xxx,00.

⦁	[Cadastrar transporte] O programa deverá permitir ao usuário listar uma sequência de cidades e adicionar uma 
lista de itens a transportar (e seus pesos). O programa deverá calcular a distância total a ser percorrida e 
identificar o modelo de caminhão mais adequado para este transporte, bem como os custos envolvidos (por trecho e totais). 
Por exemplo: de PORTO ALEGRE para SÃO PAULO, a distância a ser percorrida é de X km, para transporte dos produtos X, Y , Z 
será necessário utilizar 2 caminhões de porte PEQUENO e um de porte MÉDIO, de forma a resultar no menor custo de transporte 
por km rodado. O valor total do transporte dos itens é R$ xxx,00, sendo R$ xxx,00 é o custo unitário médio.
Para realizar esta questão, considere os seguintes cenários de exemplo:
Cenário 1: A empresa TikStop deseja transportar o total de 300 celulares, 50 geladeiras, 70 freezers e 2000 luminárias. 
O transporte deverá partir da cidade de Porto Alegre, com parada em Florianópolis onde serão descarregados 25 geladeiras, 
50 freezers e 100 celulares. O restante da carga seguirá até a cidade de Curitiba. 
Cenário 2: A empresa LeMour deseja transportar o total de 500 celulares, 100 geladeiras, 200 freezers, 98 cadeiras. 
O transporte deverá partir da cidade de Maceió, com parada em Goiânia onde serão descarregados 90 geladeiras, 
200 freezers e 20 celulares. O restante da carga seguirá até São Paulo.
Observação: para alguns cenários de uso poderá ser necessário alocar mais de um caminhão para dar conta da carga.

⦁	[Dados estatísticos] O programa deverá exibir um relatório dos transportes até então cadastrados. Para cada um deverá ser apresentado o custo total, 
o custo por trecho, o custo médio por km, o custo médio por tipo de produto, o custo total por trecho, o custo total para cada modalidade de transporte, o número total de veículos deslocados e o total de itens transportados. 

⦁	[Finalizar o programa] O programa deve permitir que o usuário encerre o programa a qualquer momento.

Observações finais:
⦁	Você pode exibir as informações solicitadas da maneira que achar mais conveniente e útil, utilizando caracteres, símbolos, números, espaços, interface gráfica, páginas web, etc. Use a criatividade e mostre o que você sabe!
⦁	Sugere-se o desenvolvimento de um programa na linguagem de sua preferência, com uma interface também de sua preferência podendo ser gráfica ou textual/console, com um menu com as opções enumeradas nos requisitos;
⦁	Você deve escrever o código que realiza as funções requeridas e armazena os dados lidos em memória (do jeito que você quiser). 
⦁	Não é necessário gravar dados em nenhum formato, nem usar sistemas de banco de dados.
⦁	O programa deverá lidar com dados de entrada inválidos e informar uma mensagem adequada caso ocorram. Lembre-se de demonstrar isso nas capturas de tela ao realizar os testes.
⦁	Não esqueça de enviar os resultados desse desafio utilizando o modelo fornecido.'''


#Importando a biblioteca PANDAS, para conseguir abrir o arquivo .csv
import pandas as pd

#Colocando o arquivo em uma variável
arquivo = pd.read_csv("DNIT-Distancias[135].csv",sep = ";")

#Criando o Menu para que o usuário escolha o procedimento que deseja

print(arquivo)

#Criando as listas que serão utilizadas durante o código

#A lista "carrinho" obtém todos os itens que serão transportados. A lista é esvaziada assim que as informações são mandadas para a classe Transporte.
carrinho = []

#A lista "transporte" obtém todas as operações que serão realizadas
transportes_lista = []

#Classe Produto obtém todas as informações dos produtos selecionados
class Produto:
    def __init__(self, id, nome, peso, qntdd, peso_total):
        self.id = id
        self.nome = nome
        self.peso = peso
        self.qntdd = qntdd
        self.peso_total = peso_total

#Classe Transporte obtem todas as informações do transporte. Assim que criada, é armazenada na lista "transporte_lista"
class Transporte:
    def __init__(self, cidade_origem, cidade_destino, peso_total, tipo_caminhao, media_km):
        self. cidade_origem = cidade_origem
        self.cidade_destino = cidade_destino
        self.peso_total = peso_total
        self.tipo_caminhao = tipo_caminhao
        self.media_km = media_km
 
 #Formatando a exibição do objeto       
    def __str__(self):
        return (f"Origem: {self.cidade_origem} - Destino: {self.cidade_destino} - Peso Total: {self.peso_total}KG - Tipo de Caminhão: {self.tipo_caminhao} - Média de Custo: R${self.media_km} /KM")
 
#A função item() armazena os itens selecionados na lista carrinho           
def item(id, nome, peso):
    quantidade = int(input(f"Qual a quantidade do item {nome} você deseja levar? => "))
    quilos = quantidade * float(peso)
    produto = Produto(id,nome,peso,quantidade, quilos)
    carrinho.append(produto)
    print("Produto adicionado com sucesso!")
    
#Menu para selecionar as opções
while True:
    print('''
Qual operação deseja fazer:
1 - [Consultar trechos x modalidade]
2 - [Cadastrar transporte]
3 - [Dados estatísticos]
4 - [Finalizar o programa]
            ''')
    escolha = input("=> ")

    if escolha == '1':
        cidade1 = input("Digite a cidade de origem da carga => ").upper()
        cidade2 = input("Digite a cidade de destino da carga => ").upper()
        if cidade1 == cidade2:
            print("Cidade de origem não pode ser igual a de destino!")
        if cidade1 in arquivo.columns:
            for i, row in enumerate(arquivo[cidade1]):
                if row != 0:
                    pass
                if row == 0:            
                    if cidade2 in arquivo.columns:
                        print('''
Itens	                         Preço por Km (R$/km)
1 - Caminhão de pequeno porte	 4,87
2 - Caminhão de médio porte	 11,92
3 - Caminhão de grande porte	 27,44
''')
                        caminhao = input("Qual o porte do caminhão que fará o percurso? => ")
                        if caminhao == '1':
                            print(f"DE {cidade1} para {cidade2}, UTILIZANDO UM CAMINHÃO DE PEQUENO PORTE, a distância é de {arquivo[cidade2][i]}km e o custo será de R$ {round((4.87 * int(arquivo[cidade2][i])),2)}") 
                        if caminhao == '2':
                            print(f"DE {cidade1} para {cidade2}, UTILIZANDO UM CAMINHÃO DE MÉDIO PORTE, a distância é de {arquivo[cidade2][i]}km e o custo será de R$ {round((11.92 * int(arquivo[cidade2][i])),2)}")
                        if caminhao == '3':
                            print(f"DE {cidade1} para {cidade2}, UTILIZANDO UM CAMINHÃO DE GRANDE PORTE, a distância é de {arquivo[cidade2][i]}km e o custo será de R$ {round((27.44 * int(arquivo[cidade2][i])),2)}") 
                        else:
                            print("Opção inválida!")                     
                    else:
                        print("Cidade de destino não encontrada!") 

        else:
            print("Cidade de origem não encontrada!") 
            
    if escolha == '2':
        cidade1 = input("Digite a cidade de origem da carga => ").upper()
        cidade2 = input("Digite a cidade de destino da carga => ").upper()
        if cidade1 == cidade2:
            print("Cidade de origem não pode ser igual a de destino!")
            break
        parada = input("")
        if cidade1 in arquivo.columns:
            for iter, row in enumerate(arquivo[cidade1]):
                if row != 0:
                    pass
                if row == 0:            
                    if cidade2 in arquivo.columns:
                        print ("Quais itens você deseja transportar, e sua quantidade:")
                        print('''
Itens	Peso (kg)
1 - Celular	0.5
2 - Geladeira	60.0
3 - Freezer 	100.0
4 - Cadeira	5.0
5 - Luminária	0.8
6 - Lavadora de roupa	120kg       
''')
                        print()    
                        print("Digite FIM para finalizar a seleção.")
                        while True:
                            prod = input("=> ")
                            try:
                                if prod == "1":
                                    item(1,"CELULAR",0.5)
                                elif prod == "2":
                                    item(1,"GELADEIRA",60)
                                elif prod == "3":
                                    item(1,"FREEZER",100)
                                elif prod == "4":
                                    item(1,"CADEIRA",5)
                                elif prod == "5":
                                    item(1,"LUMINÁRIA",0.8)
                                elif prod == "6":
                                    item(1,"LAVADORA DE ROUPAS",120)
                                elif prod.upper() == 'FIM':
                                    break
                                else:
                                    print("Comando inválido!")
                            except:
                                print("Comando inválido!")                     
                        soma = 0
                        for i in carrinho:
                            soma += i.peso_total
                        print(soma)
                        
                        if soma == 0:
                            print("Carga nula. Transporte não pode ser realizado!")
                            carrinho.clear()  
                            break
                        print("O seu destino exige os seguintes veículos: ")
                                                
                        if soma > 0 and soma <= 1000:
                            print()
                            print(f"Veículo de pequeno porte, custando um total de R${4.87 * arquivo[cidade2][iter]}")
                            transporte = Transporte(cidade1, cidade2, soma, "CAMINHÃO PEQUENO", 4.87)
                            transportes_lista.append(transporte)
                            carrinho.clear() 
                            
                        elif soma > 1000 and soma <= 4000:
                            print(f"Veículo de médio porte, custando um total de R${11.92 * arquivo[cidade2][iter]}")
                            transporte = Transporte(cidade1, cidade2, soma, "CAMINHÃO MÉDIO", 11.92)
                            transportes_lista.append(transporte)
                            carrinho.clear() 
                                            
                        elif soma > 4000 and soma <= 10000:
                            print(f"Veículo de grande porte, custando um total de R${27.44 * arquivo[cidade2][iter]}")
                            transporte = Transporte(cidade1, cidade2, soma, "CAMINHÃO GRANDE", 27.44)
                            transportes_lista.append(transporte)
                            carrinho.clear()  
                    
                        else:
                            print("Carga máxima atingida!")                                 
                    else:
                        print("Cidade de destino não encontrada!") 
                
                    
        else:
            print("Cidade de origem não encontrada!") 
        pass
    if escolha == '3':
        for i in transportes_lista:
            print(i)
    if escolha == '4':
        print("Deseja sair?")
        while True:
            yes_no = input("Y - Sim / N - Não => ")
            if yes_no.upper() == 'Y':
                print("Saindo...")
                exit()
            if yes_no.upper() == 'N':
                print("Voltando ao menu")
                break
            else:
                print("Opção inválida!")


