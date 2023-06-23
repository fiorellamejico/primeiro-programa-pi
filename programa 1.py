

tempo = float(input('Tempo como fumante (em anos)...: '))
valor = float(input('Valor do maço..................:'))
qtd = float(input('Quantidade de maços por dia....:'))
meses = tempo * 12
dias = meses * 30
total = dias * valor * qtd
if total < 20000:
    print(f'Com o valor R$ {total:.2f}, você poderia ter dado entrada em um carro.')
elif 20000 < total < 50000:
    print(f'Com o valor R$ {total:.2f}, você poderia ter comprado um carro popular usado.')
elif total > 50000:
    print(f'Com o valor R$ {total:.2f}, você poderia ter comprado um carro zero.')
else:
    print('Dados inválidos! Verifique e digite novamente.')
