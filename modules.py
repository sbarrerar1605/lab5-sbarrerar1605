import os
import math

# imprimir directorio actual
cwd = os.getcwd()
print(f"Current working directory: {cwd}")

# pedir entero al usuario
num = int(input("Enter an integer: "))

# calcular log base 2
log_value = math.log2(num)
print(f"Log base 2 of {num} is: {log_value}")

# piso y techo
print(f"Floor: {math.floor(log_value)}")
print(f"Ceiling: {math.ceil(log_value)}")