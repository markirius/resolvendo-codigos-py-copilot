# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Solicita dois números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Escolha da operação
print("\nEscolha a operação:")
print("1 – Soma")
print("2 – Subtração")
print("3 – Multiplicação")
print("4 – Divisão")
op = input("Digite o número da operação desejada: ").strip()

if op == "1":
    resultado = num1 + num2
    sinal = "+"
elif op == "2":
    resultado = num1 - num2
    sinal = "-"
elif op == "3":
    resultado = num1 * num2
    sinal = "*"
elif op == "4":
    if num2 == 0:
        print("Erro: divisão por zero.")
        exit()
    resultado = num1 / num2
    sinal = "/"
else:
    print("Operação inválida.")
    exit()

print(f"\n{num1} {sinal} {num2} = {resultado}")

