import pandas as pd
from IPython.display import display
import chardet

# Caminho absoluto para o arquivo CSV
file_path = r'C:\Users\Aluno Manhã\Desktop\biano14\python2024\Programas Test\Dataset\avengers.csv'

# Detectar o codificador
def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
        return result['encoding']

# Detectar a codificação
encoding = detect_encoding(file_path)
print(f"Codificação detectada: {encoding}")

# Tentar ler o arquivo CSV usando a codificação detectada
try:
    tabela = pd.read_csv(file_path, encoding=encoding)
    print(tabela.head(60))
except:
    print(f"Erro de decodificação com a codificação detectada ({encoding}): {e}")
    # Tentar com codificações alternativas
    alternative_encodings = ['ISO-8859-1', 'cp1252']
    for enc in alternative_encodings:
        try:
            tabela = pd.read_csv(file_path, encoding=enc)
            print(f"Arquivo lido com sucesso usando a codificação: {enc}")
            display(tabela)
            break
        except:
            print(f"Falha ao ler com a codificação: {enc}")
