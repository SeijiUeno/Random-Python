import sys
import os

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Usage - python3 read_file.py ")
        sys.exit()
    file_name = sys.argv[1]
    try:
        if not os.path.exists(file_name):
            print("Erro: Arquivo não encontrado.")
            sys.exit()
        if os.path.isdir(file_name):
            print("Erro: O argumento enviado é um diretório.")
            sys.exit()
        with open(file_name, "r", encoding="utf-8") as f:
            print(f.read())
    except PermissionError:
        print("Erro inesperado: PermissionError")
    except UnicodeDecodeError:
        print("Erro inesperado: UnicodeDecodeError")
    except Exception as e:
        print(f"Erro inesperado: {type(e).__name__}")
