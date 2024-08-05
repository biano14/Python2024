import pandas as pd

# Caminho absoluto para o arquivo CSV
file_path = 'C:/Users/Aluno Manhã/Pasta para importar repositorio/python2024/Programas Test/Dataset/avengers.csv'

# PARA ESSE CODIGO SEMPRE VAI SER NECESSARIO DEFINIR O FILE_PATCH
# Detectar o codificador
def detect_encoding(file_path):
    import chardet
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
        return result['encoding']

# Ler o arquivo CSV usando o codificador detectado
encoding = detect_encoding(file_path)
try:
    data = pd.read_csv(file_path, encoding=encoding)
except FileNotFoundError:
    print(f"Arquivo não encontrado: {file_path}")
    exit()
except pd.errors.ParserError as e:
    print(f"Erro ao ler o arquivo CSV: {e}")
    exit()

# Verificar se a coluna 'Name/Alias' existe e definir como índice
if 'Name/Alias' in data.columns:
    data.set_index('Name/Alias', inplace=True)
else:
    print("Coluna 'Name/Alias' não encontrada.")
    exit()

# Exibir os 25 primeiros dados
print("Os 25 primeiros dados do dataset com 'Name/Alias' como índice:")
print(data.head(25))
