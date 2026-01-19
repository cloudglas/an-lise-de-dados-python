import pandas as pd
from datetime import datetime

print("="*70)
print("RELATÓRIO FINAL DE ANÁLISE NYPD")
print(f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
print("="*70)

# Ler todos os dados organizados
df = pd.read_csv('nypd_organizado.csv')

# Estatísticas gerais
total_prisoes = len(df)
bairros = len(df['ARREST_BORO'].unique())
distritos = len(df['ARREST_PRECINCT'].unique())
idades = len(df['AGE_GROUP'].unique())

# Contagens detalhadas
contagem_bairro = df['ARREST_BORO'].value_counts()
contagem_idade = df['AGE_GROUP'].value_counts()
contagem_distrito = df['ARREST_PRECINCT'].value_counts()

print(f"\n📊 ESTATÍSTICAS GERAIS:")
print(f"   • Total de prisões analisadas: {total_prisoes}")
print(f"   • Bairros diferentes: {bairros}")
print(f"   • Distritos diferentes: {distritos}")
print(f"   • Grupos de idade diferentes: {idades}")

print(f"\n🏙️  DISTRIBUIÇÃO POR BAIRRO:")
bairro_nomes = {'K': 'Brooklyn', 'M': 'Manhattan', 'Q': 'Queens', 
                'B': 'Bronx', 'S': 'Staten Island'}

for codigo, quantidade in contagem_bairro.items():
    nome = bairro_nomes.get(codigo, codigo)
    percentual = (quantidade / total_prisoes) * 100
    print(f"   • {nome:<12}: {quantidade:>3} prisões ({percentual:5.1f}%)")

print(f"\n👥 DISTRIBUIÇÃO POR IDADE:")
for idade, quantidade in contagem_idade.items():
    percentual = (quantidade / total_prisoes) * 100
    print(f"   • {idade:<6}: {quantidade:>3} prisões ({percentual:5.1f}%)")

print(f"\n👮 TOP 5 DISTRITOS COM MAIS PRISÕES:")
for distrito, quantidade in contagem_distrito.head().items():
    percentual = (quantidade / total_prisoes) * 100
    print(f"   • Distrito {distrito:<3}: {quantidade:>3} prisões ({percentual:5.1f}%)")

# Encontrar datas
df['ARREST_DATE'] = pd.to_datetime(df['ARREST_DATE'], errors='coerce')
datas_validas = df['ARREST_DATE'].dropna()

if not datas_validas.empty:
    print(f"\n📅 PERÍODO ANALISADO:")
    print(f"   • Data mais antiga: {datas_validas.min().strftime('%d/%m/%Y')}")
    print(f"   • Data mais recente: {datas_validas.max().strftime('%d/%m/%Y')}")
    print(f"   • Período total: {(datas_validas.max() - datas_validas.min()).days} dias")

print(f"\n💾 ARQUIVOS GERADOS:")
arquivos = [
    ('nypd_organizado.csv', 'Dados organizados completos'),
    ('prisoes_por_bairro_detalhado.csv', 'Análise por bairro'),
    ('prisoes_por_idade_detalhado.csv', 'Análise por idade'),
    ('prisoes_por_distrito.csv', 'Análise por distrito'),
    ('nypd_analisado_completo.csv', 'Dados completos analisados')
]

for arquivo, descricao in arquivos:
    try:
        with open(arquivo, 'r') as f:
            linhas = sum(1 for _ in f)
        print(f"   • {arquivo:<30} ({linhas-1 if linhas>0 else 0} linhas) - {descricao}")
    except:
        print(f"   • {arquivo:<30} (não encontrado)")

print(f"\n🎯 PRINCIPAIS DESCOBERTAS:")
print(f"   1. {bairro_nomes.get(contagem_bairro.index[0])} tem o maior número de prisões")
print(f"   2. Faixa etária {contagem_idade.index[0]} é a mais comum")
print(f"   3. Distrito {contagem_distrito.index[0]} tem mais atividade policial")
print(f"   4. {len(df[df['AGE_GROUP'] == '<18'])} prisões envolvem menores de idade")

print(f"\n📋 RECOMENDAÇÕES PARA ANÁLISE FUTURA:")
print(f"   1. Analisar tipos específicos de crime")
print(f"   2. Cruzar dados por raça e gênero")
print(f"   3. Verificar tendências temporais")
print(f"   4. Mapear localizações geográficas")

print(f"\n" + "="*70)
print("✅ RELATÓRIO CONCLUÍDO")
print("="*70)

# Salvar relatório em arquivo
with open('RELATORIO_NYPD.txt', 'w') as f:
    f.write("RELATÓRIO DE ANÁLISE NYPD\n")
    f.write("="*50 + "\n\n")
    f.write(f"Total de prisões analisadas: {total_prisoes}\n\n")
    
    f.write("Distribuição por bairro:\n")
    for codigo, quantidade in contagem_bairro.items():
        nome = bairro_nomes.get(codigo, codigo)
        f.write(f"  {nome}: {quantidade} prisões\n")
    
    f.write("\nDistribuição por idade:\n")
    for idade, quantidade in contagem_idade.items():
        f.write(f"  {idade}: {quantidade} prisões\n")

print("💾 Relatório salvo como 'RELATORIO_NYPD.txt'")
