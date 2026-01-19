# ============================================
# EXEMPLO 1: TIPOS BÁSICOS E TYPECASTING
# ============================================

print("=" * 50)
print("EXEMPLO 1: TIPOS BÁSICOS E TYPECASTING")
print("=" * 50)

# 1. INTEGERS (Inteiros)
print("\n1. INTEGERS (Inteiros):")
numero_inteiro = 42
print(f"Valor: {numero_inteiro}")
print(f"Tipo: {type(numero_inteiro)}")
print(f"Tipo impresso: {type(numero_inteiro).__name__}")

# 2. FLOATS (Números reais/ponto flutuante)
print("\n2. FLOATS (Números reais):")
numero_float = 21.213
print(f"Valor: {numero_float}")
print(f"Tipo: {type(numero_float)}")

# 3. STRINGS (Sequências de caracteres)
print("\n3. STRINGS (Texto):")
texto = "Olá Mundo!"
print(f"Valor: {texto}")
print(f"Tipo: {type(texto)}")

# 4. BOOLEANS (Valores lógicos)
print("\n4. BOOLEANS (Valores lógicos):")
verdadeiro = True
falso = False
print(f"True: {verdadeiro}, Tipo: {type(verdadeiro)}")
print(f"False: {falso}, Tipo: {type(falso)}")

# 5. TYPECASTING (Conversão entre tipos)
print("\n5. TYPECASTING (Conversões):")

# Int para Float
print("\na) Int → Float:")
inteiro = 7
convertido_float = float(inteiro)
print(f"Inteiro: {inteiro} → Float: {convertido_float}")
print(f"Tipo original: {type(inteiro)} → Tipo convertido: {type(convertido_float)}")

# Float para Int (PERDA DE INFORMAÇÃO!)
print("\nb) Float → Int (CUIDADO!):")
real = 3.14159
convertido_int = int(real)
print(f"Float: {real} → Int: {convertido_int}")
print(f"Perdemos as casas decimais! ({real - convertido_int})")

# String para Int
print("\nc) String → Int:")
string_numero = "123"
convertido_string_int = int(string_numero)
print(f"String: '{string_numero}' → Int: {convertido_string_int}")
print(f"Tipo: {type(string_numero)} → {type(convertido_string_int)}")

# String para Float
print("\nd) String → Float:")
string_decimal = "3.14"
convertido_string_float = float(string_decimal)
print(f"String: '{string_decimal}' → Float: {convertido_string_float}")

# Int/Float para String
print("\ne) Int/Float → String:")
numero = 100
texto_convertido = str(numero)
print(f"Int: {numero} → String: '{texto_convertido}'")
print(f"Agora posso concatenar com texto: 'Número: ' + '{texto_convertido}'")

# Boolean para Int/Float
print("\nf) Boolean → Int/Float:")
print(f"True → Int: {int(True)}, Float: {float(True)}")
print(f"False → Int: {int(False)}, Float: {float(False)}")

# Int/Float para Boolean
print("\ng) Int/Float → Boolean:")
print(f"1 → Boolean: {bool(1)}")
print(f"0 → Boolean: {bool(0)}")
print(f"42 → Boolean: {bool(42)}")
print(f"0.0 → Boolean: {bool(0.0)}")
print(f"3.14 → Boolean: {bool(3.14)}")

# String para Boolean
print("\nh) String → Boolean:")
print(f"String vazia '' → Boolean: {bool('')}")
print(f"String não vazia 'abc' → Boolean: {bool('abc')}")

print("\n" + "=" * 50)