import os
import shutil
import pandas as pd

def print_dataset_folder_structure(root_path):
    print('-------- Current dataset folder structure --------')
    for root, dirs, files in os.walk(root_path):
        level = root.replace(root_path, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f'{indent}{os.path.basename(root)}/')
        subindent = ' ' * 4 * (level + 1)

def restructure_dataset(root_path):
    print('-------- Changing dataset folder structure --------')
    if not os.path.exists(root_path):
        print(f"Path not found: {root_path}")
        return

    # Iterate over the class folders (High-grade IN, Normal, etc.)
    for class_name in os.listdir(root_path):
        class_dir = os.path.join(root_path, class_name)

        # Ensure we are processing directories only
        if os.path.isdir(class_dir):
            print(f"Processing: {class_name}")

            # 1. Remove 'label' folder
            label_dir = os.path.join(class_dir, 'label')
            if os.path.exists(label_dir):
                shutil.rmtree(label_dir)
                print(f"  - Removed label folder")

            # 2. Move files from 'image' folder to the class folder
            image_dir = os.path.join(class_dir, 'image')
            if os.path.exists(image_dir):
                for filename in os.listdir(image_dir):
                    src_file = os.path.join(image_dir, filename)
                    dst_file = os.path.join(class_dir, filename)

                    # Move the file
                    shutil.move(src_file, dst_file)

                print(f"  - Moved images to {class_name}/")

                # 3. Remove the now empty 'image' folder
                os.rmdir(image_dir)
                print(f"  - Removed image folder")

    print("\nRestructuring complete.")


def organize_dataset(root_folder):
    print('-------- Organizing dataset into train/val --------')

    # Define paths to CSVs
    # Assuming datasets folder is in the same directory as this script (src/datasets)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    train_csv_path = os.path.join(script_dir, 'datasets', 'train_paths.csv')
    val_csv_path = os.path.join(script_dir, 'datasets', 'val_paths.csv')
    
    # Check if CSVs exist
    if not os.path.exists(train_csv_path) or not os.path.exists(val_csv_path):
        print(f"Error: CSV files not found at {train_csv_path} or {val_csv_path}")
        return

    splits = {
        'train': train_csv_path,
        'val': val_csv_path
    }

    for split_name, csv_path in splits.items():
        print(f"Processing {split_name} split from {csv_path}...")
        df = pd.read_csv(csv_path)
        
        # Create split directory (e.g., root_folder/train)
        split_dir = os.path.join(root_folder, split_name)
        os.makedirs(split_dir, exist_ok=True)
        
        for _, row in df.iterrows():
            # CSV path example: /Adenocarcinoma/file.png
            # We need to strip the leading '/' to join correctly
            rel_path = row['path'].lstrip(os.sep).lstrip('/')
            
            # Original file location: root_folder/Adenocarcinoma/file.png
            src_path = os.path.join(root_folder, rel_path)
            
            # Destination location: root_folder/train/Adenocarcinoma/file.png
            dst_path = os.path.join(split_dir, rel_path)
            
            # Ensure destination directory exists
            os.makedirs(os.path.dirname(dst_path), exist_ok=True)
            
            try:
                # Move file
                if os.path.exists(src_path):
                    shutil.move(src_path, dst_path)
                else:
                    # It might have been moved already if duplicates exist or logic is rerunning
                    # Check if it already exists in dest, maybe do nothing?
                    # Or maybe it simply doesn't exist.
                    if not os.path.exists(dst_path):
                         print(f"Warning: Source file not found: {src_path}")
            except Exception as e:
                print(f"Error moving {src_path} to {dst_path}: {e}")
    
    # Clean up empty class folders in root_folder
    for item in os.listdir(root_folder):
        item_path = os.path.join(root_folder, item)
        if os.path.isdir(item_path) and item not in ['train', 'val']:
            shutil.rmtree(item_path)
            print(f"Removed residual folder: {item}")
    
                
    print(f"Organization complete.")


def build_dataset_from_csv(root_folder):
    print('-------------------------------------------------')
    print('-------- Start Building dataset from CSV --------')
    print('-------------------------------------------------')
    print_dataset_folder_structure(root_folder)
    restructure_dataset(root_folder)
    organize_dataset(root_folder)
    print_dataset_folder_structure(root_folder)
    print('------------------------------------------------')
    print('-------- End Building dataset from CSV ---------')
    print('------------------------------------------------')