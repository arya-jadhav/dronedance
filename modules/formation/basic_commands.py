# This example script demonstrates how to use Python to fly Tello in a box mission
# This script is part of a course on Tello drone programming
# https://learn.droneblocks.io/p/tello-drone-programming-with-python/

# Import the necessary modules
import socket
import threading
import time

class DroneSwarm:
  def __init__(self):
    self.tello1_address = ('192.168.1.104', 8889)
    self.tello2_address = ('192.168.1.103', 8889)
    self.tello3_address = ('192.168.1.102', 8889)
    self.tello4_address = ('192.168.1.105', 8889)

    self.local1_address = ('', 9000)
    self.local2_address = ('', 9001)
    self.local3_address = ('', 9010)
    self.local4_address = ('', 9011)

    self.sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.sock3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.sock4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    self.bind_sockets()

    self.receiveThread = threading.Thread(target=self.receive)
    self.receiveThread.daemon = True
    self.receiveThread.start()

  def bind_sockets(self):
    self.sock1.bind(self.local1_address)
    self.sock2.bind(self.local2_address)
    self.sock3.bind(self.local3_address)
    self.sock4.bind(self.local4_address)
  
  def send(self, id, message, delay):
  # Try to send the message otherwise print the exception
    try:
      self.sendPerDrones(id, message)
      print("Sending message: " + message)
    except Exception as e:
      print("Error sending: " + str(e))

    # Delay to allow instruction to execute
    time.sleep(delay)
  
  def sendPerDrones(self, id, message):
    match id:
      case 1:
        self.sock1.sendto(message.encode(), self.tello1_address)
      case 2:
        self.sock2.sendto(message.encode(), self.tello2_address)
      case 3:
        self.sock3.sendto(message.encode(), self.tello3_address)
      case 4:
        self.sock4.sendto(message.encode(), self.tello4_address)

  def receive(self):
    # print("recv called")
    # Continuously loop and listen for incoming messages
    while True:
      # Try to receive the message otherwise print the exception
      try:
        response1, ip_address = self.sock1.recvfrom(128)
        response2, ip_address = self.sock2.recvfrom(128)
        response3, ip_address = self.sock3.recvfrom(128)
        response4, ip_address = self.sock4.recvfrom(128)
        print("Received message: from Tello EDU #1: " + response1.decode(encoding='utf-8'))
        print("Received message: from Tello EDU #2: " + response2.decode(encoding='utf-8'))
        print("Received message: from Tello EDU #3: " + response3.decode(encoding='utf-8'))
        print("Received message: from Tello EDU #4: " + response4.decode(encoding='utf-8'))
      except Exception as e:
        # If there's an error close the socket and break out of the loop
        self.sock1.close()
        self.sock2.close()
        self.sock3.close()
        self.sock4.close()

        print("Error receiving: " + str(e))
        break
  
  def diamond(self):
    self.send(1, "up 150", 3)
    self.send(4, "up 150", 3)
    self.send(3, "left 50", 3)
    self.send(3, "up 100", 3)
    self.send(2, "up 200", 3)

  def fan(self):
    self.send(1, "up 150", 3)
    self.end(4, "up 150", 3)
    self.send(2, "up 2500", 3)
    self.send(3, "left 50", 3)
    self.send(3, "up 200", 3)

  def vertical(self):
    self.send(2, "up 100", 3)
    self.send(1, "up 150", 3)
    self.send(1, "right 50", 3)
    self.send(3, "up 200", 3)
    self.send(3, "left 50", 3)
    self.send(4, "up 250", 3)
    self.send(4, "left 100", 3)

  def icecream(self):
    self.send(1, "up 100", 3)
    self.send(2, "up 150", 3)
    self.send(3, "up 200", 3)
    self.send(4, "up 250", 3)
    self.send(1, "cw 100", 3)
    self.send(2, "cw 150", 3)
    self.send(3, "cw 200", 3)
    self.send(4, "cw 250", 3)

  def dance(self):
    self.send(1, "up 100", 3)
    self.send(2, "up 250", 3)
    self.send(3, "up 100", 3)
    self.send(4, "up 250", 3)
    #send(1, "cw 100", 3)
    #send(2, "cw 150", 3)
    #send(3, "cw 200", 3)
    #send(4, "cw 250", 3)
  
  def initialize_drones(self):
    for i in range(4):
      self.send(i+1, "command", 2)

def takeoff_drones(self):
  """
  Function for all drones to take off together
  """
  for i in range(4):
    self.send(i+1, "takeoff",  0 if i<3 else 3)

def land_drones(self):
  """
  Function to land drones one by one (can amend if required differently)
  """
  for i in range(4):
    self.send(i+1, "land",  3 if i<3 else 0)
    
def end(self):
  # Close the sockets
  self.sock1.close()
  self.sock2.close()
  self.sock3.close()
  self.sock4.close()

  print("Mission completed!")






# IP and port of Tello
# tello1_address = ('192.168.1.104', 8889)
# tello2_address = ('192.168.1.103', 8889)
# tello3_address = ('192.168.1.102', 8889)
# tello4_address = ('192.168.1.105', 8889)

