# --->   Python 3.6    <--- #


                                                                       #### MÓDULOS ###

from time import sleep          #importa o módulo 'sleep' para gerar os segundos de exibição das telas
from datetime import datetime   #importa o módulo 'datetime' para gerar as datas para o arquivo de controle das sequências expedidas (controle.xls)
from datetime import date
from getpass import getpass     #importa o módulo 'getpass' para que as senhas dos usuários não sejam exibidas na hora da digitação
from random import randint
import os
import time



                                                                 #### FUNÇÕES MÓDULO USUÁRIO ####

                                     
### FUNÇÃO PARA DEFINIR O NÚMERO INICIAL E GUARDAR NO ARQUIVO (numeros.txt)
def num():
    opera = open('numeros.txt', 'r')            #abre o arquivo 'numeros.txt'
    texto1 = opera.readlines()                  #lê o arquivo
    ultima_matricula = texto1[-1]               #lê a última linha
    trans_numero = int(ultima_matricula)        #transforma a string da última linha em um números inteiros
    ultimo_numero = trans_numero                #armazena o último numero inteiro
    trans_texto = []                            #armazena a ultima sequencia gerada em uma lista
    for i in range(100):                        #gera 100 repetições
        ultimo_numero += 1                      #acrescenta ao ultimo número + 1
        trans_texto.append(str(ultimo_numero))  #guarda o último numero acrescido em formato inteiro
        trans_texto.append('\n')                #formata o proximo número na proxima linha
        texto1 = opera.readlines()              #lê linha a linha do arquivo 'numeros.txt'
    opera = open('numeros.txt', 'a+')           #abre o arquivo e vai para a última linha preenchida
    opera.writelines(trans_texto)               #escreve no arquivo 'numeros.txt' a ultima sequencia a partir da última linha preenchida
    opera.close()                               #fecha o arquivo 'numeros.txt'



### REGISTRA OS DADOS DAS TENTATIVAS DE ACESSO DOS USUÁRIOS
def registro_de_acessos():
    global tent
    linha = []
    controle = open('provisorio.txt', 'r')
    texto = controle.readlines()
    ultima_matricula = texto[-1][12:]
    d = str(ultima_matricula)
    hora = time.asctime(time.localtime(time.time()))
    horas = ultima_matricula.strip()
    hora_emitida = horas + "\t" + hora[11:19] + "\t" + tent + "\n"
    texto = controle.readlines()
    tentativa = open('acessos.txt', 'a+')
    tentativa.writelines(hora_emitida)
    tentativa.close()



### FUNÇÃO QUE CRIA UMA LISTAGEM DAS SEQUENCIAS EMITIDAS POR DIA POR USUÁRIO
def registro_seq_usuario():
    linha = []
    controle = open('provisorio.txt', 'r')
    texto = controle.readlines()
    ultima_matricula = texto[-1][12:]
    linha.append(str(ultima_matricula))
    texto = controle.readlines()
    tentativa = open('tentativas.txt', 'a+')
    tentativa.writelines(linha)
    tentativa.close()


### FUNÇÃO LIMITA A EMISSÃO PARA 2 SEQUENCIAS DIÁRIAS POR USUÁRIO 
def limite_dia_seq():
    global num_tentativas
    lista = []
    tentativa = open('tentativas.txt', 'r')
    texto = tentativa.readlines()
    adiciona = texto[-1]
    lista.append(texto)
    for i in lista:
        num_tentativas = i.count(adiciona)
    tentativa.close()
    

### FUNÇÃO GERA UM NÚMERO PROVISORIO PARA TESTAR SE O USUÁRIO JÁ TEM MAIS DE 2 TENTATIVAS 
def provisorio():
    global cont
    data = datetime.today()
    dia = data.day
    mes = data.month
    ano = data.year
    controle = open('numeros.txt', 'r')
    texto = controle.readlines()
    ultima_matricula = texto[-1]
    cont = int(ultima_matricula)
    trans_texto = []
    guarda_cont = (str(cont))
    justifica_cont = guarda_cont.ljust(12)
    trans_texto.append(justifica_cont)
    justifica_nome = login.ljust(20)
    trans_texto.append(justifica_nome)
    trans_texto.append('\t')
    trans_texto.append(str(dia))
    trans_texto.append('/')
    trans_texto.append(str(mes))
    trans_texto.append('/')
    trans_texto.append(str(ano))
    trans_texto.append('\n')
    texto = controle.readlines()
    controle = open('provisorio.txt', 'w')
    controle.writelines(trans_texto)
    controle.close()


### FUNÇÃO QUE LIMPA O ARQUIVO tentativa.txt
def formata_tentativas():
    global formata1
    constroi_data = 0
    data = date.today()
    dia = data.day
    mes = data.month
    ano = data.year
    controle = open('tentativas.txt', 'r')
    texto = controle.readlines()
    ultima_data = texto[-1]
    constroi_data = ((str(dia)) + ('/') + (str(mes)) + ('/') + (str(ano)))
    procura_data = ultima_data.find(constroi_data)
    if procura_data < 0:
        controle = open('tentativas.txt', 'w')
        controle.writelines("")
        controle.close()
    else:
        pass



