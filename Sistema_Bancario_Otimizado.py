# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 15:52:56 2023

@author: bruno


"""

usuarios_cadastrados={}
n_conta=0
relacao_contas={}
LIMITE = 500
extrato = ''
LIMITE_SAQUES = 3



menu1 = '''

###### ###### ###### Menu inicial ###### ###### ###### ######
                Selecione a opção desejada

                [m] acessar seu menu para operação bancária
                [u] criar usuário
                [c] criar conta corrente
                [q] sair


=>'''

menu2 = '''

###### ###### ###### Operação bancária ###### ###### ###### 
                Selecione a opção desejada

                [d] depositar
                [s] sacar
                [e] extrato
                [q] retornar ao menu inicial


                =>'''



while True:
    opcao = input(menu1)
    
    if opcao == 'm':
        print("####### Acessar conta ##########")
        n_cpf=input("Informe seu CPF:")
        if n_cpf not in usuarios_cadastrados:
            print("CPF não vinculado a usuário cadastrado")
            continue
        else:
            conta_corrente=int(input("Informe seu número da conta:"))
            if conta_corrente in usuarios_cadastrados[n_cpf]["contas_corrente"]:
                saldo=sum(relacao_contas[conta_corrente]["movimentacoes"])
                
                def deposito(valor_deposito):
                    global saldo
                    global relacao_contas
                    saldo += valor_deposito
                    relacao_contas[conta_corrente]["movimentacoes"].append(valor_deposito)    
                    return saldo, relacao_contas
                    
                    
                def saque(*,valor_saque):
                    global saldo
                    global relacao_contas
                    saldo -= valor_saque
                    relacao_contas[conta_corrente]["movimentacoes"].append(-valor_saque)
                    relacao_contas[conta_corrente]["n_saques"] += 1
                
                        
                    return(saldo, relacao_contas)     


                while True:
                    opcao = input(menu2)
                        
                        
                    if opcao == 'd':
                        print("####### Depósito ##########")
                        valor_deposito=int(input("Qual o valor de depósito? \n  =>R$"))
                        print ("Por favor, insira as células na máquina \n ...")
                        print ("Estaremos realizando a contagem das células. Seu novo saldo pode ser consultado no menu inicial. \n .........................................................") 
                                
                        deposito(valor_deposito)
                        
                      
                        
                    elif opcao == 's':
                        print("####### Saque #######")
                        
                        if relacao_contas[conta_corrente]["n_saques"] >= LIMITE_SAQUES:                        
                            print("Não foi possível completar a operação. Número máximo de saques atingido.")
                            continue
                        else:
                            valor_saque=int(input("Qual o valor de saque? \n  =>R$"))
                            if valor_saque > saldo:
                                print("Não foi possível completar a operação. Saldo insuficiente.")
                                continue
                            elif valor_saque > LIMITE:
                                print("Não foi possível completar a operação. Limite máximo de R$500,00 por saque.")
                                continue
                            else:
                                saque(valor_saque=valor_saque)
                                print ("Por favor, retire as células da máquina \n ...")
                               
                    
                    elif opcao == 'e':
                        print("####### Extrato #######")
                    
                        if saldo == 0 and bool(relacao_contas[conta_corrente]["movimentacoes"]) is False:
                            print ("Não foram realizadas movimentações")
                            continue
                        else:
                            for item in relacao_contas[conta_corrente]["movimentacoes"]: 
                                movimentacao=  "Saque de       " if item<0 else "Depósito de     "
                                print (f"{movimentacao} R${item:.2f}")
                            print (".............................")
                            print (f"Seu Saldo atual é de => R${saldo:.2f}")
                            
                        
                            
                    elif opcao == 'q':
                        break
                        
                    else:
                        print("Operação inválida, por favor selecione a opção desejada novamente")
                  

            else:
                print("Conta corrente não encontrada")
                continue
        
    
    elif opcao == 'u':
        print("####### Criar usuário ##########")
        n_cpf=input("Informe seu CPF:")
        if n_cpf in usuarios_cadastrados:
            print("CPF já cadastrado")
            continue
        else:
            def criar_usuario(n_cpf,n_nome,n_data,n_rua,n_numero,n_cidade,n_estado):
                global usuarios_cadastrados
                usuarios_cadastrados[n_cpf]={"nome":n_nome,"data_de_nascimento":n_data,"endereço":{"rua":n_rua,"n":n_numero,"cidade":n_cidade,"estado":n_estado}}
                return usuarios_cadastrados, print (" ### usuário cadastrado ###")
            
            
            n_nome=input("Informe seu nome completo:")
            n_data=input("Informe sua data de nascimento (xx/xx/19xx):")
            n_rua=input("Informe seu logradouro:")
            n_numero=input("Informe o número:")
            n_cidade=input("Informe sua cidade:")
            n_estado=input("Infome a sigla do seu estado:")
            
            
            criar_usuario(n_cpf,n_nome,n_data,n_rua,n_numero,n_cidade,n_estado)
            
            usuarios_cadastrados[n_cpf].setdefault('contas_corrente',[])
            
            
    elif opcao == 'c':
        print("####### Criar conta corrente ##########")
        cpf= input("Informe seu CPF:")
        if cpf in usuarios_cadastrados:
            n_conta += 1
            print(f" Sua nova conta corrente é => {n_conta} - Ag.0001")
            
            #associa o cpf no dicionário a uma conta corrente
            usuarios_cadastrados[cpf]["contas_corrente"].append(n_conta)
            
            #cria a conta corrente no banco de dados do histórico
            relacao_contas[n_conta]={"movimentacoes":[],"n_saques":0}
            #relacao_contas[n_conta]["n_saques"]
            
            
            
        else:
            print("Necessário cadastro de um usuário")
            continue
        
        
    elif opcao == 'q':
        break
    else:
        print("Operação inválida, por favor selecione a opção desejada novamente")
         

            
        
        
    

