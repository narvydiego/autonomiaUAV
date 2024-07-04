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

        # Suscribirse a eventos del dron para obtener datos de vuelo
        drone.subscribe(drone.EVENT_FLIGHT_DATA, lambda event, sender, data, **args: handle_flight_data(event, sender, data, battery_data))

        # Subir a 10 metros
        for meter in range(1, 12):
            drone.up(50)  # Subir a una velocidad de 50 cm/s
            time.sleep(1)  # Esperar 1 segundo
            drone.up(0)  # Detener el ascenso
            time.sleep(1)  # Esperar 1 segundo mientras se obtiene el estado de la batería
            
            # Marcar cada 5 metros
            if meter % 5 == 0:
                print(f"Subiendo - Altura alcanzada: {meter} metros")

        # Bajar a 0 metros
        for meter in range(1, 12):
            drone.down(50)  # Bajar a una velocidad de 20 cm/s
            time.sleep(1)  # Esperar 1 segundo
            drone.down(0)  # Detener el descenso
            time.sleep(1)  # Esperar 1 segundo mientras se obtiene el estado de la batería
            
            # Marcar cada 5 metros
            if meter % 5 == 0:
                print(f"Bajando - Altura restante: {20 - meter} metros")

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
        'Battery': data.battery_percentage,
        'Height': data.height
    })
    print(f"{current_time} - Estado de la batería: {data.battery_percentage}%")

def save_battery_data(battery_data):
    df = pd.DataFrame(battery_data)
    df.to_excel('battery_data25g6malto.xlsx', index=False)
    print("Datos de batería guardados en battery_data.xlsx")

if __name__ == '__main__':
    main()
