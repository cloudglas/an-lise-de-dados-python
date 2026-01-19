import pandas as pd
import os

print("=== ANÁLISE DO ARQUIVO COMPLETO (1.2GB) ===")
print("Isso pode demorar e usar muita memória!")

# Ler apenas colunas específicas para economizar memória
colunas_para_ler = ['ARREST_DATE', 'ARREST_BORO', 'OFNS_DESC', 'AGE_GROUP', 'PERP_SEX', 'PERP_RACE']

print(f"\n📥 Lendo apenas {len(colunas_para_ler)} colunas...")
try:
    # Ler em chunks (pedaços) para não sobrecarregar a memória
    chunks = []
    for chunk in pd.read_csv('nypd.csv', usecols=colunas_para_ler, chunksize=10000):
        chunks.append(chunk)
        if len(chunks) >= 10:  # Limitar a 100,000 linhas
            break
    
    df = pd.concat(chunks, ignore_index=True)
    
    print(f"✅ Carregado: {len(df):,} linhas")
    print(f"\n📊 PRIMEIRAS 5 LINHAS:")
    print(df.head())
    
    # Análise rápida
    print(f"\n🚨 TOP 5 CRIMES:")
    top_crimes = df['OFNS_DESC'].value_counts().head()
    for crime, quantidade in top_crimes.items():
        print(f"  {crime}: {quantidade:,}")
    
    print(f"\n👥 DISTRIBUIÇÃO POR RAÇA:")
    raca_dist = df['PERP_RACE'].value_counts()
    for raca, quantidade in raca_dist.items():
        print(f"  {raca}: {quantidade:,}")
    
    # Salvar análise
    df.to_csv('nypd_analise_completa.csv', index=False)
    print(f"\n💾 Análise completa salva como 'nypd_analise_completa.csv'")
    
except MemoryError:
    print("❌ MEMÓRIA INSUFICIENTE!")
    print("   Use um computador com mais RAM ou analise por partes")
except Exception as e:
    print(f"❌ Erro: {e}")