### FUNÇÃO PARA GERAR A PLANILHA EXCEL DE BACKUP (controle.xls) 
def sq():
    global cont                             #informa que a variável 'cont' funcionará dentro e fora das funções
    global ultima_matricula                 #informa que a variável 'ultima_matrícula' funcionará dentro e fora das funções
    data = datetime.today()                 #cria uma variável com a data de hoje (2018, 02, 15)
    dia = data.day                          #cria uma variável com apenas o dia de hoje (ex: 15)
    mes = data.month                        #cria uma variável com apenas o mês atual   (ex: 02)
    ano = data.year                         #cria uma variável com apenas o ano atual   (ex: 2018)
    controle = open('numeros.txt', 'r')     #abre o arquivo 'numeros.txt'
    texto = controle.readlines()            #lê o arquivo
    ultima_matricula = texto[-1]            #lê a última linha
    cont = int(ultima_matricula)            #atribui a variavel 'cont' o valor da variavel 'ultima_matricula' da função 'num()'
    trans_texto = []                        #armazena a ultima sequencia gerada a partir da variavel 'cont'
    for i in range(100):                    #gera 100 repetições
        cont += 1                           #acrescenta + 1 na variavel 'cont'
        print('§' * 46, end= "  ")  #-------|
        print(cont, end = "  ")     #       |imprime na tela a sequencia dos números gerados
        print('§' * 45)             #-------|
        sleep(0.1)                          #gera 1 segundo de exibição
        trans_texto.append(str(cont))       #armazena na lista 'trans_texto' o valor acrescido na variável 'cont'
        trans_texto.append('\t')            #armazena um tab de espaço
        trans_texto.append(login)           #armazena o nome do solicitante de sequencia
        trans_texto.append('\t')          #armazena dois tabs de espaço
        trans_texto.append(str(dia))        #armazena em formato string a data atual gerada na variável 'dia'
        trans_texto.append('/')             #armazena uma barra em formato string
        trans_texto.append(str(mes))        #armazena em formato string o mês atual gerado na variável 'mes'
        trans_texto.append('/')             #armazena uma barra em formato string
        trans_texto.append(str(ano))        #armazena em formato string o mês atual gerado na variável 'mes'           
        trans_texto.append('\n')            #pula uma linha
    texto = controle.readline()             #lê linha a linha do arquivo 'numeros.txt'
    controle = open('controle.ods', 'a+')   #abre o arquivo 'controle.xls' e vai para a última linha preenchida     
    controle.writelines(trans_texto)        #escreve no arquivo 'controle.xls' a ultima sequencia a partir da última linha preenchida
    controle.close()                        #fecha o arquivo 'controle.xls'
    print('\n')
    print('-' * 100)                         #imprime uma linha preenchida com 80 traços do tipo '-'                             
    print('{:^100}'.format('SEQUENCIA GERADA COM SUCESSO ...')) #imprime uma o texto centralizado em 80 espaços
    print('-' * 100)                         #imprime uma linha preenchida com 80 traços do tipo '-'


### FUNÇÃO QUE CRIA UM ARQUIVO DE BACKUP COPIANDO O ARQUIVO 'acessos.txt' PARA 'G:\Recadastro\Backup\Backup de Acessos'
def backup_de_acessos():
    data = date.today()
    dia = data.day
    mes = data.month
    ano = data.year
    acessos = open('acessos.txt', 'r')
    texto = acessos.readlines()
    ultimos_acessos = texto
    constroi_data = ((str(dia)) + ('-') + (str(mes)) + ('-') + (str(ano)))
    nome = 'G:/Gerador Seq/Backup/Backup de Acessos/Backup de Acessos ' + '(' + constroi_data + ')' + '.txt'
    backup = open(nome, 'w')
    backup.writelines(ultimos_acessos)
    backup.close()


### FUNÇÃO QUE CRIA UM ARQUIVO DE BACKUP COPIANDO O ARQUIVO 'controle.xls' PARA 'G:\Recadastro\Backup\Backup de Acessos'
def backup_de_controle():
    data = date.today()
    dia = data.day
    mes = data.month
    ano = data.year
    controle = open('controle.ods', 'r')
    texto = controle.readlines()
    ultimos_acessos = texto
    constroi_data = ((str(dia)) + ('-') + (str(mes)) + ('-') + (str(ano)))
    nome = 'G:/Gerador Seq/Backup/Backup de Controle/Backup de Controle ' + '(' + constroi_data + ')' + '.ods'
    backup = open(nome, 'w')
    backup.writelines(ultimos_acessos)
    backup.close()


### FUNÇÃO QUE IMPRIME A IMAGEM DE ABERTURA DO PROGRAMA ###
def imagem_abertura_gerenciador():
    print('=' * 100)
    print('')
    print('{:^100}'.format('G E R E N C I A D O R   D E   S E Q U Ê N C I A S'))
    print('')
    print('=' * 100)                                                     
    print('\n' * 5)                                                     
    print("{:^100}".format('       . - - -.                 . - - -.      '))
    print("{:^100}".format('      (  ????? )               ( 123... )     '))
    print("{:^100}".format('       `-´\/`-´                 \/`´``´´      '))
    print("{:^100}".format('         ____"_               |   |           '))
    print("{:^100}".format('        /"  _)))              |\_/|______,    '))
    print("{:^100}".format('       /===| _\              /::| Q  ____)    ')) 
    print("{:^100}".format('      ("___|   >   ,_       /:::|   /    ,_   '))
    print("{:^100}".format('         o  _=    / _///   /::::|_ /    / _///'))
    print("{:^100}".format('   _______| |____/ |     _|:::::| |:___/ |    '))
    print("{:^100}".format('  |  __)  \_/ /____|    |  ---- \_/  /___|    '))
    print("{:^100}".format(' _| / \    ) )         _| /  \   :  /         '))
    print("{:^100}".format('_\\/   \    /      _\\\__/    \    /          '))
    print("{:^100}".format('       /   (                  /===(           '))
    print("{:^100}".format('      / \   \                /     \          '))
    print("{:^100}".format('     /   \   \              /       \         '))
    print("{:^100}".format('     |    \   \             |        \        '))
    print("{:^100}".format('     |     \   \            |         \       '))
    print("{:^100}".format('     |      \   \           |,_________\      '))   
    print("{:^100}".format('     |       \   \           /  )  / )        '))
    print("{:^100}".format('     |,_______\___\         /  /  (  |        '))
    print("{:^100}".format('       | /   \ |            | /    \ |        '))    
    print("{:^100}".format('       |/     \|            |/      \|        '))
    print("{:^100}".format('       S__     S__          S__      S__      '))
    print("{:^100}".format('      /___\   /___\        /___\    /___\     '))
    print('\n' * 5)



### FUNÇÃO QUE IMPRIME A IMAGEM DE FUNDO QUANDO UM NOVO CADASTRO FOI REALIZADO COM SUCESSO
def imagem_figura_opcao_2():
    print("{:^100}".format(" _|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|"))
    print("{:^100}".format(" ___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__"))
    print("{:^100}".format(" _|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|"))
    print("{:^100}".format(" ___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__"))
    print("{:^100}".format(" _|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|"))
    print("{:^100}".format(" ___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__"))
    print("{:^100}".format(" _|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|"))
    print("{:^100}".format(" ___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__"))
    print("{:^100}".format(" _|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|"))
    print("{:^100}".format(" ___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__"))
    print("{:^100}".format(" _|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|"))
    print("{:^100}".format(" ___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__"))    
    print("{:^100}".format(" _|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|"))
    print("{:^100}".format(" ___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__"))
    print("{:^100}".format(" _|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|"))
    print("{:^100}".format(" ___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__"))    
    print("{:^100}".format(" _|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|"))
    print("{:^100}".format(" ___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__"))
    print("{:^100}".format(" _|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|"))
    print("{:^100}".format(" ___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__"))
    print("{:^100}".format(" _|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|"))
    print("{:^100}".format(" ___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__"))
    print("{:^100}".format(" _|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|"))
    print("{:^100}".format(" ___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__"))
    print("{:^100}".format(" _|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|"))
    print("{:^100}".format(" ___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__"))
    print("{:^100}".format(" _|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|"))
    print("{:^100}".format(" ___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__"))
    print("{:^100}".format(" _|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|"))
    print("{:^100}".format(" ___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__"))
    print("{:^100}".format(" _|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|"))
    print("{:^100}".format(" ___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__"))
    print("{:^100}".format(" _|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|"))
    print("{:^100}".format(" ___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__"))
    print("{:^100}".format(" _|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|"))
    print("{:^100}".format(" ___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__"))
    print("{:^100}".format(" _|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|"))
    print('\n')



