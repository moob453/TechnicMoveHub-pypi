# main.py
from time import sleep
from technicmovehub import movehub2


def main():
    hub = movehub2()
    
    # Connect to the Technic Move Hub
    # This method is synchronous and will block until connection is established
    # or timeout occurs. It will print an error and exit the program if not found.
    print("Attempting to connect to Move Hub...")
    connected_hub_instance = hub.connect(timeout=10) 
    
    if connected_hub_instance:
        print("Connected to Move Hub!")
        
        # Set LED color to red
        print("Setting LED color to red...")
        hub.set_led_color("red")
        sleep(2)

        # Control Motor A: spin forward at 50% power
        print("Spinning Motor A forward at 50% power (inverted by library)...")
        hub.motor("motor A", "power", 50)
        sleep(3) # Run motor for 3 seconds

        # Stop Motor A
        print("Stopping Motor A...")
        hub.motor("motor A", "power", 0)
        sleep(1)

        # Control Motor B: spin backward at 75% power
        print("Spinning Motor B backward at 75% power...")
        hub.motor("motor B", "power", -75)
        sleep(3) # Run motor for 3 seconds

        # Stop Motor B
        print("Stopping Motor B...")
        hub.motor("motor B", "power", 0)
        sleep(1)
        
        # Disconnect from the hub
        print("Disconnecting from Move Hub...")
        hub.disconnect()
        print("Disconnected.")
    else:
        print("Failed to connect to Move Hub. Program should have exited via library.")

if __name__ == "__main__":
    main()