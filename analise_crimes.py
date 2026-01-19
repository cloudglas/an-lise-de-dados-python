import pandas as pd

print("=== ANÁLISE POR TIPO DE CRIME ===")

# Ler colunas específicas do arquivo grande
print("📥 Lendo tipos de crime...")
try:
    # Ler apenas as colunas de crime
    df_crimes = pd.read_csv('nypd.csv', usecols=['OFNS_DESC', 'PD_DESC', 'LAW_CAT_CD'], nrows=1000)
    
    print(f"✅ {len(df_crimes)} registros carregados")
    
    print("\n🚨 TOP 10 TIPOS DE CRIME (OFNS_DESC):")
    top_crimes = df_crimes['OFNS_DESC'].value_counts().head(10)
    for crime, count in top_crimes.items():
        print(f"  {crime}: {count} prisões")
    
    print("\n🔍 CATEGORIAS DE LEI (LAW_CAT_CD):")
    categorias = df_crimes['LAW_CAT_CD'].value_counts()
    for cat, count in categorias.items():
        print(f"  {cat}: {count} prisões")
    
    print("\n📋 DESCRIÇÕES DETALHADAS (PD_DESC) - Top 5:")
    descricoes = df_crimes['PD_DESC'].value_counts().head()
    for desc, count in descricoes.items():
        print(f"  {desc}: {count} prisões")
    
    # Salvar análise
    top_crimes.to_csv('top_crimes.csv')
    print("\n💾 Salvo como 'top_crimes.csv'")
    
except Exception as e:
    print(f"❌ Erro: {e}")
