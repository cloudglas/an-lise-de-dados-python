import pandas as pd
import matplotlib.pyplot as plt

print("=== ANÁLISE COMPLETA DOS DADOS NYPD ===")

# Ler o arquivo organizado (que é pequeno)
df = pd.read_csv('nypd_organizado.csv')

print(f"\n📊 DADOS ORGANIZADOS:")
print(f"• Linhas: {df.shape[0]}")
print(f"• Colunas: {df.shape[1]}")
print(f"• Colunas: {list(df.columns)}")

print(f"\n👀 PRIMEIRAS 10 LINHAS:")
print(df.head(10))

# Converter data
df['ARREST_DATE'] = pd.to_datetime(df['ARREST_DATE'])

# Análise por Bairro
print("\n" + "="*50)
print("ANÁLISE POR BAIRRO (ARREST_BORO)")
print("="*50)

prisoes_por_bairro = df['ARREST_BORO'].value_counts()
print(f"\n🚨 PRISÕES POR BAIRRO:")
for bairro, quantidade in prisoes_por_bairro.items():
    print(f"  {bairro}: {quantidade} prisões")

# Análise por Grupo de Idade
print("\n" + "="*50)
print("ANÁLISE POR IDADE (AGE_GROUP)")
print("="*50)

idade_contagem = df['AGE_GROUP'].value_counts()
print(f"\n👥 PRISÕES POR GRUPO DE IDADE:")
for idade, quantidade in idade_contagem.items():
    print(f"  {idade}: {quantidade} prisões")

# Análise por Data
print("\n" + "="*50)
print("ANÁLISE POR DATA (ARREST_DATE)")
print("="*50)

# Extrair mês e ano
df['ANO_MES'] = df['ARREST_DATE'].dt.to_period('M')
prisoes_por_mes = df['ANO_MES'].value_counts().sort_index()

print(f"\n📅 PRISÕES POR MÊS:")
for mes, quantidade in prisoes_por_mes.head().items():  # Primeiros 5
    print(f"  {mes}: {quantidade} prisões")

# Criar relatório completo
print("\n" + "="*50)
print("RELATÓRIO COMPLETO")
print("="*50)

print(f"""
🎯 RESUMO DA ANÁLISE:

1. TOTAL DE PRISÕES ANALISADAS: {len(df):,}
2. BAIRROS COM MAIS PRISÕES:
   {prisoes_por_bairro.index[0]}: {prisoes_por_bairro.iloc[0]} prisões
   {prisoes_por_bairro.index[1]}: {prisoes_por_bairro.iloc[1]} prisões
3. GRUPO DE IDADE COM MAIS PRISÕES:
   {idade_contagem.index[0]}: {idade_contagem.iloc[0]} prisões
4. PERÍODO ANALISADO:
   De: {df['ARREST_DATE'].min().date()}
   Até: {df['ARREST_DATE'].max().date()}

💡 PRÓXIMOS PASSOS:
• Analisar tipos de crime (usar OFNS_DESC do arquivo original)
• Mapa por coordenadas (Latitude/Longitude)
• Análise por raça/gênero
""")

# Salvar análises em novos arquivos
prisoes_por_bairro.to_csv('prisoes_por_bairro.csv')
idade_contagem.to_csv('prisoes_por_idade.csv')
prisoes_por_mes.to_csv('prisoes_por_mes.csv')

print("\n💾 ARQUIVOS SALVOS:")
print("1. prisoes_por_bairro.csv - Prisões por bairro")
print("2. prisoes_por_idade.csv - Prisões por idade")
print("3. prisoes_por_mes.csv - Prisões por mês")

print("\n✅ ANÁLISE COMPLETA!")