### FUNÇÃO PARA IMPRIMIR A IMAGEM COM A SEQUENCIA SOLICITADA 
def imagem_sequencia_sim():
    global a
    a = (int(ultima_matricula)+1)
    barra_esquerda = "|"
    centraliza = (str(a)) + (' até ') + (str(cont))
    barra_direita = "|"
    print("{:^100}".format(" \\|||||/"))                                      #-------------                                     
    print("{:^100}".format(" ( O O )"))                                       #             |  
    print("{:^100}".format("|---ooO-----(_)----------|"))                     #             |
    print("{:^100}".format("|                        |"))                     #             |
    print("{:^100}".format("|       Sequência:       |"))                     #             |
    print("{:^100}".format("|                        |"))                     #             |
    print(barra_esquerda.rjust(38), end='')                                 #             |
    print(centraliza.center(24), end='')                                    #             |--------- imprime a art ASCII centralizado em 80 espaços
    print(barra_direita.ljust(38))                                          #             |
    print("{:^100}".format("|                        |"))                     #             |
    print("{:^100}".format("|                        |"))                     #             |
    print("{:^100}".format("|-------------------Ooo--|"))                     #             |
    print("{:^100}".format("          |__||__|        "))                     #             |
    print("{:^100}".format("           ||  ||         "))                     #             |
    print("{:^100}".format("          ooO  Ooo        "))                     #-------------
    print('=' * 100)         #imprime uma linha preenchida com 80 sinais de igual '=' 
    os.system('pause')
    print('\n')




### FUNÇÃO QUE IMPRIME A IMAGEM QUANDO O USUÁRIO NÃO QUISER UMA SEQUENCIA
def imagem_sequencia_nao():
    print('=' * 100)         #imprime uma linha preenchida com 80 sinais de igual '=' 
    print('\n' * 30)        #imprime 30 linhas vazias
    print('\t\t\t\t    Ok, tenha um bom dia!')    # imprime esta mensagem no com 3 espaços tabs
    print('\n')             #pula uma linha
    print('                                           (    )')                             #-------------    
    print('                                            (    )')                            #             |
    print('                                           (    )')                             #             |
    print('                                             )  )')                             #             |
    print('                                            (  (                  /\ ')         #             |
    print('                                             (_)                 /  \  /\ ')    #             |
    print('                                     ________[_]________      /\/    \/  \ ')   #             |
    print('                            /\      /\        ______    \    /   /\/\  /\/\ ')  #             |
    print('                           /  \    //_\       \    /\    \  /\/\/    \/    \ ') #             |--------- imprime a art ASCII centralizado em 80 espaços
    print('                    /\    / /\/\  //___\       \__/  \    \/')                  #             |
    print('                   /  \  /\/    \//_____\       \ |[]|     \'')                 #             |
    print('                  /\/\/\/       //_______\       \|__|      \'')                #             |
    print('                 /      \      /XXXXXXXXXX\                  \'')               #             |
    print('                         \    /_I_II  I__I_\__________________\'')              #             |          
    print('                                I_I|  I__I_____[]_|_[]_____I')                  #             |
    print('                                I_II  I__I_____[]_|_[]_____I')                  #             |
    print('                                I II__I  I     XXXXXXX     I')                  #             |
    print('                            ~~~~~"   "~~~~~~~~~~~~~~~~~~~~~~~~')                #-------------                
    print('=' * 100)         #imprime uma linha preenchida com 80 sinais de igual '=' 
    sleep(10)               #gera 10 segundos de exibição




### FUNÇÃO QUE IMPRIME A IMAGEM QUANDO O USUÁRIO ERRAR O LOGIN
def imagem_erro_login():
    print('\n' * 50)        #imprime 30 linhas vazias
    print('{:^100}'.format('.-~~-.     .-~~-.     .-~~-.'))          #-------------
    print('{:^100}'.format('(_O..O_)   (_^..^_)   (_~..~_)'))        #             |--------- imprime a art ASCII centralizado em 80 espaços
    print('{:^100}'.format('|__|       HHHH       HHHH'))            #             |
    print('{:^100}'.format('`--´       `--´       `--´'))            #------------- 
    print('\n' * 2)             #pula uma linha     
    print('{:^100}'.format('LOGIN incorreto ou não cadastrado !!!')) #imprime esta mensagem centralizada em 80 espaços
    print('')
    print('{:^100}'.format('Feche o programa e tente novamente...')) #imprime esta mensagem centralizada em 80 espaços
    print('\n')             #pula uma linha
    print('\n' * 15)        #imprime 30 linhas vazias
    sleep(10)               #gera 10 segundos de exibição




### FUNÇÃO QUE IMPRIME A IMAGEM QUANDO O USUÁRIO ERRAR A SENHA
def imagem_erro_senha():
    print('\n' * 50)        #imprime 30 linhas vazias
    print('{:^100}'.format('.-~~-.     .-~~-.     .-~~-.'))          #-------------
    print('{:^100}'.format('(_O..O_)   (_^..^_)   (_~..~_)'))        #             |--------- imprime a art ASCII centralizado em 80 espaços
    print('{:^100}'.format('|__|       HHHH       HHHH'))            #             |
    print('{:^100}'.format('`--´       `--´       `--´'))            #------------- 
    print('\n' * 2)             #pula uma linha     
    print('{:^100}'.format('SENHA incorreta ou não cadastrada !!!')) #imprime esta mensagem centralizada em 80 espaços
    print('')
    print('{:^100}'.format('Feche o programa e tente novamente...')) #imprime esta mensagem centralizada em 80 espaços
    print('\n')             #pula uma linha
    print('\n' * 15)        #imprime 30 linhas vazias
    sleep(10)               #gera 10 segundos de exibição




