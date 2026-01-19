import pandas as pd

print("=== VISUALIZANDO DADOS NYPD ===")

# Ler dados
df = pd.read_csv('nypd_organizado.csv')

print("\n1. DADOS COMPLETOS:")
print(df)

print("\n2. ESTATÍSTICAS:")
print(df.describe())

print("\n3. VALORES ÚNICOS POR COLUNA:")
for coluna in df.columns:
    if df[coluna].dtype == 'object':  # Colunas de texto
        valores = df[coluna].unique()
        print(f"\n{coluna} ({len(valores)} valores):")
        print(f"  {', '.join(map(str, valores[:5]))}{'...' if len(valores) > 5 else ''}")

print("\n4. PRIMEIROS 10 REGISTROS:")
for i, linha in df.head(10).iterrows():
    print(f"\nRegistro {i}:")
    for coluna in df.columns:
        print(f"  {coluna}: {linha[coluna]}")
