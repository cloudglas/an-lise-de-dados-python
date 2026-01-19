"""
EXPRESSÕES E VARIÁVEIS EM PYTHON
Autor: [Geraldo]
Data: [18/01/2026]

Este código demonstra conceitos básicos de matemática e variáveis em Python.
Cada seção tem explicações detalhadas e exemplos práticos.
"""

print("-" * 60)
print("Expressoes e Variáveis em Python - Matemática Básica ")
print("-" * 60)

# ============================================================================
# SEÇÃO 1: OPERAÇÕES ARITMÉTICAS BÁSICAS
# ============================================================================
print("\n" + "=" * 60)
print("SEÇÃO 1: OPERAÇÕES ARITMÉTICAS BÁSICAS")
print("=" * 60)

"""
DEFINIÇÃO: Expressões são operações que o Python realiza.
COMPONENTES:
- Operandos: Os números/variáveis envolvidos (ex: 5, 10)
- Operadores: Os símbolos matemáticos (ex: +, -, *, /)
"""

# 1.1 ADIÇÃO (+)
print("\n1.1 ADIÇÃO (+)")
print("-" * 30)

# Expressão: 45 + 75 + 40
resultado_soma = 45 + 75 + 40
print(f"Expressão: 45 + 75 + 40")
print(f"Resultado: {resultado_soma}")
print(f"Explicação: Somamos três operandos (45, 75, 40) usando o operador +")
print(f"Operandos: 45, 75, 40")
print(f"Operador: +")

# 1.2 SUBTRAÇÃO (-)
print("\n1.2 SUBTRAÇÃO (-)")
print("-" * 30)

# Expressão: 10 - 25
resultado_subtracao = 10 - 25
print(f"Expressão: 10 - 25")
print(f"Resultado: {resultado_subtracao}")
print(f"Explicação: Subtraímos 25 de 10, resultando em negativo")
print(f"Regra: a - b = -(b - a) quando b > a")

# 1.3 MULTIPLICAÇÃO (*)
print("\n1.3 MULTIPLICAÇÃO (*)")
print("-" * 30)

# Expressão: 5 * 5
resultado_multiplicacao = 5 * 5
print(f"Expressão: 5 * 5")
print(f"Resultado: {resultado_multiplicacao}")
print(f"Explicação: Multiplicação é soma repetida: 5 + 5 + 5 + 5 + 5 = 25")

# 1.4 DIVISÃO REGULAR (/)
print("\n1.4 DIVISÃO REGULAR (/)")
print("-" * 30)

# Expressão: 25 / 5
divisao1 = 25 / 5
print(f"Expressão: 25 / 5")
print(f"Resultado: {divisao1}")
print(f"Tipo do resultado: {type(divisao1)}")

# Expressão: 25 / 6
divisao2 = 25 / 6
print(f"\nExpressão: 25 / 6")
print(f"Resultado: {divisao2}")
print(f"Arredondado: {divisao2:.3f}")  # Três casas decimais
print(f"Tipo do resultado: {type(divisao2)}")
print("IMPORTANTE: Em Python 3, a divisão regular SEMPRE retorna float!")

# 1.5 DIVISÃO INTEIRA (//)
print("\n1.5 DIVISÃO INTEIRA (//)")
print("-" * 30)

"""
DIVISÃO INTEIRA vs DIVISÃO REGULAR:
- // (barra dupla): Descarta a parte decimal, mantém apenas a parte inteira
- / (barra simples): Mantém as casas decimais
"""

div_int1 = 25 // 5
div_int2 = 25 // 6

print(f"Expressão: 25 // 5")
print(f"Resultado: {div_int1}")
print(f"Tipo: {type(div_int1)}")

print(f"\nExpressão: 25 // 6")
print(f"Resultado: {div_int2}")
print(f"Tipo: {type(div_int2)}")
print(f"Comparação: 25 / 6 = {25/6:.3f} vs 25 // 6 = {div_int2}")

