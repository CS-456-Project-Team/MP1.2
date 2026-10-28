import json

# Function to save the sentinel's blacklist
def save_state(blocked_ips):
    # Save the list of blocked IPs to a JSON file
    with open("checkpoint.json","w") as file:
        json.dump(blocked_ips, file)

# Function to load the sentinel's blacklist
def load_state():
    # Loads the list of blocked IPs from a JSON file
    with open("checkpoint.json","r") as file:
        blocked_ips = json.load(file)
    return blocked_ips

