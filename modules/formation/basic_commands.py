# This example script demonstrates how to use Python to fly Tello in a box mission
# This script is part of a course on Tello drone programming
# https://learn.droneblocks.io/p/tello-drone-programming-with-python/

# Import the necessary modules
import socket
import threading
import time

# IP and port of Tello
tello1_address = ('192.168.1.104', 8889)
tello2_address = ('192.168.1.103', 8889)
tello3_address = ('192.168.1.102', 8889)
tello4_address = ('192.168.1.101', 8889)

# IP and port of local computer (host, port)
# empty host=connections accepted on all IPv4 interfaces
local1_address = ('', 9010)
local2_address = ('', 9011)
# local3_address = ('', 9012)

# Create a socket object (address family: IPv4, protocol: UDP)
sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the local address and port by associating socket with a specific port number
sock1.bind(local1_address)
sock2.bind(local2_address)
# sock3.bind(local3_address)

# Send the message to Tello and allow for a delay in seconds
def send(id, message, delay):
  # Try to send the message otherwise print the exception
  try:
    if id==1:
      sock1.sendto(message.encode(), tello1_address)
    elif id==2:
      # pass
      sock2.sendto(message.encode(), tello2_address)
    elif id==3:
      sock1.sendto(message.encode(), tello3_address)
    elif id==4:
      sock2.sendto(message.encode(), tello4_address)
    print("Sending message: " + message)
  except Exception as e:
    print("Error sending: " + str(e))

  # Delay for a user-defined period of time
  time.sleep(delay)

# Receive the message from Tello
def receive():
  # print("recv called")
  # Continuously loop and listen for incoming messages
  while True:
    # Try to receive the message otherwise print the exception
    try:
      response1, ip_address1 = sock1.recvfrom(128) # 128 bytes is max size of data
      response2, ip_address2 = sock2.recvfrom(128)
    #   response3, ip_address = sock3.recvfrom(128)
      print("Received message: from Tello EDU #1: " + response1.decode(encoding='utf-8'))
      print("Received message: from Tello EDU #2: " + response2.decode(encoding='utf-8'))
    #   print("Received message: from Tello EDU #3: " + response3.decode(encoding='utf-8'))

    except Exception as e:
      # If there's an error close the socket and break out of the loop
      print("closing due to exception")
      sock1.close()
      sock2.close()
    #   sock3.close()
      print("Error receiving: " + str(e))
      break

# Create and start a listening thread that runs in the background
# This utilizes our receive functions and will continuously monitor for incoming messages
# receiveThread = threading.Thread(target=receive)
# receiveThread.daemon = True # daemon=killed whenever program ends
# receiveThread.start()


# Put Tello into command mode

send(1, "command", 0)
send(2, "command", 0)
send(3, "command", 3)

# send(1, "battery?", 3)
# send(2, "battery?", 3)
# Send the takeoff command
send(1, "takeoff", 0)
send(2, "takeoff", 0)
send(3, "takeoff", 3)

send(1, "land", 3)
send(2, "land", 3)
send(3, "land", 0)

# Print message
print("Mission completed successfully!")

# receiveThread.join()

# Close the socket
sock1.close()
sock2.close()
# sock3.close()

