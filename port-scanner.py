import socket
from concurrent.futures import ThreadPoolExecutor

# Función que intentará conectar con un puerto y verificar si está abierto
def scan_port(ip, port):
    try:
        # Crear un socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Establecer un tiempo de espera de 1 segundo
        result = sock.connect_ex((ip, port))  # Intentar conectar al puerto
        if result == 0:
            print(f"Puerto {port} abierto en {ip}")
        sock.close()  # Cerrar el socket
    except socket.error as err:
        print(f"No se pudo conectar con el puerto {port} en {ip}: {err}")

# Función que maneja la creación de hilos para escanear varios puertos simultáneamente
def scan_ports(ip, start_port, end_port, num_threads=10):
    ports = range(start_port, end_port + 1)
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Enviar los trabajos de escaneo al ThreadPoolExecutor
        executor.map(lambda port: scan_port(ip, port), ports)

# Función principal para ejecutar el escáner
def main():
    # Dirección IP a escanear y rango de puertos
    ip = input("Introduce la IP a escanear: ")
    start_port = int(input("Introduce el puerto inicial: "))
    end_port = int(input("Introduce el puerto final: "))

    print(f"Escaneando puertos del {start_port} al {end_port} en {ip}...\n")
    scan_ports(ip, start_port, end_port)

if __name__ == "__main__":
    main()
