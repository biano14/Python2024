import os
import platform

# print(f'Sistema Operacional: {os.name}.')
print(f'Sistema Operacional: {platform.system()} {platform.release()}')
print(f'Nome do usuário: {os.environ.get('USERNAME')}.')