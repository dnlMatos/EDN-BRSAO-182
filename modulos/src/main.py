def boas_vindas(nome: str) -> str:
    return f"Bem-vindo, {nome}! Vamos aprender Python!"

def main():
    nome = input("Digite seu nome: ")
    print(boas_vindas(nome))

    # Operações matemáticas
    from matematica import soma, subtrai, fatorial
    from meu_pacote.operacoes import multiplica

    a = 5
    b = 3

    print(f"Soma: {soma(a, b)}")
    print(f"Subtração: {subtrai(a, b)}")
    print(f"Multiplicação: {multiplica(a, b)}")
    print(f"Fatorial de {a}: {fatorial(a)}")

if __name__ == "__main__":
    main()