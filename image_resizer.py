from PIL import Image
import os

def resize_images(input_folder, output_folder, new_size=(300, 300)):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # List all files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp'))]

    for image_file in image_files:
        input_path = os.path.join(input_folder, image_file)
        output_path = os.path.join(output_folder, image_file)

        # Open and resize the image
        with Image.open(input_path) as img:
            resized_img = img.resize(new_size)

            # Save the resized image to the output folder
            resized_img.save(output_path)

def main():
    input_folder = 'input_images'
    output_folder = 'output_images'
    new_size = (150, 150)  # Specify the new size for the images

    resize_images(input_folder, output_folder, new_size)
    print(f"Images resized and saved to {output_folder}.")

if __name__ == "__main__":
    main()
