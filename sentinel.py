
import socket
import time
import threading
import random
import os
# Security Domain : Network Sentinel/Firewall Agent

# List of blacklisted IP addresses
BLACKLISTED_IPS = ["203.0.113.10", "198.51.100.23"]

# Function to check if an IP address is blacklisted
def check_ip(ip_address):

    if ip_address in BLACKLISTED_IPS:
        return "BLOCK"

    return "ALLOW"

# Function to check a request based on IP address and payload
def check_request(ip_address, payload):

    result = check_ip(ip_address)

    if result == "BLOCK":
        return "BLOCK: IP address is blacklisted"

    if "malware" in payload.lower():
        return "BLOCK: Suspicious payload"

    return "ALLOW: Request accepted"

# Function to receive messages over UDP
def receive_message():

    # Creates a UDP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Listens on localhost, port 5000
    server.bind(("127.0.0.1", 5000))

    # Waits at most 1 second for each message
    server.settimeout(1)

    print("Sentinel is running and waiting for messages...")
    
    try:
        while True:

            try:
                data, address = server.recvfrom(1024)

            except socket.timeout:
                continue
            # Decodes the received message as UTF-8
            message = data.decode("utf-8")

            print("Received:", message)
            # Checks if the message contains the expected format 
            # with IP address and payload separated by "|"
            if "|" in message:
                # Splits the message into IP address and payload
                ip_address, payload = message.split("|", 1)

                result = check_request(
                    ip_address.strip(),
                    payload.strip()
                )
            # If the message does not contain "|"
            # it is considered invalid
            else:
                result = "ERROR: Invalid request format"

            print("Result:", result)

            server.sendto(result.encode("utf-8"), address)

    except KeyboardInterrupt:
        print("\nSentinel stopped by user.")

    finally:
        server.close()


# Function to send a heartbeat message over UDP
def send_heartbeat():
    # Creates a UDP socket for sending the heartbeat message
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as heartbeat_socket:
        while True:
            # Sends a heartbeat message to the specified IP address and port
            # to indicate that the sender is alive
            heartbeat_socket.sendto(b"HEARTBEAT", ("127.0.0.1", 5001))

            print("Heartbeat sent")

            time.sleep(1)  # Wait for 1 seconds before sending the next heartbeat


# Function to simulate a random process crash
def random_crash():
    # Generates a random delay between 20 and 40 seconds before the simulation crashes
    delay = random.randint(20, 40)
    
    # Debug message indicating the delay before the simulated crash
    #print("Sentinel will crash after", delay, "seconds")
    
    print("Random crash simulation started")
    
    time.sleep(delay)

    print("SIMULATED CRASH: Sentinel stopped!", flush=True)
    # Exits the process with an error code to simulate a crash
    os._exit(1)

if __name__ == "__main__":
    # Start the heartbeat thread
    heartbeat_thread = threading.Thread(target=send_heartbeat, daemon=True)
    heartbeat_thread.start()

    # Start the random crash thread
    crash_thread = threading.Thread(target=random_crash, daemon=True)
    crash_thread.start()

    # Start the main security service
    receive_message()

