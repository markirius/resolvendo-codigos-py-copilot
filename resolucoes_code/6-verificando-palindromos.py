# Recebe a palavra do usuário
palavra = input("Digite a palavra a ser verificada: ").strip().lower()

# Inverte a palavra
invertida = palavra[::-1]

# Verifica se é palíndromo
if palavra == invertida:
    print(f"\"{palavra}\" é **palíndromo**.")
else:
    print(f"\"{palavra}\" **não** é palíndromo.")
