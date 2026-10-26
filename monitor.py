import logging
import socket
import threading
from datetime import datetime
import time

HOST = '127.0.0.1'
PORT = 5001
TIMEOUT = 3 #Timeout duration in seconds for considering the service down

# Function to receive heartbeat messages from a service and monitor its status
def receive_heartbeat():
    monitor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    monitor.settimeout(3) #extended wait time for network latency
    # Bind the monitor socket to the specified host and port
    monitor.bind((HOST, PORT))
    last_heartbeat = None
    service_down = False #Flag to indicate if the service is down
    
    try:
        print("Heartbeat monitor online")
        
        while True:
            try:
                message = monitor.recv(1024)
                # Checks if the received message is empty
                if not message:
                    print(f"[{datetime.now()}] Received empty message")
                    break
                # Checks if the received message is a heartbeat
                if message == b"HEARTBEAT":
                    last_heartbeat = time.monotonic()
                    print(f"[{datetime.now()}] Received heartbeat message: {message}")
                    # Checks if the service was previously down and has now recovered
                    if service_down:
                        print(f"[{datetime.now()}] Sentinel recovered")
                        service_down = False
            # Handles socket timeout exceptions
            except socket.timeout:
                logging.error(f"Heartbeat not received at {datetime.now()}")
            
            # Checks whether the last heartbeat was too long ago
            if last_heartbeat is not None and not service_down:
                # Checks if the last heartbeat was too long ago
                if time.monotonic() - last_heartbeat >= TIMEOUT:

                    print(f"[{datetime.now()}] ALERT: Sentinel is down!")
                    # Marks the service as down
                    service_down = True
    
    except socket.error as e:
        print("Server unexpectedly closed")
        
    except KeyboardInterrupt:
        print("Server stopped by user")
    
    finally:
        monitor.close()
        
        
if __name__ == "__main__":
    receive_heartbeat()
