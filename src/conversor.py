from fractions import Fraction

TERMOS = "0123456789ABCDEF"
MAX_CASAS_FRACIONARIAS = 16


def _normalizar_string_numero(valor):
    if valor is None:
        return ""
    texto = str(valor).strip().upper()
    texto = texto.replace(",", ".")
    return texto


def validar(valor, base):
    valor = _normalizar_string_numero(valor)
    termos_validos = TERMOS[:base]
    if valor.count(".") > 1:
        return False
    partes = valor.split(".")
    if len(partes) == 0:
        return False
    inteiro = partes[0]
    fracao = partes[1] if len(partes) == 2 else ""
    if inteiro == "" and fracao == "":
        return False
    if inteiro:
        for digito in inteiro:
            if digito not in termos_validos:
                return False
    if fracao:
        for digito in fracao:
            if digito not in termos_validos:
                return False
    return True


def _dividir_numero(valor):
    valor = _normalizar_string_numero(valor)
    if "." in valor:
        inteiro, fracao = valor.split(".", 1)
    else:
        inteiro, fracao = valor, ""
    return inteiro, fracao


def baseparadecimal(numero, base):
    numero = _normalizar_string_numero(numero)
    inteiro, fracao = _dividir_numero(numero)
    valor = Fraction(0, 1)
    for digito in inteiro:
        if digito == "":
            continue
        valor = valor * base + TERMOS.index(digito)
    if fracao:
        denominador = base
        for digito in fracao:
            valor += Fraction(TERMOS.index(digito), denominador)
            denominador *= base
    return valor


def _string_decimal_para_fracao(numero):
    numero = _normalizar_string_numero(numero)
    if "." not in numero:
        return Fraction(int(numero), 1)
    inteiro, fracao = numero.split(".", 1)
    inteiro_valor = int(inteiro) if inteiro != "" else 0
    numerador = int(fracao)
    denominador = 10 ** len(fracao)
    return Fraction(inteiro_valor * denominador + numerador, denominador)


def decimalparabase(numero, base, max_frac_digits=MAX_CASAS_FRACIONARIAS):
    if isinstance(numero, str):
        numero = _string_decimal_para_fracao(numero)
    elif isinstance(numero, (int, float)):
        numero = Fraction(str(numero))
    elif not isinstance(numero, Fraction):
        raise TypeError("Número inválido para conversão")

    inteiro = abs(numero.numerator) // numero.denominator
    resto = abs(numero) - inteiro
    if inteiro == 0:
        resultado_inteiro = "0"
    else:
        digitos_inteiro = []
        while inteiro > 0:
            digitos_inteiro.append(TERMOS[int(inteiro % base)])
            inteiro //= base
        resultado_inteiro = "".join(reversed(digitos_inteiro))

    if resto == 0:
        return resultado_inteiro

    digitos_fracao = []
    truncado = False
    for _ in range(max_frac_digits):
        resto *= base
        digito = int(resto.numerator // resto.denominator)
        digitos_fracao.append(TERMOS[digito])
        resto -= Fraction(digito, 1)
        if resto == 0:
            break
    if resto != 0:
        truncado = True
    resultado = resultado_inteiro + "," + "".join(digitos_fracao)
    if truncado:
        resultado += " (truncado)"
    return resultado


def _fracao_para_string_decimal(valor, max_frac_digits=MAX_CASAS_FRACIONARIAS):
    if isinstance(valor, str):
        valor = _string_decimal_para_fracao(valor)
    elif isinstance(valor, (int, float)):
        valor = Fraction(str(valor))
    elif not isinstance(valor, Fraction):
        raise TypeError("Número inválido para formatação decimal")

    inteiro = abs(valor.numerator) // valor.denominator
    resto = abs(valor) - inteiro
    if resto == 0:
        return str(inteiro)

    digitos_fracao = []
    truncado = False
    for _ in range(max_frac_digits):
        resto *= 10
        digito = int(resto.numerator // resto.denominator)
        digitos_fracao.append(str(digito))
        resto -= Fraction(digito, 1)
        if resto == 0:
            break
    if resto != 0:
        truncado = True
    resultado = f"{inteiro},{''.join(digitos_fracao)}"
    if truncado:
        resultado += " (truncado)"
    return resultado


def converter(valor, base_origem, base_saida, max_frac_digits=MAX_CASAS_FRACIONARIAS):
    if not validar(valor, base_origem):
        raise ValueError("Valor inválido para a base informada")
    if base_origem == base_saida:
        if base_origem == 10:
            return _fracao_para_string_decimal(valor, max_frac_digits)
        return decimalparabase(baseparadecimal(valor, base_origem), base_origem, max_frac_digits)
    if base_origem == 10:
        return decimalparabase(valor, base_saida, max_frac_digits)
    if base_saida == 10:
        return _fracao_para_string_decimal(baseparadecimal(valor, base_origem), max_frac_digits)
    return decimalparabase(baseparadecimal(valor, base_origem), base_saida, max_frac_digits)
