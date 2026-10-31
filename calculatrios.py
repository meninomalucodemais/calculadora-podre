numero1 = float(input("coloque o numero aqui: "))
numero2 = float(input("coloque outro numero aqui: "))
conta = input("Conta (+, -, *, /): ")

if conta == "+":
    resultado = numero1 + numero2
elif conta == "-":
    resultado = numero1 - numero2
elif conta == "*":      
    resultado: float = numero1 * numero2
elif conta == "/":
    resultado = numero1 / numero2
else: "Seu otario coloca um numero normal porra"

print("o resultado é: ", resultado)

input("Aperte enter para fechar...")
