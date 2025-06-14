def obtener_clima_semanal():
    # Esta función devuelve una lista de diccionarios con los datos climáticos de la semana.
    # Cada diccionario representa un día con su temperatura y estado del clima.
    return [
        {"dia": "Lunes", "temperatura": 28.5, "estado": "Soleado"},
        {"dia": "Martes", "temperatura": 29.0, "estado": "Nublado"},
        {"dia": "Miércoles", "temperatura": 27.5, "estado": "Lluvioso"},
        {"dia": "Jueves", "temperatura": 30.0, "estado": "Soleado"},
        {"dia": "Viernes", "temperatura": 26.0, "estado": "Nublado"},
        {"dia": "Sábado", "temperatura": 25.5, "estado": "Lluvioso"},
        {"dia": "Domingo", "temperatura": 28.0, "estado": "Soleado"}
    ]

def calcular_promedio(clima_semanal):
    # Calcula el promedio de las temperaturas registradas en la semana
    total = sum(dato["temperatura"] for dato in clima_semanal)
    return total / len(clima_semanal)

def mostrar_clima(clima_semanal):
    # Muestra en pantalla el resumen de los datos ingresados o predefinidos
    print("\nResumen del clima semanal:")
    for dato in clima_semanal:
        print(f"{dato['dia']}: {dato['temperatura']}°C, {dato['estado']}")

def main():
    # Función principal que coordina el programa tradicional
    print("=== Programa Tradicional: Promedio Semanal del Clima ===")
    clima = obtener_clima_semanal()  # Obtener los datos de la semana
    mostrar_clima(clima)             # Mostrar el resumen del clima
    promedio = calcular_promedio(clima)  # Calcular el promedio de temperatura
    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()