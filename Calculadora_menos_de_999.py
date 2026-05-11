# Pedir dos números al usuario
imprimir("=== Calculadora Simple ===")("=== Calculadora Simple ===")
num1 = float(entrada("Ingresa el primer número: "))float(entrada("Ingresa el primer número: "))
num2 = float(entrada("Ingresa el segundo número: "))float(entrada("Ingresa el segundo número: "))

# Calcular todas las operaciones
suma = num1 + num2
resta = num1 - num2
multiplicación = num1 * num2

# División con protección de división por cero
si num2 != 0: num2 != 0:
 división = num1 / num2
 división_texto = str(división)str(división)
de lo contrario::
 división_texto = "Error: No se puede dividir por cero""Error: No se puede dividir por cero"

módulo = num1 % num2 si num2 != 0 de lo contrario "N/A"si num2 != 0 else "N/A"
potencia = num1 ** num2

# Mostrar resultados
imprimir("\n=== RESULTADOS ===")("\n=== RESULTADOS ===")
imprimir(f"Suma: {num1} + {num2} = {suma}")(f"Suma: {num1} + {num2} = {suma}")
imprimir(f"Resta: {num1} - {num2} = {resta}")(f"Resta: {num1} - {num2} = {resta}")
imprimir(f"Multiplicación: {num1} × {num2} = {multiplicación}")(f"Multiplicación: {num1} × {num2} = {multiplicación}")
imprimir(f"División: {num1} ÷ {num2} = {división_texto}")(f"División: {num1} ÷ {num2} = {división_texto}")
imprimir(f"Módulo: {num1} % {num2} = {módulo}")(f"Módulo: {num1} % {num2} = {módulo}")
imprimir(f"Potencia: {num1} ^ {num2} = {potencia}")(f"Potencia: {num1} ^ {num2} = {potencia}")
