#!/usr/bin/env python3
"""
Comando rápido para inspecionar qualquer CSV
Uso: python3 inspecionar.py arquivo.csv
"""

import pandas as pd
import sys

if len(sys.argv) < 2:
    print("❌ Especifique um arquivo CSV")
    print("Uso: python3 inspecionar.py arquivo.csv")
    sys.exit(1)

arquivo = sys.argv[1]

try:
    # Ler só as primeiras 50 linhas
    df = pd.read_csv(arquivo, nrows=50)
    
    print(f"\n🔍 INSPEÇÃO: {arquivo}")
    print(f"   Linhas: {len(df)} (amostra)")
    print(f"   Colunas: {len(df.columns)}")
    
    print("\n📋 COLUNAS:")
    for i, col in enumerate(df.columns, 1):
        print(f"   {i:2}. {col}")
    
    print("\n👀 PRIMEIRAS 10 LINHAS:")
    print(df.head(10).to_string())
    
    print("\n📊 RESUMO:")
    print(df.describe().to_string())
    
except Exception as e:
    print(f"❌ Erro: {e}")

print()