### FUNÇÃO QUE IMPRIME A IMAGEM QUANDO O USUÁRIO JÁ OUVER ESGOTA SUAS EMISSÕES DE SEQUÊNCIA
def imagem_acima_limite_diario():
    print("\n" * 20)
    print("              _                        )      ((   ))     (                         _ ")
    print("             (@)                      /|\      ))_((     /|\                       (@)")
    print("             |-|                     / | \    (/\|/\)   / | \                      |-|")
    print("             | |\-------------------/--|-voV---\`|´/--Vov-|--\--------------------/|-|")
    print("             |-|                         `^`   (o o)  `^`                          | |")
    print("             | |                               `\Y/'                               |-|")
    print("             |-|                                                                   | |")
    print("             |-|                                                                   | |")
    print("             | |                                                                   |-|")
    print("             | |                                                                   |-|")
    print("             |-|                                                                   | |")
    print("             | |                                                                   |-|")
    print("             |-|                                                                   | |")
    print("             | |                                                                   |-|")
    print("             | |      Você já esgotou suas emissões de sequências por hoje!!!      |-|")
    print("             | |                                                                   |-|")
    print("             | |       Se precisar, solicite uma junto ao seu Coordenador e        |-|")
    print("             | |                                                                   |-|")
    print("             | |            vá embora antes que o dragão pule o muro!              |-|")
    print("             |-|                                                                   | |")
    print("             | |                                                                   |-|")
    print("             |-|                                                                   | |")
    print("             | |                                                                   |-|")
    print("             |-|                                                                   | |")
    print("             | |                                                                   |-|")
    print("             |-|                                                                   | |")
    print("             |-|                                                                   | |")
    print("             | |                                                                   |-|")
    print("             | |                                                                   |-|")
    print("             |_| __________________________________________________________________| |")
    print("             |-|/             l   /\ /         ( (       \ /\   l                \|-|")
    print("             (@)              l /   V           \ \       V   \ l                  (@)")
    print("                              l/                _) )_          \I")
    print("                                                `\ /´")
    print("                                                  V  ")
    print("\n" * 2)
    sleep(15)







                                                      ### FUNÇÕES MÓDULO SUPERVISOR ###


### FUNÇÃO QUE RESGATA AS SENHAS E OS LOGINS GERADOS
def resgata_login_senha():
    global login_usuarios
    global senha_usuarios
    senlog = open('G:/Gerador Seq/Backup/senlog.txt', 'r')            
    recebe_texto = senlog.readlines()
    fatiador = recebe_texto
    lista_logins = []
    lista_senhas = []
    for i in fatiador:
        item = i[:30]
        login_extrai = str(i[:30].strip(' '))
        senha_extrai = str(i[30:].strip('\n'))
        lista_logins.append(login_extrai)
        lista_senhas.append(senha_extrai)
    login_usuarios = lista_logins
    senha_usuarios = lista_senhas
    senlog.close()



### FUNÇÃO QUE GUARDA NOVO LOGIN E SENHA GERADOS
def arquiva_novo_login_senha():
    global log
    global sen
    texto = []
    for i in range(len(log)):
        novo_login_senha = []
        monta_linha = (log[i].ljust(30)) + (sen[i].rjust(4)) + ('\n')
        texto.append(monta_linha)
    senlog = open('G:/Gerador Seq/Backup/senlog.txt', 'w')       
    senlog.writelines(texto)
    senlog.close()
    for i in novo_login_senha:
        print(i)



### FUNÇÃO EXCLUI LOGIN E SENHA GERADOS
def exclui_login_senha():
    global log
    global sen
    texto = ''
    for i in range(len(log)):
        novo_login_senha = []
        monta_linha = (log[i].ljust(30)) + (sen[i].rjust(4)) + ('\n')
        texto += monta_linha
    senlog = open('G:/Gerador Seq/Backup/senlog.txt', 'w')            
    senlog.write(texto)
    senlog.close()
    for i in novo_login_senha:
        print(i)




### FUNÇÃO PARA OPÇÃO 1 E QUE EMITE SEQUENCIAS NO MODO SUPERVISOR, SEM LIMITAR AS TENTATIVAS
def opcao1_modo_coordenador():
    global cont
    global tent
    tent = ''
    sequencia = str(input('\t    Olá {}, você deseja imprimir uma sequência? [S - Sim / N - Não] '.format(login))).strip().upper()[0]  #pergunte se o usuário quer imprimir uma sequência
    if sequencia in 'Ss':                                                   #se o usuário preencher com 'S' ou 's' a linha acima, faça o seguinte:
        print('-' * 100)                                                     #imprima uma linha preenchida com 80 traços do tipo '-'  
        print('{:^100}'.format('PROCESSANDO ...'))                           #imprima esta mensagem centralizada em 80 espaços
        print('-' * 100)                                                     #imprime uma linha preenchida com 80 traços do tipo '-' 
        a = cont + 1
        b = (str(a + 100))
        c = (str(cont + 200))
        tent0 = ('Gerou sequencia (' + b + " até " + c + ')')
        tent = tent0
        num()
        sq()
        registro_de_acessos()
        backup_de_controle()
        backup_de_acessos()
        imagem_figura_opcao_2()
        imagem_sequencia_sim()                                              #imprima na tela o a art ASCII contida na função 'imagem_sequencia_sim()'
    elif sequencia not in 'Ss':                                         #porém, se o usuário não confirmar com 'S' ou 's', faça o seguinte:
        tent = 'Cancelou processo'
        registro_de_acessos()
        backup_de_acessos()
        imagem_sequencia_nao()                                              #imprima na tela o a art ASCII contida na função 'imagem_sequencia_nao()'



