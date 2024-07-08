import tellopy
import pygame
import sys
from datetime import datetime

def main():
    velDron = 50 # Velocidad del dron en cm/s
    battery_data = [] # Lista para almacenar los datos de la batería
    # Inicializa Pygame
    pygame.init()

    # Crea una ventana de 300x300
    pygame.display.set_mode((300, 300))

    # Inicializa el dron Tello
    drone = tellopy.Tello()

    # Suscríbete al evento de datos de vuelo
    drone.subscribe(drone.EVENT_FLIGHT_DATA, lambda event, sender, data, **args: handle_flight_data(event, sender, data, battery_data))
    try:
        # Conecta al dron
        drone.connect()
        drone.wait_for_connection(60.0)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    # Controla el dron con teclado
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_j:  # j para despegue
                        drone.takeoff()
                    elif event.key == pygame.K_k:  # k para aterrizar
                        drone.land()
                    elif event.key == pygame.K_UP:  # Flecha arriba para avanzar
                        drone.forward(velDron)
                    elif event.key == pygame.K_DOWN:  # Flecha abajo para retroceder
                        drone.backward(velDron)
                    elif event.key == pygame.K_LEFT:  # Flecha izquierda para moverse a la izquierda
                        drone.left(velDron)
                    elif event.key == pygame.K_RIGHT:  # Flecha derecha para moverse a la derecha
                        drone.right(velDron)
                    elif event.key == pygame.K_w:  # w para subir
                        drone.up(velDron)
                    elif event.key == pygame.K_s:  # s para bajar
                        drone.down(velDron)
                    elif event.key == pygame.K_a:  # a para girar a la izquierda
                        drone.counter_clockwise(30)
                    elif event.key == pygame.K_d:  # d para girar a la derecha
                        drone.clockwise(30)
                elif event.type == pygame.KEYUP:
                    # Detener el dron cuando se suelta la tecla
                    if event.key == pygame.K_UP:
                        drone.forward(0)
                    elif event.key == pygame.K_DOWN:
                        drone.backward(0)
                    elif event.key == pygame.K_LEFT:
                        drone.left(0)
                    elif event.key == pygame.K_RIGHT:
                        drone.right(0)
                    elif event.key == pygame.K_w:
                        drone.up(0)
                    elif event.key == pygame.K_s:
                        drone.down(0)
                    elif event.key == pygame.K_a:
                        drone.counter_clockwise(0)
                    elif event.key == pygame.K_d:
                        drone.clockwise(0)

    finally:
        # Asegura que el dron aterrice si algo falla
        drone.land()
        drone.quit()
        pygame.quit()
        sys.exit()

def handle_flight_data(event, sender, data, battery_data):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    battery_data.append({
        'Time': current_time,
        'Battery': data.battery_percentage,
        'Height': data.height
    })
    print(f"{current_time} - Estado de la batería: {data.battery_percentage}% - Altura: {data.height} cm")

if __name__ == '__main__':
    main()
