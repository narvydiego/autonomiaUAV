import tellopy
import time
import pandas as pd
from datetime import datetime

def main():
    drone = None
    battery_data = []

    try:
        # Crear una instancia del dron
        drone = tellopy.Tello()

        # Conectar al dron
        drone.connect()
        drone.wait_for_connection(60.0)

        # Despegar el dron
        drone.takeoff()

        # Subir 2 metros
        drone.up(50)  # Ajustar velocidad de ascenso según sea necesario
        time.sleep(2)  # Esperar 2 segundos
        drone.up(0)  # Detener el ascenso

        # Suscribirse a eventos del dron para obtener datos de vuelo
        drone.subscribe(drone.EVENT_FLIGHT_DATA, lambda event, sender, data, **args: handle_flight_data(event, sender, data, battery_data))

        # Mantener la altura durante 1 segundo y tomar el primer dato de batería
        time.sleep(1)
        mark_battery('Manteniendo altura a 2m', battery_data)

        # Iniciar movimiento a la izquierda (20 metros)
        mark_battery('Inicia movimiento a la izquierda (20m)', battery_data)
        for _ in range(10):
            drone.left(50)  # Ajustar velocidad según sea necesario
            time.sleep(1)  # Moverse durante 1 metro
            drone.left(0)  # Detener el movimiento
            mark_battery('Movimiento a la izquierda (1m)', battery_data)

        # Mantener la posición durante 1 segundo
        time.sleep(1)

        # Iniciar movimiento a la derecha (20 metros)
        mark_battery('Inicia movimiento a la derecha (20m)', battery_data)
        for _ in range(10):
            drone.right(50)  # Ajustar velocidad según sea necesario
            time.sleep(1)  # Moverse durante 1 metro
            drone.right(0)  # Detener el movimiento
            mark_battery('Movimiento a la derecha (1m)', battery_data)

        # Mantener la posición durante 1 segundo
        time.sleep(1)

        # Iniciar el descenso
        mark_battery('Inicia descenso', battery_data)
        drone.down(50)  # Ajustar velocidad de descenso según sea necesario
        time.sleep(2)  # Esperar a que descienda
        drone.down(0)  # Detener el descenso

        # Aterrizar el dron
        drone.land()

    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
    finally:
        # Verificar si la instancia de drone fue creada antes de llamar a quit
        if drone:
            drone.quit()
        
        # Guardar los datos de la batería en un archivo Excel
        save_battery_data(battery_data)

def handle_flight_data(event, sender, data, battery_data):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    battery_data.append({
        'Time': current_time,
        'Battery': data.battery_percentage  # Guardar con dos decimale
    })
    print(f"{current_time} - Estado de la batería: {round(data.battery_percentage, 2)}%")

def mark_battery(event, battery_data):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    battery_data.append({
        'Time': current_time,
        'Event': event,
        'Battery': round(battery_data[-1]['Battery'], 2) if battery_data else 'Unknown'
    })
    print(f"{current_time} - {event} - Estado de la batería: {round(battery_data[-1]['Battery'], 2)}%")

def save_battery_data(battery_data):
    df = pd.DataFrame(battery_data)
    df.to_excel('battery_data15glateral.xlsx', index=False)
    print("Datos de batería guardados en battery_data.xlsx")

if __name__ == '__main__':
    main()
