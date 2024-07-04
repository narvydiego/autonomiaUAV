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

        # Volar a 1 metro de altura
        drone.up(50)  # Subir
        time.sleep(8)  # Esperar 2 segundos
        drone.up(0)  # Detener el ascenso

        # Suscribirse a eventos del dron para obtener datos de vuelo
        drone.subscribe(drone.EVENT_FLIGHT_DATA, lambda event, sender, data, **args: handle_flight_data(event, sender, data, battery_data))

        # Mantener la altura durante 1 minuto
        start_time = time.time()
        while time.time() - start_time < 300:
            time.sleep(2)

        # Comenzar el descenso a una velocidad de 40 m/h (aproximadamente 11.1 cm/s)
        drone.down(11)
        descend_start_time = time.time()

        # Verificar la batería cada 2 segundos mientras desciende
        while True:
            current_time = time.time()
            elapsed_time = current_time - descend_start_time
            if elapsed_time > 10:  # Volar por 10 segundos antes de aterrizar
                break
            time.sleep(2)

        # Detener el descenso
        drone.down(0)

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
        'Battery': data.battery_percentage
    })
    print(f"{current_time} - Estado de la batería: {data.battery_percentage}%")

def save_battery_data(battery_data):
    df = pd.DataFrame(battery_data)
    df.to_excel('battery_data.xlsx', index=False)
    print("Datos de batería guardados en battery_data.xlsx")

if __name__ == '__main__':
    main()
