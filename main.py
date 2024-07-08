import os

def delete_empty_folders(path):
    try:
        subdirs = [os.path.join(path, d) for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    except PermissionError as e:
        print(f"Permission error: {e}")
        return
    except FileNotFoundError as e:
        print(f"File not found error: {e}")
        return

    empty_folders = []

    for dir_path in subdirs:
        if not os.listdir(dir_path):
            empty_folders.append(dir_path)
    
    if not empty_folders:
        print("No empty folders found.")
        return
    
    print("The following empty folders were found:")
    for folder in empty_folders:
        print(folder)
    
    confirm = input("Do you want to delete these empty folders? (yes/no): ").strip()
    if confirm.lower() == 'yes':
        for folder in empty_folders:
            os.rmdir(folder)
            print(f"Deleted empty directory: {folder}")
    else:
        print("No directories were deleted.")

path_to_check = input("Enter the path of the directory to check for empty folders: ").strip()
delete_empty_folders(path_to_check)
