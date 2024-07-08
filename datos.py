import pandas as pd
import numpy as np

# Configuración inicial
total_time = 47  # tiempo total en segundos para el ascenso y descenso completo
time_step = 0.1  # paso de tiempo en segundos
ascend_rate = 0.182  # tasa de ascenso calculada
descend_rate = -0.174  # tasa de descenso calculada

# Crear un array para almacenar la altura en cada paso de tiempo
heights = np.zeros(int(total_time / time_step) + 1)

# Estado inicial
heights[0:int(2 / time_step)] = 1  # Altura inicial de 1 metro hasta el segundo 2

# Simular el comportamiento
for i in range(int(2 / time_step), len(heights)):
    current_time = i * time_step
    if current_time < 24:  # De 2 a 24 segundos, asciende a 5 metros
        heights[i] = heights[i - 1] + ascend_rate * time_step
    elif current_time < 47:  # De 24 a 47 segundos, desciende a 1 metro
        heights[i] = heights[i - 1] + descend_rate * time_step
    else:  # Mantener en 1 metro después de 47 segundos
        heights[i] = 1

# Crear DataFrame para almacenar los resultados
times = np.arange(0, total_time + time_step, time_step)
data = pd.DataFrame({
    'Tiempo (s)': times,
    'Altura (m)': heights
})

# Guardar los resultados en un archivo Excel
data.to_excel('alturas_dron_ascenso_descenso.xlsx', index=False)
