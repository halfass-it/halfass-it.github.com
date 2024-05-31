from PIL import Image
import sys

def remove_white_background(input_path, output_path):
    # Open the image file
    img = Image.open(input_path)

    # Convert the image to RGBA (if it's not already in this mode)
    img = img.convert("RGBA")

    # Get the data of the image
    data = img.getdata()

    # Replace white background with transparency
    new_data = []
    for item in data:
        # Change all white (also shades of whites) to transparent
        if all(color > 200 for color in item[:3]):
            new_data.append((255, 255, 255, 0))  # Set alpha to 0 for white pixels
        else:
            new_data.append(item)

    # Update image data
    img.putdata(new_data)

    # Save the image as PNG (to preserve transparency)
    img.save(output_path, format="PNG")

    return output_path

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input_image_path output_image_path")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    remove_white_background(input_path, output_path)
    print("Image with white background removed and saved as", output_path)
