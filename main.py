from primeiraQuestao import *
from segundaQuestao import *

from data import *

def main():
    opcao = int(input("Selecione a questão que deseja testar(1 ou 2): "))

    if opcao == 1:
        print("[1] validar nome")
        print("[2] validar email")
        print("[3] validar senha")
        print("[4] validar cpf")
        print("[5] validar telefone")
        print("[6] validar timestamp")
        print("[7] validar numero")
        opcao = int(input("Selecione a opção que deseja testar: "))

        if opcao == 1:
            testarNomes(nomes)
        elif opcao == 2:
            testarEmails(emails)
        elif opcao == 3:
            testarSenhas(senhas)
        elif opcao == 4:
            testarCPFs(cpfs)
        elif opcao == 5:
            testarTelefones(telefones)
        elif opcao == 6:
            testarTimestamps(timestamps)
        elif opcao == 7:
            testarNumeros(numeros)
        else:
            print("Opção inválida")
        
    elif opcao == 2:
        print("[1] validar padrão a")
        print("[2] validar padrão b")
        print("[3] validar padrão c")
        print("[4] validar padrão d")
        print("[5] validar padrão e")
        print("[6] validar padrão f")
        print("[7] validar padrão g")
        opcao = int(input("Selecione a opção que deseja testar: "))

        if opcao == 1:
            testar_familias(padroes['a'], familiasA)
        elif opcao == 2:
            testar_familias(padroes['b'], familiasB)
        elif opcao == 3:
            testar_familias(padroes['c'], familiasC)
        elif opcao == 4:
            testar_familias(padroes['d'], familiasD)
        elif opcao == 5:
            testar_familias(padroes['e'], familiasE)
        elif opcao == 6:
            testar_familias(padroes['f'], familiasF)
        elif opcao == 7:
            min = int(input("Digite o valor para x: "))
            max = int(input("Digite o valor para y: "))

            min, max = verificaxy(min, max)
            
            testar_familias(padraoG(min,max), familiasG)
        else:
            print("Opção inválida")

    else:
        print("Opção inválida")

while True:
    main()
    if input("Deseja testar novamente? (s/n): ") == "n":
        break
