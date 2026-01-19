import pandas as pd

print("=== ANÁLISE RÁPIDA NYPD ===")

# Ler dados
df = pd.read_csv('nypd_organizado.csv')
print(f"✅ {len(df)} registros carregados\n")

# 1. Mostrar todos os dados
print("1. 📋 TODOS OS DADOS:")
print(df.to_string())

# 2. Contagens básicas
print("\n\n2. 📊 CONTAGENS:")

print("\n   Por Bairro (ARREST_BORO):")
print("   K = BROOKLYN, M = MANHATTAN, Q = QUEENS, B = BRONX, S = STATEN ISLAND")
for bairro, count in df['ARREST_BORO'].value_counts().items():
    print(f"   {bairro}: {count} prisões")

print("\n   Por Idade (AGE_GROUP):")
for idade, count in df['AGE_GROUP'].value_counts().items():
    print(f"   {idade}: {count} prisões")

print("\n   Por Distrito (ARREST_PRECINCT) - Top 5:")
for distrito, count in df['ARREST_PRECINCT'].value_counts().head().items():
    print(f"   Distrito {distrito}: {count} prisões")

# 3. Estatísticas
print("\n\n3. 📈 ESTATÍSTICAS DO DISTRITO:")
print(f"   Média: {df['ARREST_PRECINCT'].mean():.1f}")
print(f"   Mínimo: {df['ARREST_PRECINCT'].min()}")
print(f"   Máximo: {df['ARREST_PRECINCT'].max()}")

# 4. Ver datas
print("\n\n4. 📅 DATAS (primeiras 5):")
print(df['ARREST_DATE'].head().to_string())

print("\n✅ Fim da análise!")
