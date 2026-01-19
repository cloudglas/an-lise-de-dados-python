import pandas as pd
from datetime import datetime

print("=== ANÁLISE COMPLETA DOS DADOS NYPD ===")
print("Versão sem matplotlib - só análise de dados\n")

# Ler o arquivo organizado
df = pd.read_csv('nypd_organizado.csv')

print(f"📊 DADOS ORGANIZADOS:")
print(f"• Total de registros: {len(df):,}")
print(f"• Colunas: {list(df.columns)}")

print(f"\n👀 AMOSTRA DOS DADOS (5 primeiros):")
for i in range(min(5, len(df))):
    print(f"\nRegistro {i}:")
    for col in df.columns:
        print(f"  {col}: {df.iloc[i][col]}")

# Converter data
print(f"\n📅 CONVERTENDO DATAS...")
df['ARREST_DATE'] = pd.to_datetime(df['ARREST_DATE'], errors='coerce')

# Análise por Bairro
print("\n" + "="*60)
print("🚨 ANÁLISE POR BAIRRO (ARREST_BORO)")
print("="*60)

# Mapear códigos de bairro
bairro_nomes = {
    'K': 'BROOKLYN',
    'M': 'MANHATTAN', 
    'Q': 'QUEENS',
    'B': 'BRONX',
    'S': 'STATEN ISLAND'
}

prisoes_por_bairro = df['ARREST_BORO'].value_counts()
print(f"\n📊 PRISÕES POR BAIRRO:")
for codigo, quantidade in prisoes_por_bairro.items():
    nome = bairro_nomes.get(codigo, f'Desconhecido ({codigo})')
    print(f"  {nome:<20} ({codigo}): {quantidade:>3} prisões")

# Análise por Grupo de Idade
print("\n" + "="*60)
print("👥 ANÁLISE POR GRUPO DE IDADE")
print("="*60)

idade_contagem = df['AGE_GROUP'].value_counts().sort_index()
print(f"\n📊 PRISÕES POR IDADE:")
for idade, quantidade in idade_contagem.items():
    print(f"  {idade:<10}: {quantidade:>3} prisões")

# Análise por Precinto
print("\n" + "="*60)
print("👮 ANÁLISE POR DISTRITO POLICIAL (PRECINCT)")
print("="*60)

precinto_contagem = df['ARREST_PRECINCT'].value_counts().head(10)
print(f"\n📊 TOP 10 DISTRITOS COM MAIS PRISÕES:")
for precinto, quantidade in precinto_contagem.items():
    print(f"  Distrito {precinto:<3}: {quantidade:>3} prisões")

# Análise por Data
print("\n" + "="*60)
print("📅 ANÁLISE POR DATA")
print("="*60)

if 'ARREST_DATE' in df.columns and df['ARREST_DATE'].notna().any():
    print(f"\n📆 PERÍODO ANALISADO:")
    print(f"  Data mais antiga: {df['ARREST_DATE'].min().strftime('%d/%m/%Y')}")
    print(f"  Data mais recente: {df['ARREST_DATE'].max().strftime('%d/%m/%Y')}")
    
    # Por mês
    df['MES'] = df['ARREST_DATE'].dt.month
    df['ANO'] = df['ARREST_DATE'].dt.year
    
    mes_contagem = df['MES'].value_counts().sort_index()
    print(f"\n📊 PRISÕES POR MÊS:")
    meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 
             'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    for mes_num, quantidade in mes_contagem.items():
        if 1 <= mes_num <= 12:
            print(f"  {meses[mes_num-1]}: {quantidade:>3} prisões")

# Estatísticas
print("\n" + "="*60)
print("📈 ESTATÍSTICAS GERAIS")
print("="*60)

print(f"\n📋 DISTRIBUIÇÃO DOS DADOS:")
print(f"• Total de registros: {len(df)}")
print(f"• Registros com data válida: {df['ARREST_DATE'].notna().sum()}")
print(f"• Bairros diferentes: {df['ARREST_BORO'].nunique()}")
print(f"• Distritos diferentes: {df['ARREST_PRECINCT'].nunique()}")
print(f"• Grupos de idade diferentes: {df['AGE_GROUP'].nunique()}")

# Criar tabela resumo
print("\n" + "="*60)
print("📋 TABELA RESUMO")
print("="*60)

