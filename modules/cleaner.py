import os

def cleaner():
    # Detecta o sistema operacional e executa o comando de limpeza apropriado
    if os.name == 'posix':   # Sistemas Unix/Linux/Mac
        os.system('clear')
    elif os.name == 'nt':    # Sistema Windows
        os.system('cls')