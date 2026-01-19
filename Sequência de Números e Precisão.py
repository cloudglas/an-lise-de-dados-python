# ============================================
# EXEMPLO 2: SEQUÊNCIA NUMÉRICA E PRECISÃO
# ============================================

print("\n\n" + "=" * 50)
print("EXEMPLO 2: SEQUÊNCIA NUMÉRICA E PRECISÃO")
print("=" * 50)

# Criando uma sequência de números
print("\n1. SEQUÊNCIA DE NÚMEROS ENTRE 0 E 1:")

# Usando range para inteiros (só funciona com inteiros)
sequencia_inteiros = list(range(0, 11))  # 0 a 10
print(f"Inteiros de 0 a 10: {sequencia_inteiros}")
print(f"Tipo dos elementos: Todos são {type(sequencia_inteiros[0]).__name__}")

# Criando floats entre 0 e 1
print("\n2. FLOATS ENTRE 0 E 1:")
# Dividindo cada inteiro por 10 para obter floats
sequencia_floats = [i/10 for i in range(0, 11)]
print(f"Floats de 0.0 a 1.0: {sequencia_floats}")
print(f"Tipo dos elementos: Todos são {type(sequencia_floats[0]).__name__}")

# Demonstração de precisão com floats
print("\n3. DEMONSTRAÇÃO DE PRECISÃO DOS FLOATS:")

# Entre 0.5 e 0.6
print("\nEntre 0.5 e 0.6:")
numeros_detalhados = [0.5 + i/100 for i in range(0, 11)]
for num in numeros_detalhados:
    print(f"  {num:.3f} → Tipo: {type(num).__name__}")

# Problema de precisão com floats
print("\n4. PROBLEMA DE PRECISÃO DOS FLOATS:")
print("Cálculo: 0.1 + 0.2 =", 0.1 + 0.2)
print("Esperado: 0.3")
print("Diferença:", (0.1 + 0.2) - 0.3)
print("Isso ocorre porque floats são aproximações binárias!")

# Comparação entre int e float
print("\n5. COMPARAÇÃO ENTRE INT E FLOAT:")

# Intervalo de inteiros vs floats
print("Inteiros: Números discretos (contáveis)")
print("  Exemplo: 1, 2, 3, 4, 5")
print("Floats: Números contínuos (infinitos entre cada inteiro)")
print("  Entre 1 e 2 existem infinitos floats: 1.1, 1.11, 1.111, ...")

# Demonstração prática
print("\n6. DEMONSTRAÇÃO PRÁTICA:")
print("Convertendo sequência de floats para inteiros:")

valores_mistos = [1.0, 1.1, 1.5, 1.9, 2.0]
for valor in valores_mistos:
    valor_int = int(valor)
    print(f"  Float: {valor} → Int: {valor_int} (perde: {valor - valor_int:.1f})")

# Operações entre diferentes tipos
print("\n7. OPERAÇÕES ENTRE DIFERENTES TIPOS:")

a = 10      # int
b = 3.5     # float
c = "2"     # string

print(f"Int {a} + Float {b} = {a + b}")
print(f"  Resultado é do tipo: {type(a + b).__name__}")

# Para somar com string, precisa converter
print(f"Int {a} + String '{c}' (convertida): {a + int(c)}")

# Verificação de tipos
print("\n8. VERIFICAÇÃO DE TIPOS:")
valores = [42, 3.14, "Python", True, None]
for i, valor in enumerate(valores, 1):
    print(f"  {i}. Valor: {valor:10} | Tipo: {type(valor).__name__:10} | bool(): {bool(valor)}")

print("\n" + "=" * 50)
print("CONCLUSÃO:")
print("1. Inteiros (int): números inteiros, positivos ou negativos")
print("2. Floats (float): números reais/com decimais, têm limitações de precisão")
print("3. Strings (str): sequências de caracteres/texto")
print("4. Booleanos (bool): True ou False")
print("5. Typecasting: converter entre tipos pode causar perda de informação!")
print("=" * 50)