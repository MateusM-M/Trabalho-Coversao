import funcoes as fc
valor = input('Qual o valor?: ')
base = input('Qual sua base?: ')
nova_base = input('Qual sua nova base?: ')
decimal = fc.basepradec(valor, int(base))
print (fc.deciprabase(decimal, int(nova_base)))