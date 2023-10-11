menu = "s"
turma = []
nota = 0

while menu == "s":
    print("\n========================================")
    print("    1. Cadrastrar novo aluno \n    2. incluir notas \n    3. Gerar Relatorio de Desempenho ")
    print("    4. Consultar Informações \n    5. Sair")
    print("========================================\n")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        print("\n===========Tela de Cadrastro============\n           Maximo 15 alunos             ")

        NumAlunos = int(input("  Quantos alunos deseja cadrastrar:  "))
        if NumAlunos < 16:
            print("\n========================================")
            for aluno in range (0, NumAlunos):

                turma.append({ 
                "nome":"",
                "idade": 0,
                "matricula": 0,
                "turma":"BH42",
                "nota_algor": [[0],[0],[0],[0],[0]],
                "nota_segura": [[0],[0],[0],[0],[0]],
                "nota_dev": [[0],[0],[0],[0],[0]]})
                turma[aluno]["nome"] = (str(input("Nome do Aluno: ")))
                turma[aluno]["idade"] = (int(input("Idade do Aluno: ")))
                turma[aluno]["matricula"] = (int(input("Matricula do Aluno: ")))
                print("========================================")      
        menu = str(input(" Deseja voltar ao menu?(s/n): "))
        
    elif opcao == 2:
        print("\n============== Matérias ================")
        print("    1. Algoritimo \n    2. Segurança \n    3. Desenv. web      \n    4. Voltar ao Menu")
        print("========================================\n")
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            print("\n===========Inclusao de Notas============")
            matricula = int(input("Matricula do aluno:"))
            for aluno in turma:
                if aluno["matricula"] == matricula:
                    print("\n============= Algoritimos ==============")
                    
                    print("          Notas do(a)", aluno["nome"],"\n")
                    for cont in range(0, 5):
                        mensagem = "Informe a " + str(cont + 1) + " nota: "
                        nota= float(input(mensagem))
                        while nota < 0 or nota > 10:
                            print("Insira uma nota valida")
                            nota= float(input(mensagem))
                        aluno["nota_algor"][cont] = nota
                elif aluno ["matricula"] != matricula : 
                    print ("Aluno não encontrado")
                    
        elif opcao == 2:
            print("\n===========Inclusao de Notas============")
            matricula = int(input("Matricula do aluno: "))
            for aluno in turma:
                if aluno["matricula"] == matricula:
                    print("\n============= Segurança ==============")
                    print("          Notas do(a)", aluno["nome"],"\n")
                    for cont in range(0, 5):
                        mensagem = "Informe a " + str(cont + 1) + " nota: "
                        nota= float(input(mensagem))
                        while nota < 0 or nota > 10:
                            print("Insira uma nota valida")
                            nota = float(input(mensagem))
                        aluno["nota_segura"][cont] = nota                     
                elif aluno ["matricula"] != matricula: 
                    print ("Aluno não encontrado")

        elif opcao == 3:
            print("\n===========Inclusao de Notas============")
            matricula = int(input("Matricula do aluno: "))
            for aluno in turma:
                if aluno["matricula"] == matricula:
                    print("\n============= Desenv. Web ==============")
                    print("          Notas do(a)", aluno["nome"],"\n")
                    for cont in range(0, 5):
                        mensagem = "Informe a " + str(cont + 1) + " nota: "
                        nota= float(input(mensagem))
                        while nota < 0 or nota > 10:
                            print("Insira uma nota valida")
                            nota= float(input(mensagem))
                        aluno["nota_dev"][cont] = nota                       
                elif aluno ["matricula"] != matricula: 
                    print ("Aluno não encontrado")
        elif opcao == 4:
            menu = "s"
        
    elif opcao == 3:
        print("\n=========== Desempenho ============")
        matricula = int(input("Matricula do aluno:"))
        for aluno in turma:
                if aluno["matricula"] == matricula:
                    media = 0.0
                    for notas in aluno["nota_algor"]:                                                
                        media += notas
                    media /= 5
                    print ( "Media em Algoritimo é:", media)

                    media = 0.0
                    for notas in aluno["nota_segura"]:                                                
                        media += notas
                    media /= 5
                    print ( "Media em Algoritimo é:", media)

                    media = 0.0
                    for notas in aluno["nota_dev"]:
                        media += notas
                    media /= 5
                    print ( "Media em Desenv. Web é:", media)

                elif aluno ["matricula"] != matricula : 
                    print ("Aluno não encontrado")
        print("\n========================================")
        menu = str(input("Deseja voltar ao menu?(s/n): "))
    elif opcao == 4:
        print("\n========================================")
        matricula = int(input("Matricula do aluno:"))
        for aluno in turma:
                if aluno["matricula"] == matricula:
                    print("Nome: ", aluno ["nome"])
                    print("Idade: ", aluno ["idade"])
                    print("Turma: ", aluno ["turma"])
                    print("Algoritimo: ", aluno ["nota_algor"])
                    print("Segurança: ", aluno ["nota_segura"])
                    print("Desenv. Web: ", aluno ["nota_dev"])
        print("\n========================================")
        menu = str(input("Deseja voltar ao menu?(s/n): "))
    elif opcao == 5:
        menu ="n"
        print("\n================\ FIM /=================")