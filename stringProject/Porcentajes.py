# Porcentajes
percentage_increase_sales = 12.93720081
percentage_growth_revenue = 18.33206078

# Formatear los porcentajes a dos decimales
formatted_sales = f"{percentage_increase_sales:.2f}"
formatted_revenue = f"{percentage_growth_revenue:.2f}"

# Crear la cadena
result = f"Las ventas de la empresa láctea aumentaron un {formatted_sales.replace('.', ',')}% y los ingresos crecieron un {formatted_revenue.replace('.', ',')}%."

# Imprimir el resultado
print(result)

