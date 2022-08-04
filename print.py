


nome = ' Thomas turbano '
idade = int( input("Entre idade "))
altura = float( input("Entre altura "))
peso = float( input("Entre peso "))
indice_massa_c = float (peso / (altura ** 2))
print('{n} tem {i} anos e seu IMC é {im}.'.format (n=nome , i=idade , im=indice_massa_c))
print(type(idade))

