import os

folder_path = 'f:\\shtosh python\\video'

# key names will be folder names!
extensions = {

    'img': ['jpg', 'png', 'gif', 'ai', 'psd', 'jpeg', 'svg'],

    'audio': ['mp3', 'wav', 'ogg'],

    'footage': ['mp4', 'mov', 'avi', 'wmv', 'mpg'],

    'mkv': ['mkv'],

    'prj': []
}


# also creates folders from dictionary keys
def create_folders_from_list(folder_names):
    for fn in folder_names:
        if not os.path.exists(os.path.join(folder_path, fn)):
            print("Creating", fn, 'folder\n')
            os.mkdir(os.path.join(folder_path, fn))


def get_subfolder_paths():
    for fp in os.scandir(folder_path):
        if fp.is_dir():
            yield fp.path


def get_file_paths():
    for fp in os.scandir(folder_path):
        if not fp.is_dir():
            yield fp.path


def sort_files():
    file_paths = get_file_paths()
    ext_items_list = list(extensions.items())

    for fp in file_paths:
        extension = fp.split('.')[-1]
        file_name = os.path.split(fp)[-1]

        for dict_key in enumerate(ext_items_list):
            subfolder_name = ext_items_list[dict_key[0]][0]
            ext_list = ext_items_list[dict_key[0]][1]

            if extension in ext_list:
                print(f'Moving {file_name} in {subfolder_name} folder\n')
                os.rename(fp, os.path.join(folder_path, subfolder_name, file_name))


def remove_empty_folders():
    subfolder_paths = get_subfolder_paths()

    for sp in subfolder_paths:
        if not os.listdir(sp):
            print('Deleting', os.path.basename(sp), 'folder\n')
            os.rmdir(sp)


if __name__ == "__main__":
    print("# # # Creating folders # # #\n")
    create_folders_from_list(extensions)

    print("# # # Sorting files # # #\n")
    sort_files()

    print("# # # Removing empty folders # # #\n")
    remove_empty_folders()
