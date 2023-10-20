def calcular_total(lineas):
    total_con_iva = 0
    total_sin_iva = 0

    # Recorrer cada línea de artículo
    for linea in lineas[2:]:
        # Obtener precio

        articulo_precio = float(linea[18:].strip())

        # Calcular precio sin IVA y sumar al total correspondiente
        precioSinIVA = round(articulo_precio / 1.21, 2)
        total_con_iva += articulo_precio
        total_sin_iva += precioSinIVA

    return (total_con_iva, total_sin_iva)

def factura():
# Abrir archivo de texto
    with open('factura.txt', 'r', encoding='utf-8') as f:
    # Leer líneas del archivo
        lineas = f.readlines()

    # Crear archivo resultado
    with open('resultado.txt', 'w', encoding='utf-8') as f:
        # Escribir encabezado
        f.write(f'ID Denominación                   Precio SIN-IVA\n{"-"*50}\n')

        # Recorrer cada línea de artículo
        for linea in lineas[2:]:
            # Obtener información del artículo
            articulo_id = linea[:3].strip()
            articulo_nombre = linea[3:18].strip()
            articulo_precio = float(linea[18:].strip())

            # Calcular precio sin IVA y escribir información en archivo resultado
            precioSinIVA = round(articulo_precio / 1.21, 2)
            f.write(f'{articulo_id:2} {articulo_nombre:15} \
                {articulo_precio:6.2f}  {precioSinIVA:6.2f}\n')
        # Calcular y escribir total de la factura
        f.write('-'*50)
        total_con_iva, total_sin_iva = calcular_total(lineas)
        f.write(f'\nTotal{" "*29}{total_con_iva:7.2f} {total_sin_iva:7.2f}\n')


factura()
