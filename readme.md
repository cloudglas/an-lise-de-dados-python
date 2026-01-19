# Navegar para pasta do projeto
cd ~/python_ibm

# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate

deactivate

# Execute o dashboard
streamlit run nypd_dashboard.py

# Ou para rodar em uma porta específica
streamlit run nypd_dashboard.py --server.port 8501

# Instalar bibliotecas
pip install pandas
pip install matplotlib  # opcional




# Listar arquivos
ls
ls -la
ls *.csv

# Ver tamanho de arquivo
ls -lh nypd.csv

# Contar linhas de CSV
wc -l nypd.csv

# Ver primeiras linhas
head -n 5 nypd.csv
head -n 1 nypd.csv | tr ',' '\n' | nl


import pandas as pd
import os

# Leitura simples
df = pd.read_csv('arquivo.csv')

# Leitura com limitação de linhas
df = pd.read_csv('arquivo.csv', nrows=100)

# Leitura de colunas específicas
df = pd.read_csv('arquivo.csv', usecols=['col1', 'col2'])

# Leitura com encoding específico
df = pd.read_csv('arquivo.csv', encoding='latin-1')

# Informações básicas
print(df.shape)        # (linhas, colunas)
print(df.columns)      # Nome das colunas
print(df.dtypes)       # Tipos de dados
print(df.head())       # Primeiras linhas
print(df.tail())       # Últimas linhas
print(df.describe())   # Estatísticas

# Valores nulos
print(df.isnull().sum())

# Valores únicos
print(df['coluna'].unique())
print(df['coluna'].value_counts())

# Converter data
df['data'] = pd.to_datetime(df['data'])

# Extrair ano/mês
df['ano'] = df['data'].dt.year
df['mes'] = df['data'].dt.month

# Filtrar dados
filtrado = df[df['idade'] > 25]
filtrado = df[df['bairro'] == 'MANHATTAN']

# Selecionar colunas
novo_df = df[['col1', 'col2', 'col3']]

# Ordenar
ordenado = df.sort_values('data', ascending=False)

# Contagem por categoria
contagem = df['categoria'].value_counts()

# Média por grupo
media = df.groupby('bairro')['valor'].mean()

# Tabela cruzada
cruzada = pd.crosstab(df['raça'], df['sexo'])

import pandas as pd

df = pd.read_csv('nypd.csv', nrows=1000)
print(f"Linhas: {df.shape[0]}, Colunas: {df.shape[1]}")
print(df.columns.tolist())
print(df.head())

bairros = df['ARREST_BORO'].value_counts()
bairro_nomes = {'K':'Brooklyn','M':'Manhattan','Q':'Queens','B':'Bronx','S':'Staten Island'}

for codigo, quantidade in bairros.items():
    nome = bairro_nomes.get(codigo, codigo)
    print(f"{nome}: {quantidade} prisões")

    relatorio = f"""
RELATÓRIO DE ANÁLISE:
Total de registros: {len(df)}
Bairros analisados: {df['ARREST_BORO'].nunique()}
Período: {df['ARREST_DATE'].min()} a {df['ARREST_DATE'].max()}
"""
print(relatorio)



# Problema: Encoding errado
try:
    df = pd.read_csv('arquivo.csv')
except:
    df = pd.read_csv('arquivo.csv', encoding='latin-1')

# Problema: Memória insuficiente
chunks = []
for chunk in pd.read_csv('grande.csv', chunksize=10000):
    chunks.append(chunk)
df = pd.concat(chunks)

# Problema: Datas inconsistentes
df['data'] = pd.to_datetime(df['data'], errors='coerce')

# Executar qualquer script Python
python3 nome_do_script.py

# Verificar instalações
python3 -c "import pandas; print(pandas.__version__)"

# Desativar ambiente virtual
deactivate

# Ver todos os arquivos gerados
ls -lh *.csv *.txt *.py

# Vá para sua pasta
cd ~/python_ibm

# Ative o ambiente virtual
source venv/bin/activate

# Você verá (venv) antes do prompt
(venv) cloud@Workstation-CloudGlas:~/python_ibm$


 3. CÓDIGOS PYTHON ESSENCIAIS
