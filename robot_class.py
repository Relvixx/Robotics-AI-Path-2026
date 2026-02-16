class Robot:
    # The Constructor: Runs when you create a new Robot
    def __init__(self, name, battery_level=100):
        self.name = name
        self.battery_level = battery_level
        self.status = "Idle"
        print(f"🤖 {self.name} has come online with {self.battery_level}% battery.")

    # A Method to report status
    def status_report(self):
        print(f"[{self.name}] Status: {self.status} | Battery: {self.battery_level}%")

    # A Method to move the robot (Consumes battery)
    def move(self, distance):
        if self.battery_level < 10:
            print(f"⚠️ {self.name} Low Battery! Cannot move.")
            self.status = "Low Battery"
        else:
            self.battery_level -= distance * 5 # Costs 5% per meter
            self.status = "Moving"
            print(f"➡️ {self.name} moved {distance} meters.")
            
            if self.battery_level < 0:
                self.battery_level = 0
                self.status = "Shutdown"
                print(f"💀 {self.name} has run out of power!")

    # A Method to charge
    def charge(self):
        self.status = "Charging"
        print(f"⚡ {self.name} is charging...")
        self.battery_level = 100
        self.status = "Idle"
        print(f"🔋 {self.name} is fully charged!")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # Create two different robots (Objects)
    my_robot = Robot("R2D2")
    security_bot = Robot("SecBot", battery_level=50)

    # Use their methods
    my_robot.status_report()
    my_robot.move(10) # Move 10 meters
    my_robot.status_report()

    print("---")

    security_bot.status_report()
    security_bot.move(20) # This should drain it completely
    security_bot.status_report()
    security_bot.charge()
    security_bot.status_report()