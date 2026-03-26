from robot_class import Robot

# --- Subclasses (Drone & TransitBot) ---
class Drone(Robot):
    def __init__(self, name, battery_level=100, max_altitude=100):
        super().__init__(name, battery_level)
        self.altitude = 0
        self.max_altitude = max_altitude
        print(f"🚁 Drone systems online. Max altitude: {self.max_altitude}m")

    def fly(self, height):
        if self.battery_level < 15:
            print(f"⚠️ {self.name} battery too low for flight!")
            return
        if height > self.max_altitude:
            print(f"❌ {self.name} cannot fly that high!")
        else:
            self.altitude = height
            self.battery_level = max(0, self.battery_level - height * 0.2)
            print(f"⬆️ {self.name} taking off to {self.altitude} meters.")

    def status_report(self):
        return f"[{self.name}] Status: {self.status} | Battery: {self.battery_level:.1f}% | Alt: {self.altitude}m"


class TransitBot(Robot):
    def __init__(self, name, routes_loaded=True):
        super().__init__(name, battery_level=100)
        self.routes_loaded = routes_loaded
        print(f"🚌 Transit assistant '{self.name}' initialized.")

    def calculate_route(self, start_point, end_point):
        if self.battery_level < 10:
            print(f"⚠️ {self.name} battery too low to calculate routes!")
            return
        if self.routes_loaded:
            print(f"🗺️ {self.name} calculating route from {start_point} to {end_point}...")
            print("✅ Route locked. Ready to assist travelers.")
            self.battery_level -= 2
        else:
            print(f"❌ {self.name} has no map data loaded!")

    def status_report(self):
        return f"[{self.name}] Status: {self.status} | Battery: {self.battery_level}% | Routes: {self.routes_loaded}"


# --- Fleet Simulation ---
class FleetManager:
    def __init__(self):
        self.robots = []

    def add_robot(self, robot):
        self.robots.append(robot)

    def run_tasks(self):
        print("\n--- Fleet Task Execution ---")
        for bot in self.robots:
            if isinstance(bot, Drone):
                bot.fly(50)
            elif isinstance(bot, TransitBot):
                bot.calculate_route("Village Hub A", "City Station B")

    def fleet_status(self):
        print("\n--- Fleet Status Reports ---")
        for bot in self.robots:
            print(bot.status_report())


# --- MAIN EXECUTION ---
if __name__ == "__main__":
    scout = Drone("AeroScout", battery_level=80, max_altitude=500)
    routly_unit = TransitBot("Routly-Core")

    fleet = FleetManager()
    fleet.add_robot(scout)
    fleet.add_robot(routly_unit)

    fleet.run_tasks()
    fleet.fleet_status()