A. Importação básica
python
import pandas as pd
import os
B. Leitura de CSV
python
# Leitura simples
df = pd.read_csv('arquivo.csv')

# Leitura com limitação de linhas
df = pd.read_csv('arquivo.csv', nrows=100)

# Leitura de colunas específicas
df = pd.read_csv('arquivo.csv', usecols=['col1', 'col2'])

# Leitura com encoding específico
df = pd.read_csv('arquivo.csv', encoding='latin-1')
C. Análise Exploratória
python
# Informações básicas
print(df.shape)        # (linhas, colunas)
print(df.columns)      # Nome das colunas
print(df.dtypes)       # Tipos de dados
print(df.head())       # Primeiras linhas
print(df.tail())       # Últimas linhas
print(df.describe())   # Estatísticas

# Valores nulos
print(df.isnull().sum())

# Valores únicos
print(df['coluna'].unique())
print(df['coluna'].value_counts())
D. Transformação de Dados
python
# Converter data
df['data'] = pd.to_datetime(df['data'])

# Extrair ano/mês
df['ano'] = df['data'].dt.year
df['mes'] = df['data'].dt.month

# Filtrar dados
filtrado = df[df['idade'] > 25]
filtrado = df[df['bairro'] == 'MANHATTAN']

# Selecionar colunas
novo_df = df[['col1', 'col2', 'col3']]

# Ordenar
ordenado = df.sort_values('data', ascending=False)
E. Análise Agregada
python
# Contagem por categoria
contagem = df['categoria'].value_counts()

# Média por grupo
media = df.groupby('bairro')['valor'].mean()

# Tabela cruzada
cruzada = pd.crosstab(df['raça'], df['sexo'])
F. Salvar Resultados
python
# Salvar como CSV
df.to_csv('resultado.csv', index=False)

# Salvar análise
contagem.to_csv('analise_contagem.csv')
📊 4. CÓDIGOS COMPLETOS DE ANÁLISE
Análise Básica
python
import pandas as pd

df = pd.read_csv('nypd.csv', nrows=1000)
print(f"Linhas: {df.shape[0]}, Colunas: {df.shape[1]}")
print(df.columns.tolist())
print(df.head())
Análise por Bairro
python
bairros = df['ARREST_BORO'].value_counts()
bairro_nomes = {'K':'Brooklyn','M':'Manhattan','Q':'Queens','B':'Bronx','S':'Staten Island'}

for codigo, quantidade in bairros.items():
    nome = bairro_nomes.get(codigo, codigo)
    print(f"{nome}: {quantidade} prisões")
Criação de Relatório
python
relatorio = f"""
RELATÓRIO DE ANÁLISE:
Total de registros: {len(df)}
Bairros analisados: {df['ARREST_BORO'].nunique()}
Período: {df['ARREST_DATE'].min()} a {df['ARREST_DATE'].max()}
"""
print(relatorio)
🔧 5. SOLUÇÃO DE PROBLEMAS COMUNS
python
# Problema: Encoding errado
try:
    df = pd.read_csv('arquivo.csv')
except:
    df = pd.read_csv('arquivo.csv', encoding='latin-1')

# Problema: Memória insuficiente
chunks = []
for chunk in pd.read_csv('grande.csv', chunksize=10000):
    chunks.append(chunk)
df = pd.concat(chunks)

# Problema: Datas inconsistentes
df['data'] = pd.to_datetime(df['data'], errors='coerce')
📈 6. ANÁLISES AVANÇADAS QUE VOCÊ APRENDEU
Geográfica: Mapeamento por coordenadas

Temporal: Tendências por mês/ano

Demográfica: Análise por idade, raça, gênero

Criminal: Tipos de crime mais comuns

Operacional: Eficiência por distrito policial

CHECKLIST DE APRENDIZADOS
✅ Configuração de ambiente Python/WSL
✅ Manipulação de grandes volumes de dados
✅ Limpeza e transformação com Pandas
✅ Análise exploratória de dados
✅ Criação de relatórios automatizados
✅ Solução de problemas reais (encoding, memória)
✅ Interpretação de resultados estatísticos
✅ Versionamento de análise (arquivos CSV intermediários)
✅ Documentação de processos
✅ Comunicação de insights