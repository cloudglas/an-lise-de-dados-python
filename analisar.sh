#!/bin/bash
echo -e "\033[1;35m"
echo "🧠 ANALISADOR DE DADOS NYPD - 1 LINHA"
echo -e "\033[0m"
python3 -c "
import pandas as pd
from datetime import datetime
print(f'🔍 {datetime.now().strftime(\"%H:%M\")} | Iniciando análise...')
df=pd.read_csv('nypd.csv', nrows=10000)
print(f'✅ {len(df):,} registros | {len(df.columns)} colunas')
print(f'\\n\\033[1;36m📍 BAIRROS:\\033[0m')
for b,c in df['ARREST_BORO'].value_counts().items():
    bar='█'*(c//50);n={'K':'BKN','M':'MAN','Q':'QNS','B':'BRX','S':'SI'}.get(b,b)
    print(f'{n}: {c:>4} {bar}')
print(f'\\n\\033[1;36m👤 IDADES:\\033[0m')
for i,c in df['AGE_GROUP'].value_counts().items():
    print(f'{i}: {c:>4} ({c/len(df)*100:.1f}%)')
print(f'\\n🎯 INSIGHT: {df[\"AGE_GROUP\"].value_counts().index[0]} é o grupo mais comum')
"
