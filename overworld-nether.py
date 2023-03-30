
print('=' + '-='*20)
print('1 = NETHER -> OVERWORLD')
print('2 = OVERWORLD -> NETHER')
print('=' + '-='*20)
opt = int(input('Digite a opção referente à sua escolha: '))
if opt < 1 or opt > 2:
    raise Exception('DIGITE UMA OPÇÃO DE CONVERSÃO VÁLIDA!')

dim_x, dim_z = input('Digite as coordenadas no eixo \033[32mX e Z\033[m, respectivamente: ').split()

dim_x = float(dim_x)
dim_z = float(dim_z)

if opt == 1:
    print('Coordenadas no Overworld: \033[32m{:.2f}, {:.2f}\033[m'.format(dim_x*8, dim_z*8))
elif opt == 2:
    print('Coordenadas no Nether: \033[31m{:.2f}, {:.2f}\033[m'.format(dim_x/8, dim_z/8))
