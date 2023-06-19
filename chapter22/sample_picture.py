# Define a sample picture using a multidimensional array
sample_picture = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

# Display the sample picture
for row in sample_picture:
    for pixel in row:
        if pixel == 1:
            print("█", end="") # The character "█" represents a solid block or a filled square
        else:
            print(" ", end="")
    print()


# Define a sample picture using a multidimensional array
sample_picture = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Define characters to represent different pixel values
pixel_chars = {
    0: "█",   # Black pixel
    1: " "    # White pixel
}

# Display the sample picture
for row in sample_picture:
    for pixel in row:
        print(pixel_chars[pixel], end="")
    print()

from PIL import Image

# Define the size of the image
width = 1024  # Adjust the width as per your preference
height = 1024  # Adjust the height as per your preference

# Create a new image with RGB mode
image = Image.new("RGB", (width, height))

# Define the colors for the bird
background_color = (100, 200, 255)  # Light blue background
body_color = (255, 0, 0)  # Red body color
beak_color = (255, 255, 0)  # Yellow beak color
eye_color = (0, 0, 0)  # Black eye color

# Draw the bird on the image
pixels = image.load()
for y in range(height):
    for x in range(width):
        if y < height // 2:
            pixels[x, y] = background_color
        else:
            if x < width // 2:
                pixels[x, y] = body_color
            else:
                if y < height // 2 + height // 8:
                    pixels[x, y] = beak_color
                else:
                    pixels[x, y] = eye_color

# Save the image as a 2MB JPEG file
image.save("colorful_bird.jpg", "JPEG", quality=80)

