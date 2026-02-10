import numpy as np

# --- 1. GENERATE FAKE DATA ---
# A Lidar usually returns an array of distances (in meters).
# Let's generate 360 readings (one for each degree).
# 'inf' means "no object detected" (infinite distance).
raw_lidar_data = np.random.uniform(0.2, 10.0, 360).tolist()

# Let's introduce some "noise" (sensor errors) manually
raw_lidar_data[10] = float('inf')  # Infinite reading
raw_lidar_data[50] = 0.0           # Error reading
raw_lidar_data[100] = -1.5         # Impossible reading

print(f"Original Data Length: {len(raw_lidar_data)}")
print(f"Sample raw data: {raw_lidar_data[:5]}") # Print first 5 items

# --- 2. YOUR TASK: CLEAN THE DATA ---
# TODO: Create a new list called 'clean_data' that:
# 1. Contains NO 'inf' values.
# 2. Contains NO values <= 0.
# Hint: Use a for loop or list comprehension.
clean_data = [] 
# [WRITE YOUR CODE HERE for the filtering loop]
clean_data = [d for d in raw_lidar_data if d != float('inf') and d > 0]
print(f"Clean Data Length: {len(clean_data)}")

# --- 3. YOUR TASK: ANALYZE THE DATA ---
# TODO: Find the closest object (min value) and furthest object (max value) from 'clean_data'.
# TODO: Calculate the average distance.

min_dist = max(clean_data) # Replace with code
max_dist = min(clean_data)# Replace with code
avg_dist = sum(clean_data)/len(clean_data) # Replace with code

print(f"Closest Obstacle: {min_dist} meters")
print(f"Furthest Obstacle: {max_dist} meters")
print(f"Average Distance: {avg_dist} meters")

# --- 4. DICTIONARIES & TUPLES ---
# TODO: Create a dictionary named 'scan_summary' containing:
# 'id': 101
# 'timestamp': '12:00:00'
# 'device_type': 'Lidar_V1'
# 'ranges': (The clean_data list)
# 'min_reading': (The min_dist value)

scan_summary = {
    'id': 101,
    'timestamp': '12:00:00',
    'device_type': 'Lidar_V1',
    'ranges': clean_data,
    'min_reading': min_dist,
} # Replace with your dictionary

print("--- Scan Summary ---")
# Use the dictionary to print the ID and Min Reading
print(f"Scan ID: {scan_summary.get('id')}")
print(f"Min Reading: {scan_summary.get('min_reading')}")