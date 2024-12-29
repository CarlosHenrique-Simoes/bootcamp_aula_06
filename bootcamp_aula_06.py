def incrementar(numero):
    return numero + 1


def decrementar(numero):
    return numero - 1


def main():
    numero = 0
    while True:
        print(f"Valor atual: {numero}")
        escolha = input(
            "Digite 'i' para incrementar, 'd' para decrementar ou 'q' para sair: "
        ).lower()

        if escolha == "i":
            numero = incrementar(numero)
        elif escolha == "d":
            numero = decrementar(numero)
        elif escolha == "q":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()
