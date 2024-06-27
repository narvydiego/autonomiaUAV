"""
Codigo para obtencion de datos del escenario 1 altura de dron DJI Tello
"""
from djitellopy import Tello
import time

if __name__ == "__main__":
    drone = Tello()
    drone.connect()
    print(f"Batería inicial: {drone.get_battery()}%")

    alturas = [2, 4, 6]  # alturas a las que quieres elevar el dron en metros
    consumo = []
    posicion = []

    # Abrir archivo para escribir los resultados
    with open("resultados_altura_y_consumo.txt", "w") as file:
        file.write("Altura (m), Consumo de batería (%), Posición actual (cm)\n")

        for altura in alturas:
            drone.takeoff()
            drone.move_up(altura * 100)  # La altura debe especificarse en cm en send_rc_control
            time.sleep(5)  # Tiempo para estabilizar y medir

            # Medir consumo y posición después de subir
            consumo_actual = drone.get_battery()
            posicion_actual = drone.get_height()
            consumo.append(consumo_actual)
            posicion.append(posicion_actual)

            # Escribir los resultados después de subir
            file.write(f"{altura}, {consumo_actual}, {posicion_actual}\n")

            drone.send_rc_control(0, 0, 0, 0)  # Estabilizar el dron en el aire
            time.sleep(5)  # Tiempo para estabilizar y medir

            # Medir consumo y posición al estabilizar
            consumo_actual = drone.get_battery()
            posicion_actual = drone.get_height()
            consumo.append(consumo_actual)
            posicion.append(posicion_actual)

            # Escribir los resultados al estabilizar
            file.write(f"{altura}, {consumo_actual}, {posicion_actual}\n")

            drone.land()
            time.sleep(2)  # Pausa entre cada ciclo de despegue y aterrizaje

    print("Prueba completada y datos guardados.")

    