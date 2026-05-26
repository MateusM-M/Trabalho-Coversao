import conversor as fc
import entrada as ent
import saida as sd

modo = int(input("Escolha o modo da aplicação: 1(modo normal), 2(modo passo-a-passo), 3(modo csv), 4(modo quiz): ").strip())

match modo:
    case 1:
        print("Modo normal selecionado.")

        #Coleta os dados
        valor = ent.valor()
        base_origem = int(ent.base_origem)
        base_saida = int(ent.base_saida)

        #Valida a entrada. Se der erro, avisa e para por aqui.
        if not fc.validar(valor, base_origem):
            sd.mensagem_de_erro()
        else:

            if base_origem == 10 and base_saida in (2, 8, 16):
                resultado = fc.decimalparabase(valor, base_saida)

            elif base_origem in (2, 8, 16) and base_saida == 10:
                resultado = fc.baseparadecimal(valor, base_origem)

            elif (base_origem == 2 and base_saida in (8, 16)) or (base_origem in (8, 16) and base_saida == 2):
                resultado = fc.bin_oct_hex(valor, base_origem, base_saida)

            elif (base_origem == 8 and base_saida == 16) or (base_origem == 16 and base_saida == 8):
                resultado = fc.oct_hex(valor, base_origem, base_saida)

            sd.printa_valor(resultado)
            
    case 2:
        print("Modo passo-a-passo selecionado.")
        #Coleta os dados
        valor = ent.valor()
        base_origem = int(ent.base_origem)
        base_saida = int(ent.base_saida)

        #Valida a entrada. Se der erro, avisa e para por aqui.
        if not fc.validar(valor, base_origem):
            sd.mensagem_de_erro()
        else:

            if base_origem == 10 and base_saida in (2, 8, 16):
                resultado = fc.decimalparabase(valor, base_saida, passo_a_passo=True)

            elif base_origem in (2, 8, 16) and base_saida == 10:
                resultado = fc.baseparadecimal(valor, base_origem, passo_a_passo=True)

            elif (base_origem == 2 and base_saida in (8, 16)) or (base_origem in (8, 16) and base_saida == 2):
                resultado = fc.bin_oct_hex(valor, base_origem, base_saida, passo_a_passo=True)

            elif (base_origem == 8 and base_saida == 16) or (base_origem == 16 and base_saida == 8):
                resultado = fc.oct_hex(valor, base_origem, base_saida, passo_a_passo=True)

            sd.printa_valor(resultado)
            
        