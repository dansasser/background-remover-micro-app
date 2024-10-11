import sys
from rembg import remove, new_session
from PIL import Image
import io

def remove_background(
    input_path, 
    output_path, 
    model_name='u2net', 
    alpha_matting=False, 
    alpha_matting_foreground_threshold=240, 
    alpha_matting_background_threshold=10
):
    with open(input_path, 'rb') as input_file:
        input_data = input_file.read()

        # Create a session for the specified model
        session = new_session(model_name)

        # Configure the settings for background removal
        output_data = remove(
            input_data,
            session=session,
            alpha_matting=alpha_matting,
            alpha_matting_foreground_threshold=alpha_matting_foreground_threshold,
            alpha_matting_background_threshold=alpha_matting_background_threshold
        )
        
        # Save the output as a PNG to preserve transparency
        with open(output_path, 'wb') as output_file:
            output_file.write(output_data)
        print(f"Background removed using {model_name} model and saved to: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python remove_bg.py <input_image_path> <output_image_path> [model_name] [alpha_matting] [foreground_threshold] [background_threshold]")
        sys.exit(1)

    input_image_path = sys.argv[1]
    output_image_path = sys.argv[2]
    model_name = sys.argv[3] if len(sys.argv) > 3 else 'u2net'
    alpha_matting = bool(int(sys.argv[4])) if len(sys.argv) > 4 else False
    alpha_matting_foreground_threshold = int(sys.argv[5]) if len(sys.argv) > 5 else 240
    alpha_matting_background_threshold = int(sys.argv[6]) if len(sys.argv) > 6 else 10

    remove_background(
        input_image_path, 
        output_image_path, 
        model_name, 
        alpha_matting, 
        alpha_matting_foreground_threshold, 
        alpha_matting_background_threshold
    )
