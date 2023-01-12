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
    self.send(3, "up 80", 3)
    self.send(3, "left 50", 4)
    self.send(2, "down 20", 5)

  def triangle(self):
    self.send(2, "up 100", 2)
    self.send(1, "up 50", 4)
    self.send(3, "up 50", 4)

  def vertical(self):
    self.send(2, "up 50", 3)
    self.send(1, "up 70", 5)
    self.send(1, "right 50", 6)
    self.send(3, "up 100", 7)
    self.send(3, "left 50", 8)
    self.send(4, "up 120", 9)
    self.send(4, "left 50", 10)

  def icecream(self):
    self.send(2, "up 20", 3)
    self.send(3, "up 50", 5)
    self.send(4, "up 80", 6)
    self.send(1, "cw 100", 7)
    self.send(2, "cw 150", 8)
    self.send(3, "cw 200", 9)
    self.send(4, "cw 250", 10)

  def dance(self):
    self.send(2, "up 80", 3)
    self.send(4, "up 80", 5)
    self.send(1, "up 80", 7)
    self.send(3, "up 80", 8)
    self.send(2, "down 80", 9)
    self.send(4, "down 80", 10)
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
      self.send(i+1, "takeoff",  2)

  def land_drones(self):
    """
    Function to land drones one by one (can amend if required differently)
    """
    for i in range(4):
      self.send(i+1, "land",  15)
      
  def end(self):
    # Close the sockets
    self.sock1.close()
    self.sock2.close()
    self.sock3.close()
    self.sock4.close()

  # print("Mission completed!")


# Intialize class
drone = DroneSwarm()
drone.takeoff_drones()
drone.triangle()
drone.land_drones()