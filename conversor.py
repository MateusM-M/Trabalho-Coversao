# F1 #
def deciprabase(numero, base): 
    termos = "0123456789ABCDEF"
    if numero == 0:
        return "0"
    lista = []
    while numero > 0:
        resto = numero % base 
        numero = numero // base
        lista.append(termos[resto])
    lista.reverse()
    return "".join(lista)

# F2 #
def basepradec(numero, base):
    termos = "0123456789ABCDEF"
    cont = 0
    decimal = 0
    numero_str = str(numero)
    num_d_algaris = len(numero_str)
    for i in range(num_d_algaris - 1, -1, -1):
            caractere = numero_str[i]
            num_para_calc = termos.index(caractere)
            decimal += num_para_calc * base ** cont
            cont += 1
    return decimal

# F3 #
def bin_oct_hex(numero, base, nova_base):
    numero = numero.upper()
    resultado = ""


    #############dicionarios para conversões: #######################
    tabela_conversao_octal = {
         "000": "0", "001": "1",
         "010": "2", "011": "3",
         "100": "4", "101": "5",
         "110": "6", "111": "7",
    }
    tabela_conversao_hex = {
         "0000": "0", "0001": "1", "0010": "2", "0011": "3",
         "0100": "4", "0101": "5", "0110": "6", "0111": "7",
         "1000": "8", "1001": "9", "1010": "A", "1011": "B",
         "1100": "C", "1101": "D", "1110": "E", "1111": "F"
    }
    tabela_bin_octal = {
         "0": "000", "1": "001", "2": "010", "3": "011",
         "4": "100", "5": "101", "6": "110", "7": "111"
    }
    tabela_bin_hex = {
         "0": "0000", "1": "0001", "2": "0010", "3": "0011",
         "4": "0100", "5": "0101", "6": "0110", "7": "0111",
         "8": "1000", "9": "1001", "A": "1010", "B": "1011",
         "C": "1100", "D": "1101", "E": "1110", "F": "1111"
    }
    #################################################################


    #Binário para octal:
    if base == 8:
        while len(numero) % 3 != 0:
             numero = "0" + numero
        for i in range(0, len(numero), 3):
            bloco = numero[i : i + 3]
            resultado += tabela_conversao_octal[bloco]
    
    #Binário para hexadecimal:
    if base == 16:
        while len(numero) % 4 !=0:
              numero = "0" + numero
        for i in range(0, len(numero), 4):
            bloco = numero[i : i + 4]
            resultado += tabela_conversao_hex[bloco]

    #Octal para Binário:
    if base == 8 and nova_base == 2:
         for i in numero:
              bloco = tabela_bin_octal[i]
              resultado += bloco
              
    #Hexadecimal para Binário:
    if base == 16 and nova_base == 2:
         for i in numero:
              bloco = tabela_bin_hex[i]
              resultado += bloco
            

    return resultado


# F4 #
def oct_hex(numero, base, nova_base):
     
     resultado = ""

     #Octal para Hexadecimal
     if base == 8 and nova_base == 16:
          binario = bin_oct_hex(numero, 8, 2)
          resultado = bin_oct_hex(binario, 2, 16)
          return resultado
     #Hexadecimal para Octal
     if base == 16 and nova_base == 8:
          binario = bin_oct_hex(numero, 16, 2)
          resultado = bin_oct_hex(binario, 2, 8)
          return resultado
      