import pandas as pd

print("=== ANÁLISE DEMOGRÁFICA ===")

# Ler dados demográficos
print("📥 Lendo dados demográficos...")
try:
    df_demo = pd.read_csv('nypd.csv', usecols=['PERP_RACE', 'PERP_SEX', 'AGE_GROUP'], nrows=1000)
    
    print(f"✅ {len(df_demo)} registros carregados")
    
    print("\n👥 DISTRIBUIÇÃO POR RAÇA:")
    distribuicao_raca = df_demo['PERP_RACE'].value_counts()
    for raca, count in distribuicao_raca.items():
        porcentagem = (count / len(df_demo)) * 100
        print(f"  {raca:<20}: {count:>4} ({porcentagem:.1f}%)")
    
    print("\n🚻 DISTRIBUIÇÃO POR GÊNERO:")
    distribuicao_sexo = df_demo['PERP_SEX'].value_counts()
    for sexo, count in distribuicao_sexo.items():
        porcentagem = (count / len(df_demo)) * 100
        print(f"  {sexo}: {count} ({porcentagem:.1f}%)")
    
    print("\n📊 CRUZANDO RAÇA E GÊNERO:")
    cruzamento = pd.crosstab(df_demo['PERP_RACE'], df_demo['PERP_SEX'])
    print(cruzamento)
    
    # Salvar
    distribuicao_raca.to_csv('distribuicao_raca.csv')
    print("\n💾 Salvo como 'distribuicao_raca.csv'")
    
except Exception as e:
    print(f"❌ Erro: {e}")
