import time


def animacaoJogoDaVelha(tempo, vezes, string, tamString):
    def freme(tempo):
        time.sleep(tempo)
        print('\n' * 40)

    if vezes == 0:
        time.sleep(1.0)
        return
    elif tamString < 0:
        animacaoJogoDaVelha(tempo, vezes - 1, string, len(string))
    else:
        freme(tempo)
        print(string[tamString:])
        animacaoJogoDaVelha(tempo, vezes, string, tamString-1)

def textoIniciaPartida(vezes):
    a = 0
    while a < vezes: 
        print('iniciando partida.')
        time.sleep(0.1)
        print('\n' * 40)
        print('iniciando partida..')
        time.sleep(0.1)
        print('\n' * 40)
        print('iniciando partida...')
        time.sleep(0.1)
        print('\n' * 40)
        print('iniciando partida...')
        time.sleep(0.1)
        print('\n' * 40)
        print('iniciando partida....')
        time.sleep(0.1)
        print('\n' * 40)
        a = a + 1
    print(a1+a2+a3+pula+ linha+ pula+ b1+ b2+ b3+ pula+ linha+ pula+ c1+ c2+ c3)
    
def textoFinalizaPartida(vezes):
    a = 0
    while a < vezes: 
        print('saindo.')
        time.sleep(0.1)
        print('\n' * 40)
        print('saindo..')
        time.sleep(0.1)
        print('\n' * 40)
        print('saindo...')
        time.sleep(0.1)
        print('\n' * 40)
        print('saindo...')
        time.sleep(0.1)
        print('\n' * 40)
        print('saindo....')
        time.sleep(0.1)
        print('\n' * 40)
        a = a + 1
    print(a1+a2+a3+pula+ linha+ pula+ b1+ b2+ b3+ pula+ linha+ pula+ c1+ c2+ c3)

def formataXeO():
    if valor == str('x'):
        valor = str(' x')
    elif valor == str('o'):
        valor = str(' o')
    posicao = ''    


titulo = '             *****JOGO DA VELHA*****'
animacaoJogoDaVelha(0.1, 2, titulo, len(titulo))

i = 0
while i != 1:
    i = input(' aperte ENTER para jogar ou digite (sair) para sair:')
    if  i == str('sair'):
        textoFinalizaPartida(2)
        break
    valor = str('')
    posicao = str('')
    linha = '  -------------'
    pula = '\n'
    a1 = f' a    |'
    a2 = f'   |'
    a3 = f''

    b1 = f' b    |'
    b2 = f'   |'
    b3 = f''

    c1 = f' c    |'
    c2 = f'   |'
    c3 = f''
    textoIniciaPartida(5)
    arrPosition = {}
    iPositionIndex = 0

    while valor != str('x') and valor != str('o'):
        valor = input('escolha  x ou o:')

    contador = 0
    while contador <= 8:
        if valor == str('x'):
            valor = str(' x')
        elif valor == str('o'):
            valor = str(' o')
        posicao = '' 
        while posicao != str('a1') and posicao != str('a2') and posicao != str('a3') and posicao != str('b1') and posicao != str('b2') and posicao != str('b3') and posicao != str('c1') and posicao != str('c2') and posicao != str('c3') and posicao != str('sair'):

            if contador > 0:
                if valor == str(' x'):
                    valor = str(' o')
                elif valor == str(' o'):
                    valor = str(' x')
            i = 0
            while (i < 1):
                posicao = input(f'essa é a vez do ({valor} ) ecolha uma posição:')
                if posicao in arrPosition:
                    print(f"Escolha outra poição que não seja {posicao}!")
                else:
                    arrPosition[posicao] = valor
                    break
            
        if posicao == str('a1'):
            a1 = f'a {valor} |'
        elif posicao == str('a2'):
            a2 = f'{valor} |'
        elif posicao == str('a3'):
            a3 = f'{valor}'
        elif posicao == str('b1'):
            b1 = f' b {valor} |'
        elif posicao == str('b2'):
            b2 = f'{valor} |'
        elif posicao == str('b3'):
            b3 = f'{valor}'
        elif posicao == str('c1'):
            c1 = f' c {valor} |'
        elif posicao == str('c2'):
            c2 = f'{valor} |'
        elif posicao == str('c3'):
            c3 = f'{valor}'
        elif posicao == str('sair'):
            break 
        

        layout = a1+a2+a3+pula+ linha+ pula+ b1+ b2+ b3+ pula+ linha+ pula+ c1+ c2+ c3

        print ("\n" * 130) 
        print('    1   2   3\n', layout)
        #verifica quem venceu:
            #linhas
        if 'x' in a1 and 'x' in a2 and 'x' in a3 or 'o' in a1 and 'o' in a2 and 'o' in a3:
            print(f'{valor} venceu')
            break
        elif 'x' in b1 and 'x' in b2 and 'x' in b3 or 'o' in b1 and 'o' in b2 and 'o' in b3:
            print(f'{valor} venceu')
            break
        elif 'x' in c1 and 'x' in c2 and 'x' in c3 or 'o' in c1 and 'o' in c2 and 'o' in c3:
            print(f'{valor} venceu')
            break
        #colunas
        elif 'x' in a1 and 'x' in b1 and 'x' in c1 or 'o' in a1 and 'o' in b1 and 'o' in c1:
            print(f'{valor} venceu')
            break
        elif 'x' in a2 and 'x' in b2 and 'x' in c2 or 'o' in a2 and 'o' in b2 and 'o' in c2:
            print(f'{valor} venceu')
            break
        elif 'x' in a3 and 'x' in b3 and 'x' in c3 or 'o' in a3 and 'o' in b3 and 'o' in c3:
            print(f'{valor} venceu')
            break
            #laterais
        elif 'x' in a1 and 'x' in b2 and 'x' in c3 or 'o' in a1 and 'o' in b2 and 'o' in c3:
            print(f'{valor} venceu')
            break
        elif 'x' in a3 and 'x' in b2 and 'x' in c1 or 'o' in a3 and 'o' in b2 and 'o' in c1:
            print(f'{valor} venceu')
            break
        contador = contador +1

        if contador >= 8:
            print('niguem ganhou!')
            break
    input("aperte 'ENTER' para continuar...")
    print('\n'* 40)
