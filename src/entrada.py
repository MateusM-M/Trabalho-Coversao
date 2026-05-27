def valor():
     return input('Qual o valor?: ')
def base_origem():
     return int(input('Qual sua base?: '))
def base_saida():
     return int(input('Qual sua nova base?: '))
def entrada_arq():
     entrada_csv = open("../entrada.csv", "r")
     
     for linha in entrada_csv:

                linha = linha.strip()

                linha = linha.split(";")

                valor = linha[0]
                base_origem = int(linha[1])
                base_saida = int(linha[2])
     entrada_csv.close()
     return valor, base_origem, base_saida