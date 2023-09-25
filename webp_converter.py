import os
from PIL import Image
import shutil

def convert_webp_to_png(src_path, dest_path):
    """Converts a WEBP image to PNG format."""
    with Image.open(src_path) as image:
        image.save(dest_path, 'PNG')

def move_to_child_directory(original_path, child_dir_name="original_webp"):
    """Moves the file into a new child directory."""
    parent_dir = os.path.dirname(original_path)
    child_dir_path = os.path.join(parent_dir, child_dir_name)
    
    # Create child directory if it doesn't exist
    os.makedirs(child_dir_path, exist_ok=True)
    
    new_path = os.path.join(child_dir_path, os.path.basename(original_path))
    shutil.move(original_path, new_path)

def traverse_and_convert(directory):
    """Traverses child directories, converts WEBP files to PNG and moves original WEBP to a child directory."""
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.lower().endswith('.webp'):
                full_path = os.path.join(dirpath, filename)
                new_path = os.path.splitext(full_path)[0] + '.png'
                convert_webp_to_png(full_path, new_path)
                move_to_child_directory(full_path)
                print(f"Converted {full_path} to {new_path} and moved the original to {os.path.join(dirpath, 'original_webp', filename)}")

if __name__ == "__main__":
    base_directory = './'
    traverse_and_convert(base_directory)