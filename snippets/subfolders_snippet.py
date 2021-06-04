import os

main_path = 'd:\\downloads'


def get_subfolder_paths(folder_path) -> list:
    subfolder_paths = [f.path for f in os.scandir(folder_path) if f.is_dir()]

    return subfolder_paths


def get_subfolder_names(folder_path) -> list:
    subfolder_paths = get_subfolder_paths(folder_path)
    subfolder_names = [f.split('\\')[-1] for f in subfolder_paths]

    return subfolder_names


print(get_subfolder_paths(main_path))
print(get_subfolder_names(main_path))
