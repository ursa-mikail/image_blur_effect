from PIL import Image
import requests
import cv2
import numpy as np
from io import BytesIO
import matplotlib.pyplot as plt

def blur_image(image, clarity_percentage):
    # Convert image to numpy array
    image = np.array(image)
    # Calculate blur intensity (clarity_percentage is between 0 and 100)
    blur_intensity = max(1, int((100 - clarity_percentage) / 10))  # Ensure at least a small blur

    # Apply Gaussian blur using OpenCV
    blurred_image = cv2.GaussianBlur(image, (blur_intensity * 2 + 1, blur_intensity * 2 + 1), 0)

    # Convert back to PIL Image
    blurred_image = Image.fromarray(blurred_image)

    return blurred_image


# Example usage
clarity_percentage = 50  # Change this value between 0 (fully blurred) and 100 (no blur)
image_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5jss0IeznaB1NzwXgay5C8W416TR6ers8cw&s'
image_path = 'path_to_your_image.jpg'

OPT_FROM_URL = True
image = None

if OPT_FROM_URL:
    # Download image from URL
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
else:
    # Load image using PIL
    image = Image.open(image_path)


# Usage
# Example usage: Range run 1
clarity_percentage = 50  # Change this value between 0 (fully blurred) and 100 (no blur)
blurred_image = blur_image(image, clarity_percentage)

# Show the blurred image
blurred_image.show()

# Save the blurred image
blurred_image.save('blurred_image_'+ str(clarity_percentage) +'_percent_.jpg')

# Generate and plot blurred images at different clarity percentages
clarity_percentages = range(10, 101, 10)
num_images = len(clarity_percentages)
cols = 5
rows = (num_images // cols) + (1 if num_images % cols != 0 else 0)

plt.figure(figsize=(15, rows * 3))
for i, clarity_percentage in enumerate(clarity_percentages):
    blurred_image = blur_image(image, clarity_percentage)
    plt.subplot(rows, cols, i + 1)
    plt.imshow(blurred_image)
    plt.title(f'Clarity: {clarity_percentage}%')
    plt.axis('off')

plt.suptitle('Blurred Images at Different Clarity Percentages')
plt.tight_layout()
plt.show()

# Example usage: Range run 2
# Generate and plot blurred images at different clarity percentages
step = 1
clarity_percentages = range(1, 10, step)
num_images = len(clarity_percentages)
cols = 5
rows = (num_images // cols) + (1 if num_images % cols != 0 else 0)

plt.figure(figsize=(15, rows * 3))
for i, clarity_percentage in enumerate(clarity_percentages):
    blurred_image = blur_image(image, clarity_percentage)
    plt.subplot(rows, cols, i + 1)
    plt.imshow(blurred_image)
    plt.title(f'Clarity: {clarity_percentage}%')
    plt.axis('off')

plt.suptitle('Blurred Images at Different Clarity Percentages')
plt.tight_layout()
plt.show()

# Example usage: Fine-grained range run
# Define the range of clarity percentages
clarity_percentages = np.arange(0, 10.1, 0.1)  # From 0% to 10% in 0.1% increments

# Determine the number of rows and columns for subplots

# Determine the number of rows and columns for subplots
num_plots = len(clarity_percentages)
cols = 10  # Adjust as needed
rows = (num_plots + cols - 1) // cols  # Calculate the number of rows needed

# Create the figure and set its size
plt.figure(figsize=(15, rows * 3))

# Iterate over the clarity percentages and create subplots
for i, clarity_percentage in enumerate(clarity_percentages):
    blurred_image = blur_image(image, clarity_percentage)
    plt.subplot(rows, cols, i + 1)
    plt.imshow(blurred_image)
    plt.title(f'Clarity: {clarity_percentage:.1f}%')
    plt.axis('off')

# Display the figure
plt.suptitle('Blurred Images at Different Clarity Percentages')
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()

