
def printa_valor(valorfinal):
    print(f"O valor na base pedida é {valorfinal}.")


def printa_valor(valorfinal):
    print(f"O valor na base pedida é {valorfinal}.")


def mensagem_de_erro(valor, base):
    print(f"O {valor} não pode estar na base {base}.")


def printa_maxbits(bits, valorfinal):
    print(f"O maior valor representável com {bits} bits em cada base é: \n" f"{valorfinal}")
    

def saida_csv(valor, base_origem, resultado, base_saida):
    saida_csv = open("../saida.csv", "w")
    saida_csv.write(f"{valor};{base_origem};{resultado};{base_saida}\n")
                
    saida_csv.close()