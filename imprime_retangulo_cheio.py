largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
caractere = "#"


def retângulo(largura, altura, caractere):

    linha = caractere * largura

    for i in range(altura):
        print(linha)

retângulo(caractere, altura, largura)