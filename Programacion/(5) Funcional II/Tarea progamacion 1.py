"""
Los médicos forenses utilizan la longitud de los huesos para determinar la altura de una persona, cuando la persona estaba viva.

Por ejemplo, par los varones:

altura (en cm) = 69.089 + 2.232 * longitud de la tibia

Para las mujeres, el valor es el siguiente:

altura (en cm) = 61.412 + 2.317 * longitud de la tibia

A partir de los 30 años, la altura de una persona decrece a una tasa de 0.06 cm por año.

Escribir un programa que, dados los valores de la longitud de la tibia, el sexo y la edad del paciente, nos calcule la altura aproximada.
"""
# Datos de entrada:
long_tibia = 30.4
sexo = 'V'
edad = 45

# Dato intermedio
aprox = 69.089 + 2.232 * long_tibia if sexo == 'V' else 61.412 + 2.317 * long_tibia

# Datos de salida:
altura = aprox - 0.06 * (edad - 29) if edad >= 30 else aprox