# height and weight are available as a regular lists
import numpy as np
height_in = [74, 74, 72, 72, 73, 69, 69]

weight_lb = [180, 215, 210, 210, 188, 176, 209]
# Import numpy


# Calculate the BMI: bmi
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array
light = bmi < 21

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])
