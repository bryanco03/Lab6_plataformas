import threading
import time
from datamanager import RealTimeDataManager

def imprimir_datos(data):
    print(f"Datos en tiempo real actualizados: {data}")


def main():
        
    real_time_data_manager = RealTimeDataManager()

    real_time_data_manager.event_manager.subscribe("datos", imprimir_datos)

    update_thread = threading.Thread(target=real_time_data_manager.start_real_time_updates)
    update_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nPrograma terminado.")    


if __name__ == "__main__":
    main()