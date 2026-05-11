# Pedir dos números al usuario
print("=== Calculadora Simple ===")
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Calcular todas las operaciones
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

# División con protección de división por cero
if num2 != 0:
    division = num1 / num2
    division_texto = str(division)
else:
    division_texto = "Error: No se puede dividir por cero"

modulo = num1 % num2 if num2 != 0 else "N/A"
potencia = num1 ** num2

# Mostrar resultados
print("\n=== RESULTADOS ===")
print(f"Suma:           {num1} + {num2} = {suma}")
print(f"Resta:          {num1} - {num2} = {resta}")
print(f"Multiplicación: {num1} × {num2} = {multiplicacion}")
print(f"División:       {num1} ÷ {num2} = {division_texto}")
print(f"Módulo:         {num1} % {num2} = {modulo}")
print(f"Potencia:       {num1} ^ {num2} = {potencia}")