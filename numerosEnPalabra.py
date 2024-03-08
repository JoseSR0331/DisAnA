from num2words import num2words

numero = int(input("Ingrese cualquier numero entero: "))

# Convertir el número en palabras
texto_numero = num2words(numero, lang='es')
print("El numero {} en palabras es: {}".format(numero, texto_numero))
