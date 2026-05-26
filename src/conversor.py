from fractions import Fraction

# --- FUNÇÃO AUXILIAR DE SUPORTE (F6) ---
def _preparar_numero(valor):
    """Padroniza a string substituindo vírgula por ponto e separa em inteiro e fração."""
    texto = str(valor).strip().upper().replace(",", ".")
    if "." in texto:
        inteiro, fracao = texto.split(".", 1)
    else:
        inteiro, fracao = texto, ""
    return inteiro, fracao


# --- F1: DECIMAL PARA BASE ---
def decimalparabase(numero_str, base): 
    inteiro_str, fracao_str = _preparar_numero(numero_str)
    termos = "0123456789ABCDEF"
    
    # Processamento da Parte Inteira (Divisões Sucessivas)
    numero_int = int(inteiro_str) if inteiro_str else 0
    if numero_int == 0:
        res_inteiro = "0"
    else:
        lista = []
        while numero_int > 0:
            lista.append(termos[numero_int % base])
            numero_int //= base
        lista.reverse()
        res_inteiro = "".join(lista)
        
    # Processamento da Parte Fracionária (Multiplicações Sucessivas)
    if not fracao_str:
        return res_inteiro

    res_fracao = []
    truncado = False
    # Transforma a string fracionária em uma fração exata (Ex: "625" -> 625/1000)
    resto = Fraction(int(fracao_str), 10**len(fracao_str))
    
    for _ in range(16):
        resto *= base
        digito = int(resto)
        res_fracao.append(termos[digito])
        resto -= digito
        if resto == 0:
            break
    else:
        if resto > 0:
            truncado = True
            
    resultado = f"{res_inteiro},{''.join(res_fracao)}"
    if truncado:
        resultado += " (truncado)"
    return resultado


# --- F2: BASE PARA DECIMAL ---
def baseparadecimal(numero_str, base):
    inteiro_str, fracao_str = _preparar_numero(numero_str)
    termos = "0123456789ABCDEF"
    
    # Processamento da Parte Inteira (Somatório Posicional)
    decimal_int = 0
    cont = 0
    for i in range(len(inteiro_str) - 1, -1, -1):
        decimal_int += termos.index(inteiro_str[i]) * (base ** cont)
        cont += 1
        
    # Processamento da Parte Fracionária (Potências Negativas)
    if not fracao_str:
        return str(decimal_int)
        
    decimal_frac = Fraction(0)
    for i, digito in enumerate(fracao_str):
        decimal_frac += Fraction(termos.index(digito), base ** (i + 1))
        
    # Soma exata utilizando Fraction para evitar floating-point bugs do Python
    total = Fraction(decimal_int) + decimal_frac
    
    # Formatação controlada da saída em base 10 (até 16 casas)
    int_part = total.numerator // total.denominator
    resto_part = total - int_part
    
    res_frac = []
    truncado = False
    for _ in range(16):
        resto_part *= 10
        digito = int(resto_part)
        res_frac.append(str(digito))
        resto_part -= digito
        if resto_part == 0:
            break
    else:
        if resto_part > 0:
            truncado = True
            
    resultado = f"{int_part},{''.join(res_frac)}"
    if truncado:
        resultado += " (truncado)"
    return resultado


# --- F3: BINÁRIO <-> OCTAL / HEXADECIMAL ---
def bin_oct_hex(numero_str, base_origem, base_destino):
    inteiro_str, fracao_str = _preparar_numero(numero_str)
    
    tabela_conversao_octal = {"000": "0", "001": "1", "010": "2", "011": "3", "100": "4", "101": "5", "110": "6", "111": "7"}
    tabela_conversao_hex = {"0000": "0", "0001": "1", "0010": "2", "0011": "3", "0100": "4", "0101": "5", "0110": "6", "0111": "7", "1000": "8", "1001": "9", "1010": "A", "1011": "B", "1100": "C", "1101": "D", "1110": "E", "1111": "F"}
    tabela_bin_octal = {"0": "000", "1": "001", "2": "010", "3": "011", "4": "100", "5": "101", "6": "110", "7": "111"}
    tabela_bin_hex = {"0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111", "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111"}

    res_inteiro = ""
    res_fracao = ""
    truncado = False

    # Binário para Octal ou Hexadecimal
    if base_origem == 2:
        tam_bloco = 3 if base_destino == 8 else 4
        tabela = tabela_conversao_octal if base_destino == 8 else tabela_conversao_hex
        
        # Inteiro: Agrupa da direita para a esquerda (Completa à ESQUERDA)
        while len(inteiro_str) % tam_bloco != 0:
            inteiro_str = "0" + inteiro_str
        for i in range(0, len(inteiro_str), tam_bloco):
            res_inteiro += tabela[inteiro_str[i : i + tam_bloco]]
            
        # Fração: Agrupa da esquerda para a direita (Completa à DIREITA)
        if fracao_str:
            while len(fracao_str) % tam_bloco != 0:
                fracao_str += "0"
            for i in range(0, len(fracao_str), tam_bloco):
                res_fracao += tabela[fracao_str[i : i + tam_bloco]]
            
            if len(res_fracao) > 16:
                res_fracao = res_fracao[:16]
                truncado = True

    # Octal ou Hexadecimal para Binário
    else:
        tabela = tabela_bin_octal if base_origem == 8 else tabela_bin_hex
        
        for digito in inteiro_str:
            res_inteiro += tabela[digito]
        res_inteiro = res_inteiro.lstrip("0") or "0"
        
        if fracao_str:
            for digito in fracao_str:
                res_fracao += tabela[digito]
            if len(res_fracao) > 16:
                res_fracao = res_fracao[:16]
                truncado = True

    resultado = res_inteiro
    if fracao_str:
        resultado += "," + res_fracao
        if truncado:
            resultado += " (truncado)"
    return resultado


# --- F4: OCTAL <-> HEXADECIMAL (USANDO BINÁRIO) ---
def oct_hex(numero_str, base_origem, base_destino):
    if base_origem == 8 and base_destino == 16:
        binario = bin_oct_hex(numero_str, 8, 2)
        return bin_oct_hex(binario, 2, 16)
    if base_origem == 16 and base_destino == 8:
        binario = bin_oct_hex(numero_str, 16, 2)
        return bin_oct_hex(binario, 2, 8)


# --- F5: VALIDAR ENTRADA ---
def validar(valor, base):
    valor = str(valor).upper().replace(",", ".")
    termos = "0123456789ABCDEF"
    termos_validos = termos[0:base]
    
    if valor.count(".") > 1:
        return False
        
    numeroseparado = valor.split(".")
    
    if len(numeroseparado) == 2 and (numeroseparado[0] == "" and numeroseparado[1] == ""):
        return False

    for parte in numeroseparado:
        for digito in parte:
            if digito not in termos_validos:
                return False
    return True


# --- F10: CALCULADORA DE MÁXIMOS ---
def valores_max(quantidade_bits):
    valor_max = 2 ** quantidade_bits - 1
    
    print(f"\n--- Máximos para {quantidade_bits} bits ($2^{{{quantidade_bits}}} - 1$) ---")
    print(f"Decimal:     {valor_max}")
    print(f"Binário:     {bin(valor_max)[2:]}")
    print(f"Octal:       {oct(valor_max)[2:]}")
    print(f"Hexadecimal: {hex(valor_max)[2:].upper()}")
    print("-" * 40)
    return valor_max    