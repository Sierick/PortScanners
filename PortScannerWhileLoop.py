import socket

host = input("Enter the IP you wish to scan: ")
port = 0
port_count = 0
port_open = []


while port_count < 65535:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)
    port += 1
    port_count += 1
    if s.connect_ex((host, port)):
        s.close()
        print("Port", port, "is closed")
    else:
        s.close()
        print("Port", port, "is open!")
        port_open.append(port)

print("List of open ports:")
print(port_open)
