import zipfile
import os

zip_path = 'data/chest-xray-pneumonia.zip'
extract_path = 'data/'

# Extração
if os.path.exists(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    print(f'Arquivo {zip_path} extraído com sucesso em {extract_path}')

    os.remove(zip_path)
    print('Arquivo zip removido após extração.')
else:
    print(f'ERRO: Arquivo {zip_path} não encontrado.')

# Verificação da estrutura de diretórios
print('Estrutura de diretórios após extração:')
for root, dirs, files in os.walk(extract_path):
    level = root.replace(extract_path, '').count(os.sep)
    indent = ' ' * 4 * (level)
    print(f'{indent}{os.path.basename(root)}/')
    subindent = ' ' * 4 * (level + 1)
    for f in files[:2]:
        print(f'{subindent}{f}')
    if len(files) > 2:
        print(f'{subindent}...')
    break