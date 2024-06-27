"""
Codigo para obtencion de datos del escenario 2 desplazamiento horizotal con velocidades diferentes de dron DJI Tello
"""
from djitellopy import Tello
import time

if __name__ == "__main__":
    drone = Tello()
    drone.connect()
    print(f"Batería inicial: {drone.get_battery()}%")

    distancia = 400  # Distancia constante en centímetros
    velocidades = [20, 40, 60]  # velocidades en cm/s para simular diferentes velocidades

    # Abrir archivo para escribir los resultados
    with open("resultados_desplazamiento_horizontal.txt", "w") as file:
        file.write("Distancia (cm), Velocidad (cm/s), Consumo de batería antes (%), Consumo de batería después (%), Diferencia de batería (%)\n")

        for velocidad in velocidades:
            drone.takeoff()
            drone.move_up(120)  # Elevar el dron a 1.2 metros antes de empezar
            time.sleep(2)  # Estabilización después del ascenso

            # Mover el dron horizontalmente a la izquierda
            consumo_inicial = drone.get_battery()
            tiempo_movimiento = distancia / velocidad  # Calcular el tiempo de movimiento necesario
            drone.send_rc_control(0, -velocidad, 0, 0)  # Mover a la izquierda a la velocidad especificada
            time.sleep(tiempo_movimiento)  # Mantener el movimiento durante el tiempo calculado
            drone.send_rc_control(0, 0, 0, 0)  # Detener el dron
            time.sleep(2)  # Estabilizar antes de medir

            # Medir consumo después de moverse a la izquierda
            consumo_despues_izquierda = drone.get_battery()
            diferencia_consumo = consumo_inicial - consumo_despues_izquierda

            # Escribir los resultados en el archivo
            file.write(f"{distancia}, {velocidad}, {consumo_inicial}, {consumo_despues_izquierda}, {diferencia_consumo}\n")

            drone.land()
            time.sleep(2)  # Pausa entre pruebas

    print("Prueba completada y datos guardados.")