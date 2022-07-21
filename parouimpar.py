import random
from time import sleep

print('=-='*10)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-='*10)
sleep(1)
nome = input('Meu nome é Charlie, qual é o seu nome?')
vitorias = 0

while True:
    d = input('Par ou Impar? [P/I] ').upper().strip()
    sleep(1)
    n = int(input('Digite um número de 0 a 10: '))
    sleep(1)
    vm = random.randint(0,10) #Valor da maquina
    soma = n + vm
    if soma % 2 == 0:
        jogo = 'PAR'
        if d == 'P':
            vitorias += 1
            resultado = 'VENCEU'
        else:
            resultado = 'PERDEU'
            break
    else:
        jogo = 'IMPAR'
        if d == 'I':
            vitorias += 1
            resultado = 'VENCEU'
            print('Vamos mais uma...')
        else:
            resultado = 'PERDEU'
            print(f'Você jogou {n} e o computador {vm}. Total de {soma} Deu {jogo}')
            break
    print(f'Você jogou {n} e o computador {vm}. Total de {soma} Deu {jogo}')
    sleep(1)
    print(f'Você {resultado}')
    sleep(1)

print(f'GAME OVER! Você venceu {vitorias} vezes')