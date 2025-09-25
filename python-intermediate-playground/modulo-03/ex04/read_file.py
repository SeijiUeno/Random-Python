import sys
import os

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Usage - python3 read_file.py ")
        sys.exit()
    file_name = sys.argv[1]
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    except IsADirectoryError:
        print("Erro: O argumento enviado é um diretório.")
    except Exception as e:
        print(f"Erro inesperado: {type(e).__name__}")