resumo_data = []
for i in range(min(20, len(df))):  # Primeiros 20 registros
    registro = df.iloc[i]
    data_formatada = registro['ARREST_DATE'].strftime('%d/%m/%Y') if pd.notna(registro['ARREST_DATE']) else 'N/A'
    bairro_nome = bairro_nomes.get(registro['ARREST_BORO'], registro['ARREST_BORO'])
    
    resumo_data.append({
        'ID': registro['ARREST_KEY'],
        'Data': data_formatada,
        'Bairro': bairro_nome,
        'Distrito': registro['ARREST_PRECINCT'],
        'Idade': registro['AGE_GROUP']
    })

# Mostrar tabela
print(f"\n{'ID':<12} {'Data':<12} {'Bairro':<15} {'Distrito':<10} {'Idade':<10}")
print("-" * 60)
for linha in resumo_data:
    print(f"{linha['ID']:<12} {linha['Data']:<12} {linha['Bairro']:<15} {linha['Distrito']:<10} {linha['Idade']:<10}")

# Salvar análises
print("\n" + "="*60)
print("💾 SALVANDO RESULTADOS")
print("="*60)

# Salvar DataFrame original
df.to_csv('nypd_analisado_completo.csv', index=False)
print("✅ 1. nypd_analisado_completo.csv - Todos os dados com datas convertidas")

# Salvar por bairro
prisoes_bairro_df = pd.DataFrame({
    'Bairro_Codigo': prisoes_por_bairro.index,
    'Bairro_Nome': [bairro_nomes.get(cod, cod) for cod in prisoes_por_bairro.index],
    'Prisoes': prisoes_por_bairro.values
})
prisoes_bairro_df.to_csv('prisoes_por_bairro_detalhado.csv', index=False)
print("✅ 2. prisoes_por_bairro_detalhado.csv - Prisões por bairro")

# Salvar por idade
idade_df = pd.DataFrame({
    'Idade_Grupo': idade_contagem.index,
    'Prisoes': idade_contagem.values
})
idade_df.to_csv('prisoes_por_idade_detalhado.csv', index=False)
print("✅ 3. prisoes_por_idade_detalhado.csv - Prisões por idade")

# Salvar por distrito
precinto_df = pd.DataFrame({
    'Distrito': precinto_contagem.index,
    'Prisoes': precinto_contagem.values
})
precinto_df.to_csv('prisoes_por_distrito.csv', index=False)
print("✅ 4. prisoes_por_distrito.csv - Prisões por distrito")

print("\n" + "="*60)
print("🎯 RELATÓRIO FINAL")
print("="*60)

print(f"""
📊 RESUMO DA ANÁLISE NYPD:

1. DADOS ANALISADOS:
   • Total: {len(df):,} registros de prisão
   • Período: {df['ARREST_DATE'].min().strftime('%d/%m/%Y') if 'ARREST_DATE' in df.columns else 'N/A'} a {df['ARREST_DATE'].max().strftime('%d/%m/%Y') if 'ARREST_DATE' in df.columns else 'N/A'}
   
2. DISTRIBUIÇÃO GEOGRÁFICA:
   • Bairro com mais prisões: {bairro_nomes.get(prisoes_por_bairro.index[0], prisoes_por_bairro.index[0])} ({prisoes_por_bairro.iloc[0]} prisões)
   • Distrito com mais prisões: {precinto_contagem.index[0]} ({precinto_contagem.iloc[0]} prisões)
   
3. PERFIL POR IDADE:
   • Grupo mais frequente: {idade_contagem.index[0]} ({idade_contagem.iloc[0]} prisões)

4. ARQUIVOS GERADOS:
   • nypd_analisado_completo.csv - Dados completos analisados
   • prisoes_por_bairro_detalhado.csv - Análise por bairro
   • prisoes_por_idade_detalhado.csv - Análise por idade
   • prisoes_por_distrito.csv - Análise por distrito

💡 PRÓXIMOS PASSOS SUGERIDOS:
1. Analisar tipos de crime (precisa do arquivo original completo)
2. Cruzar dados por raça/gênero
3. Criar mapa por coordenadas
4. Análise temporal (tendências por mês/ano)
""")

print("\n✅ ANÁLISE CONCLUÍDA COM SUCESSO!")