### FUNÇÃO PARA O MODO SUPERVISOR
def modo_coordenador():
    global log
    global sen
    resgata_login_senha()
    log = login_usuarios
    sen = senha_usuarios
    while True:
        imagem_tela_inicial_supervisor()
        print('-' * 100)
        print('\n')
        opcao = str(input('\t\t\t\t         Digite sua opção: ')).strip()[0]
        print('\n')
        print('-' * 100)

        #[ 1 ] EMITIR SEQUÊNCIA# 
        if opcao == '1':
            opcao1_modo_coordenador()

        #[ 2 ] CADASTRAR USUÁRIO#
        elif opcao == '2':
            imagem_figura_opcao_2()
            global login_gerado
            global senha_gerada
            global tent
            print('-' * 100)
            print('')
            login_gerado_nome = str(input('\t\t         Digite o primeiro NOME do usuário: ')).upper()
            print('')
            imagem_constroi_cadastro_senha()
            print('')
            login_gerado_sobrenome = str(input('\t\t      Digite o primeiro SOBRENOME do usuário: ')).upper()
            print('')
            print('-' * 100)
            login_gerado = login_gerado_nome + (' ') + login_gerado_sobrenome

            gera = randint(1000,9999)
            senha_gerada = str(gera)

            if login_gerado not in log:
                log.append(login_gerado)

                if senha_gerada not in sen:
                    sen.append(senha_gerada)
                
                    imagem_login_senha_gerados()
                    arquiva_novo_login_senha()
                    tent = ("Gerou login e senha ({} - {})".format(login_gerado, senha_gerada))
                    registro_de_acessos()

                elif senha_gerada in sen:
                    imagem_senha_utilizada()
                else:
                    imagem_senha_errada()
                    print('\n')
                        
            elif login_gerado in log:
                imagem_login_utilizada()
                print('\n' * 15)
            else:
                imagem_login_errado()

        #[ 3 ] DELETAR USUÁRIO#
        elif opcao == '3':
            imagem1_opcao3()
            confirma = str(input('\t\t   Deletar permanentemente usuário e senha? [S - Sim / N - Não] ')).strip().upper()[0]
            print('\n')
            if confirma in 'Ss':
                digita_login = str(input('\t\t\t\t    LOGIN do usuário: ')).upper().strip()
                print('\n')
                if digita_login in log:
                    index_log = log.index(digita_login)
                    imagem2_opcao3()
                    imagem3_opcao3()
                    print("{:^100}".format('O login {} e a senha {} foram excluídos com sucesso!!!'.format(digita_login, sen[index_log])))
                    print('\n' * 5)
                    imagem4_opcao3()
                    del log[index_log]
                    del sen[index_log]
                    exclui_login_senha()
                    tent = ("Excluiu login e senha ({})".format(digita_login))
                    registro_de_acessos()
                    imagem_tela_inicial_supervisor()
                else:
                    imagem_login_não_cadastrado()
            else:
                imagem_login_nao_confirmou_escolha()

        #[ 4 ] EMITIR LISTA LOGIN E SENHA#
        elif opcao == '4':
            imagem_imprime_login_senha()
            tent = ("Listou logins e senhas")
            registro_de_acessos()
        

        #[ 5 ] EMITIR LISTA ACESSOS#
        elif opcao == '5':
            print('\n')
            busca_acesso = str(input('\t\t\t    Digite o LOGIN do usuário: ')).strip().upper() 
            print('\n' * 3)
            acessos = open('acessos.txt', 'r')
            recebe_acessos = acessos.readlines()
            nome_acesso = []
            for i in recebe_acessos:
                fatia_recebe_acessos = i[:20].strip()
                if fatia_recebe_acessos == busca_acesso:
                    nome_acesso.append(i)
            if nome_acesso == []:
                imagem_login_acesso_negativo()
                sleep(5)
            elif busca_acesso == nome_acesso[0][:20].strip():
                conta_acesso = 0
                print('\n' * 3)
                for i in nome_acesso:
                    conta_acesso += 1
                    print(i)
                    if conta_acesso % 20 == 0:
                        print('\n')
                        os.system('pause')
                        print('\n')
                print('\n')
                os.system('pause')
                tent = ("Listou acessos ({})".format(busca_acesso))
                registro_de_acessos()
                print('\n')
            elif busca_acesso != nome_acesso[0][:20].strip():
                imagem_login_acesso_negativo()
                print('\n')
                os.system('pause')
                print('\n')

        #[ 6 ] SAIR#
        elif opcao == '6':
            break
        else:
            imagem_opcao_invalida()

        backup_de_acessos()





### FUNÇÃO PARA IMPRIMIR UMA IMAGEM COM OS LOGINS E SENHAS EXISTENTES
def imagem_imprime_login_senha():
    print('\n' * 20)
    print("{:^100}".format('                         ```~´´´                        '))
    print("{:^100}".format('                         ( o o )                        '))
    print("{:^100}".format(' +------------------.oooO--(_)--Oooo.------------------+'))
    print("{:^100}".format('                                                        '))
    print("{:^100}".format('                                                        '))
    print("{:^100}".format('                                                        '))
    sen_log = open('G:/Gerador Seq/Backup/senlog.txt', 'r')
    recebe_senlog = sen_log.readlines()
    for i in recebe_senlog:
        print('{:^100}'.format(i))
    print("{:^100}".format('                                                        '))
    print("{:^100}".format('                      .oooO                             '))
    print("{:^100}".format('                      (   )   Oooo.                     '))
    print("{:^100}".format(' +---------------------\ (----(   )--------------------+'))
    print("{:^100}".format('                        \_)    ) /                      '))
    print("{:^100}".format('                              (_/                       '))
    print('\n' * 15)
    os.system('pause')
    print('\n' * 2)




### FUNÇÃO QUE IMPRIME A TELA INICIAL DO MODO SUPERVISOR
def imagem_tela_inicial_supervisor():
    print('=' * 100)
    print('\n' * 2)
    print('{:^100}'.format('G E R E C I A D O R   D E   S E Q U Ê N C I A S')) #imprime esta mensagem centralizada em 80 espaços
    print('\n')
    print('{:^100}'.format('(supervisor)')) #imprime esta mensagem centralizada em 80 espaços
    print('')
    print('=' * 100)
    print('\n' * 8)
    print('                           ) ) )                      ) ) )')
    print('                          ( ( (                      ( ( (')
    print('                           ) ) )                      ) ) )')
    print('                       (~~~~~~~~~)                 (~~~~~~~~~)')
    print('                        |  MÓD. |                   | POWER |')
    print('                        |       |                   |       |')
    print('                        |       |                   |       |')
    print('                        |       |                   |       |')
    print('                        |       |                   |       |')
    print('                        |       |                   |       |')
    print('                        I      _._                  I       _._')
    print('                        I    /´   `\                I     /´   `,')
    print('                        I   |   N   |               I    |   N   |')
    print('                        f   |   |~~~~~~~~~~~~~~|    f    |    |~~~~~~~~~~~~~~|')
    print('                       .´   |   ||~~~~~~~~|    |  .´     |    | |~~~~~~~~|   |')
    print('                      /´____|___||__|--|__|/___|/________|____|_|__|--|___|___\|')
    print('\n' * 2)
    print('')
    print('{:^100}'.format('  Olá Coordenador, vamos começar escolhendo uma das opções abaixo:'))
    print('')
    print('-' * 100)
    print('\n')
    print(' \t\t    [ 1 ] EMITIR SEQUÊNCIA        [ 4 ] EMITIR LISTA LOGIN E SENHA ')
    print(' \t\t    [ 2 ] CADASTRAR USUÁRIO       [ 5 ] EMITIR LISTA ACESSOS ')
    print(' \t\t    [ 3 ] DELETAR USUÁRIO         [ 6 ] SAIR ' )
    print('\n')




