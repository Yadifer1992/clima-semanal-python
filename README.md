# clima-semanal-python
Repositorio con los códigos en Python (programación tradicional y POO) y un análisis comparativo para el cálculo de temperaturas semanales.
# Comparativa: Programación tradicional vs Programación orientada a objetos (POO)

Este proyecto contiene dos versiones de un programa en Python que calcula el promedio de temperatura semanal:
- `tradicional.py`: código con programación estructurada.
- `poo.py`: código con programación orientada a objetos.

## Comparación

### Programación tradicional
- Se usan funciones y listas de diccionarios.
- Es más sencilla para programas pequeños.
- Los datos no están encapsulados, cualquier parte del programa puede modificarlos.
- Menos modular y más difícil de mantener si el proyecto crece.

### Programación POO
- Se usan clases para representar el día y la semana.
- Se aplica encapsulamiento para proteger los datos.
- Más modular y fácil de ampliar (por ejemplo, añadir humedad o viento).
- Ideal para programas grandes o en crecimiento.
  
## Conceptos aplicados en POO

- **Encapsulamiento:** Los datos de cada día (temperatura, estado) están protegidos dentro de los objetos, evitando que partes externas del programa los modifiquen directamente.
- **Herencia:** (En este caso no se aplicó herencia porque el problema no lo requería, pero podría usarse si tuviéramos diferentes tipos de días, como festivos o especiales).
- **Polimorfismo:** No se implementó explícitamente, pero podría aplicarse si tuviéramos distintas clases con métodos que se comportan de forma diferente (por ejemplo, diferentes cálculos de promedio según el tipo de semana).

## Conclusión
Ambos programas dan el mismo resultado, pero la estructura POO es más adecuada para proyectos escalables y mantenibles.