# Demonstração do descarte da parte decimal
print(f"\nDemonstração do descarte:")
print(f"7 // 2 = {7 // 2} (parte inteira de 3.5)")
print(f"10 // 3 = {10 // 3} (parte inteira de 3.333...)")

# 1.6 MÓDULO/RESTO (%)
print("\n1.6 MÓDULO/RESTO (%)")
print("-" * 30)

"""
MÓDULO: Retorna o resto da divisão
Útil para verificar divisibilidade (par/ímpar, múltiplos, etc.)
"""

resto1 = 25 % 5
resto2 = 25 % 6

print(f"Expressão: 25 % 5")
print(f"Resultado: {resto1}")
print(f"Interpretação: 25 dividido por 5 tem resto {resto1}")

print(f"\nExpressão: 25 % 6")
print(f"Resultado: {resto2}")
print(f"Interpretação: 25 = 6 * 4 + {resto2}")

# Exemplos práticos
print(f"\nExemplos práticos:")
print(f"10 % 2 = {10 % 2} (números pares têm resto 0)")
print(f"11 % 2 = {11 % 2} (números ímpares têm resto 1)")
print(f"15 % 4 = {15 % 4} (15 = 4 * 3 + 3)")

# ============================================================================
# SEÇÃO 2: ORDEM DAS OPERAÇÕES
# ============================================================================
print("\n" + "=" * 60)
print("SEÇÃO 2: ORDEM DAS OPERAÇÕES (PRECEDÊNCIA)")
print("=" * 60)

"""
PEMDAS (Regra mnemônica):
1. Parênteses
2. Expoentes
3. Multiplicação e Divisão (da esquerda para direita)
4. Adição e Subtração (da esquerda para direita)

Python segue as convenções matemáticas padrão!
"""

# 2.1 Multiplicação antes da adição
print("\n2.1 MULTIPLICAÇÃO ANTES DA ADIÇÃO")
print("-" * 30)

expressao1 = 10 + 5 * 2
expressao2 = (10 + 5) * 2

print(f"Expressão 1: 10 + 5 * 2")
print(f"Cálculo: Primeiro 5 * 2 = 10, depois 10 + 10 = 20")
print(f"Resultado Python: {expressao1}")

print(f"\nExpressão 2: (10 + 5) * 2")
print(f"Cálculo: Primeiro (10 + 5) = 15, depois 15 * 2 = 30")
print(f"Resultado Python: {expressao2}")

print("\nCONCLUSÃO: Parênteses mudam a ordem das operações!")

# 2.2 Exemplo mais complexo
print("\n2.2 EXEMPLO COMPLEXO DE PRECEDÊNCIA")
print("-" * 30)

complexa = (10 + 2) * 3 / 4 - 1
print(f"Expressão: (10 + 2) * 3 / 4 - 1")

# Passo a passo:
print("\nPasso a passo:")
print("1. Parênteses: (10 + 2) = 12")
print("2. Multiplicação: 12 * 3 = 36")
print("3. Divisão: 36 / 4 = 9.0")
print("4. Subtração: 9.0 - 1 = 8.0")
print(f"Resultado final: {complexa}")

# ============================================================================
# SEÇÃO 3: VARIÁVEIS E ATRIBUIÇÃO
# ============================================================================
print("\n" + "=" * 60)
print("SEÇÃO 3: VARIÁVEIS E ATRIBUIÇÃO")
print("=" * 60)

"""
VARIÁVEL: Um nome que referencia um valor na memória
OPERADOR DE ATRIBUIÇÃO: = (sinal de igual)
"""

# 3.1 Atribuição básica
print("\n3.1 ATRIBUIÇÃO BÁSICA")
print("-" * 30)

# Atribuindo valor 1 à variável
minha_variavel = 1
print(f"Comando: minha_variavel = 1")
print(f"Valor atual de 'minha_variavel': {minha_variavel}")
print(f"Tipo da variável: {type(minha_variavel)}")

