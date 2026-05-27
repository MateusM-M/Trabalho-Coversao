import random
import conversor as fc
def quiz():
    print("Modo quiz selecionado.")
    pontos = 0
     
    for nivel in range(1, 6):
        if nivel == 1:
            valor_decimal = random.randint(0, 15)

        elif nivel == 2:
            valor_decimal = random.randint(16, 255)

        elif nivel == 3:
            valor_decimal = random.randint(256, 1023)

        elif nivel == 4:
            valor_decimal = random.randint(1024, 65535)

        elif nivel == 5:
            parte_inteira = random.randint(0, 255)
            parte_fracionaria = random.randint(1, 1000)
            valor_decimal = f"{parte_inteira}.{parte_fracionaria}"

        base_origem = random.choice([2, 8, 10, 16])
        base_saida = random.choice([2, 8, 10, 16])

        while base_saida == base_origem:
            base_saida = random.choice([2, 8, 10, 16])

        if base_origem == 10:
            valor = str(valor_decimal)

        else:
            valor = fc.decimalparabase(str(valor_decimal), base_origem)
            valor = valor.replace(" (truncado)", "")
        if base_origem == 10 and base_saida in (2, 8, 16):
            resposta_correta = fc.decimalparabase(valor, base_saida)

        elif base_origem in (2, 8, 16) and base_saida == 10:
            resposta_correta = fc.baseparadecimal(valor, base_origem)

        elif (base_origem == 2 and base_saida in (8, 16)) or (base_origem in (8, 16) and base_saida == 2):
            resposta_correta = fc.bin_oct_hex(valor, base_origem, base_saida)

        elif (base_origem == 8 and base_saida == 16) or (base_origem == 16 and base_saida == 8):
            resposta_correta = fc.oct_hex(valor, base_origem, base_saida)

        resposta_usuario = input(f"Converta o {valor} da base {base_origem} para base {base_saida}: ").upper()

        if resposta_usuario == str(resposta_correta).upper():
            
            print("Correto!")
            pontos += 1

        else:

            print(f"Errado!\n O correto seria {resposta_correta}")
    
    print(f"Sua pontuação final foi de: {pontos} pontos de cinco.")