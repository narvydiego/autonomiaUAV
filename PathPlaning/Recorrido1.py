"""
Codigo para el primer 
"""
#Importacion de librerias
import tellopy
import time 
import pandas as pd
from datetime import datetime

#Funcion principal
def main():
    drone = None
    data_dron = []
    file_data_name = 'data_dron.xlsx'
    try:
        drone = tellopy.Tello() # Instacia del dron
        drone.connect() # Conectar al dron
        drone.wait_for_connection(60.0) # Esperar conexión
        drone.takeoff() # Despegar el dron
        drone.subscribe(drone.EVENT_FLIGHT_DATA, lambda event, sender, data, **args: handle_flight_data(event, sender, data, data_dron)) # Suscribirse a eventos del dron para obtener datos de vuelo

    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
    finally:
        # Verificar si la instancia de drone fue creada antes de llamar a quit
        if drone:
            drone.quit()
        
        # Guardar los datos de la batería en un archivo Excel
        save_data(data_dron, file_data_name)

# Funcion para obtener los datos del drone
def handle_flight_data(event, sender, data, battery_data):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    battery_data.append({
        'Time': current_time,
        'Battery': data.battery_percentage,
        'Height': data.height
    })
    print(f"{current_time} - Estado de la batería: {data.battery_percentage}%")

# Funcion para guardar los datos de drone en un archivo Excel
def save_data(data_dron, file_data_name):
    df = pd.DataFrame(data_dron)
    df.to_excel(file_data_name, index=False)
    print(f"Datos guardados en {file_data_name}")

if __name__ == '__main__':
    main()