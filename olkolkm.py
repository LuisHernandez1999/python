
while True: 
    print() 
    num_1 = input( 'Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input ('Digite um operador: ')
        
    num_1 = float(num_1)
    num_2 = float(num_2)
         

    
    #if not num_1.isnumeric() or not num_2.isnumeric():
      #  print('Você precisa entrar um número ')
       # continue 
    

    if operador == '+':
        print(num_1 + num_2)
    elif operador == "-":
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2 )  
    else:
        print('Operador inválido') 
    
    sair = input('Deseja sair ? [s]im ou [n]ão: ')
    if sair == 's':
        break            
    