# Reatribuindo valor
minha_variavel = 10
print(f"\nComando: minha_variavel = 10")
print(f"Novo valor de 'minha_variavel': {minha_variavel}")
print("O valor anterior (1) foi substituído!")

# 3.2 Armazenando resultados de expressões
print("\n3.2 ARMAZENANDO RESULTADOS DE EXPRESSÕES")
print("-" * 30)

# Criando variável x com resultado de expressão
x = 45 + 75 + 40
print(f"Comando: x = 45 + 75 + 40")
print(f"Valor de x: {x}")
print(f"Python calcula a expressão e armazena o resultado em x")

# Operações com variáveis
y = x / 60
print(f"\nComando: y = x / 60")
print(f"Cálculo: y = {x} / 60 = {y}")
print(f"Valor de y: {y:.3f}")

# Atualizando o valor de uma variável
print("\n3.3 ATUALIZANDO VALOR DE VARIÁVEL")
print("-" * 30)

x = x / 60  # Atualizando x com novo cálculo
print(f"Comando: x = x / 60")
print(f"Interpretação: x recebe o valor atual de x dividido por 60")
print(f"Novo valor de x: {x:.3f}")
print("O valor anterior de x foi sobrescrito!")

# 3.4 Verificando tipos de variáveis
print("\n3.4 VERIFICANDO TIPOS DE VARIÁVEIS")
print("-" * 30)

print(f"Tipo de x: {type(x)}")
print(f"Tipo de y: {type(y)}")
print("Ambas são float porque envolvem divisão!")

# ============================================================================
# SEÇÃO 4: EXEMPLO PRÁTICO - CONVERSÃO DE MINUTOS PARA HORAS
# ============================================================================
print("\n" + "=" * 60)
print("SEÇÃO 4: EXEMPLO PRÁTICO - CONVERSÃO DE MINUTOS PARA HORAS")
print("=" * 60)

"""
PROBLEMA: Converter duração total de músicas de minutos para horas
DADOS: Temos uma playlist com músicas de diferentes durações
"""

# 4.1 Dados das músicas (em minutos)
print("\n4.1 DURAÇÃO DAS MÚSICAS (EM MINUTOS)")
print("-" * 30)

musica1 = 3.5   # 3 minutos e 30 segundos
musica2 = 4.2   # 4 minutos e 12 segundos
musica3 = 5.8   # 5 minutos e 48 segundos
musica4 = 2.9   # 2 minutos e 54 segundos
musica5 = 6.1   # 6 minutos e 6 segundos

print(f"Música 1: {musica1} minutos")
print(f"Música 2: {musica2} minutos")
print(f"Música 3: {musica3} minutos")
print(f"Música 4: {musica4} minutos")
print(f"Música 5: {musica5} minutos")

# 4.2 Cálculo do total de minutos
print("\n4.2 CÁLCULO DO TOTAL DE MINUTOS")
print("-" * 30)

# Boas práticas: nomes descritivos para variáveis
total_minutos = musica1 + musica2 + musica3 + musica4 + musica5

print(f"Expressão: total_minutos = soma de todas as músicas")
print(f"Cálculo: {musica1} + {musica2} + {musica3} + {musica4} + {musica5}")
print(f"Total de minutos: {total_minutos:.2f}")

# 4.3 Conversão para horas
print("\n4.3 CONVERSÃO PARA HORAS")
print("-" * 30)

total_horas = total_minutos / 60
print(f"Fórmula: horas = minutos ÷ 60")
print(f"Cálculo: {total_minutos:.2f} ÷ 60 = {total_horas:.4f}")
print(f"Total de horas: {total_horas:.4f}")

# 4.4 Formatação para horas e minutos
print("\n4.4 FORMATAÇÃO PARA HORAS E MINUTOS")
print("-" * 30)

# Extraindo horas inteiras
horas_inteiras = int(total_horas)
print(f"Horas inteiras: {horas_inteiras}")

# Calculando minutos restantes
minutos_restantes = total_minutos - (horas_inteiras * 60)
print(f"Minutos restantes: {minutos_restantes:.1f}")

