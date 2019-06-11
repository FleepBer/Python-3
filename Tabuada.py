linha = 1
coluna = 1
while linha <= 10:
    while coluna <= 10:
        print (linha*coluna, end ="\t")
        coluna = coluna + 1
#Quando bater linha x coluna e der 11...ele pula pro próximo while
    linha = linha + 1
    print ()
    coluna = 1
#print (" ") = espaço em branco
#print ("\t")= TAB = Outra linha