### FUNÇÃO QUE IMPRIME A IMAGEM QUANDO HOUVER TENTATIVA DE CADASTRO DE SENHA JÁ UTILIZADA
def imagem_senha_utilizada():
    print('\n' * 30)        #imprime 30 linhas vazias
    print('{:^100}'.format('.-~~-.     .-~~-.     .-~~-.'))          #-------------
    print('{:^100}'.format('(_O..O_)   (_^..^_)   (_~..~_)'))        #             |--------- imprime a art ASCII centralizado em 80 espaços
    print('{:^100}'.format('|__|       HHHH       HHHH'))            #             |
    print('{:^100}'.format('`--´       `--´       `--´'))            #------------- 
    print('\n')             #pula uma linha     
    print('{:^100}'.format('Senha já utilizada!!!')) #imprime esta mensagem centralizada em 80 espaços
    print('')
    print('{:^100}'.format('Tente novamente...')) #imprime esta mensagem centralizada em 80 espaços
    print('\n')             #pula uma linha
    print('\n' * 10)        #imprime 30 linhas vazias
    sleep(5)               #gera 10 segundos de exibição




### FUNÇÃO QUE IMPRIME A IMAGEM QUANDO HOUVER TENTATIVA DE CADASTRO DE LOGIN JÁ UTILIZADO
def imagem_login_utilizada():
    print('\n' * 30)        #imprime 30 linhas vazias
    print('{:^100}'.format('.-~~-.     .-~~-.     .-~~-.'))          #-------------
    print('{:^100}'.format('(_O..O_)   (_^..^_)   (_~..~_)'))        #             |--------- imprime a art ASCII centralizado em 80 espaços
    print('{:^100}'.format('|__|       HHHH       HHHH'))            #             |
    print('{:^100}'.format('`--´       `--´       `--´'))            #------------- 
    print('\n')             #pula uma linha     
    print('{:^100}'.format('Login já utilizado!!!')) #imprime esta mensagem centralizada em 80 espaços
    print('')
    print('{:^100}'.format('Tente novamente...')) #imprime esta mensagem centralizada em 80 espaços
    print('\n')             #pula uma linha
    print('\n' * 10)        #imprime 30 linhas vazias
    sleep(5)               #gera 10 segundos de exibição




### FUNÇÃO QUE IMPRIME A IMAGEM QUANDO A SENHA FOR DIGITADA INCORRETAMENTE
def imagem_senha_errada():
    print('\n' * 30)        #imprime 30 linhas vazias
    print('{:^100}'.format('.-~~-.     .-~~-.     .-~~-.'))          #-------------
    print('{:^100}'.format('(_O..O_)   (_^..^_)   (_~..~_)'))        #             |--------- imprime a art ASCII centralizado em 80 espaços
    print('{:^100}'.format('|__|       HHHH       HHHH'))            #             |
    print('{:^100}'.format('`--´       `--´       `--´'))            #------------- 
    print('\n')             #pula uma linha     
    print('{:^100}'.format('Senha incorreta, tente novamente!!!')) #imprime esta mensagem centralizada em 80 espaços
    print('\n')             #pula uma linha
    print('\n' * 10)        #imprime 30 linhas vazias
    sleep(5)               #gera 10 segundos de exibição




### FUNÇÃO QUE IMPRIME A IMAGEM QUANDO O LOGIN FOR DIGITADO INCORRETAMENTE
def imagem_login_errado():
    print('\n' * 30)        #imprime 30 linhas vazias
    print('{:^100}'.format('.-~~-.     .-~~-.     .-~~-.'))          #-------------
    print('{:^100}'.format('(_O..O_)   (_^..^_)   (_~..~_)'))        #             |--------- imprime a art ASCII centralizado em 80 espaços
    print('{:^100}'.format('|__|       HHHH       HHHH'))            #             |
    print('{:^100}'.format('`--´       `--´       `--´'))            #------------- 
    print('\n')             #pula uma linha     
    print('{:^100}'.format('Login incorreto, tente novamente!!!')) #imprime esta mensagem centralizada em 80 espaços
    print('\n')             #pula uma linha
    print('\n' * 10)        #imprime 30 linhas vazias
    sleep(5)               #gera 10 segundos de exibição




### FUNÇÃO QUE IMPRIME A IMAGEM QUANDO A OPÇÃO DIGITADA NO MODO SUPERVISOR FOR INVÁLIDA OU INEXISTENTE
def imagem_opcao_invalida():
    print('\n' * 30)        #imprime 30 linhas vazias
    print('{:^100}'.format('.-~~-.     .-~~-.     .-~~-.'))          #-------------
    print('{:^100}'.format('(_O..O_)   (_^..^_)   (_~..~_)'))        #             |--------- imprime a art ASCII centralizado em 80 espaços
    print('{:^100}'.format('|__|       HHHH       HHHH'))            #             |
    print('{:^100}'.format('`--´       `--´       `--´'))            #------------- 
    print('\n')             #pula uma linha     
    print('{:^100}'.format('Opção inválida, digite novamente!!!')) #imprime esta mensagem centralizada em 80 espaços
    print('\n')             #pula uma linha
    print('\n' * 10)        #imprime 30 linhas vazias
    sleep(5)               #gera 10 segundos de exibição




### FUNÇÃO QUE IMPRIME A IMAGEM QUANDO NÃO HOUVER ACESSOS PARA O LOGIN DIGITADO
def imagem_login_acesso_negativo():
    print('\n' * 30)        #imprime 30 linhas vazias
    print('{:^100}'.format('.-~~-.     .-~~-.     .-~~-.'))          #-------------
    print('{:^100}'.format('(_O..O_)   (_^..^_)   (_~..~_)'))        #             |--------- imprime a art ASCII centralizado em 80 espaços
    print('{:^100}'.format('|__|       HHHH       HHHH'))            #             |
    print('{:^100}'.format('`--´       `--´       `--´'))            #------------- 
    print('\n')             #pula uma linha     
    print('{:^100}'.format('Não há acessos registrados para esse login !!!')) #imprime esta mensagem centralizada em 80 espaços
    print('\n')             #pula uma linha
    print('\n' * 10)        #imprime 30 linhas vazias