print(f"\nRESULTADO FINAL:")
print(f"A playlist tem {total_minutos:.1f} minutos no total")
print(f"Isso equivale a {horas_inteiras} horas e {minutos_restantes:.1f} minutos")

# 4.5 Modificando dados e recalculando
print("\n4.5 MODIFICAÇÃO DE DADOS E RECÁLCULO")
print("-" * 30)

print("Adicionando mais uma música de 7.5 minutos...")
total_minutos = total_minutos + 7.5  # Atualizando total
total_horas = total_minutos / 60     # Recalculando horas

print(f"Novo total de minutos: {total_minutos:.2f}")
print(f"Novo total de horas: {total_horas:.4f}")

# ============================================================================
# SEÇÃO 5: EXERCÍCIOS PRÁTICOS
# ============================================================================
print("\n" + "=" * 60)
print("SEÇÃO 5: EXERCÍCIOS PRÁTICOS")
print("=" * 60)

print("\nTente resolver esses exercícios:")
print("1. Calcule a média das durações das músicas")
print("2. Converta 2.5 horas para minutos")
print("3. Calcule quanto tempo sobra se você tem 3 horas e quer ouvir todas as músicas")
print("4. Calcule quantas músicas de 3 minutos cabem em 1 hora")

# Soluções dos exercícios
print("\n" + "-" * 30)
print("SOLUÇÕES DOS EXERCÍCIOS")
print("-" * 30)

# Exercício 1: Média
media_minutos = total_minutos / 6  # Agora temos 6 músicas
print(f"\n1. Média das músicas: {media_minutos:.2f} minutos")

# Exercício 2: Conversão de horas para minutos
horas_para_minutos = 2.5 * 60
print(f"\n2. 2.5 horas = {horas_para_minutos} minutos")

# Exercício 3: Tempo restante
tempo_disponivel = 3 * 60  # 3 horas em minutos
tempo_sobra = tempo_disponivel - total_minutos
print(f"\n3. Tempo sobrando: {tempo_sobra:.1f} minutos")

# Exercício 4: Quantas músicas cabem em 1 hora
musicas_por_hora = 60 / 3  # 60 minutos ÷ duração da música
print(f"\n4. Cabem {musicas_por_hora:.1f} músicas de 3 minutos em 1 hora")

# ============================================================================
# RESUMO FINAL
# ============================================================================
print("\n" + "=" * 60)
print("RESUMO DOS CONCEITOS APRENDIDOS")
print("=" * 60)

print("\nOPERADORES ARITMÉTICOS:")
print(f"  Adição: + (ex: 5 + 3 = {5 + 3})")
print(f"  Subtração: - (ex: 5 - 3 = {5 - 3})")
print(f"  Multiplicação: * (ex: 5 * 3 = {5 * 3})")
print(f"  Divisão regular: / (ex: 5 / 3 = {5 / 3:.2f})")
print(f"  Divisão inteira: // (ex: 5 // 3 = {5 // 3})")
print(f"  Resto/Módulo: % (ex: 5 % 3 = {5 % 3})")

print("\nORDEM DAS OPERAÇÕES (PEMDAS):")
print("  1. Parênteses")
print("  2. Expoentes")
print("  3. Multiplicação e Divisão (esquerda → direita)")
print("  4. Adição e Subtração (esquerda → direita)")

print("\nVARIÁVEIS:")
print("  • Nomes que armazenam valores")
print("  • Podem ser reatribuídas")
print("  • Podem armazenar resultados de expressões")
print("  • Nomes descritivos facilitam a leitura do código")

print("\nBOAS PRÁTICAS:")
print("  1. Use nomes descritivos para variáveis")
print("  2. Use parênteses para clareza")
print("  3. Comente seu código")
print("  4. Verifique tipos com type() quando necessário")

print("\n" + "=" * 60)
print("FIM DO PROGRAMA")
print("=" * 60)