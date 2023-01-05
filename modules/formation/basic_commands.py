# This example script demonstrates how to use Python to fly Tello in a box mission
# This script is part of our course on Tello drone programming
# https://learn.droneblocks.io/p/tello-drone-programming-with-python/

# Import the necessary modules
import socket
import threading
import time

# IP and port of Tello
tello1_address = ('192.168.1.104', 8889)
tello2_address = ('192.168.1.102', 8889)
# tello3_address = ('192.168.1.107', 8889)

# IP and port of local computer
local1_address = ('', 9010)
local2_address = ('', 9011)
# local3_address = ('', 9012)

# Create a UDP connection that we'll send the command to
sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the local address and port
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
      sock2.sendto(message.encode(), tello2_address)
    # sock3.sendto(message.encode(), tello3_address)
    print("Sending message: " + message)
  except Exception as e:
    print("Error sending: " + str(e))

  # Delay for a user-defined period of time
  time.sleep(delay)

# Receive the message from Tello
def receive():
  # Continuously loop and listen for incoming messages
  while True:
    # Try to receive the message otherwise print the exception
    try:
      response1, ip_address = sock1.recvfrom(128)
      response2, ip_address = sock2.recvfrom(128)
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
receiveThread = threading.Thread(target=receive)
receiveThread.daemon = True
receiveThread.start()

# Each leg of the box will be 100 cm. Tello uses cm units by default.
box_leg_distance = 100

# Yaw 90 degrees
yaw_angle = 90

# Yaw clockwise (right)
yaw_direction = "cw"

# Put Tello into command mode

send(1, "command", 3)
send(2, "command", 3)
# send(1, "battery?", 3)
# send(2, "battery?", 3)
# Send the takeoff command
send(1, "takeoff", 3)
send(2, "takeoff", 3)
# Loop and create each leg of the box
# for i in range(4):
#   # Fly forward
#   send("forward " + str(box_leg_distance), 4)
#   # Yaw right
#   send("cw " + str(yaw_angle), 3)

send(1, "ccw 360", 3)
send(2, "cw 360", 3)
# Land
send(1, "land", 3)
send(2, "land", 3)

# Print message
print("Mission completed successfully!")

# Close the socket
sock1.close()
sock2.close()
# sock3.close()