"""
Codigo para obtencion de datos del escenario 3 altura con velocidades de elevacion diferentes de dron DJI Tello
"""
from djitellopy import Tello
import time

if __name__ == "__main__":
    drone = Tello()
    drone.connect()
    print(f"Batería inicial: {drone.get_battery()}%")

    altura = 400
    incremento = 50
    pausas = [0.5, 1, 1.5, 2]  # Diferentes pausas para simular diferentes velocidades de ascenso
    # Abrir archivo para escribir los resultados
    with open("resultados_altura_y_consumo.txt", "w") as file:
        file.write("Altura (cm), Pausa entre Incrementos (s), Consumo de batería antes (%), Consumo de batería después (%), Diferencia de batería (%)\n")
        for pausa in pausas:
            drone.takeoff()
            time.sleep(2)  # Espera para estabilización después de despegar
            consumo_inicial = drone.get_battery()

            # Ascender en incrementos hasta alcanzar la altura objetivo
            altura_actual = 0
            while altura_actual < altura:
                drone.send_rc_control(0, 0, 50, 0)  # Comando de ascenso
                altura_actual += incremento
                if altura_actual >= altura:
                    drone.send_rc_control(0, 0, 0, 0)  # Estabilizar el dron en el aire
                    break
                time.sleep(pausa)  # Controlar la "velocidad" de ascenso ajustando la pausa

            time.sleep(5)  # Estabilizar antes de medir
            consumo_final = drone.get_battery()
            diferencia_consumo = consumo_inicial - consumo_final
            # Escribir resultados en el archivo
            file.write(f"{altura}, {pausa}, {consumo_inicial}, {consumo_final}, {diferencia_consumo}\n")

            drone.land()
            time.sleep(2)  # Pausa entre cada ciclo de despegue y aterrizaje
    print("Prueba completada y datos guardados.")
