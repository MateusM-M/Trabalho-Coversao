import funcoes
valor = input('Qual o valor?: ')
base = input('Qual sua base?: ')
nova_base = input('Qual sua nova base?: ')
decimal = funcoes.basepradeci(valor, int(base))
print (funcoes.deciprabase(decimal, int(nova_base)))