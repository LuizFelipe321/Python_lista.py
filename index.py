import os

def limpar_tela():
    """Limpa a tela do terminal."""
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS e Linux
        os.system('clear')

# Definindo a lista de contatos
contatos = []

def listar_contatos(contatos): 
    """Lista todos os contatos. Se a lista estiver vazia, informa que não há contatos."""
    if not contatos:
        print("Nenhum contato encontrado.")
    else:
        print("Lista de contatos:")
        for i, contato in enumerate(contatos):
            print(f"{i + 1}. Nome: {contato['nome']}, Telefone: {contato['telefone']}")

def atualizar_contatos(indice, novo_nome, novo_telefone):
    """Atualiza o contato no índice especificado com o novo nome e telefone."""
    contatos[indice] = {"nome": novo_nome, "telefone": novo_telefone}

def excluir_contato(indice):
    """Exclui o contato no índice especificado, se for válido."""
    if 0 <= indice < len(contatos):
        contatos.pop(indice)
        print("Contato excluído com sucesso.")
    else:
        print("Índice inválido.")

# Simulação do menu
while True:
    limpar_tela()  # Limpa a tela a cada iteração do menu
    print("\nMenu:")
    print("1. Adicionar contato")
    print("2. Atualizar contato")
    print("3. Listar contatos")
    print("4. Excluir contato")
    print("5. Sair")
    
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        # Adiciona um novo contato
        nome = input("Digite o nome: ")
        telefone = input("Digite o telefone: ")
        contatos.append({"nome": nome, "telefone": telefone})
    elif escolha == "2":
        # Lista os contatos e solicita o índice do contato a ser atualizado
        listar_contatos(contatos)
        indice = int(input("Digite o número do contato que deseja atualizar: ")) - 1
        if 0 <= indice < len(contatos):
            novo_nome = input("Digite o novo nome: ")
            novo_telefone = input("Digite o novo telefone: ")
            atualizar_contatos(indice, novo_nome, novo_telefone)
            print("Contato atualizado com sucesso!")
        else:
            print("Índice inválido.")
    elif escolha == "3":
        # Lista todos os contatos
        listar_contatos(contatos)
        input("Pressione Enter para continuar...")  # Aguarda o usuário para continuar

    elif escolha == "4":
     # Excluir contato
        limpar_tela()  # Limpa a tela
        listar_contatos(contatos)
        indice = int(input("Digite o indice do contato que deseja excluir: ")) - 1
        if 0 <= indice < len(contatos):
            excluir_contato(indice)
        else:
            print("Índice inválido.")
    elif escolha == "5":
        # Encerra o programa
        print("Saindo do programa. Até logo!")
        break
    else:
        # Mensagem de erro para opções inválidas
        print("Opção inválida. Tente novamente.")