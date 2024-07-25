import os
import sys
from PIL import Image

def resize_pngs_in_folder(folder_path, target_size=(800, 600)):
    # 폴더 내 모든 파일 및 하위 폴더 탐색
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 파일이 png 형식인지 확인
            if file.lower().endswith('.png'):
                file_path = os.path.join(root, file)
                try:
                    # 이미지 열기
                    with Image.open(file_path) as img:
                        # 이미지 리사이즈
                        img_resized = img.resize(target_size, Image.ANTIALIAS)
                        # 원본 파일 덮어쓰기
                        img_resized.save(file_path)
                        print(f'Resized and saved: {file_path}')
                except Exception as e:
                    print(f'Error processing file {file_path}: {e}')


if __name__ == "__main__":
#     # 사용 예시
#     resize_pngs_in_folder('./', target_size=(709, 1181))
    if len(sys.argv) != 4:
        print("Usage: python resize_png.py <folder_path> <width> <height>")
        sys.exit(1)
    
    folder_path = sys.argv[1]
    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a valid directory.")
        sys.exit(1)
    
    try:
        width = int(sys.argv[2])
        height = int(sys.argv[3])
    except ValueError:
        print("Error: width and height must be integers.")
        sys.exit(1)

    target_size = (width, height)
    resize_pngs_in_folder(folder_path, target_size)