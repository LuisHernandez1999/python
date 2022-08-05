nota1 = float(input('Entre a nota 1: '))
nota2 = float(input('Entre a nota 2: '))
nota3 = float(input('Entre a nota 3: '))
nota4 = float(input('Entre a nota 4: '))
 
nome_aluno= input('Entre o nome do aluno: ')
média = ((nota1+nota2+nota3+nota4)/4)
print(f'{nome_aluno}, {média}: ')
if média  >= 7:
    print('Aprovado')
else:
    print('Reprovado')
    
media_peso = ((nota1*1)+(nota2*2)+(nota3*3)+(nota4*4))/10
if media_peso < 5:
    print('Reprovado')
elif media_peso < 7:
    print('Recuperação')
else:
    print('Aprovado')  

    
         
