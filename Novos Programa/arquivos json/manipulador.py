# importa biblioteca
import json

# classe ArquivoJson
class Manipulador:
    def criar_arquivo(self,nome_arquvivo):
        try:
          usuarios = [
              {
                  'Código': 0,
                  'Nome': 'Admin',
                  'CPF': '000.000.000-00',
                  'E-mail': 'admin@admin.com',
                  'Profissão': 'Adinistrador'
              }
          ]  
          # serializando objeto python com o json
          json_dados = json.dumps(usuarios)
          with open(f'{nome_arquvivo}.json','w',encoding='utf-8') as f:
              f.write(json_dados)
        except Exception as e:
            return f'Não é possível criar o arquivo. {e}.'
        
        
    def __del__(self):
        return 'Manipulador destruido' 