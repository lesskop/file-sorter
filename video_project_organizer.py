import os

main_folder = 'f:\\shtosh python\\new video'

# key names will be folder names!
extensions = {

    'img': ['jpg', 'png', 'bmp', 'gif', 'ai', 'psd', 'ico', 'jpeg', 'ps', 'svg', 'tif', 'tiff'],

    'audio': ['mp3', 'wav', 'ogg', 'flac', 'aif', 'mid', 'midi', 'mpa', 'wma', 'wpl', 'cda'],

    'footage': ['mp4', 'mov', 'avi', 'wmv', '3gp', '3g2', 'mpg', 'mpeg', 'm4v', 'h264', 'flv',
                'rm', 'swf', 'vob'],

    'mkv': ['mkv'],

    'prj': []
}


# also creates folders from dictionary keys
def create_folders_from_list(folder_path, folder_names):
    for folder in folder_names:
        if not os.path.exists(f"{folder_path}\\{folder}"):
            os.mkdir(f"{folder_path}\\{folder}")


def get_subfolder_paths(folder_path) -> list:
    subfolder_paths = [f.path for f in os.scandir(folder_path) if f.is_dir()]

    return subfolder_paths


def get_file_paths(folder_path) -> list:
    file_paths = [f.path for f in os.scandir(folder_path) if not f.is_dir()]

    return file_paths


def remove_empty_folders(folder_path):
    subfolder_paths = get_subfolder_paths(folder_path)

    for p in subfolder_paths:
        if not os.listdir(p):
            print('Deleting empty folder:', p.split('\\')[-1], '\n')
            os.rmdir(p)


def sort_files(folder_path) -> None:
    file_paths = get_file_paths(folder_path)
    ext_list = list(extensions.items())

    for file_path in file_paths:
        extension = file_path.split('.')[-1]
        file_name = file_path.split("\\")[-1]

        for folder_int in range(len(ext_list)):
            if extension in ext_list[folder_int][1]:
                print(f'Moving {file_name} in {ext_list[folder_int][0]} folder\n')
                os.rename(file_path, f'{main_folder}\\{ext_list[folder_int][0]}\\{file_name}')


if __name__ == "__main__":
    create_folders_from_list(main_folder, extensions)
    sort_files(main_folder)
    # remove_empty_folders(main_folder)
