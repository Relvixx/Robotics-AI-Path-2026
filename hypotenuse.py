import numpy as np

# 1. Define the parameters (Sides of the triangle)
side_a = 30.0
side_b = 40.0

# 2. Compute using Numpy (Vectorized operation)
hypotenuse = np.hypot(side_a, side_b)

# 3. Output the result
print(f"--- Robotics Math Check ---")
print(f"Side A: {side_a}")
print(f"Side B: {side_b}")
print(f"Hypotenuse: {hypotenuse}")

# 4. Verify logic
if hypotenuse == 50.0:
    print("SUCCESS: Numpy is installed and logic is correct.")
else:
    print("ERROR: Something is wrong with the calculation.")