class DiaClima:
    # Clase que representa el clima de un día
    def __init__(self, nombre, temperatura, estado):
        # Encapsulamos los atributos con __ para indicar que son privados
        self.__nombre = nombre
        self.__temperatura = temperatura
        self.__estado = estado

    def get_temperatura(self):
        # Método para acceder a la temperatura (encapsulamiento)
        return self.__temperatura

    def mostrar_info(self):
        # Muestra la información de un día
        print(f"{self.__nombre}: {self.__temperatura}°C, {self.__estado}")

class ClimaSemana:
    # Clase que agrupa los datos de la semana
    def __init__(self):
        # Lista privada de objetos DiaClima con datos predefinidos
        self.__dias = [
            DiaClima("Lunes", 28.5, "Soleado"),
            DiaClima("Martes", 29.0, "Nublado"),
            DiaClima("Miércoles", 27.5, "Lluvioso"),
            DiaClima("Jueves", 30.0, "Soleado"),
            DiaClima("Viernes", 26.0, "Nublado"),
            DiaClima("Sábado", 25.5, "Lluvioso"),
            DiaClima("Domingo", 28.0, "Soleado")
        ]

    def calcular_promedio(self):
        # Calcula el promedio de las temperaturas de los días registrados
        total = sum(dia.get_temperatura() for dia in self.__dias)
        return total / len(self.__dias)

    def mostrar_clima(self):
        # Muestra el resumen del clima de la semana
        print("\nResumen del clima semanal:")
        for dia in self.__dias:
            dia.mostrar_info()

def main():
    # Función principal del programa POO
    print("=== Programa POO: Promedio Semanal del Clima ===")
    semana = ClimaSemana()            # Crear un objeto ClimaSemana
    semana.mostrar_clima()            # Mostrar los datos
    promedio = semana.calcular_promedio()  # Calcular promedio
    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()