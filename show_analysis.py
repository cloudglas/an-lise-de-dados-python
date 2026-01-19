import pandas as pd
import time

def print_color(text, color_code):
    """Imprime texto colorido"""
    print(f"\033[{color_code}m{text}\033[0m")

def animated_print(text, delay=0.05):
    """Imprime texto com animação"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Limpar tela e mostrar título
print("\033[2J\033[H")  # Limpa tela
print_color("╔══════════════════════════════════════════════╗", "1;36")
print_color("║      DEMONSTRAÇÃO: ANÁLISE DE DADOS NYPD     ║", "1;33")
print_color("╚══════════════════════════════════════════════╝", "1;36")
print()
time.sleep(1)

# Passo 1: Carregando dados
animated_print("📥 CARREGANDO DADOS...", 0.1)
df = pd.read_csv('nypd_organizado.csv')
print_color(f"✅ {len(df)} REGISTROS CARREGADOS", "1;32")
time.sleep(0.5)

# Passo 2: Análise por bairro
print()
animated_print("🏙️  ANALISANDO POR BAIRRO...", 0.1)
time.sleep(0.5)

print_color("\n┌─────────────────┬─────────┬────────────────┐", "1;37")
print_color("│     BAIRRO      │ PRISÕES │ DISTRITO MÉDIO │", "1;37")
print_color("├─────────────────┼─────────┼────────────────┤", "1;37")

bairro_counts = df['ARREST_BORO'].value_counts()
nomes = {'K':'BROOKLYN', 'M':'MANHATTAN', 'Q':'QUEENS', 'B':'BRONX', 'S':'STATEN ISLAND'}

for bairro in ['K', 'M', 'Q', 'B', 'S']:
    if bairro in bairro_counts:
        qtd = bairro_counts[bairro]
        media = df[df['ARREST_BORO'] == bairro]['ARREST_PRECINCT'].mean()
        
        # Animação de contagem
        print(f"│ {nomes[bairro]:<15} │ ", end='', flush=True)
        time.sleep(0.3)
        print(f"{qtd:>7} │ ", end='', flush=True)
        time.sleep(0.3)
        print(f"{media:>14.1f} │")
        time.sleep(0.2)

print_color("└─────────────────┴─────────┴────────────────┘", "1;37")

# Passo 3: Gráfico ASCII
print()
animated_print("📊 VISUALIZAÇÃO DE DISTRIBUIÇÃO:", 0.05)
print()

max_qtd = bairro_counts.max()
for bairro in ['K', 'M', 'Q', 'B', 'S']:
    if bairro in bairro_counts:
        qtd = bairro_counts[bairro]
        bar_length = int((qtd / max_qtd) * 40)
        bar = '█' * bar_length
        nome = nomes[bairro]
        print(f"{nome:<15} {bar} {qtd}")
        time.sleep(0.2)

# Passo 4: Insights
print()
print_color("💡 PRINCIPAIS INSIGHTS:", "1;33")
time.sleep(0.5)

bairro_mais = bairro_counts.idxmax()
qtd_mais = bairro_counts.max()
nome_mais = nomes[bairro_mais]

print(f"• {nome_mais} tem o maior número de prisões: {qtd_mais}")
time.sleep(0.3)

idade_mais = df['AGE_GROUP'].value_counts().idxmax()
qtd_idade = df['AGE_GROUP'].value_counts().max()
print(f"• Faixa etária {idade_mais} é a mais frequente: {qtd_idade} casos")
time.sleep(0.3)

distrito_mais = df['ARREST_PRECINCT'].value_counts().idxmax()
qtd_distrito = df['ARREST_PRECINCT'].value_counts().max()
print(f"• Distrito {distrito_mais} é o mais ativo: {qtd_distrito} prisões")

# Final
print()
print_color("="*50, "1;36")
print_color("✅ ANÁLISE CONCLUÍDA COM SUCESSO!", "1;32")
print_color("="*50, "1;36")
print()
print("Comando usado: python3 show_analysis.py")
print("Tecnologias: Python, Pandas, Terminal")
