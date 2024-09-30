import os
from PIL import Image

def is_valid_jpeg(file_path):
    try:
        with Image.open(file_path) as img:
            return img.format == 'JPEG'
    except:
        return False

def is_valid_png(file_path):
    try:
        with Image.open(file_path) as img:
            return img.format == 'PNG'
    except:
        return False

def convert_jpeg_to_png(input_path, output_path):
    try:
        with Image.open(input_path) as img:
            # Process the image (you can add more processing steps here if needed)
            img = img.convert('RGB')  # Ensure image is in RGB mode
            img.save(output_path, 'PNG')
        return True
    except Exception as e:
        print(f"Error during conversion: {str(e)}")
        return False

def main():
    while True:
        input_path = input("Enter the path to the JPEG file (or 'q' to quit): ")
        
        if input_path.lower() == 'q':
            break

        if not is_valid_jpeg(input_path):
            print("Error: Invalid JPEG file. Please provide a valid JPEG file.")
            continue

        output_path = os.path.splitext(input_path)[0] + '.png'

        print("Converting JPEG to PNG...")
        if convert_jpeg_to_png(input_path, output_path):
            if is_valid_png(output_path):
                print(f"Conversion successful. PNG file saved as: {output_path}")
            else:
                print("Error: Converted file is not a valid PNG.")
        else:
            print("Conversion failed. Please try again.")

    print("Thank you for using the JPEG to PNG converter!")

if __name__ == "__main__":
    main()