# IP and port of local computer (host, port)
# empty host=connections accepted on all IPv4 interfaces
# local1_address = ('', 9000)
# local2_address = ('', 9001)
# local3_address = ('', 9010)
# local4_address = ('', 9011)

# Create a socket object (address family: IPv4, protocol: UDP)
# sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the local address and port by associating socket with a specific port number
# sock1.bind(local1_address)
# sock2.bind(local2_address)
# sock3.bind(local3_address)
# sock4.bind(local4_address)

# Send the message to Tello and allow for a delay in seconds
# def send(id, message, delay):
#   # Try to send the message otherwise print the exception
#   try:
#     sendPerDrones(id, message)
#     print("Sending message: " + message)
#   except Exception as e:
#     print("Error sending: " + str(e))

#   # Delay for a user-defined period of time
#   time.sleep(delay)

# def sendPerDrones(id, message):
#  match id:
#   case 1:
#     sock1.sendto(message.encode(), tello1_address)
#   case 2:
#     sock2.sendto(message.encode(), tello2_address)
#   case 3:
#     sock3.sendto(message.encode(), tello3_address)
#   case 4:
#     sock4.sendto(message.encode(), tello4_address)

# Receive the message from Tello
# def receive():
#   # print("recv called")
#   # Continuously loop and listen for incoming messages
#   while True:
#     # Try to receive the message otherwise print the exception
#     try:
#       response1, ip_address = sock1.recvfrom(128)
#       response2, ip_address = sock2.recvfrom(128)
#       response3, ip_address = sock3.recvfrom(128)
#       response4, ip_address = sock4.recvfrom(128)
#       print("Received message: from Tello EDU #1: " + response1.decode(encoding='utf-8'))
#       print("Received message: from Tello EDU #2: " + response2.decode(encoding='utf-8'))
#       print("Received message: from Tello EDU #3: " + response3.decode(encoding='utf-8'))
#       print("Received message: from Tello EDU #4: " + response4.decode(encoding='utf-8'))
#     except Exception as e:
#       # If there's an error close the socket and break out of the loop
#       sock1.close()
#       sock2.close()
#       sock3.close()
#       sock4.close()

#       print("Error receiving: " + str(e))
#       break


# Create and start a listening thread that runs in the background
# This utilizes our receive functions and will continuously monitor for incoming messages
# receiveThread = threading.Thread(target=receive)
# receiveThread.daemon = True
# receiveThread.start()

# formation shape function 
# def diamond():
#   send(1, "up 150", 3)
#   send(4, "up 150", 3)
#   send(3, "left 50", 3)
#   send(3, "up 100", 3)
#   send(2, "up 200", 3)

# def fan():
#   send(1, "up 150", 3)
#   send(4, "up 150", 3)
#   send(2, "up 2500", 3)
#   send(3, "left 50", 3)
#   send(3, "up 200", 3)

# def vertical():
#   send(2, "up 100", 3)
#   send(1, "up 150", 3)
#   send(1, "right 50", 3)
#   send(3, "up 200", 3)
#   send(3, "left 50", 3)
#   send(4, "up 250", 3)
#   send(4, "left 100", 3)

# def icecream():
#   send(1, "up 100", 3)
#   send(2, "up 150", 3)
#   send(3, "up 200", 3)
#   send(4, "up 250", 3)
#   send(1, "cw 100", 3)
#   send(2, "cw 150", 3)
#   send(3, "cw 200", 3)
#   send(4, "cw 250", 3)

# def dance():
#   send(1, "up 100", 3)
#   send(2, "up 250", 3)
#   send(3, "up 100", 3)
#   send(4, "up 250", 3)
#   #send(1, "cw 100", 3)
#   #send(2, "cw 150", 3)
#   #send(3, "cw 200", 3)
#   #send(4, "cw 250", 3)


# Create and start a listening thread that runs in the background
# This utilizes our receive functions and will continuously monitor for incoming messages
# receiveThread = threading.Thread(target=receive)
# receiveThread.daemon = True # daemon=killed whenever program ends
# receiveThread.start()


# Put Tello into command mode
# def initialize_drones():

#   for i in range(4):
#     send(i+1, "command", 2)

# def takeoff_drones():
#   """
#   Function for all drones to take off together
#   """
#   for i in range(4):
#     send(i+1, "takeoff",  0 if i<3 else 3)

# def land_drones():
#   """
#   Function to land drones one by one can amend if required
#   """
 
#   for i in range(4):
#     send(i+1, "land",  3 if i<3 else 0)



# send(1, "command", 2)
# send(2, "command", 2)
# send(3, "command", 2)
# send(4, "command", 2)
# initialize_drones()

# send(1, "takeoff", 2)
# send(2, "takeoff", 0)
# send(3, "takeoff", 0)
# send(4, "takeoff", 3)
# takeoff_drones()

# send(1,"forward 50", 3)
# send(2, "forward 50", 4)
# send(3, "left 20", 5)
# send(4, "down 50", 6)

# send(1, "land", 0)
# send(2, "land", 3)
# send(3, "land", 3)
# send(4, "land", 0)
# land_drones()

# Print message
# print("Mission completed successfully!")

# # receiveThread.join()

# # Close the socket
# sock1.close()
# sock2.close()
# sock3.close()
# sock4.close()


