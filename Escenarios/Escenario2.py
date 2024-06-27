"""
Codigo para obtencion de datos del escenario 2 desplazamiento horizotal de dron DJI Tello
"""
from djitellopy import Tello
import time
if __name__ == "__main__":
    drone = Tello()
    drone.connect()
    print(f"Batería inicial: {drone.get_battery()}%")
    distancias = [2, 4, 6]  # distancias a las que quieres desplazar el dron en metros
    consumo = []
    posicion = []
    # Abrir archivo para escribir los resultados
    with open("resultados_distancia_y_consumo.txt", "w") as file:
        file.write("Distancia (m), Consumo de batería (%), Posición actual (cm)\n")
        for distancia in distancias:
            drone.takeoff()
            drone.move_up(120)
            drone.move_left(distancia * 100)  # La distancia debe especificarse en cm en send_rc_control
            time.sleep(5)  # Tiempo para estabilizar y medir
            # Medir consumo y posición después de desplazar
            consumo_actual = drone.get_battery()
            posicion_actual = drone.get_distance_tof()
            consumo.append(consumo_actual)
            posicion.append(posicion_actual)
            # Escribir los resultados después de desplazar
            file.write(f"{distancia}, {consumo_actual}, {posicion_actual}\n")
            # Mover el dron de regreso
            drone.move_backward(distancia)
            time.sleep(5)  # Tiempo para estabilizar y medir
            # Medir consumo y posición después de regresar
            consumo_actual = drone.get_battery()
            posicion_actual = drone.get_height()
            consumo.append(consumo_actual)
            posicion.append(posicion_actual)
            # Escribir los resultados después de moverse hacia atrás
            file.write(f", {posicion_actual}\n")
            drone.land()
            time.sleep(2)
    print("Prueba completada y datos guardados.")

    