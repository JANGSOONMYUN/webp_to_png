# Image Processing Script

This Python script provides functionality to convert `.webp` images to `.png` format, move the original `.webp` files to a new subdirectory, and resize `.png` images within a specified directory.

## Features
- **Convert WEBP to PNG**: Converts `.webp` images to `.png` format.
- **Resize PNGs**: Resizes `.png` images within a specified directory to a target size.

## Requirements
- Python 3.x
- PIL (Pillow)
- OS and Shutil modules (pre-installed with Python)

## Installation
- **Install the required libraries**:
    ```bash
    pip install Pillow
    ```

## Usage

### Convert WEBP to PNG and Move Original Files

- **Run the script with the directory path**:

    ```bash
    python webp_converter.py <directory_path>
    ```

    Replace `<directory_path>` with the path to the directory you want to traverse.

### Resize PNG Images

- **Run the script with the folder path and target size**:
    ```bash
    python resize_png.py <folder_path> <width> <height>
    ```

    Replace `<folder_path>` with the path to the folder you want to resize PNG images in, and `<width>` and `<height>` with the target dimensions.

## Functions

### `convert_webp_to_png(src_path, dest_path)`
Converts a WEBP image to PNG format.

- **Parameters**:
  - `src_path`: Source path of the WEBP image.
  - `dest_path`: Destination path for the PNG image.

### `move_to_child_directory(original_path, child_dir_name="original_webp")`
Moves the original file to a new child directory.

- **Parameters**:
  - `original_path`: Path of the original file to be moved.
  - `child_dir_name`: Name of the child directory (default is `original_webp`).

### `traverse_and_convert(directory)`
Traverses directories, converts WEBP files to PNG, and moves the original WEBP files to a child directory.

- **Parameters**:
  - `directory`: The root directory to start traversing.

### `resize_pngs_in_folder(folder_path, target_size=(800, 600))`
Resizes all PNG images in a specified folder to a target size.

- **Parameters**:
  - `folder_path`: Path to the folder containing PNG images.
  - `target_size`: Tuple specifying the target width and height (default is `(800, 600)`).

## Example

### Convert and Move WEBP Files
```bash
python webp_converter.py /path/to/directory
```

### Resize PNG Files
```bash
python resize_png.py /path/to/folder 709 1181
```
