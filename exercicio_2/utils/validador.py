def validar_nota(nota_str):
    try:
        nota = float(nota_str)
        if 0 <= nota <= 10:
            return nota
        else:
            print("Nota inválida. Digite um valor entre 0 e 10.")
            return None
    except ValueError:
        print("Entrada inválida. Digite um número ou 'fim' para encerrar.")
        return None
 