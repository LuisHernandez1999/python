print('Secelecione a opcao almejada')
print ( '1  Fitness ')
print (' 2 Comum ')
opcao = input('opcao: ')

if opcao == '1':
    d1 ={1:'Salada de sardinha', 2:'Arroz colorido',3:'Salada com sardinha', 4:'Macarrão colorido '}
    print(d1)
    print ( f'Alimentacao comum, esta sao sua opcao {d1}')  
    prato_escolhido = int(input('Entre um prato:'))
    print(d1[prato_escolhido])
    print("Prato fitness escolhido") 
            
elif opcao  == '2':
    d2 ={1:'Panqueca de Carne Moida', 2:'Arroz de forno', 3:'Salada de macarrão com sardinha', 4:'Macarrão de panela de pressão'}
    print(d2)
    print(f'Alimentacao comum, esta sao sua opcao {d2}')
    prato_escolhido = int(input('Entre um prato:'))
    print(d2[prato_escolhido])         
    print("Prato Comum escolhido")
else: 
    print ("Este prato esta indispodivel")
            
user = float(input("entre sua renda: " ))
if user >= 1754:
    print('Renda ok ')
elif user < 1754 :
    print('renda muito abaixo')

user_mes = float(input("esta querendo gastar quanto por mês em alimentos ?:  "))
if user_mes >= 300 and user_mes <=600:
    print("Está dentro do orcamento")
elif user_mes < 300 and user_mes > 600:
    print("Está fora do orcamento do mes ")
    
else: 
  print ("Este prato esta indispodivel")
  
  
print ('Deseja vizualizar uma receita ?')
print('1 sim')
print('2 nao')

deseja_ver_receita = input('opcao: ')

if deseja_ver_receita == '1': 
  d3={1:'2 colheres (sopa) de azeite , 1 cebola grande picada ,  1 colher de sobremesa de sal,1 xícara (chá) de arroz integral,molho de tomate e carne ,colher (sopa) de óleo , xícara (chá) de arroz lavado e escorrido ',2:'1 xícara de cenouras picadas e levemente cozidas,1 xícara de batatas picadas e levemente cozidas,1 xícara de brócolis em pedaços levemente cozido,1 lata de ervilhas,2 tomates médios em fatias médias,1 cebola média em fatias largas,Azeitonas em fatias,1 1/2 de manteiga,cheiro verde,sal a gosto',3:'1 xícara (chá) de feijão,3 colheres (sopa) de azeite extravirgem ou óleo,200g de linguiça fresca,1 xícara (chá) de talos de couve picado,3 colheres (sopa) de cebola picada,2 dentes de alho picado,Sal a gosto,½ xícara (chá) de aveia em flocos finos,2 unidades de ovos,½ xícara (chá) de salsa picado'}
  print( f'Alimentacao comum, esta sao sua opcao {d3}' )
  ver_receita = int(input('Entre receita:'))
  print(d3[ver_receita])
  print("pode se deliciar agora")
  
elif deseja_ver_receita == '2':
    print("Acabou") 
else: 
    print('Receita nao existe')