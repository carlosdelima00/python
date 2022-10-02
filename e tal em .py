print(" digite seu nome: ")
nome=input("")
print(" digite seu dinheiro, sr " + nome  +  " para saber sua condição: ")
money=int(input())
if money<=1000:
    adjetivo="foda"
    print(nome + " você é " + adjetivo)
else:
    adjetivo="npc"
    print(nome + " você é " + adjetivo)

print("dê sua avaliação do programa de 1.0 á 5.0 :")
av=float(input())
if av>=3.5 : 
    print(" obrigado pela nota" )    
else :
     print("iremos melhorar pelo valor de sua nota foi muito baixo e iremos fazer de tudo para melhorar sua experiencia: ," )

print(" fim,do programa! ")

print(" nome do estudante: ")
nome_do_aluno=input("")
print("digite as notas")
n1=float(input())
n2=float(input())
media=(n1 + n2) /2
print(" a media: " +  str(media))
if media>=6:
    print(" o " + nome_do_aluno + " foi aprovado" )
else:
    print(" o " + nome_do_aluno + " foi reprovado ")   