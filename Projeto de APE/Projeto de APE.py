#Funções# 
def repeatcpf(cpf):
    cadastro = open('cadastro.txt', 'r')
    linhas = cadastro.readlines()
    for linha in linhas:
        aux = linha.split(';')
        if cpf == aux[1]:
            while True:
                print('Já existe, redigite')
                novocpf = int(input('Digite seu CPF:\n'))
                novocpf = str(novocpf)
                if novocpf != aux[1]:
                    cpf = novocpf
                    break
    return cpf
    print('|CPF valido|'+'\n')
    cadastro.close()
def busca(cpf):
    cadastro = open('cadastro.txt', 'r')
    linhas = cadastro.readlines()
    for linha in linhas:
        aux = linha.split(';')
        if cpf == aux[1]:
            print('Nome: '+aux[0]+'\n'+'CPF: '+aux[1]+'\n'+'E-mail: '+aux[2])
        if cpf != aux[1]:
            print('|O CPF não existe|'+'\n')
    cadastro.close()
def repeatemail(opcaoemail):
    cadastro = open('cadastro.txt', 'r+')
    linhas = cadastro.readlines()
    for linha in linhas:
        aux = linha.split(';')
        if opcaoemail+'\n' == aux[2]:
            while True:
                print('Já existe esse Email, escolha outra opção')
                opcao =int(input('Escolha a opção 1 ou 2 ou 3:\n'))
                if opcao == 1:
                    novoopcaoemail = cpf+email
                elif opcao == 2:
                    novoopcaoemail = listanome[0]+'.'+listanome[-1]+email
                elif opcao == 3:
                    novoopcaoemail = listanome[0]+cpf[0]+cpf[1]+cpf[2]+email
                else:
                    print('Você não escolheu nenhuma das opções')
                if novoopcaoemail+'\n' != aux[2]:
                    opcaoemail = novoopcaoemail
                    break
    return opcaoemail
    print('|Email valido|'+'\n')
    cadastro.close()
#######################################################################################

#Menu#
while True:
    escolha = int(input('''Escolha\n
    Pesquisar Usuário - [1]\n
    Cadastrar Usuário - [2]\n
    Alterar Usuário - [3]\n
    Excluir Usuário - [4]\n
    Listar Usuários - [5]\n
    Sair - [0]\n'''))
#######################################################################################

 #Sair#   
    if escolha == 0:
        break
#######################################################################################
    
#Busca
    if escolha == 1:
        cpf = input('Insira o CPF a ser buscado: ')
        cadastro = open('cadastro.txt','r')
        contem = False
        linhas = cadastro.readlines()
        for linha in linhas:
            aux = linha.split(';')
            if cpf == aux[1]:
                contem = True
                print('-'*50)
                print('Nome: '+aux[0]+'\n'+'CPF: '+aux[1]+'\n'+'E-mail: '+aux[2])
                print('-'*50+'\n')
        if contem == False:
            print('|O CPF não existe|'+'\n')
        cadastro.close()
#######################################################################################
       
#Processo de cadastro #
    if escolha == 2:
        email = '@ifnet.com.br'
        print('Vamos cadastrar seu email')
        while True:
            #Coleta de informações #
            cadastro = open('cadastro.txt', 'a+')
            nome = input('Digite seu nome inteiro(Enter p/ encerrar):\n')
            if nome == '':
                break
            nome = nome.lower()
            listanome = nome.split(' ')
            cpf = int(input('Digite seu CPF:\n'))
            cpf = str(cpf)
            #Procura por repetições de CPF#
            cpf = repeatcpf(cpf)
            #Escolha do e-mail#
            print('''Escolha a opção de email:\n
            1 = CPF@ifnet.com.br\n
            2 = PrimeiroNome.UltimoNome@ifnet.com.br\n
            3 = PrimeiroNome+3PrimeirosDigitosDoCPF@ifnet.com.br''')
            while True:
                opcao =int(input('Escolha a opção 1 ou 2 ou 3:\n'))
                if opcao == 1:
                    opcaoemail = cpf+email
                    break
                elif opcao == 2:
                    opcaoemail = listanome[0]+'.'+listanome[-1]+email
                    break
                elif opcao == 3:
                    opcaoemail = listanome[0]+cpf[0]+cpf[1]+cpf[2]+email
                    break
                else:
                    print('você não escolheu nenhuma das opções')
            opcaoemail = repeatemail(opcaoemail)
            cadastro.write(nome+';'+cpf+';'+opcaoemail+'\n')
            print('|Cadastro feito com sucesso|'+'\n')
            cadastro.close()
            break
#######################################################################################
          
#Alterar usuário#
        
    if escolha == 3:
        cpf= input('Digite o CPF a ser alterado: ')
        cadastro = open('cadastro.txt', 'r+')
        linhas = cadastro.readlines()
        j = len(linhas)
        s=0
        for k in range(j):
            ls=linhas[k]
            li=ls.split(';')
            if cpf == li[1]:
                s+=1
                alt = input('Insira o novo Usuário: ')
                del(li[0])
                li.insert(0, alt)
                lk=li[0]+';'
                lk+=li[1]+';'
                lk+=li[2]
                linhas.insert(k, lk)
                del(linhas[k+1])
                print('|Cadastro Alterado com Sucesso|'+'\n')
                break
        lin=''
        for k in range(j):
            lin+=linhas[k]
            cadastro = open('cadastro.txt', 'w')
            cadastro.write(lin)
        if s==0:
            
           print('|CPF não existe|'+'\n')
        cadastro.close()        
######################################################################################

#Excluir Usuário

    if escolha == 4:
        cpf= input('Digite o CPF a ser Excluído: ')
        cadastro = open('cadastro.txt', 'r+')
        linhas = cadastro.readlines()
        j = len(linhas)
        contem=False
        lin=''
        for k in range(j):
            ls=linhas[k]
            li=ls.split(';')
            if cpf == li[1]:
                contem=True
                print('-'*50)
                print(k+1,'- '+'Nome: '+li[0]+'\n'+'    CPF: '+li[1]+'\n'+'    E-mail: '+li[2])
                print('-'*50+'\n')
                r=input('Deseja Excluir? S/N:')
                if r=='S' or r=='s':
                    del(linhas[k])
                    print('|Cadastro Deletado com sucesso|'+'\n')
                    for q in range(j-1):
                        lin+=linhas[q]
                        cadastro = open('cadastro.txt', 'w')
                        cadastro.write(lin)
                    break
                if r=='N' or r=='n':
                    break            
        if contem==False:
           print('|CPF não existe|'+'\n')
        cadastro.close()
######################################################################################


#Listar Usuários


    if escolha==5:
            cadastro = open('cadastro.txt', 'r+')
            linhas = cadastro.readlines()
            j = len(linhas)
            for k in range(j):
                linha = linhas[k]
                y=len(linha)
                aux = linha.split(';')
                print('-'*50)
                print(k+1,'- '+'Nome: '+aux[0]+'\n'+'    CPF: '+aux[1]+'\n'+'    E-mail: '+aux[2])
                print('-'*50+'\n')
            




            
######################################################################################

