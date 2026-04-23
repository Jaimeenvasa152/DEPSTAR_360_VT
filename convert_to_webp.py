import os
import glob
from PIL import Image

def main():
    img_dir = "img"
    jpg_files = glob.glob(os.path.join(img_dir, "DRONE.png")) + glob.glob(os.path.join(img_dir, "*.jpeg"))
    
    print(f"Found {len(jpg_files)} JPEG images.")
    for file in jpg_files:
        filename = os.path.basename(file)
        webp_name = os.path.splitext(filename)[0] + ".webp"
        webp_path = os.path.join(img_dir, webp_name)
        
        # Skip if already exists
        if os.path.exists(webp_path):
            continue
            
        print(f"Compressing {filename} -> {webp_name}...")
        try:
            with Image.open(file) as im:
                # Convert to WebP with good quality but high compression
                im.save(webp_path, 'webp', quality=85, optimize=True)
        except Exception as e:
            print(f"Failed to convert {filename}: {e}")

if __name__ == '__main__':
    main()
