import subprocess
import os

def convert_image(input_file, output_file, resize=None, grayscale=False):
    """
    Use ImageMagick to process an image.
    
    :param input_file: Path to the input image file.
    :param output_file: Path to save the output image file.
    :param resize: Optional tuple for resizing (width, height).
    :param grayscale: Boolean to convert the image to grayscale.
    """
    print(f"Processing image: {input_file}")
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file {input_file} does not exist.")
    
    # Base command
    command = ["magick", input_file]
    
    # Add resize option if specified
    if resize:
        command.extend(["-resize", f"{resize[0]}x{resize[1]}"])
    
    # Add grayscale option if specified
    if grayscale:
        command.append("-colorspace")
        command.append("Gray")
    
    # Output file
    command.append(output_file)
    
    # Execute the command
    try:
        subprocess.run(command, check=True)
        print(f"Image successfully processed and saved to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error processing image: {e}")


input_file = ".\input.jpg"
output_file = ".\output.jpg"

# Convert image to grayscale and resize
convert_image(input_file, output_file, resize=(200, 200), grayscale=True)
