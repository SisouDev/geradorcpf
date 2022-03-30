
#FUNÇÃO PARA VALIDAR O CPF
#cpf = input('Digite seu CPF: ')
from random import randint

#-----------------------------------------------------------------------------------------------------------------------

#GERA NUMERO ALEATORIO , TAMANHO 11 (CPF TAM)
numero = str(randint(1000000000,9999999999))

#-----------------------------------------------------------------------------------------------------------------------

novocpf = numero                                #ELIMINA OS DOIS ULTIMOS DIGITOS DO CPF
reverso = 10                                    #CONTADOR REVERSO
total = 0

#-----------------------------------------------------------------------------------------------------------------------

#LOOP DO CPF
for index in range(19):
    if index > 8:                               #PRIMEIRO INDICE DE 0 A 9
        index -= 9                              #9 PRIMEIROS DIGITOS DO CPF
    total += int(novocpf[index]) * reverso      #VALOR TOTAL DA MULTIPLICAÇÃO

#-----------------------------------------------------------------------------------------------------------------------

reverso -= 1                                    #DECREMENTA O CONTADOR REVERSO
if reverso < 2:
    reverso = 11
    d = 11 - (total % 11)

    # -----------------------------------------------------------------------------------------------------------------------

    if d > 9:                                   #SE O DIGITO FOR MAIOR QUE 9 O VALOR É 0
        d = 0
    total = 0                                   # 0 NO TOTAL
    novocpf += str(d)                           #CONCATENA O DIGITO GERADO NO NOVO CPF

print(novocpf)

#-----------------------------------------------------------------------------------------------------------------------

#VALIDADOR DE CPF

#if cpf == novocpf:
#print('Valido')
#else:
#print('Inválido')










