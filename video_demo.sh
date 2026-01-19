#!/bin/bash

# Configurações visuais
clear
echo -e "\033[1;36m"
echo "=================================================="
echo "       DEMONSTRAÇÃO: ANÁLISE DE DADOS NYPD       "
echo "=================================================="
echo -e "\033[0m"
sleep 2

# 1. Mostrar o arquivo gigante
clear
echo -e "\033[1;33m[PASSO 1] O DESAFIO: Arquivo de 1.2GB\033[0m"
echo ""
ls -lh nypd.csv | awk '{print "📁 " $9 " - " $5 " - " $6 " " $7 " " $8}'
echo ""
echo -e "\033[90mArquivo real da NYPD com 6 milhões de registros\033[0m"
sleep 3

# 2. Ativar ambiente Python
clear
echo -e "\033[1;33m[PASSO 2] Ambiente Python\033[0m"
echo ""
echo -e "\033[92m$ source venv/bin/activate\033[0m"
source venv/bin/activate
echo -e "\033[92m$ python3 -c \"import pandas as pd; print(f'✅ Pandas v{pd.__version__}')\"\033[0m"
python3 -c "import pandas as pd; print(f'✅ Pandas v{pd.__version__}')"
sleep 2

# 3. Análise rápida
clear
echo -e "\033[1;33m[PASSO 3] Análise Instantânea\033[0m"
echo ""
cat << 'PYCODE'
import pandas as pd
print("📥 Carregando dados...")
df = pd.read_csv('nypd.csv', nrows=10000)
print(f"✅ {len(df):,} registros processados")

print("\n🏙️  DISTRIBUIÇÃO GEOGRÁFICA:")
bairros = {'K':'Brooklyn','M':'Manhattan','Q':'Queens','B':'Bronx','S':'Staten Island'}
for cod, cnt in df['ARREST_BORO'].value_counts().items():
    print(f"  {bairros.get(cod,cod)}: {cnt}")

print("\n👥  PERFIL POR IDADE:")
for idade, cnt in df['AGE_GROUP'].value_counts().items():
    print(f"  {idade}: {cnt}")
PYCODE | python3
sleep 4

# 4. Insights visuais
clear
echo -e "\033[1;36m"  # Ciano
echo "╔══════════════════════════════════════════════╗"
echo "║              📊 INSIGHTS CHAVE               ║"
echo "╚══════════════════════════════════════════════╝"
echo -e "\033[0m"

python3 << 'EOF'
import pandas as pd
df = pd.read_csv('nypd.csv', nrows=5000)

# Cores no terminal
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'
BOLD = '\033[1m'

print(f"\n{BOLD}📍 DISTRIBUIÇÃO POR BAIRRO:{RESET}")
boro_counts = df['ARREST_BORO'].value_counts()
colors = [RED, GREEN, YELLOW, BLUE, MAGENTA]
bairro_nomes = {'K':'Brooklyn','M':'Manhattan','Q':'Queens','B':'Bronx','S':'Staten Island'}

for (codigo, qtd), cor in zip(boro_counts.items(), colors):
    nome = bairro_nomes.get(codigo, codigo)
    bar = '█' * (qtd // 10)  # Barra gráfica simples
    print(f"{cor}  {nome:<12} {qtd:>4} {bar}{RESET}")

print(f"\n{BOLD}👤 DISTRIBUIÇÃO POR IDADE:{RESET}")
idade_counts = df['AGE_GROUP'].value_counts()
for idade, qtd in idade_counts.items():
    bar = '█' * (qtd // 5)
    print(f"  {idade:<6} {qtd:>4} {GREEN}{bar}{RESET}")

print(f"\n{BOLD}📅 ANÁLISE TEMPORAL:{RESET}")
df['ARREST_DATE'] = pd.to_datetime(df['ARREST_DATE'], errors='coerce')
if df['ARREST_DATE'].notna().any():
    print(f"  Período: {df['ARREST_DATE'].min().date()} a {df['ARREST_DATE'].max().date()}")
    print(f"  Total de dias: {(df['ARREST_DATE'].max() - df['ARREST_DATE'].min()).days}")
