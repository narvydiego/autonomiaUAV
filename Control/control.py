import tellopy
import pygame
import sys
import time

def main():
    # Inicializa Pygame
    pygame.init()

    # Crea una ventana de 300x300
    pygame.display.set_mode((300, 300))

    # Inicializa el dron Tello
    drone = tellopy.Tello()

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
                        drone.forward(10)
                        time.sleep(1)
                        drone.forward(0)
                    elif event.key == pygame.K_DOWN:  # Flecha abajo para retroceder
                        drone.backward(10)
                        time.sleep(1)
                        drone.backward(0)
                    elif event.key == pygame.K_LEFT:  # Flecha izquierda para moverse a la izquierda
                        drone.left(10)
                        time.sleep(1)
                        drone.left(0)
                    elif event.key == pygame.K_RIGHT:  # Flecha derecha para moverse a la derecha
                        drone.right(10)
                        time.sleep(1)
                        drone.right(0)
                    elif event.key == pygame.K_w:  # w para subir
                        drone.up(10)
                        time.sleep(1)
                        drone.up(0)
                    elif event.key == pygame.K_s:  # s para bajar
                        drone.down(10)
                        time.sleep(1)
                        drone.down(0)
                    elif event.key == pygame.K_a:  # a para girar a la izquierda
                        drone.counter_clockwise(30)
                        time.sleep(1)
                        drone.counter_clockwise(0)
                    elif event.key == pygame.K_d:  # d para girar a la derecha
                        drone.clockwise(30)
                        time.sleep(1)
                        drone.clockwise(0)

    finally:
        # Asegura que el dron aterrice si algo falla
        drone.land()
        drone.quit()
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    main()