### FUNÇÃO QUE IMPRIME A IMAGEM QUANDO A SENHA FOR DIGITADA INCORRETAMENTE
def imagem_login_não_cadastrado():
    print('\n' * 30)        #imprime 30 linhas vazias
    print('{:^100}'.format('.-~~-.     .-~~-.     .-~~-.'))          #-------------
    print('{:^100}'.format('(_O..O_)   (_^..^_)   (_~..~_)'))        #             |--------- imprime a art ASCII centralizado em 80 espaços
    print('{:^100}'.format('|__|       HHHH       HHHH'))            #             |
    print('{:^100}'.format('`--´       `--´       `--´'))            #------------- 
    print('\n')             #pula uma linha     
    print('{:^100}'.format('LOGIN não cadastrado!!!')) #imprime esta mensagem centralizada em 80 espaços
    print('\n')             #pula uma linha
    print('\n' * 10)        #imprime 30 linhas vazias
    sleep(5)               #gera 10 segundos de exibição



### FUNÇÃO QUE IMPRIME A IMAGEM QUANDO O USUÁRIO NÃO CONFIRMAR ESCOLHA DE OPÇÃO
def imagem_login_nao_confirmou_escolha():
    print('\n' * 30)        #imprime 30 linhas vazias
    print('{:^100}'.format('.-~~-.     .-~~-.     .-~~-.'))          #-------------
    print('{:^100}'.format('(_O..O_)   (_^..^_)   (_~..~_)'))        #             |--------- imprime a art ASCII centralizado em 80 espaços
    print('{:^100}'.format('|__|       HHHH       HHHH'))            #             |
    print('{:^100}'.format('`--´       `--´       `--´'))            #------------- 
    print('\n')             #pula uma linha     
    print('{:^100}'.format('Não confirmou escolha!!!')) #imprime esta mensagem centralizada em 80 espaços
    print('\n')             #pula uma linha
    print('\n' * 10)        #imprime 30 linhas vazias
    sleep(5)               #gera 10 segundos de exibição



### FUNÇÃO QUE IMPRIME IMAGEM TRANSITÓRIA ENTRE A DIGITAÇÃO DO NOME E O SOBRENOME EM PROCESSO DE CADASTRO
def imagem_constroi_cadastro_senha():
    print('-' * 100)
    print("{:^100}".format('                           ___'))
    print("{:^100}".format('               /======/'))
    print("{:^100}".format('                ____     //      \___       ,/'))
    print("{:^100}".format('               |  \\   //           :,   ./'))
    print("{:^100}".format('       |______|___|_//            ;:; /'))
    print("{:^100}".format('     _L_____________\o           ;;;/'))
    print("{:^100}".format('_______________________(CCCCCCCCCCCCCC)______________-/________________'))
    print("{:^100}".format(" _|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|"))
    print("{:^100}".format(" ___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__"))
    print("{:^100}".format(" _|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|"))
    print("{:^100}".format(" ___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__"))
    print('-' * 100)




### FUNÇÃO QUE IMPRIME A IMAGEM QUANDO HOUVER SUCESSO NA CRIAÇÃO DE SENHAS E LOGINS
def imagem_login_senha_gerados():
    print("{:^100}".format(" ___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__"))
    print("{:^100}".format(" _|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|"))
    print("{:^100}".format(" ___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__"))
    print("{:^100}".format(" _|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|"))
    print("{:^100}".format(" ___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__"))
    print("{:^100}".format(" _|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|"))
    print("{:^100}".format(" ___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__"))
    print("{:^100}".format(" _|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|"))
    print('')
    barra_esquerda = "|"
    centraliza1 = ('Login: {}'.format(login_gerado))
    centraliza2 =  ('Senha: {}'.format(senha_gerada))
    barra_direita = "|"
    print("{:^100}".format("  \\|||||/"))                                   
    print("{:^100}".format(" ( O O )")) 
    print("{:^100}".format("|----ooO-----(_)-----------|"))
    print("{:^100}".format("|                          |"))
    print(barra_esquerda.rjust(37), end='')
    print(centraliza1.center(26), end='')
    print(barra_direita.ljust(37))
    print("{:^100}".format("|                          |"))
    print(barra_esquerda.rjust(37), end='')
    print(centraliza2.center(26), end='')
    print(barra_direita.ljust(37))
    print("{:^100}".format("|                          |"))
    print("{:^100}".format("|---------------------Ooo--|"))
    print("{:^100}".format("         |__||__|        "))
    print("{:^100}".format("          ||  ||         "))
    print("{:^100}".format("         ooO  Ooo        "))  
    print('')
    print("{:^100}".format(" ___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__"))
    print("{:^100}".format(" _|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|"))
    print("{:^100}".format(" ___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__"))
    print("{:^100}".format(" _|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|"))
    print("{:^100}".format(" ___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__"))
    print("{:^100}".format(" _|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|"))
    print("\n")
    sleep(5)   




### FUNÇÃO QUE IMPRIME A IMAGEM QUANDO DA CONFIRMAÇÃO DE EXCLUSÃO DE LOGIN E SENHA
def imagem1_opcao3():
    print('\n' * 29)
    print('                              \|/                 \|/                  \|/     ')
    print('                             .-*-                .-*-                 .-*-     ')
    print('                            / /|\               / /|\                / /|\    ')
    print('                           _L_                 _L_                  _L_       ')
    print('                         ,"   ".             ,"   ".              ,"   ".     ')
    print('                     (\ /  O O  \ /)     (\ /  O O  \ /)      (\ /  O O  \ /) ')
    print('                      \|    _    |/       \|    _    |/        \|    _    |/  ')
    print('                        \  (_)  /           \  (_)  /            \  (_)  /    ')
    print('                        _/.___,\_           _/.___,\_            _/.___,\_    ')
    print('                       (_/     \_)         (_/     \_)          (_/     \_)   ')
    print('\n' * 3)
    print('')




