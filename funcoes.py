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
