from socket import *
import time

# Create a UDP socket on given port
client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.bind(('', 1234))

# Throws timeout exception if socket does not receive reply mess.
client_socket.settimeout(1)

# Send 10 pings, and time RTT of each packet
for i in range(0, 10):
    try:
        t_initial = time.perf_counter_ns()
        client_socket.sendto("ping".encode(), ("localhost", 12000))  # Send a packet
        message = client_socket.recv(1024)      # Receive response message from server
        t_final = time.perf_counter_ns()
        t_elapsed = t_final - t_initial     # Time final
        print("Server Response: " + message.decode())
        print("Time Elapsed (ms): ", t_elapsed)
    except IOError:
        print("Request timed out!")
