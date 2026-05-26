import conversor as fc
import entrada as ent

modo = int(input("Escolha o modo da aplicação: 1(modo normal), 2(modo csv) 3(modo quiz): ").strip())

match modo:
    case 1:
        print("Modo normal selecionado.")
        valor = ent.valor
        base_origem = int(ent.base)
        base_saida = int(ent.nova_base)
        if base_origem < 2 or base_origem > 16 or base_saida < 2 or base_saida > 16:
            print("Base inválida. Use uma base entre 2 e 16.")
        else:
            try:
                resultado = fc.converter(valor, base_origem, base_saida)
                print(resultado)
            except ValueError as err:
                print(f"Erro: {err}")
    case 2:
        print("Modo csv selecionado.")
    case 3:
        print("Modo quiz selecionado.")
    case _:
        print("Modo inválido.")