### FUNÇÃO QUE IMPRIME IMAGEM TRANSITÓRIO NO PROCESSO DE EXCLUSÃO DE LOGIN E SENHA
def imagem2_opcao3():
    print("*" * 100)
    print('\n' * 40)
    print("{:^100}".format('                                \         .  ./'))
    print("{:^100}".format('                              \      .:";.:.."   /'))
    print("{:^100}".format('                                  (M^^.^~~:.´´´).'))
    print("{:^100}".format('                             -   (/  .    . . \ \)  -'))
    print("{:^100}".format('    O                          ((| :. ~ ^  :. .|))'))
    print("{:^100}".format('     |\\                       -   (\- |  \ /  |  /)  -'))
    print("{:^100}".format('  |   T                         -\  \     /  /-'))
    print("{:^100}".format('/ \[_]..........................\  \   /  /'))
    print("_" * 100)
    sleep(1)


    

### FUNÇÃO QUE IMPRIME IMAGEM TRANSITÓRIO NO PROCESSO DE EXCLUSÃO DE LOGIN E SENHA
def imagem3_opcao3():
    print('\n' * 38)
    print("{:^100}".format('                                    ..-^~~~^-..'))
    print("{:^100}".format('                                  .~            ~.'))
    print("{:^100}".format('                                   (;:               :;)'))
    print("{:^100}".format('                                  (:              :)'))
    print("{:^100}".format('                                    ´:._      _.:`'))
    print("{:^100}".format('                                    | |'))
    print("{:^100}".format('                                   (=====)'))
    print("{:^100}".format('                                   | |'))
    print("{:^100}".format('-O-                                | |'))
    print("{:^100}".format('  \                                | |'))
    print("{:^100}".format('     /\                            ((/   \))'))
    print("_" * 100)
    sleep(1)
    print('\n' * 15)




### FUNÇÃO QUE IMPRIME IMAGEM DE CONFIRMAÇÃO DE EXCLUSÃO DE LOGIN E SENHA
def imagem4_opcao3():
    print('\n' * 3)
    print("                                          ________________")
    print("                                     ____/ (  (    )   )  \___")
    print("                                    /( (  (  )   _    ))  )   )\'")
    print("                                  ((     (   )(    )  )   (   )  )")
    print("                                ((/  ( _(   )   (   _) ) (  () )  )")
    print("                               ( (  ( (_)   ((    (   )  .((_ ) .  )_")
    print("                              ( (  )    (      (  )    )   ) . ) (   )")
    print("                             (  (   (  (   ) (  _  ( _) ).  ) . ) ) ( )")
    print("                             ( (  (   ) (  )   (  ))     ) _)(   )  )  )")
    print("                            ( (  ( \ ) (    (_  ( ) ( )  )   ) )  )) ( )")
    print("                             (  (   (  (   (_ ( ) ( _    )  ) (  )  )   )")
    print("                            ( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )")
    print("                             ((  (   )(    (     _    )   _) _(_ (  (_ )")
    print("                              (_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)")
    print("                              ((__)         \\||lll|l||///          \_))")
    print("                                        (   /(/ (  )  ) )\   )")
    print("                                      (    ( ( ( | | ) ) )\   )")
    print("                                       (   /(| / ( )) ) ) )) )")
    print("                                    (      ( ((((_(|)_)))))     )")
    print("                                      (      ||\(|(|)|/||     )")
    print("                                    (        |(||(||)||||        )")
    print("                                      (     //|/l|||)|\\ \     )")
    print("                                   (/ / //  /|//||||\\  \ \  \ _)")
    print("_" * 100)
    print('\n' * 2)
    sleep(10)





                                                                ### PROGRAMA - GERENCIADOR DE SEQUÊNCIAS ###

resgata_login_senha()
tent = ''
imagem_abertura_gerenciador()
login = str(input('\t\t\t\t        LOGIN: ')).strip().upper()              #solicita o login do usuário armazenado na lista 'login_usuarios'
print('\n')
if login in login_usuarios:
    login_indice = login_usuarios.index(login)
    senha = getpass('\t\t\t\t        SENHA: ').strip()
    print('\n')
    if senha in senha_usuarios:
        senha_indice = senha_usuarios.index(senha)
        if login_indice == senha_indice and login == "BRUNO FONSECA" or login == "OSIAS ROSARIO":
            provisorio()
            modo_coordenador()
        elif login_indice == senha_indice:
            print("")                                                           #imprima um espaço
            print('\n' * 2)                                                     #imprima 3 linhas vazias
            provisorio()
            formata_tentativas()
            registro_seq_usuario()
            limite_dia_seq()
            print('-' * 100)
            if num_tentativas <= 2:
                sequencia = str(input('\t   Olá {}, você deseja imprimir uma sequência? [S - Sim / N - Não] '.format(login))).strip().upper()[0]  #pergunte se o usuário quer imprimir uma sequência
                if sequencia in 'Ss':                                                   #se o usuário preencher com 'S' ou 's' a linha acima, faça o seguinte:
                    print('-' * 100)                                                     #imprima uma linha preenchida com 80 traços do tipo '-'  
                    print('{:^100}'.format('PROCESSANDO ...'))                           #imprima esta mensagem centralizada em 80 espaços
                    print('-' * 100)                                                     #imprime uma linha preenchida com 80 traços do tipo '-' 
                    a = cont + 1
                    b = (str(a + 100))
                    c = (str(cont + 200))
                    tent0 = ('Gerou sequencia (' + b + " até " + c + ')')
                    tent = tent0
                    num()
                    sq()
                    registro_de_acessos()
                    backup_de_acessos()
                    backup_de_controle()
                    imagem_figura_opcao_2()
                    imagem_sequencia_sim()
                elif sequencia not in 'Ss':                                         #porém, se o usuário não confirmar com 'S' ou 's', faça o seguinte:
                    tent = 'Cancelou processo'
                    registro_de_acessos()
                    backup_de_acessos()
                    imagem_sequencia_nao()                                              #imprima na tela o a art ASCII contida na função 'imagem_sequencia_nao()'
            elif num_tentativas > 2:
                tent = 'Excedeu tentativas diárias'
                registro_de_acessos()
                backup_de_acessos()
                imagem_acima_limite_diario()
        elif login_indice != senha_indice:
            tent = 'Senha incorreta ou não cadastrada'
            registro_de_acessos()
            backup_de_acessos()
            imagem_erro_senha()
    elif senha not in senha_usuarios:
        tent = 'Senha incorreta ou não cadastrada'
        registro_de_acessos()
        backup_de_acessos()
        imagem_erro_senha()
elif login not in login_usuarios:
    tent = 'Login errado ou não cadastrado'
    registro_de_acessos()
    backup_de_acessos()
    imagem_erro_login()

backup_de_controle()
backup_de_acessos()




