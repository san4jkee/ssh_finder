import socket

def scan_network():
    subnet = '192.168.0'  # Замените на свою подсеть
    open_ports = []

    for i in range(1, 255):
        ip = f'{subnet}.{i}'
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Установите таймаут соединения
        result = sock.connect_ex((ip, 22))
        if result == 0:
            open_ports.append(ip)
        sock.close()

    return open_ports

if __name__ == '__main__':
    open_ips = scan_network()
    print('IP-адреса с открытым портом 22:')
    for ip in open_ips:
        print(ip)