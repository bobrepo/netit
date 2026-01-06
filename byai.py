import socket

UDP_IP = "mlszc-160-238-73-112.a.free.pinggy.link"  # The target IP address (localhost in this case)
UDP_PORT = 59257  # The target port number
MESSAGE = b"Hello, World!"  # The message must be encoded as bytes

print(f"UDP target IP: {UDP_IP}")
print(f"UDP target port: {UDP_PORT}")
print(f"Message: {MESSAGE}")

# Create a UDP socket (AF_INET for IPv4, SOCK_DGRAM for UDP)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send the message to the specified address and port
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

# The socket is automatically closed when the script finishes.
