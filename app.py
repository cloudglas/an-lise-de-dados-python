# Crie um programa que:
# 1. Pede 3 nomes ao usuário
# 2. Salva em um arquivo "nomes.txt"
# 3. Lê e mostra o conteúdo

# Escrita
with open("nomes.txt", "w") as arquivo:
    for i in range(3):
        nome = input(f"Digite o {i+1}º nome: ")
        arquivo.write(nome + "\n")

print("\nNomes salvos! Conteúdo do arquivo:")
print("=" * 30)

# Leitura
with open("nomes.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)