#listas(arrays) dada pelo simbolo "[]"
#ex:
playstations=["ps1", "ps2" , "ps3" , "ps4" , "ps5"]
print(playstations[4])
# para sabermos a quantidade de itens que temos em uma lista basta adicionarmos a keyword "len"
#ex
print(str(len(playstations)) + " esse é o total de itens ! ")
# se quiser adicionar mais itens a sua lista sem alterar o codigo original usa se a keyword 'append'!
#ex:
guitarra=["stratocaster","les paul"]
guitarra.append("telecaster")
#del guitarra[1], o "del" serve paraa deletar algum elemento da lista!
print(str(len(guitarra))) ; print(guitarra)
instrumentos=list(guitarra)
print( " o total foi:" + str(len(instrumentos))) ; print(instrumentos)
