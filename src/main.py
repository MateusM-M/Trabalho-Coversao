import conversor as fc
modo = input("Escolha o modo da aplicação: 1(modo normal), 2(modo csv) 3(modo quiz)")
if modo == "1":
    valor = input('Qual o valor?: ')
    base_origem = int(input('Qual sua base?: '))
    base_saida = int(input('Qual sua nova base?: '))
    if base_origem == 10 and (base_saida == 2 or base_saida == 8 or base_saida == 16):
        print(fc.decimalparabase(valor, base_saida)) 
    elif (base_origem == 2 or base_origem == 8 or base_origem == 16) and base_saida == 10:
        print(fc.baseparadecimal(valor, base_origem))
    elif (base_origem == 2 and base_saida == 8) or (base_origem == 8 and base_saida == 2):
    
    elif (base_origem == 16 and base_saida == 2) or (base_origem == 2 and base_saida == 16):
    elif (base_origem == 8 and base_saida == 16) or (base_origem == 16 and base_saida == 8):
elif modo == "2":

elif modo == "3":
