from validador import senha_forte

def main():
    while True:
        senha = input("Digite uma senha forte (ou 'sair' para encerrar): ")
        if senha.lower() == 'sair':
            print("Encerrando o programa.")
            break
        if senha_forte(senha):
            print("Senha forte cadastrada com sucesso!")
            break
        else:
            print("Senha fraca. A senha deve ter pelo menos 8 caracteres e conter pelo menos 1 número.")

if __name__ == "__main__":
    main()
