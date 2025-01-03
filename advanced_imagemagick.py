import subprocess
import os

def process_images(input_folder, output_folder, watermark_file=None, resize=(800, 800), blur=0, brightness=100):
    """
    Batch process images using ImageMagick.
    
    :param input_folder: Path to the folder containing input images.
    :param output_folder: Path to save the processed images.
    :param watermark_file: Path to the watermark image file (optional).
    :param resize: Tuple to resize images (width, height).
    :param blur: Integer for blur radius (0 for no blur).
    :param brightness: Brightness adjustment percentage (default is 100).
    """
    if not os.path.exists(input_folder):
        raise FileNotFoundError(f"Input folder {input_folder} does not exist.")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each image in the input folder
    for filename in os.listdir(input_folder):
        input_file = os.path.join(input_folder, filename)
        if not os.path.isfile(input_file):
            continue
        
        # Generate the output file path
        output_file = os.path.join(output_folder, filename)
        
        # Base command
        command = ["magick", input_file]
        
        # Resize
        if resize:
            command.extend(["-resize", f"{resize[0]}x{resize[1]}"])
        
        # Apply blur
        if blur > 0:
            command.extend(["-blur", f"0x{blur}"])
        
        # Adjust brightness
        if brightness != 100:
            command.extend(["-modulate", str(brightness)])
        
        # Add watermark
        if watermark_file:
            command.extend([
                "(", watermark_file, "-gravity", "southeast", "-geometry", "+10+10", "-composite", ")"
            ])
        
        # Add the output file
        command.append(output_file)
        
        # Execute the command
        try:
            subprocess.run(command, check=True)
            print(f"Processed: {input_file} -> {output_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error processing {input_file}: {e}")

# Example usage
if __name__ == "__main__":
    input_folder = "input_images"
    output_folder = "output_images"
    watermark_file = "watermark.png"
    
    process_images(
        input_folder=input_folder,
        output_folder=output_folder,
        watermark_file=watermark_file,
        resize=(1024, 1024),
        blur=2,
        brightness=120
    )
