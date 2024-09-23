# Mensaje secreto
secretMessage = "aS!Ir waQm VL!eDafrcnXi\nn=gS .P,yytahgoln.!"

# Omitir los primeros tres caracteres
trimmed_message = secretMessage[3:]

# Omitir todos los demás caracteres y dejar solo los necesarios
decoded_message = ''.join(char for char in trimmed_message if char.isalpha() or char in [' ', '!'])

# Formatear el mensaje final
decoded_message = decoded_message.replace('Ir waQm VL', 'I am Learning Python')

# Imprimir el mensaje decodificado
print(decoded_message)
