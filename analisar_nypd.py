import pandas as pd
import os

print("=== ANÁLISE SIMPLES DO NYPD.CSV ===")

# Verificar se o arquivo existe
if not os.path.exists('nypd.csv'):
    print("❌ Arquivo nypd.csv não encontrado!")
    exit()

print(f"✅ Arquivo encontrado: {os.path.getsize('nypd.csv'):,} bytes")

# Ler apenas as primeiras 100 linhas para teste
print("\n📥 Lendo primeiras 100 linhas...")
try:
    df = pd.read_csv('nypd.csv', nrows=100)
except Exception as e:
    print(f"❌ Erro ao ler: {e}")
    # Tentar com encoding diferente
    try:
        df = pd.read_csv('nypd.csv', nrows=100, encoding='latin-1')
    except:
        print("❌ Não consegui ler o arquivo")
        exit()

print(f"✅ Dados carregados: {df.shape[0]} linhas, {df.shape[1]} colunas")

# Mostrar informações
print("\n📋 COLUNAS DISPONÍVEIS:")
for i, coluna in enumerate(df.columns, 1):
    print(f"{i:3}. {coluna}")

print(f"\n👀 PRIMEIRAS 5 LINHAS:")
print(df.head())

print(f"\n🔍 TIPOS DE DADOS:")
print(df.dtypes)

# Escolher colunas importantes automaticamente
print("\n🎯 SELECIONANDO COLUNAS IMPORTANTES...")
colunas_interessantes = []
for col in df.columns:
    col_lower = col.lower()
    if any(x in col_lower for x in ['date', 'year', 'time', 'boro', 'precinct', 'crime', 'offense', 'arrest', 'age']):
        colunas_interessantes.append(col)

if not colunas_interessantes:
    colunas_interessantes = df.columns[:5]  # Primeiras 5 colunas

print(f"Colunas selecionadas: {colunas_interessantes}")

# Criar nova tabela
nova_tabela = df[colunas_interessantes].copy()

# Salvar
nova_tabela.to_csv('nypd_organizado.csv', index=False)
print(f"\n💾 Salvo como 'nypd_organizado.csv'")

print("\n✅ ANÁLISE COMPLETA!")
print("   Verifique o arquivo 'nypd_organizado.csv'")
