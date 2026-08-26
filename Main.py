from PIL import Image
from pyzbar.pyzbar import decode
import os

def scan_qr_file(image_path):
    print(f" Analyzing image: '{image_path}'...")
    
    # Check if the file actually exists
    if not os.path.exists(image_path):
        print(f" Error: The file '{image_path}' was not found.")
        return

    try:
        # Open the image file using Pillow
        img = Image.open(image_path)
        
        # Decode the QR data from the static image
        decoded_objects = decode(img)
        
        if not decoded_objects:
            print(" No QR code detected in this image.")
            return

        # Print the results
        print("\n Success! Found QR Data:")
        print("---------------------------------")
        for obj in decoded_objects:
            # Convert the byte data to a readable text string
            qr_text = obj.data.decode('utf-8')
            print(f"• Data: {qr_text}")
            print(f"• Type: {obj.type}")
        print("---------------------------------")

    except Exception as e:
        print(f" Failed to process image: {e}")

if __name__ == "__main__":
    # Change this string to match your image file name
    target_image = "my_qrcode.png" 
    
    scan_qr_file(target_image)
