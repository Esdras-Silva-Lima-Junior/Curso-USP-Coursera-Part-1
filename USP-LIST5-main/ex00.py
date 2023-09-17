largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

a = 0
l = 0

while a != altura:
    while l != largura:
        if l != largura:
            print("#", end="")
            l = l + 1
    print("")
    a = a + 1
    l = 0