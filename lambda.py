contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
print(soma(5,10))

calculadora = {
    'soma': lambda a, b: a+b, 
    'subtracao': lambda a, b: a - b,
    'mult': lambda a, b: a * b,
    'divisao': lambda a, b: a / b,
}

soma = calculadora['soma']
mult = calculadora['mult']

print('A soma é {}'.format(soma(10,15)))
print('A multiplicacao é: {}'.format(mult(10,2)))