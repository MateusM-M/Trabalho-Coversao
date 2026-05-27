import conversor as fc
import entrada as ent
import saida as sd
import modo_quiz as quiz
from ansi import Fore, Style

sair='0'



while (sair == '0'): #Condição de Saída
    modo = int(input(Fore.CYAN + "ESCOLHA O MODO DA APLICAÇÃO:\n\n" + 
                    Fore.WHITE + "1: modo normal\n" + 
                    Fore.BLUE + "2: modo passo-a-passo\n" +
                    Fore.LIGHTMAGENTA_EX + "3: modo CSV\n" + 
                    Fore.RED + "4: modo quiz\n" +
                    Fore.MAGENTA + "5: Calcular máximos\n" +
                    Fore.CYAN + "> " + Style.RESET_ALL) 
            .strip())


    match modo:
        case 1:
            print(Fore.WHITE + "\n\nModo normal selecionado." + Style.RESET_ALL)

            #Coleta os dados
            valor = ent.valor()
            base_origem = int(ent.base_origem())
            base_saida = int(ent.base_saida())

            #Valida a entrada. Se der erro, avisa e para por aqui.
            if not fc.validar(valor, base_origem):
                sd.mensagem_de_erro(valor, base_origem)
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
            print(Fore.BLUE + "\n\nModo passo-a-passo selecionado." + Style.RESET_ALL)
            #Coleta os dados
            valor = ent.valor()
            base_origem = int(ent.base_origem())
            base_saida = int(ent.base_saida())

            #Valida a entrada. Se der erro, avisa e para por aqui.
            if not fc.validar(valor, base_origem):
                sd.mensagem_de_erro(valor, base_origem)
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
        
        case 3:
            print(Fore.LIGHTMAGENTA_EX + "\n\nModo CSV selecionado." + Style.RESET_ALL)

            ent.entrada_arq(valor, base_origem, base_saida)

            
            if not fc.validar(valor, base_origem):
                    sd.mensagem_de_erro(valor, base_origem)

            else:

                if base_origem == 10 and base_saida in (2, 8, 16):
                    resultado = fc.decimalparabase(valor, base_saida)

                elif base_origem in (2, 8, 16) and base_saida == 10:
                    resultado = fc.baseparadecimal(valor, base_origem)

                elif (base_origem == 2 and base_saida in (8, 16)) or (base_origem in (8, 16) and base_saida == 2):
                    resultado = fc.bin_oct_hex(valor, base_origem, base_saida)

                elif (base_origem == 8 and base_saida == 16) or (base_origem == 16 and base_saida == 8):
                    resultado = fc.oct_hex(valor, base_origem, base_saida)

                sd.saida_csv(valor, base_origem, resultado, base_saida)
            
        
        case 4:
            quiz.quiz()
                
                
        case 5:
        
            print(Fore.MAGENTA + "\n\nCalculadora de Máximos selecionada." + Style.RESET_ALL)
            
            bits = int(input(Fore.LIGHTMAGENTA_EX + "\nInsira a quantidade de bits: " + Style.RESET_ALL))
            resultado = fc.valores_max(bits)
            sd.printa_maxbits(bits, resultado)

    
        case _:
            print(Fore.RED + "Opção Inválida. Tente novamente" + Style.RESET_ALL)

        
    sair = input(Fore.CYAN + "\n\n0: REINICIAR\n" + Fore.RED + "1: SAIR\n" + Fore.WHITE + "> " + Style.RESET_ALL)
            
            