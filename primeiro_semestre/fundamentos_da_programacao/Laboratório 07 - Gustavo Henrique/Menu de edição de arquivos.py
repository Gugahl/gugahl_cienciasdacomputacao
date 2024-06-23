import os

while True:
    print("""\n      ===MENU===
  1. Criar Arquivo
  2. Editar Arquivo
  3. Ler Arquivo
  4. Limpar Arquivo
  5. Criar Cópia de Arquivo
  6. Sair""")

    escolha = input("Escolha uma opção: ")

    if not escolha.isdigit():
        print("Opção inválida. Por favor, insira um número entre 1 e 6.")
        continue
    
    escolha = int(escolha)
    
    if escolha < 1 or escolha > 6:
        print("Opção inválida. Por favor, escolha um número entre 1 e 6.")
        continue

    if escolha == 1:
        nome = input("Diga o nome do arquivo a ser criado: ")
        if os.path.exists(nome):
            print(f"O arquivo '{nome}' já existe.")
        else:
            arquivo = open(nome, 'w')
            arquivo.close()
            print(f"Arquivo '{nome}' criado com sucesso.")
    
    elif escolha == 2:
        nome = input("Diga o nome do arquivo a ser editado: ")
        if os.path.exists(nome):
            conteudo = input("Digite o conteúdo que deseja adicionar ao arquivo: ")
            arquivo = open(nome, 'a')
            arquivo.write(conteudo + '\n')
            arquivo.close()
            print(f"Arquivo '{nome}' editado com sucesso.")
        else:
            print(f"O arquivo '{nome}' não existe.")
    
    elif escolha == 3:
        nome = input("Digite o nome do arquivo a ser lido: ")
        if os.path.exists(nome):
            arquivo = open(nome, 'r')
            conteudo = arquivo.read()
            arquivo.close()
            print(f"O conteúdo do arquivo '{nome}' é:")
            print(conteudo)
        else:
            print(f"O arquivo '{nome}' não existe.")
    
    elif escolha == 4:
        nome = input("Diga o nome do arquivo a ser limpo: ")
        if os.path.exists(nome):
            arquivo = open(nome, 'w')
            arquivo.close()
            print(f"Arquivo '{nome}' limpo com sucesso.")
        else:
            print(f"O arquivo '{nome}' não existe.")
    
    elif escolha == 5:
        origem = input("Diga o nome do arquivo fonte: ")
        if os.path.exists(origem):
            destino = input("Digite o nome do novo arquivo: ")
            arquivo_origem = open(origem, 'r')
            conteudo = arquivo_origem.readlines()
            arquivo_origem.close()
            arquivo_destino = open(destino, 'w')
            arquivo_destino.writelines(conteudo)
            arquivo_destino.close()
            print(f"Cópia do arquivo '{origem}' criada com sucesso como '{destino}'.")
        else:
            print(f"O arquivo '{origem}' não existe.")
    
    elif escolha == 6:
        print("Saindo do programa...")
        break
