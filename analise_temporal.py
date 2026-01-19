import pandas as pd

print("=== ANÁLISE TEMPORAL ===")

# Ler dados com data
print("📥 Lendo dados temporais...")
try:
    df_temp = pd.read_csv('nypd.csv', usecols=['ARREST_DATE', 'ARREST_BORO'], nrows=5000)
    
    # Converter data
    df_temp['ARREST_DATE'] = pd.to_datetime(df_temp['ARREST_DATE'])
    df_temp['MES'] = df_temp['ARREST_DATE'].dt.month
    df_temp['ANO'] = df_temp['ARREST_DATE'].dt.year
    df_temp['ANO_MES'] = df_temp['ARREST_DATE'].dt.to_period('M')
    
    print(f"✅ {len(df_temp)} registros carregados")
    print(f"📅 Período: {df_temp['ARREST_DATE'].min().date()} a {df_temp['ARREST_DATE'].max().date()}")
    
    print("\n📈 PRISÕES POR MÊS:")
    prisao_mes = df_temp['ANO_MES'].value_counts().sort_index().tail(12)  # Últimos 12 meses
    for mes, count in prisao_mes.items():
        print(f"  {mes}: {count} prisões")
    
    print("\n🏙️ PRISÕES POR BAIRRO AO LONGO DO TEMPO:")
    bairros = ['K', 'M', 'Q', 'B', 'S']
    for bairro in bairros:
        count = len(df_temp[df_temp['ARREST_BORO'] == bairro])
        print(f"  {bairro}: {count} prisões")
    
    # Análise mensal por bairro
    print("\n📊 EVOLUÇÃO MENSAL (últimos 3 meses):")
    ultimos_meses = df_temp['ANO_MES'].value_counts().sort_index().tail(3).index
    
    for mes in ultimos_meses:
        mes_data = df_temp[df_temp['ANO_MES'] == mes]
        print(f"\n  {mes}:")
        for bairro in bairros:
            count = len(mes_data[mes_data['ARREST_BORO'] == bairro])
            if count > 0:
                print(f"    {bairro}: {count} prisões")
    
    # Salvar
    prisao_mes.to_csv('prisoes_por_mes_completo.csv')
    print("\n💾 Salvo como 'prisoes_por_mes_completo.csv'")
    
except Exception as e:
    print(f"❌ Erro: {e}")
