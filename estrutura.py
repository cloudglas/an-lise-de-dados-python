import os
import pandas as pd

print("="*60)
print("ANÁLISE DA ESTRUTURA DE DADOS DISPONÍVEIS")
print("="*60)

# Listar arquivos CSV
csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]
print(f"\n📁 Arquivos CSV encontrados: {len(csv_files)}")

for csv in csv_files:
    size = os.path.getsize(csv)
    size_mb = size / (1024*1024)
    
    # Tentar ler cabeçalho
    try:
        df_sample = pd.read_csv(csv, nrows=1)
        cols = len(df_sample.columns)
        print(f"\n  📄 {csv}")
        print(f"     Tamanho: {size_mb:.1f} MB ({size:,} bytes)")
        print(f"     Colunas: {cols}")
        if cols > 0:
            print(f"     Exemplo de colunas: {list(df_sample.columns)[:5]}...")
    except:
        print(f"\n  ❌ {csv} - Não pude ler")

print("\n" + "="*60)
print("RECOMENDAÇÃO PARA DASHBOARD:")
print("="*60)

if 'nypd.csv' in csv_files:
    print("✅ Use 'nypd_organizado.csv' para dashboard rápido")
    print("✅ Use 'nypd.csv' para análise profunda (carregue em partes)")
elif 'nypd_organizado.csv' in csv_files:
    print("✅ Use 'nypd_organizado.csv' - já está organizado")
else:
    print("❌ Crie primeiro um arquivo organizado com:")
    print("   python3 analisar_nypd.py")

print("\n🎯 Para criar dashboard:")
print("   1. streamlit run dashboard_nypd.py")
print("   2. Abra dashboard_simples.html no navegador")
print("   3. python3 terminal_dashboard.py")
