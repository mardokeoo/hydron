import matplotlib.pyplot as plt

# Datos de ejemplo para las subidas y bajadas del nivel de agua
tiempos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
niveles_agua = [1, 3, 2, 5, 7, 4, 6, 8, 9, 10]

# Crear la gráfica
plt.figure(figsize=(10, 6))

# Graficar la línea del nivel de agua
plt.plot(tiempos, niveles_agua, label='Nivel de Agua', color='blue')

# Marcar las subidas y bajadas
for i in range(1, len(tiempos)):
    cambio_nivel = niveles_agua[i] - niveles_agua[i-1]
    if cambio_nivel > 0:
        plt.annotate('Subida', (tiempos[i], niveles_agua[i]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8, color='red')
    elif cambio_nivel < 0:
        plt.annotate('Bajada', (tiempos[i], niveles_agua[i]), textcoords="offset points", xytext=(0, -15), ha='center', fontsize=8, color='green')

# Configurar etiquetas y título
plt.xlabel('Tiempo')
plt.ylabel('Nivel de Agua')
plt.title('Subidas y Bajadas del Nivel de Agua')
plt.legend()

# Establecer el rango del eje y
plt.ylim(1, 10)
plt.yticks(range(1, 11))

# Mostrar la gráfica
plt.grid(True)
plt.show()
