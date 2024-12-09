import os

def listar_arquivos_e_diretorios(caminho, nivel=0):
    """
    Percorre um diretório especificado e lista todos os arquivos e subdiretórios.

    Args:
        caminho (str): O caminho do diretório a ser explorado.
        nivel (int): Nível de profundidade (usado para identação visual).
    """
    try:
        itens = os.listdir(caminho)  
        for item in itens:
            caminho_completo = os.path.join(caminho, item)
            if os.path.isdir(caminho_completo):  
                print("  " * nivel + f"[D] {item}/")
                listar_arquivos_e_diretorios(caminho_completo, nivel + 1)  
            else:
                print("  " * nivel + f"[A] {item}")
    except PermissionError:
        print("  " * nivel + f"[!] Sem permissão para acessar {caminho}")
    except FileNotFoundError:
        print("  " * nivel + f"[!] Caminho não encontrado: {caminho}")

# Exemplo de uso
diretorio_inicial = input("Digite o caminho do diretório a ser explorado: ")
listar_arquivos_e_diretorios(diretorio_inicial)