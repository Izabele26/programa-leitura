soma = 0
nova = float('inf')
velha = 0
nome_velha = ''
menos20 = 0
mais40 = 0
sexo_nova = ''

for i in range(3):
    nome = input('Nome: ')
    idade = float(input('Idade: '))
    sexo = input('Sexo (M/F): ')
    
    if idade > velha:
        velha = idade
        nome_velha = nome

    if idade < 20:
        menos20 += 1
    elif idade > 40:
        mais40 += 1

    if idade < nova:
        nova = idade
        sexo_nova = sexo

    soma += idade 

media = soma / 3
print(f'A média das idades é: {media}')
print(f'Pessoa mais velha: {nome_velha}')
print(f'Quantidade de pessoas com menos de 20 anos: {menos20}')
print(f'Quantidade de pessoas com mais de 40 anos: {mais40}')
print(f'Sexo da pessoa mais nova: {sexo_nova}.')
