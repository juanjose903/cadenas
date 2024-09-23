# Solicitar el nombre completo al usuario
full_name = input("Por favor, ingresa tu nombre completo: ")

# Contar el número de letras ignorando los espacios
letter_count = len(full_name.replace(" ", ""))

# Saludar al usuario e informar la longitud de su nombre
print(f"Hola, {full_name}! Tu nombre tiene {letter_count} letras (sin contar los espacios).")
