# Paso 1: Determinar el valor de cambio de cada tipo de moneda (eur/usd)

valor_de_cambio_EUR = 20.00
valor_de_cambio_USD = 23.00

# Paso 2: Solicitar al usuario que indique el tipo de moneda inicial

Tipo_de_cambio = input("Por favor ingrese el tipo de cambio (USD/EUR): ")

# Paso 3: Solicitar al usuario que ingrese el monto a convertir

Monto = float(input("Por favor ingrese el monto a convertir: "))

# Paso 4: Convertir el monto indicado a la moneda correspodiente

if Tipo_de_cambio.upper() == "EUR":
    Resultado_EUR = Monto * valor_de_cambio_EUR
    print("La conversión de EUR a Pesos MXN da:", Resultado_EUR )
elif Tipo_de_cambio.upper() == "USD": 
   Resultado_USD = Monto * valor_de_cambio_USD 
   print("La conversión de USD a Pesos MXN da:", Resultado_USD)
else:
    print("El tipo de cambio no está disponible")
