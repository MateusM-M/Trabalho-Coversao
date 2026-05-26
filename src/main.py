import conversor as fc
import entrada as ent

modo = int(input("Escolha o modo da aplicação: 1(modo normal), 2(modo csv) 3(modo quiz): ").strip())

match modo:
    case 1:
        print("Modo normal selecionado.")
        valor = ent.valor
        base_origem = int(ent.base)
        base_saida = int(ent.nova_base)
        if base_origem == 10 and (base_saida == 2 or base_saida == 8 or base_saida == 16):
            print(fc.decimalparabase(valor, base_saida)) 
        elif (base_origem == 2 or base_origem == 8 or base_origem == 16) and base_saida == 10:
            print(fc.baseparadecimal(valor, base_origem))
        elif (base_origem == 2 and base_saida == 8) or (base_origem == 8 and base_saida == 2):
            print(fc.bin_oct_hex(valor, base_origem, base_saida))
        elif (base_origem == 16 and base_saida == 2) or (base_origem == 2 and base_saida == 16):
            print(fc.bin_oct_hex(valor, base_origem, base_saida))
        elif (base_origem == 8 and base_saida == 16) or (base_origem == 16 and base_saida == 8):
            print(fc.oct_hex(valor, base_origem, base_saida))
    case 2:
        print("Modo csv selecionado.")
        

