from num2words import num2words

numero = int(input("Por favor, ingrese un número entero: "))

# Convertir el número en palabras
texto_numero = num2words(numero, lang='es')
print("El número {} en palabras es: {}".format(numero, texto_numero))